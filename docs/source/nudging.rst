Nudging meteorology
====================

This process is WRF-specific but may be useful for your WRF-GC runs. The namelist options described here are also described in `the WRF User's Guide <https://www2.mmm.ucar.edu/wrf/users/docs/user_guide_V3/user_guide_V3.9/users_guide_chap5.htm#Namelist>`_ 

Grid nudging using input FNL data
----------------------------

1. Add the following lines to your ``namelist.input``, into a new section ``&fdda`` as shown below:

.. code-block::

	&fdda
	 grid_fdda                           =   1,    1,    1,
	 gfdda_inname                        = "wrffdda_d<domain>",
	 gfdda_interval_m                    = 360,  360,  360,
	 gfdda_end_h                         = 9999, 9999, 9999,
	 io_form_gfdda                       =   2,
	 fgdt                                =   0,    0,   0,
	 if_no_pbl_nudging_uv                =   1,    1,   1,
	 if_no_pbl_nudging_t                 =   1,    1,   1,
	 if_no_pbl_nudging_q                 =   1,    1,   1,
	 if_zfac_uv                          =   1,    1,   1,
	 k_zfac_uv                           =  10,   10,  10,
	 if_zfac_t                           =   0,    0,  10,
	 k_zfac_t                            =  10,   10,  10,
	 if_zfac_q                           =   0,    0,   0,
	 k_zfac_q                            =  10,   10,  10,
	 guv                                 = 0.0003, 0.0003, 0.0003,
	 gt                                  = 0.0003, 0.0003, 0.0003,
	 gq                                  = 0.0003, 0.0003, 0.0003,
	 if_ramping                          = 0,
	 dtramp_min                          = 60.0
	 /

The configuration options you need to change with a brief description are listed below.

* ``grid_fdda`` (per-domain): 0 for grid analysis nudging off; 1 for grid analysis nudging on.
* ``gfdda_inname``: name of fdda input file (``wrffdda_d<domain>``) that will be generated when running real.exe.
* ``gfdda_interval_m`` (per-domain): time interval (in mins) for NCEP FNL analysis times.
* ``gfdda_end_h`` (per-domain): time (in hours) to stop nudging after the start of the simulation.
* ``io_form_gfdda``: analysis data format (2 for netCDF format).
* ``fgdt`` (per-domain): calculation frequency (in mins) for analysis nudging; 0 = every time step (recommended).
* ``if_no_pbl_nudging_uv/if_no_pbl_nudging_t/if_no_pbl_nudging_q`` (per-domain): 0 for nudging in the PBL; 1 for no nudging of uv-winds/air temperature/water vapor in the PBL.
* ``if_zfac_uv/if_zfac_t/if_zfac_q`` (per-domain): 0 for nudge uv-winds/air temperature/water vapor in all layers; 1 for limit nudging to levels above ``k_zfac_uv\k_zfac_t\k_zfac_q``.
* ``k_zfac_uv/k_zfac_t/k_zfac_q`` (per-domain): model level below which nudging is switched off for uv-winds/air temperature/water vapor.
* ``guv/gt/gq`` (per-domain): nudging coefficient for uv-winds/air temperature/water vapor (s-1).
* ``if_ramping``: 0 for nudging ends as a step function; 1 for ramping nudging down at the end of the period.
* ``dtramp_min``: time (in mins) for ramping function. 

To change whether winds, air temperature, and/or water vapor are nudged you can change ``if_no_pbl_nudging_uv`` (``t`` or ``q``.)

2. **Re-run real.exe.** This will generate ``wrffdda_d<domain>`` files in your run directory.
3. **Run wrf.exe.**

Analysis nudging using surface and upper-air observations
------------------------------------------------

1. Downloading surface and upper air observation data in rda.ucar.edu (ds461.0 and ds351.0).

(a) `Upper air observational data <https://rda.ucar.edu/datasets/ds351.0/#!description>`_
(b) `Surface observational data <https://rda.ucar.edu/datasets/ds461.0/#!description>`_

2. Compiling ``obsgrid.exe`` and ``get_rda_data.exe``.

(a) To compile ``obsgrid.exe``, please refer to `OBSGRID Github <https://github.com/wrf-model/OBSGRID>`_. If successful, this will generate the executable ``obsgrid.exe``. 

.. code-block::

   git clone https://github.com/wrf-model/OBSGRID.git OBSGRID
   ./configure
   ./compile


(b) To compile ``get_rda_data.exe``, please refer to OBSGRID/util/get_rda_data.f.

.. code-block::

   cd OBSGRID/util
   ifort -FR get_rda_data.f -o get_rda_data.exe

3. Using ``combineSurfaceToObs.sh`` to combine the downloaded files ``SURFACE_OBS:YYYYMMDDHH`` and ``OBS:YYYYMMDDHH`` into new files (e.g. ``C_OBS:YYYYMMDDHH``). This script is available in Github `WRF_Nudging <https://github.com/fengx7/WRF_Nudging>`_.

4. Using ``combineCobsToRdaobs.sh`` to combine those new files (``C_OBS:YYYYMMDDHH``) into ``rda_obs``. This script is available in Github `WRF_Nudging <https://github.com/fengx7/WRF_Nudging>`_.

5. Using ``get_rda_data.exe`` to generate files (``OBS:YYYY-MM-DD-HH``) for obsgrid.exe.

6. Setting up the options in configuration file (``namelist.oa``). Here is an example of `OBSGRID Namelist <https://github.com/fengx7/WRF_Nudging>`_ for running obsgrid.exe.

7. Running ``obsgrid.exe``. This will generate files ``metoa_em*`` and ``wrfsfdda_d01``. Please note that ``obsgrid.exe`` needs to be run after ``metgrid.exe``. The files ``met_em*`` must be available in OBSGRID/ directory. 

.. code-block::
   
   ./obsgrid.exe >& obsgrid.out