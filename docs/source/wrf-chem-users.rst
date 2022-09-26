For WRF-Chem Users
===================

.. note::

	**If you are a WRF-Chem user but you have found this page through search, congratulations!** WRF-GC is a model just like WRF-Chem, but uses chemistry provided
	by the `GEOS-Chem <https://geos-chem.seas.harvard.edu/>`_ chemical model instead of the chemical schemes in WRF. `Learn more about WRF-GC <https://fugroup.org/index.php/WRF-GC>`_.

This page details some differences (such as advantages) of WRF-GC compared to WRF-Chem. It may be useful to existing WRF-Chem users,
**because the running workflow of WRF-GC is very similar and you can get up and running quickly.**

Major differences to WRF-Chem
------------------------------

* WRF-GC only supports one chemistry option provided by GEOS-Chem, using ``chem_opt = 233``. WRF-GC must be downloaded separately, **replacing** the ``chem`` folder under ``WRF``. See :doc:`/guide-2-downloading`.
* WRF-GC does **not** use off-line emissions, instead using on-line emissions computed by `HEMCO <https://github.com/geoschem/HEMCO>`_. You do **not** need to pre-process any emissions data anymore, and can simply configure emissions using a text file. Most inventories, such as CEDS, MIX, NEI, EDGAR, are available out-of-the-box. MEIC emissions for China, etc. are also developed by other groups. WRF-GC is fully compatible with any emission files used by GEOS-Chem users.

WRF-Chem has X feature, does WRF-GC have it?
---------------------------------------------

* **Support for WRF physical/dynamics options...** *Maybe*. But this is also a *maybe* in WRF-Chem. See :doc:`/guide-4-wps-domain-real` for a table with supported options.
* **Nested domains?** Yes.
* **Aerosol-radiation and aerosol-cloud interactions?** Yes, using GEOS-Chem aerosols. `Feng et al., 2021 GMD <https://doi.org/10.5194/gmd-14-3741-2021>`_ describes this capability.
* **Restarts?** Yes.
* **Nudging?** Yes. See :doc:`/nudging`.
* **Initial/boundary conditions?** Yes, from GEOS-Chem global outputs. See :doc:`/icbc`. We used to support CAM-chem and MOZART4GEOS5 outputs used by WRF-Chem, but this support is deprecated. We recommend running global GEOS-Chem instead. But we use a modified but similar version of ``mozbc``, so you can use CAM-chem/MOZART4GEOS5 outputs at your own risk.

Do I have to run WRF and GEOS-Chem separately?
-----------------------------------------------

**No**, WRF-GC is an online coupled model just like WRF-Chem. Compile them together, run them together.

Does GEOS-Chem output separately?
----------------------------------

**No**, species are written to the ``wrfout_d0...`` files like WRF-Chem. Species names are different, and generally are the same as GEOS-Chem.

Can I use offline emissions like WRF-Chem?
-------------------------------------------

**No**, only HEMCO can be used when GEOS-Chem chemistry is used.

Can I run WRF-GC and WRF-Chem in the same WRF install?
-----------------------------------------------------

**No**, they must be installed separately. WRF-GC removes all the existing chemistry in WRF-Chem.

I'm sold! How do I get started quickly, as a WRF-Chem user?
-------------------------------------------------------------

* You need some GEOS-Chem input files, see :doc:`/guide-1-system-requirements`. The libraries required for WRF-GC are completely covered by WRF-Chem, so you can reuse the computational environment.
* You need to replace the ``chem`` folder with WRF-GC, see :doc:`/guide-2-downloading`. Then ``./configure -hyb`` (WRFv3) or ``./configure`` (WRFv4), **then you must go to** ``chem`` and run ``make install_registry``, *then* go back and ``./compile em_real``.
* Everything is configured in ``namelist.input``, set ``chem_opt=233``.
* No need to prepare emissions input files manually using prep_chem_sources or whatever - HEMCO will do it. Configure emissions using a text file in ``run/HEMCO_Config.rc``.
* Simply run WRF-GC like before - ``real.exe``, do initial/boundary conditions with our mozbc (:doc:`/icbc`), then ``wrf.exe`` and off you go.
