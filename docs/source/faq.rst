Frequently Asked Questions
===========================

.. note::
	This section is still heavily under construction as we aggregate questions and answers into this document.

Running environment
-------------------

What are the system requirements for WRF-GC?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Linux-based system, either on your local cluster or cloud services. Software requirements are: a Fortran/C compiler (Intel or GNU GCC+GFortran), MPI, HDF5, netCDF (with netCDF Fortran).

Recommended system specifications are at least 6 CPU cores, and at least 32 GB of RAM. Storage requirements depend on the resolution of your run, but plan for generally ~2 GB per output file. Input data for GEOS-Chem and WRF meteorology is also necessary, and may be around hundreds of GB.

Can I run WRF-GC on my own computer?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generally we recommend running on a computing cluster. If this is not possible, cloud services such as AWS may also be available.

If you want to test WRF-GC locally, a Linux system with at least 32 GB of memory is recommended. However, running on your own computer may be extremely slow and only recommended for debugging.

Input
-----

How do I generate chemical initial/boundary conditions?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

WRF-GC is a regional model. Boundary conditions from a global model are generally required. Initial conditions can be provided by a WRF-GC run or other global models.

You can use MOZART4-GEOS5, CAM-chem, or GEOS-Chem as input for initial/boundary conditions.

The general process is as follows:

* Identify which data source you want to use as ic/bc.
* Set-up WRF-GC, and run `real.exe` to generate `wrfinput_d01` (initial conditions), and `wrfbdy_d01` (boundary conditions)
* Prepare ic/bc inputs into a netCDF format accepted by `mozbc`.
* Use `mozbc` to add these inputs to `wrfinput_d01` and/or `wrfbdy_d01` files.
* Run the WRF-GC model.

**GEOS-Chem input:** Refer to the getting started guide. A MATLAB script will process global GEOS-Chem outputs to netCDF files accepted by `mozbc`, which are then generated into WRF(-GC) initial/boundary files.

Can I nudge the input meteorology data?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. The process is similar to WRF, or WRF-Chem. More details soon.

Running and configuration
-------------------------

Can I run the model in multiple segmented runs?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. WRF will generate restart files based on the namelist configuration.


Output
------

How can I configure output?
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use `history_interval` in WRF's `namelist.input`.

What is the output format? What are some tools to process them?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The output is in `wrfout_` netCDF format used by WRF, and WRF-Chem. As such, tools to process WRF and WRF-Chem outputs may be useful for WRF-GC with some species name modifications.

Can I output GEOS-Chem diagnostics?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Limited support is available for this at this time. Generally, only very specific diagnostics such as wet deposition loss rates are available.

Planeflight diagnostics are not available at this time but may be developed in the future.