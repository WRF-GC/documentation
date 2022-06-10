Domain, meteorology, and configuration
======================================

.. warning::
	Coming soon - please refer to the PDF User's Guide for this section for now.


This section discusses:

* Setting up the domain using WPS's ``geogrid.exe`` tool.
* Processing the meteorological initial and boundary conditions by downloading, running WPS's ``ungrib.exe``, and ``metgrid.exe``.
* Basic configuration of WRF-GC using the ``namelist.input``.
* Using WRF's ``real.exe`` to prepare input before adding in chemical initial/boundary conditions.

.. note::
	The WRF Pre-Processor can be learned best from the `WRF User's Guide <https://www2.mmm.ucar.edu/wrf/users/docs/user_guide_V3/user_guide_V3.9/users_guide_chap3.html>`_ , as this is not specific to chemistry.

Setting up the domain using GEOGRID
-------------------------------------

Downloading meteorological data
--------------------------------

Setting up Vtable
------------------

Depending on the meteorological data, the appropriate ``Vtable`` needs to be linked...

Running UNGRIB and METGRID
---------------------------

1. Link GRIB files - ``./link_grib.csh gfs*``
2. Run ``./ungrib.exe``, then ``./metgrid.exe``.

Configuring WRF-GC - ``namelist.input``
----------------------------------------

Configuring WRF-GC - ``input.geos``
------------------------------------

**Most** input.geos options known by GEOS-Chem users are not configured in input.geos in WRF-GC, and are instead controlled by ``namelist.input``. Only two exceptions: the path to ``CHEM_INPUTS`` needs to be specified in:

.. code-block::
	
	Root data directory     : /n/holyscratch01/external_repos/GEOS-CHEM/gcgrid/data/ExtData/

and

.. code-block::

	%%% PHOTOLYSIS MENU %%% :
	FAST-JX directory       : /n/holyscratch01/external_repos/GEOS-CHEM/gcgrid/data/ExtData/CHEM_INPUTS/FAST_JX/v2021-10/

**Most other options in input.geos for WRF-GC are ignored.**

Configuring WRF-GC - emissions in ``HEMCO_Config.rc``
------------------------------------------------------

Configuration of HEMCO is exactly the same as the GEOS-Chem model. Remember to update the HEMCO data path in this configuration file:

.. code-block::

	ROOT:                        /n/holyscratch01/external_repos/GEOS-CHEM/gcgrid/data/ExtData/HEMCO

.. note::
	A reminder about ``input.geos``, ``HEMCO_Config.rc``, and ``namelist.input`` configuration files - **these files are replaced every time the WRF model is recompiled** (when ``./compile em_real`` is ran). **Please remember to back up your configuration files!**

Running ``real.exe``
---------------------

After configuring, run ``real.exe``. This is a memory and compute intensive operation - if you are on a cluster, you will need to submit a batch job like you would do when running other models. Otherwise, run

.. code-block::

	mpirun -np 32 ./real.exe

Where "32" would be the number of cores. The output can be watched by ``tail -f rsl.out.0000`` and any errors would be in ``rsl.error.0000``.