Lightning NOx emissions
========================

Lightning NOx emissions are supported in WRF-GC v2.0 through HEMCO nad WRF lightning schemes.

To turn on the lightning NOx emissions in WRF-GC v2.0, you should turn on the lightning scheme in WRF-GC. The lightning NOx emissions are highly dependent on the flash rate simulated by WRF model.

Two lightning schemes are supported in WRF-GC:

* PR92 (Price and Rind, 1992) based on maximum w
* PR92 based on 20 dBz top

Please set the options in the configuration file (``namelist.input``) as follows:

.. code-block::

	&physics
	lightning_option                     = 2,
	lightning_dt                         = 120,
	lightning_start_seconds              = 600,
	cellcount_method                     = 0,
	iccg_method                          = 2,
	do_radar_ref                         = 1,
	/

