Chemical Initial/Boundary Conditions (IC/BC)
===============================================

WRF-GC is a regional model. Boundary conditions from a global model are generally required. Initial conditions can be provided by a WRF-GC run or other global models.

You can use MOZART4-GEOS5, CAM-chem, or GEOS-Chem as input for initial/boundary conditions.

The general process is as follows:

* Identify which data source you want to use as ic/bc.
* Set-up WRF-GC, and run ``real.exe`` to generate ``wrfinput_d01`` (initial conditions), and ``wrfbdy_d01`` (boundary conditions)
* Prepare ic/bc inputs into a netCDF format accepted by ``mozbc``. (`mozbc for WRF-GC is located here <https://github.com/fengx7/mozbc_for_WRFv3.9>`_)
* Use `mozbc` to add these inputs to ``wrfinput_d01`` and/or ``wrfbdy_d01`` files.
* Run the WRF-GC model.

Preparing IC/BC file from global GEOS-Chem output
-------------------------------------------------

Details are available in the PDF getting started guide. `A MATLAB script <https://github.com/fengx7/WRF-GC-GCC_ICBC>`_ will process global GEOS-Chem outputs to netCDF files accepted by ``mozbc``, which are then generated into WRF(-GC) initial/boundary files.

Run the GEOS-Chem standard full-chemistry simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend running at a resolution 2 x 2.5 degree because this will provide higher resolution initial and boundary condition data to WRF-GC (which generally has higher resolution). 4 x 5 degree is also supported.

The running time must cover the WRF-GC simulation period, **with at least one day preceding**: e.g. if the simulation period of WRF-GC is from 2015-06-10 00:00:00 to 2015-06-20 00:00:00 (UTC), the time ranges for GEOS-Chem should be **at least** available from 2015-06-09 00:00:00 to 2015-06-20 00:00:00, not including necessary initialization (spin-up).

Output the netCDF diagnostic files every 6 hours (00, 06, 12, 18), including:

(a) ``GEOSChem.SpeciesConc.YYYYMMDD_HHIIz.nc4`` (contains **instantaneous** ``SpeciesConc_?ADV?``)

(b) ``GEOSChem.StateMet.YYYYMMDD_HHIIz.nc4`` (contains ``Met_PS1DRY``).

Using the ``HISTORY.rc`` configuration similar to follows:

.. code-block::

          SpeciesConc.template:       '%y4%m2%d2_%h2%n2z.nc4',
          SpeciesConc.frequency:      00000000 060000
          SpeciesConc.duration:       00000000 060000
          SpeciesConc.mode:           'instantaneous'
          SpeciesConc.fields:         'SpeciesConc_?ALL?             ',
        ::

          StateMet.template:          '%y4%m2%d2_%h2%n2z.nc4',
          StateMet.frequency:         00000000 060000
          StateMet.duration:          00000000 060000
          StateMet.mode:              'instantaneous'
          StateMet.fields:            'Met_AD                        ',
                                      'Met_AIRDEN                    ',
                                      'Met_AIRVOL                    ',
                                      'Met_BXHEIGHT                  ',
                                      'Met_PBLTOPL                   ',
                                      'Met_PBLH                      ',
                                      'Met_PMID                      ',
                                      'Met_PMIDDRY                   ',
                                      'Met_PS1DRY                    ',
                                      'Met_PS1WET                    ',
                                      'Met_PS2DRY                    ',
                                      'Met_PS2WET                    ',
                                      'Met_PSC2WET                   ',
                                      'Met_PSC2DRY                   ',
                                      'Met_T                         ',
                                      'Met_TO3                       ',
                                      'Met_TropHt                    ',
                                      'Met_TropLev                   ',
                                      'Met_TropP                     ',
                                      'Met_TS                        ',
        ::


Converting GEOS-Chem output to mozbc readable format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Use the MATLAB script ``convert_gcoutput_mozart_structure_selected_domain.m`` (`available here <https://github.com/fengx7/WRF-GC-GCC_ICBC/blob/master/convert_gcoutput_mozart_structure_selected_domain.m>`_, GNU Octave may work as well) to merge the GEOS-Chem output files and reconstruct the data structure for ``mozbc`` to read.

Run the script in the GEOS-Chem output directory (``OutputDir``). Modify the script before running as follows:

(a) ``filename_input``: set the input filename as any one of the GEOS-Chem species concentration output files, e.g. ``GEOSChem.SpeciesConc.20150601_0000z.nc4``.

(b) ``filename_output``: set the output filename freely. **If your file is too large, you may want to split the dates into separate files.** In this case, the file names must end in 4-character integers, i.e., ``0001.nc``, ``0002.nc``, ``0003.nc``, ...

(c) ``simulation_4_5``/``simulation_2_25``:

