Guide to outputs
=================

The WRF-GC outputs are provided by WRF in standard ``netCDF`` format. 

.. note::
	Are you a WRF or WRF-Chem user? Most of your tools for processing WRF-Chem output may only need species names to be changed to the GEOS-Chem names, and you will be good to go!

Here are some useful tools for analyzing WRF-GC outputs:

* **Python**: Standard tools for netCDF should work. There is also a `wrf-python <https://pypi.org/project/wrf-python/1.0.1/>`_ package for diagnostic and interpolation routines.
* **MATLAB**: You may find `m_map <https://www.eoas.ubc.ca/~rich/map.html>`_ useful for plotting.
* **NCL**: `The NCAR Command Language (NCL) <http://www.ncl.ucar.edu/Applications/wrf.shtml>`_ can read in NetCDF data and create plots based on many example scripts for WRF.

Your system may also have `ncview <http://meteora.ucsd.edu/~pierce/ncview_home_page.html>`_ which is a super handy tool to quickly look at netCDF files on your system. `Panoply <https://www.giss.nasa.gov/tools/panoply/>`_ is useful as well.

Can I output GEOS-Chem / HEMCO diagnostics?
--------------------------------------------

Now we have reimplement GEOS-Chem / HEMCO diagnostics in WRF-GC 3.0. Please refer to :doc:`/extra-diagnostics`.

The outputs are too large / how can I compress them?
-----------------------------------------------------

Please refer to the :doc:`/faq`'s "Outputs" section.
