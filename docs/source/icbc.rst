Generating Initial/Boundary Conditions (IC/BC)
===============================================

WRF-GC is a regional model. Boundary conditions from a global model are generally required. Initial conditions can be provided by a WRF-GC run or other global models.

You can use MOZART4-GEOS5, CAM-chem, or GEOS-Chem as input for initial/boundary conditions.

The general process is as follows:

* Identify which data source you want to use as ic/bc.
* Set-up WRF-GC, and run ``real.exe`` to generate ``wrfinput_d01`` (initial conditions), and ``wrfbdy_d01`` (boundary conditions)
* Prepare ic/bc inputs into a netCDF format accepted by ``mozbc``. (`mozbc for WRF-GC is located here <https://github.com/fengx7/mozbc_for_WRFv3.9>`_)
* Use `mozbc` to add these inputs to ``wrfinput_d01`` and/or ``wrfbdy_d01`` files.
* Run the WRF-GC model.

Preparing IC/BC file from sources
----------------------------------

Using global GEOS-Chem output as IC/BC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Details are available in the PDF getting started guide. `A MATLAB script <https://github.com/fengx7/WRF-GC-GCC_ICBC>`_ will process global GEOS-Chem outputs to netCDF files accepted by ``mozbc``, which are then generated into WRF(-GC) initial/boundary files.

1. **Run the GEOS-Chem standard full-chemistry/tropchem simulation at a resolution of 2×2.5/4×5 degree (2×2.5 degree recommended).** The running time must cover the WRF-GC simulation period: e.g. if the simulation period of WRF-GC is from 2015-06-10 00:00:00 to 2015-06-20-00:00:00 (UTC), the time ranges for GEOS-Chem can be from 2015-06-07 00:00:00 to 2015-06-21 00:00:00 (UTC). Output the netCDF diagnostic files every 6 hours (00, 06, 12, 18), including

(a) ``GEOSChem.SpeciesConc.xxxxxxxxxxxxxx.nc4`` (contains **instantaneous** ``SpeciesConc_?ADV?``)

(b) ``GEOSChem.StateMet.xxxxxxxxxxxxxx.nc4`` (contains ``Met_PS1DRY``).

2. **Use the MATLAB script** ``convert_gcoutput_mozart_structure_selected_domain.m`` to merge the GEOS-Chem output files and reconstruct the data structure for ``mozbc`` to read.

Run the MATLAB script in the GEOS-Chem output file directory. Modify the script before running as follows:

(a) ``filename_input``: set the input filename as any one of the GEOS-Chem species concentration output files, e.g.     
    ``GEOSChem.SpeciesConc.20150601_0000z.nc4``.

(b) ``filename_output``: set the output filename freely.

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

(e) Set the domain for output file (needs to be larger than your WRF-GC domain)

If the resolution of global GEOS-Chem simulation is 2x2.5:

longitude: 0 (index 1):2.5:357.5 (index 144)
latitude: -90 (index 1):2:90 (index 91)

Here is an example:

.. code-block::

        lon_left                     = 1;  % longitude of western lateral condition
        lon_right                    = 73; % longitude of eastern lateral condition
        lat_bottom                   = 46; % latitude of southern lateral condition
        lat_upper                    = 91; % latitude of northern lateral condition

The netCDF file will be generated after running the script.

3. **Run mozbc using the generated file.** We provide mozbc input files ``GEOSCHEM_v12_2_1.inp`` and ``GEOSCHEM_v12_8_1.inp``, which contain the default advected species (``SpeciesConc_?ADV?``) of GEOS-Chem v12.2.1 or GEOS-Chem v12.8.1. If you want to change the species, please modify the ``spc_map`` in the input file, e.g.

.. code-block::

    'isoprene -> ISOP'

where "isoprene" is the name of WRF-GC chemical species and "ISOP" is the name of GEOS-Chem species.

If the chemical IC/BC have been successfully written into the ``wrfinput_d<domain>`` and ``wrfbdy_d<domain>`` files, "bc_wrfchem completed successfully" will appear.

Using MOZART4-GEOS5/WACCM as IC/BC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
