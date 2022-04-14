Preflight Checklist
======================

Here is a list of all the steps that should be performed before running WRF-GC. The specifics are in the getting started guide.

.. warning::
   This is still under construction and being actively updated.

Downloading WRF-GC and input data
-----------------------------------

* **Download the WRF model and the WPS pre-processor.**
* **Download WRF-GC.** Go into the WRF model and delete the ``chem`` folder, then download WRF-GC into ``WRF/chem`` folder.
* **Download the GEOS-Chem input data.** If you already run GEOS-Chem, remember the GEOS-Chem input data path. Otherwise, download `GEOS-Chem data directories <http://wiki.seas.harvard.edu/geos-chem/index.php/Downloading_GEOS-Chem_data_directories>`__. All ``CHEM_INPUTS`` are required, then choose inventories you need for ``HEMCO``.

Compiling WRF-GC
------------------

.. note::
	Your WRF root directory may be ``WRFV3`` or ``WRF``. We use ``WRF`` for consistency.

* **Configure your bash/shell environment**. It should have ``NETCDF``, ``HDF5``, the appropriate ``PATH`` with access to netCDF binaries, and specify the MPI type, etc.
* Go into ``WRF`` and configure to your environment. Run ``./configure -hyb`` (WRF version 3) or ``./configure`` (WRF version 4+). Choose your compiler and ``(dmpar)`` option corresponding to your compiler.
* Go into ``WRF/chem`` and run ``make install_registry``. **This is very important. If you did not do this before the following steps, you have to start over from here.**
* Compile WRF-GC: ``./compile em_real``.

Compiling WPS
--------------

Compile WPS **after** you compile WRF-GC.

Running WRF-GC
----------------

* **Update configuration files to correct paths**. Paths to your GEOS-Chem input data are specified in **three locations**: ``HEMCO_Config.rc``, and twice in ``input.geos``.
* **Update namelist.input to be consistent with namelist.wps**.
* Link the meterology data to your run directory (``ln -sf ../../WPS/met_em* .``)
* Run ``real.exe`` using MPI (e.g., ``mpirun -np $SLURM_NTASKS ./real.exe`` - depending on your cluster configuration you may need to batch this).
* **Create the initial/boundary conditions using ``mozbc`` or another tool.**
* **Run WRF-GC.** Run ``wrf.exe``.