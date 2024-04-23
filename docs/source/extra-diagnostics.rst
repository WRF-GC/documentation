Additional diagnostics
=======================

For WRF-GC 3.0
---------------
Since WRF-GC 3.0, we reimplement the GEOS-Chem diagnostics (specified in ``HISTORY.rc``) and HEMCO diagnostics (specified in ``HEMCO_Diagn.rc`` and ``HEMCO_Config.rc``).
To enable WRF-GC 3.0 diagnostics, you need to install and define ``PNETCDF`` in your environment configuration file **before** you compile WRF-GC.

For HISTORY.rc we currently support attributes:

- template
- frequency
- duration
- mode

Not supported:

- LON_RANGE
- LAT_RANGE
- levels

For more information about ``History diagnostics``, please refer to the `GEOS-Chem documentation <https://wiki.seas.harvard.edu/geos-chem/index.php/Overview_of_History_diagnostics>`_.

.. note::
	``SpeciesConc`` collection in GEOS-Chem is still output through ``wrfout``, it is not available in ``HISTORY.rc``. Turning on this collection in ``HISTORY.rc`` may cause errors. 

For HEMCO diagnostics, we current only support ``instantaneous`` mode, for more information, please refer to `HEMCO diagnostics <https://hemco.readthedocs.io/en/stable/hco-ref-guide/diagnostics.html>`_.

Legacy (WRF-GC 2.0) diagnostics output method conflicts with the new functionality and has been commented out. If you wish to use it, you can uncomment in ``wrfgc_convert_state_mod.F``, although they are considerably more limited than the new functionality.

For WRF-GC 2.0
----------------
By default, WRF-GC 2.0 outputs **all instantaneous species mixing ratios (ppmv)** at the output frequency (``history_interval`` in ``namelist.input``). However, other diagnostics provided by GEOS-Chem may be useful for your research. We document some methods to write GEOS-Chem diagnostics in WRF-GC.

.. note::
	Because WRF-GC uses WRF as output, GEOS-Chem diagnostics (specified in ``HISTORY.rc``) are unavailable in WRF-GC. But they can be written using some light code editing.

Limited support for GEOS-Chem diagnostics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following GEOS-Chem diagnostics (from `the GEOS-Chem netCDF/History diagnostics list <http://wiki.seas.harvard.edu/geos-chem/index.php/Collections_for_History_diagnostics>`_) are supported in a limited way:

.. list-table:: Limited GEOS-Chem diagnostics supported
   :widths: 50 25 25
   :header-rows: 1

   * - Diagnostic name
     - GEOS-Chem name
     - WRF-GC name (output)
   * - Cloud convection flux
     - ``CloudConvFlux``
     - ``cldcnvflx_n#``
   * - Budget: Emissions and Dry deposition
     - ``BudgetEmisDryDep``
     - ``gcemisdrydep_<area>_n#``
   * - Budget: Boundary layer mixing
     - ``BudgetMixing``
     - ``gcmixing_<area>_n#``
   * - Budget: Convection
     - ``BudgetConvection``
     - ``gcconv_<area>_n#``
   * - Budget: Chemistry
     - ``BudgetChemistry``
     - ``gcchem_<area>_n#``
   * - Budget: Wet deposition
     - ``BudgetWetDep``
     - ``gcwetdep_<area>_n#``
   * - Fraction of soluble species lost in convective updrafts
     - ``WetLossConvFrac``
     - ``wetlscnvfrc_n#``
   * - Loss of soluble species in convective updrafts
     - ``WetLossConv``
     - ``wetlscnv_n#``
   * - Loss of soluble species in large-scale precipitation
     - ``WetLossLS``
     - ``wetlossls_n#``

* For ``<area>`` corresponding to the "Budget" diagnostic series, this can be ``full`` (full column), ``trop`` (troposphere), and ``pbl`` (boundary layer).
* For ``n#``, **only four species are supported in WRF-GC**. The species IDs corresponding to the four species chosen for diagnostic output are specified in ``namelist.input``:

.. code-block::

	 gc_diagn_spc_n0                     = 0,
	 gc_diagn_spc_n1                     = 0,
	 gc_diagn_spc_n2                     = 0,
	 gc_diagn_spc_n3                     = 0,

The species list corresponding to their IDs can be obtained in the ``rsl.out.0000`` log by setting ``namelist.input``'s ``debug_level`` to ``5``, and it will be output after the first time step (search for ``%%%%%% WRFGC_Convert_State_Mod Chemistry State Export %%%%%%``). (Remember to set the debug level back to a lower level or your model will run slow!)


Writing custom diagnostics from the GEOS-Chem/HEMCO models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please refer to `Haipeng's website on outputting extra diagnostics <https://jimmielin.me/2020/wrfgc-extra-diags/>`_ for now. We will migrate this page later.

