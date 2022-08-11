Preparing your system
======================

This section discusses:

* Required system **libraries** for running WRF-GC.
* Required **common input data** for running WRF-GC.

**The steps in this page only need to be run once, and generally do not need to be re-done unless WRF-GC version updates.**

Software requirements
----------------------

You will need a **Linux** system with the following compilers, libraries, and tools:

* **Compiler:** Intel (version 15 or above), or gfortran.
* **MPI Library:** MVAPICH2 (version 2.3 or above), OpenMPI, or Intel MPI.
* zlib, hdf5 (version 1.8 or above), netCDF-C (version 4.6.1 or above), netCDF-Fortran (version 4.4.4 or above), JasPer (version 1.900)
* Git version management

If you already run GEOS-Chem, you may already have met the compiler and netCDF requirements.

Below are some specific guidance, but if you already know how to set up libraries, point WRF-GC to them in the environment configuration file, editing as necessary.

**See :ref:`Environmental configuration file (for reference)` for all the environmental variables that need to be defined.**


Running on a cluster
^^^^^^^^^^^^^^^^^^^^^

Your system administrator may have installed these packages. For example, on the Harvard "Cannon" cluster, the following libraries are used:

.. code-block::

	module load git/2.17.0-fasrc01
	module load intel/17.0.4-fasrc01
	module load openmpi/2.1.0-fasrc02
	module load netcdf/4.5.0-fasrc02
	module load netcdf-fortran/4.4.4-fasrc06
	module load jasper/1.900.1-fasrc02

.. note::
	**Special note about the netCDF libraries.** Since version 4, netCDF has been split into "netCDF-C" and "netCDF-Fortran". **Both of these are required for WRF-GC**, and WRF expects them to be in the same folder. This is problematic in some clusters, as they may store ``netcdf`` and ``netcdf-fortran`` in different paths. The solution is to create your own paths, e.g., ``~/wrf-gc/include``, ``~/wrf-gc/bin``, and ``~/wrf-gc/lib``, and link the netCDF-C and netCDF-Fortran files into these folders respectively. e.g.,

	.. code-block::
		ln -sf $NETCDF_HOME/lib64/* lib/
		ln -sf $NETCDF_FORTRAN_HOME/lib/* lib/
		ln -sf $NETCDF_HOME/bin/* bin/
		ln -sf $NETCDF_FORTRAN_HOME/bin/* bin/
		ln -sf $NETCDF_HOME/include/* include/
		ln -sf $NETCDF_FORTRAN_HOME/include/* include/

Then see the environment configuration above to point WRF-GC to the libraries.

Running on AWS or with Spack
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some of the package setup from `Haipeng's guide on WRF-GC on AWS <https://jimmielin.me/2019/wrf-gc-aws/>`_ may be helpful.

Running on your own system
^^^^^^^^^^^^^^^^^^^^^^^^^^

Compile libraries in the following order:

* Install the compiler
* Install MPI (e.g., MVAPICH2)
* Install zlib
* Install JasPer
* Install HDF5
* Install netCDF-C
* Install netCDF-Fortran

When configuring these libraries, specify the install location somewhere, e.g.:

.. code-block::

	./configure --prefix=/home/example/wrf-gc

The general process to install libraries is to run ``configure``, then ``make``, then ``make install``, then ``make check`` to make sure it is working.

Then see the environment configuration above to point WRF-GC to the libraries.

Data requirements
------------------

GEOS-Chem shared inputs ("ExtData")
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
	If someone on your cluster / system already runs GEOS-Chem, you may have the data already. If so, you may be able to skip all of the below steps.

Download the GEOS-Chem input data directories, specifically ``HEMCO`` and ``CHEM_INPUTS``. For ``HEMCO`` they are very large, and you only need to download folders corresponding to the simulation year(s) you expect to run.

Refer to the GEOS-Chem User's Guide:
* `Downloading data from WashU <http://wiki.seas.harvard.edu/geos-chem/index.php/Downloading_data_from_WashU>`_

WRF-GC needs ``ExtData/HEMCO/`` and ``ExtData/CHEM_INPUTS/``.

If you are running GEOS-Chem as well (e.g., for making WRF-GC boundary / initial conditions), you also need some meteorology fields, etc. Refer to the GEOS-Chem User's Guide.

.. _wps-input-data:

WRF Pre-Processor Geographical Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download the **required** geographical input data for WRF.

* For WRF version 3, visit `this page <https://www2.mmm.ucar.edu/wrf/users/download/get_sources_wps_geog_V3.html>`_
* For WRF version 4 and above, visit `this page <https://www2.mmm.ucar.edu/wrf/users/download/get_sources_wps_geog.html#mandatory>`_

For high-resolution simulations, we recommend downloading "Download Highest Resolution of each Mandatory Field". This takes approximately ~50 GB of disk space.

Environmental configuration file (for reference)
-------------------------------------------------

Below is an example environment file using the Intel compilers + OpenMPI. The following need to be edited to fit your system:

* ``NETCDF`` needs to point to your netCDF install (inside this path there should be ``bin``, ``lib``, ``include`` for both NetCDF-C and NetCDF-Fortran)
* ``JASPERLIB`` needs to point to your JasPer install's ``lib`` folder
* ``JASPERINC`` needs to point to your JasPer install's ``include`` folder
* ``NETCDF_HOME`` and ``NETCDF_FORTRAN_HOME`` point to NetCDF-C and NetCDF-Fortran. Can be the same as ``$NETCDF``

If you are using the GNU compilers (``gcc`` and ``gfortran``), you also need to edit:

* ``CC=gcc``, ``CXX=gcc``, ``FC=gfortran``, ``ESMF_COMPILER=gfortran``

If you are using other MPI libraries, you also need to edit:

* ``ESMF_COMM`` to ``openmpi``, ``mvapich2``, or ``intelmpi``.
* If your system has weird, non-standard MPI installations, you may need to manually edit WRF-GC's ``chem/Makefile``.

.. code-block::

	export CC=icc
	export OMPI_CC=$CC

	export CXX=icpc
	export OMPI_CXX=$CXX

	export FC=ifort
	export F77=$FC
	export F90=$FC
	export OMPI_FC=$FC
	export COMPILER=$FC
	export ESMF_COMPILER=intel

	# MPI Communication
	export ESMF_COMM=openmpi
	export MPI_ROOT=$MPI_HOME

	export NETCDF=/n/holyscratch01/jacob_lab/hplin/wrfgc
	export NETCDF_HOME=$NETCDF
	export NETCDF_FORTRAN_HOME=$NETCDF
	export JASPERLIB=$JASPER_HOME/lib64
	export JASPERINC=$JASPER_HOME/include

	# WRF options
	export WRF_EM_CORE=1
	export WRF_NMM_CORE=0
	export WRF_CHEM=1

	# needed forwrfv4
	export NETCDF_classic=1

	# GC extras (only for GC not WRF-GC)
	export OMP_STACKSIZE=1000000000
	export KMP_STACKSIZE=$OMP_STACKSIZE

	# Base paths
	export GC_BIN="$NETCDF_HOME/bin"
	export GC_INCLUDE="$NETCDF_HOME/include"
	export GC_LIB="$NETCDF_HOME/lib"

	# If using NetCDF after the C/Fortran split (4.3+), then you will need to
	# specify the following additional environment variables
	export GC_F_BIN="$NETCDF_FORTRAN_HOME/bin"
	export GC_F_INCLUDE="$NETCDF_FORTRAN_HOME/include"
	export GC_F_LIB="$NETCDF_FORTRAN_HOME/lib"