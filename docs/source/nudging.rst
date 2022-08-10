Nudging meteorology
====================

This process is WRF-specific but may be useful for your WRF-GC runs. The namelist options described here are also described in `the WRF User's Guide <https://www2.mmm.ucar.edu/wrf/users/docs/user_guide_V3/user_guide_V3.9/users_guide_chap5.htm#Namelist>`_ 

Grid Nudging using input FNL data
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

Nudging using surface and upper-air observations
------------------------------------------------

Coming soon.