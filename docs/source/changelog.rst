Changelog
==========

2022 Technology Preview - work in progress
------------------------------------------
* *Currently unreleased*. This technology preview is targeting a 3.0 release.
* Feature: Supports **GEOS-Chem 14.0.0.rc.3** and **HEMCO 3.5.0**.
* Feature: Supports **WRF version 4.4**.
* Feature: Infrastructure for specialty simulations. Now can install couplers for fullchem, ch4, and co2 using the ``install_registry`` command.
* Feature: Compiles GEOS-Chem 13+ without using CMake by maintenance of the legacy GNU infrastructure.
* Enhancement: Recompile no longer wipes configuration files by automatically calling ``make install_configs``. Configuration files are installed **once** using ``make install_registry`` or others for specialty simulations.
* Enhancement: New coupler species generation infrastructure shared with CESM2-GC.
* Enhancement: Support for ``QV2M`` met field for online blowing snow emissions.
* Bugfix: Fix stack corruption issue in ``chemics_init`` coordinates.
* Bugfix: More robust support for ``get_last_gas`` due to WRF upstream updates.
* Bugfix: Month-boundary HEMCO emissions missing timesteps.
* Bugfix: ParaNOx stability issue via upstream GEOS-Chem 14.0.1 fix.

v2.0.1 (September 16, 2021)
----------------------------
* Bugfix: Boundary conditions incorrect dimension.

v2.0 (April 7, 2020)
---------------------
* **Feng et al., 2021 GMD release.** Formerly *2020 Technology Preview*.
* Feature: Support **GEOS-Chem 12.7.2, 12.6.3**.
* Feature: Nested domain functionality.
* Feature: Aerosol-radiation interactions and aerosol-cloud interactions.
* Feature: Lightning NOx emissions.
* Enhancement: Intel MPI support.
* Bugfix: MPI issue for HEMCO masks.
* Bugfix: Regridding bug causing striped artifacts in MPI CPU boundaries.

v1.1-twoway (December 28, 2019)
--------------------------------
* Feature: Aerosol-radiation interactions and aerosol-cloud interactions.

v1.0 (June 19, 2019)
--------------------
* **First stable release, Lin et al., 2020 GMD.**
* Feature: Support **GEOS-Chem 12.2.1**.
* Bugfix: PEDGE incorrect values, surface pressure too low.
* Bugfix: Boundary conditions input.

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