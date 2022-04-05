Common Errors
==============

.. note::
	This section is still heavily under construction as we aggregate questions and answers into this document.

We hope you don't run into these errors. But if you do, we hope they will be a useful reference.

**Tip:** Use ``Ctrl+F`` (or ``Command+F``) in your browser to search this page, it'll be much faster!

.. note::
	WRF-GC has several output files. Most GEOS-Chem output is in the root CPU output file, ``rsl.out.0000``. **Look in this file for any GEOS-Chem related errors.** HEMCO-related errors are in ``HEMCO.log``. WRF-related errors can be in any of the files numbered ``rsl.error.*`` and ``rsl.out.*``. You may want to use ``tail -n 5 rsl.* | less`` to quickly look at all log files to identify errors.

Compiling errors
-----------------

WPS-related errors
-------------------


WRF-related errors
------------------

ERROR: Mismatch between namelist and input file dimensions NOTE:       1 namelist vs input data inconsistencies found.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you see an error similar to:

.. code-block::

	d01 2016-05-11_12:00:00  input_wrf.F: SIZE MISMATCH:  namelist   ide,jde,num_metgrid_levels=         245         181          27
	d01 2016-05-11_12:00:00  input_wrf.F: SIZE MISMATCH:  input file ide,jde,kde               =         245         181          32
	d01 2016-05-11_12:00:00 ---- ERROR: Mismatch between namelist and input file dimensions
	NOTE:       1 namelist vs input data inconsistencies found.

You've hit a problem where your meteorology data source (e.g., GFS) has updated **during your model run times!** This doesn't happen often but you are bound to run into it sometime - see the list of updates and their dates `on this changelog page <https://www.nco.ncep.noaa.gov/pmb/changes/>`_ from NOAA.

**If your model run time did go across two GFS/FNL updates:** Usually this can be fixed by making a custom data request, e.g., in FNL `at the NCAR/UCAR Research Data Archive (RDA) <https://rda.ucar.edu/datasets/ds083.2/index.html#!access>`__ with a consistent number of vertical levels, and this can be solved.

**If your model run time did not go across:** Then maybe you're using old data and ``num_metgrid_levels`` is different. For example, try changing the ``namelist.input`` so it has the right number (in this case ``32`` instead of ``27``). If this doesn't fix the issue, see above.

GEOS-Chem related errors
------------------------

## INTEGRATE FAILED TWICE !!! 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you see ``--> Step size too small: T + 10*H = T or H < Roundoff``, this means that the conditions in that grid box are not optimal and resulted in integration errors. Try a better set of initial / boundary conditions.

My NOx / HNO3 or nitrogen-related species are extremely high!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If this is happening near the coast, this is a bug with the ParaNOx extension. Go to ``HEMCO_Config.rc`` and turn off the `ParaNOx` extension. We are looking for a more permanent fix.


HEMCO related errors
--------------------

HEMCO ERROR: Invalid time index in (file)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check the file that it is pointing to. There are a few likely reasons:
* The file was corrupted / not fully downloaded. Try opening it with ``ncview`` and checking!
* This inventory does not have the appropriate file for this date/time.

Red herrings
-------------
If you see anything on this list, **this means that there's an error somewhere else!**

Cannot find -lGCHPint
^^^^^^^^^^^^^^^^^^^^^^

This is not an error, ignore. If you cannot successfully compile WRF-GC, there is an error above in the compile log.

HEMCO ERROR: MaxNest too low, cannot enter GET_TIMEIDX (hco_read_std_mod.F90)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Any kind of error that says ``HEMCO ERROR: MaxNest too low`` means that there is an error somewhere above, in ``HEMCO.log``. Check further!

forrtl: severe (408): fort: (2): Subscript #1 of the array LOC has value 11 which is greater than the upper bound of 10
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This means that there is an error in ``HEMCO.log`` - check the HEMCO log instead! Maybe inventories are missing, etc.