If the resolution of global GEOS-Chem simulation is 2×2.5 degree, please set it as follows:

.. code-block::

        simulation_4_5               = false;
        simulation_2_25              = true;

If the resolution of global GEOS-Chem simulation is 4×5 degree, please set it as follows:

.. code-block::

        simulation_4_5               = true;
        simulation_2_25              = false;

(d) Set the time ranges for output file

.. code-block::

        startyr                      = 2015;
        endyr                        = 2015;
        startmon                     = 6;
        endmon                       = 6;
        startdate                    = 7;
        enddate                      = 21;

(e) Set the domain for output file (needs to be larger than your WRF-GC domain). The subsetting is index-based.

For example, if the resolution of global GEOS-Chem simulation is 2x2.5, longitude indices range from 0 to 144 and correspond to longitudes ``0:2.5:357.5``, latitude indices range from 1 to 91 and correspond to ``-90:2:90``. Then these indices would be set in the script as follows:

.. code-block::

        lon_left                     = 1;  % longitude of western lateral condition
        lon_right                    = 73; % longitude of eastern lateral condition
        lat_bottom                   = 46; % latitude of southern lateral condition
        lat_upper                    = 91; % latitude of northern lateral condition

The netCDF file will be generated after running the script.

.. info::

    If you want to use data from other year / months to run WRF-GC, you can tweak the script to read alternative GEOS-Chem output file names. The time slices in the GEOS-Chem output files is not checked by the script.

.. warning::

    If the script is taking too long to write the netCDF output file, try splitting the file into multiple contiguous date chunks. ``mozbc`` will be able to read and automatically increment the file number, provided they end with four integer digits.

Preparing IC/BC file from CAM-chem/WACCM output
------------------------------------------------

Refer to the WRF-Chem documentation.


Using ``mozbc``
-----------------

Building mozbc (only need to do once)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Download a customized version of mozbc for WRF-GC's hybrid sigma-eta grid.** This is available at `Xu Feng's GitHub, fengx7/mozbc_for_WRFv3.9 <https://github.com/fengx7/mozbc_for_WRFv3.9/>`_

.. code-block::

        git clone https://github.com/fengx7/mozbc_for_WRFv3.9.git mozbc

2. **Go to the mozbc directory downloaded and configure the environment.** Set up the path to your netCDF library

.. code-block::

        export NETCDF_DIR=/path/to/netcdf/here

The content inside ``$NETCDF_DIR`` should have ``include``, ... folders that correspond to netCDF.

3. **Compile mozbc.** Run ``./make_mozbc``.

Configuring mozbc
^^^^^^^^^^^^^^^^^^

Edit the input configuration file ending in ``.inp``, corresponding to the version of GEOS-Chem you are using.

* GEOS-Chem 14.0.0 with Simple SOA: `GEOSCHEM_v14_0_0_SimpleSOA.inp <https://github.com/jimmielin/WRF-GC-GCC_ICBC/blob/master/GEOSCHEM_v14_0_0_SimpleSOA.inp>`_
* GEOS-Chem 13.4.x: `GEOSCHEM_v13_4_0.inp <https://github.com/jimmielin/WRF-GC-GCC_ICBC/blob/master/GEOSCHEM_v13_4_0.inp>`_
* GEOS-Chem 12.8.x: `GEOSCHEM_v12_8_1.inp <https://github.com/fengx7/WRF-GC-GCC_ICBC/blob/master/GEOSCHEM_v12_8_1.inp>`_
* GEOS-Chem 12.2.1: `GEOSCHEM_v12_2_1.inp <https://github.com/fengx7/WRF-GC-GCC_ICBC/blob/master/GEOSCHEM_v12_2_1.inp>`_

Configure the paths to the WRF input in ``dir_wrf`` (``wrfinput_d01``, ``wrfbdy_d01`` ... - **run real.exe to generate these first**) and the source netCDF file for IC/BC (created in step above). **Make sure the paths end in trailing slashes** (``/``)

.. code-block::

        dir_wrf = '/my/path/to/WRF/run/' 
        dir_moz = '/my/path/to/source/data/for/ic-bc/'
        fn_moz  = 'wrfgc_icbc_data_test1.nc'

Run ``mozbc``:

.. code-block::

        ./mozbc < input.inp

.. note::
    If you want to change the species mapping or add new species, please modify the ``spc_map`` in the input file, e.g.: ``'isoprene -> ISOP'`` where "isoprene" is the name of WRF-GC chemical species and "ISOP" is the name of GEOS-Chem species.


If the chemical IC/BC have been successfully written into the ``wrfinput_d<domain>`` and ``wrfbdy_d<domain>`` files, "bc_wrfchem completed successfully" will appear.
