Nudging meteorology
====================

This process is WRF-specific but may be useful for your WRF-GC runs. The namelist options described here are also described in `the WRF User's Guide <https://www2.mmm.ucar.edu/wrf/users/docs/user_guide_V3/user_guide_V3.9/users_guide_chap5.htm#Namelist>`_ 

Nudging using input FNL data
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

To change whether winds, temperature, and/or water vapor are nudged you can change ``if_no_pbl_nudging_uv`` (``t`` or ``q``.)

2. **Re-run ``real.exe``.** This will generate ``wrffdda_d<domain>`` files in your run directory.
3. **Run ``wrf.exe``.**

Nudging using surface and upper-air observations
------------------------------------------------

Coming soon.