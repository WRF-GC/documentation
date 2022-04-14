Generating Initial/Boundary Conditions (IC/BC)
===============================================

WRF-GC is a regional model. Boundary conditions from a global model are generally required. Initial conditions can be provided by a WRF-GC run or other global models.

You can use MOZART4-GEOS5, CAM-chem, or GEOS-Chem as input for initial/boundary conditions.

The general process is as follows:

* Identify which data source you want to use as ic/bc.
* Set-up WRF-GC, and run ``real.exe`` to generate ``wrfinput_d01`` (initial conditions), and ``wrfbdy_d01`` (boundary conditions)
* Prepare ic/bc inputs into a netCDF format accepted by ``mozbc``. (`mozbc for WRF-GC is located here <https://github.com/fengx7/mozbc_for_WRFv3.9>`_)
* Use `mozbc` to add these inputs to ``wrfinput_d01`` and/or ``wrfbdy_d01`` files.
* Run the WRF-GC model.

**GEOS-Chem input:** Refer to the getting started guide. `A MATLAB script <https://github.com/fengx7/WRF-GC-GCC_ICBC>`_ will process global GEOS-Chem outputs to netCDF files accepted by ``mozbc``, which are then generated into WRF(-GC) initial/boundary files.