Key concepts (Glossary)
=======================

Here is a list of concepts for WRF-GC that may be useful for using and developing WRF-GC.

.. glossary::

   WRF
      The `Weather Research and Forecasting Model <https://www.mmm.ucar.edu/weather-research-and-forecasting-model>`_, a mesoscale weather model.

   GEOS-Chem
      Atmospheric chemistry model that WRF-GC uses for chemistry. Not an acronym [#f1]_. `Website <http://geos-chem.org/>`_

   WRF-GC Model
      An online, two-way coupling of WRF and GEOS-Chem into one model, using the **WRF-GC Coupler**. The two models do not run separately - WRF-GC runs through WRF and the coupler will run GEOS-Chem chemistry at the appropriate time steps. Running WRF-GC is very similar to running `WRF-Chem <https://www2.acom.ucar.edu/wrf-chem>`_.

.. rubric:: Footnotes

.. [#f1] Cited from `the GEOS-Chem narrative description <https://geos-chem.seas.harvard.edu/narrative>`_: *The name "GEOS-Chem" was coined in 2001 and is first referred to in Bey et al. [2001]. It is not an acronym - there is nothing to spell out. GEOS stands for Goddard Earth Observing System and Chem stands for Chemistry but calling it the "Goddard Earth Observing System - Chemistry" model would be inappropriate because the GEOS Earth System Model can use other chemical modules besides GEOS-Chem, and GEOS-Chem can use other meteorological drivers besides GEOS.*