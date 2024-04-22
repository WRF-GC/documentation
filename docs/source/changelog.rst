Changelog
==========

v3.0 (April 22, 2024)
---------------------
* Feature: Supports **GEOS-Chem 14.1.1**, **KPP 3.0.0**, and **HEMCO 3.6.2**.
* Feature: Supports **WRF version 4.4**.
* Feature: Infrastructure for specialty simulations. Now can install couplers for fullchem, ch4, and co2 using the ``install_registry`` command.
* Feature: Add support for History diagnostics and HEMCO diagnostics ("WRF-GC 3.0 Diagnostics") using pNETCDF.
* Technical Update: Compiles GEOS-Chem 13+ without using CMake by maintaining the legacy GNU infrastructure.
* Technical Update: Auto-patching of ``wrf_io.F90`` to support more than 3,000 variables in ``wrfbdy``.
* Technical Update: No longer inputs initial/boundary conditions for non-advected species through ``i0{12}`` switch in ``registry.chem``.
* Enhancement: Recompile no longer wipes configuration files by automatically calling ``make install_configs``. Configuration files are installed **once** using ``make install_registry`` or others for specialty simulations.
* Enhancement: New coupler species generation infrastructure shared with CESM2-GC.
* Enhancement: Support for ``QV2M`` met field for online blowing snow emissions.
* Bugfix: Fix stack corruption issue in ``chemics_init`` coordinates.
* Bugfix: More robust support for ``get_last_gas`` due to WRFv4 upstream updates.
* Bugfix: Month-boundary HEMCO emissions missing timesteps.
* Bugfix: ParaNOx stability issue via upstream GEOS-Chem 14.0.1 fix. Note that according to `Colombi et al., 2023 ACP <https://acp.copernicus.org/articles/23/4031/2023/>`_ it may not be necessary to use ParaNOx for high-resolution simulations with WRF-GC.
* Bugfix: Initial condition input bug for nested domain(s).


v2.0.2 (September 30, 2022)
----------------------------
* Bugfix: Initial condition input bug for nested domain(s). (Backport)

v2.0.1 (September 16, 2021)
----------------------------
* Bugfix: Boundary conditions incorrect dimension. (Regressed bug)

v2.0 (April 7, 2020)
---------------------
* **Feng et al., 2021 GMD release.**
* Feature: Support **GEOS-Chem 12.7.2, 12.6.3**.
* Feature: Nested domain functionality.
* Feature: Aerosol-radiation interactions and aerosol-cloud interactions.
* Feature: Lightning NOx emissions.
* Enhancement: Intel MPI support.
* Bugfix: MPI issue for HEMCO masks.
* Bugfix: Regridding bug causing striped artifacts in MPI CPU boundaries.

2020 Technology Preview (December 28, 2019)
--------------------------------------------
* Feature: Experimental nested domain functionality.
* Feature: Initial version of aerosol-radiation interactions and aerosol-cloud interactions.

v0.92 (January 2, 2021)
-----------------------
* Bugfix: Fix for HEMCO 3.0 (Lin et al., 2021 GMD) supporting vertical regridding of emissions data. (Backport)

v0.91 (July 6, 2020)
--------------------
* Bugfix: Boundary conditions incorrect dimension.

v0.9-hotfix (August 6, 2019)
-----------------------------
* Bugfix: Support Intel 2017 compilers.

v1.0 (June 19, 2019)
--------------------
* **Lin et al., 2020 GMD release. (First stable release)** Released August 2, 2019 as **v0.9**.
* Feature: Support **GEOS-Chem 12.2.1**.
* Enhancement: Support OpenMPI.
* Enhancement: Experimental support for GNU compilers.
* Bugfix: PEDGE incorrect values, surface pressure too low.
* Bugfix: Boundary conditions input.

v0.11 (May 7, 2019)
-------------------
* Bugfix: AREA_M2 heap overflow.

v0.1 (Beta 1) (December 8, 2018)
--------------------------------
* Bugfix: Landmap, convection, meteorology field conversion.
* Bugfix: Double emissions due to tendency application.

Alpha 6 (November 22, 2018)
---------------------------
* Enhancement: Significantly faster coupler.

Alpha 5 (November 14, 2018)
---------------------------
* Feature: Support ntiedtke scheme.
* Feature: WRF-GC performance timers.

Alpha 4 (November 12, 2018)
---------------------------
* Bugfix: HEMCO projection issues.

Alpha 3 (October 26, 2018)
--------------------------
* Feature: Support **GEOS-Chem 12.1.0**.

Alpha 2 (October 11, 2018)
--------------------------
* Feature: Partial support for GEOS-Chem "netCDF" diagnostics (now History diagnostics)

Alpha 1 (August 15, 2018)
--------------------------
* Feature: Support for out-of-the-box GEOS-Chem 12.0.0, changes made in collaboration with GCST.

Alpha 0 (July 2018)
-------------------
* Bugfix: Convection fixes.

GCA1 Technology Preview (April 2018)
------------------------------------
* First ever release of WRF-GC defining the isolated coupler and source code infrastructure.
* Feature: Supports **GEOS-Chem v11-02c**.
* Feature: Supports **WRF 3.9.1.1**.
