Key concepts (Glossary)
=======================

Here is a list of concepts for WRF-GC that may be useful for using and developing WRF-GC.

.. glossary::

   WRF
      The `Weather Research and Forecasting Model <https://www.mmm.ucar.edu/weather-research-and-forecasting-model>`_, a mesoscale weather model. It provides the meteorology and framework for WRF-GC to work.

   GEOS-Chem
      Atmospheric chemistry model that WRF-GC uses for chemistry. Not an acronym [#f1]_. `Website <http://geos-chem.org/>`_

   WRF-GC Model
      An online, two-way coupling of WRF and GEOS-Chem into one model, using the **WRF-GC Coupler**. The two models do not run separately - WRF-GC runs through WRF and the coupler will run GEOS-Chem chemistry at the appropriate time steps. Running WRF-GC is very similar to running `WRF-Chem <https://www2.acom.ucar.edu/wrf-chem>`_.

   HEMCO
      The Harmonized Emissions Component, an on-line emissions component that WRF-GC uses for emissions. WRF-GC uses a modified version of HEMCO for coupling to WRF-GC and is described by Lin et al., 2021 [#f2]_.

   WPS
      The WRF Pre-Processor, a tool to prepare the grid and input meteorological fields (initial and boundary conditions) for the WRF model.

   mozbc
      A tool for inserting chemical initial and boundary conditions into WRF-Chem or WRF-GC's input files. We document the usage in :doc:`/icbc`.

.. rubric:: Footnotes

.. [#f1] Cited from `the GEOS-Chem narrative description <https://geos-chem.seas.harvard.edu/narrative>`_: *The name "GEOS-Chem" was coined in 2001 and is first referred to in Bey et al. [2001]. It is not an acronym - there is nothing to spell out. GEOS stands for Goddard Earth Observing System and Chem stands for Chemistry but calling it the "Goddard Earth Observing System - Chemistry" model would be inappropriate because the GEOS Earth System Model can use other chemical modules besides GEOS-Chem, and GEOS-Chem can use other meteorological drivers besides GEOS.*

.. [#f2] Lin, H., Jacob, D. J., Lundgren, E. W., Sulprizio, M. P., Keller, C. A., Fritz, T. M., Eastham, S. D., Emmons, L. K., Campbell, P. C., Baker, B., Saylor, R. D., and Montuoro, R.: Harmonized Emissions Component (HEMCO) 3.0 as a versatile emissions component for atmospheric models: application in the GEOS-Chem, NASA GEOS, WRF-GC, CESM2, NOAA GEFS-Aerosol, and NOAA UFS models, Geosci. Model Dev., 14, 5487–5506, https://doi.org/10.5194/gmd-14-5487-2021, 2021. 