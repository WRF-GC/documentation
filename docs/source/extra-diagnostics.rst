Additional diagnostics
=======================

By default, WRF-GC outputs **all instantaneous species mixing ratios (ppmv)** at the output frequency (``history_interval`` in ``namelist.input``). However, other diagnostics provided by GEOS-Chem may be useful for your research. We document some methods to write GEOS-Chem diagnostics in WRF-GC.

.. note::
	Because WRF-GC uses WRF as output, GEOS-Chem diagnostics (specified in ``HISTORY.rc``) are unavailable in WRF-GC. But they can be written using some light code editing.

Limited support for GEOS-Chem diagnostics
------------------------------------------

The following GEOS-Chem diagnostics are supported in a limited way:

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
-----------------------------------------------------------

Please refer to `Haipeng's website on outputting extra diagnostics <https://jimmielin.me/2020/wrfgc-extra-diags/>`_ for now. We will migrate this page later.