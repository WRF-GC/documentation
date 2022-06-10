Compiling WRF-GC
=================

This section discusses:
* Configuring WRF compile.
* **Installing the GEOS-Chem species into WRF.**
* Compiling WRF-GC.
* Compiling :term:`WPS`.

Configuring WRF compile
------------------------

Go to the ``WRF`` folder.

**If you are using WRF version 3:**

.. code-block::

	./configure -hyb

**If you are using WRF version 4 or above:**

.. code-block::

	./configure

Select the compiler option corresponding to your environment, and select the **(dmpar) option**. e.g., Intel compiler, icc, ifort, (dmpar). dmpar is required and means distributed-memory parallel, which uses MPI and is used by WRF-GC.

Installing the GEOS-Chem species into WRF
------------------------------------------

.. warning::
	This step is **crucial**. If this step is not performed, you will have to start this page over and waste hours of your time.

Go to the ``WRF/chem`` folder and run ``make install_registry``.

If this step shows an error, make sure you did download WRF-GC into ``WRF/chem`` folder. It should look like this:

.. code-block::

	WRF/chem$ ls
	chem_driver.F 		Makefile 		gc 		config 
	wrfgc_convert_state_mod.F ...

Compiling WRF-GC
----------------

Go back to the ``WRF`` folder and run:

.. code-block::

	./compile em_real

Wait patiently. The process may take up to 2 - 4 hours depending on your system. If you encounter errors, note them down. A list of common errors is available at :doc:`/common-errors`.

Compiling WPS
--------------

1. Go one level up and then into the ``WPS`` folder.
2. Run ``./configure``.
3. Run ``./compile``.

If you encounter errors, note them down. A list of common errors is available at :doc:`/common-errors`.