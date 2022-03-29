Common Errors
==============

.. note::
	This section is still heavily under construction as we aggregate questions and answers into this document.

We hope you don't run into these errors. But if you do, we hope they will be a useful reference.

**Tip:** Use ``Ctrl+F`` (or ``Command+F``) in your browser to search this page, it'll be much faster!

.. note::
	WRF-GC has several output files. Most GEOS-Chem output is in the root CPU output file, ``rsl.out.0000``. **Look in this file for any GEOS-Chem related errors.** HEMCO-related errors are in ``HEMCO.log``. WRF-related errors can be in any of the files numbered ``rsl.error.*`` and ``rsl.out.*``. You may want to use ``tail -n 5 rsl.* | less`` to quickly look at all log files to identify errors.

WPS-related errors
-------------------


WRF-related errors
------------------


GEOS-Chem related errors
------------------------


HEMCO related errors
--------------------