Downloading WRF-GC
===================

This section discusses:

* Downloading the :term:`WRF` model.
* Downloading the WRF-GC coupler and the :term:`GEOS-Chem` model.
* Downloading the :term:`WPS` (WRF Pre-Processor).

.. note::
	Currently, the GEOS-Chem model is included within the WRF-GC coupler. In the future, we plan to distribute these separately.

	However, the GEOS-Chem model version within the WRF-GC coupler, located within the ``gc`` folder, **is unmodified.** You can change this copy of GEOS-Chem just as you would change any other copy of GEOS-Chem, for your research.

.. warning::
	**Do not move** the WRF-GC directory after compiling, even on the same machine. Do not share a compiled copy of WRF-GC with others because during the compile process, the file paths are fixed. **Always install a fresh copy of WRF and download the WRF-GC into the chem directory when you move folders!**

Choose a folder to store your WRF-GC model, then proceed with the steps below.

Downloading WRF
----------------

Obtain the WRF model from `the NCAR/WRFV3 GitHub <https://github.com/NCAR/WRFV3/releases>`_ (version 3.9.1.1 for WRF-GC v1.0 and v2.0) or `the wrf-model/WRF GitHub <https://github.com/wrf-model/WRF/releases>`_ (version 4.0 and above for WRF-GC v3.0)


For WRF-GC v1.0 and v2.0, use WRF version 3.9.1.1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

	wget https://github.com/NCAR/WRFV3/archive/refs/tags/V3.9.1.1.zip
	unzip V3.9.1.1.zip

Extract WRF into the ``WRFV3`` folder (version 3). For simplicity, we refer to the folder as ``WRF`` below.

For WRF-GC v3.0, use WRF version 4.3 or 4.4
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

	wget https://github.com/wrf-model/WRF/releases/download/v4.4/v4.4.zip
	unzip v4.4.zip

Extract WRF into the ``WRFV4.X`` folder (version 4), and **rename it** to ``WRF``.

Downloading the WRF-GC coupler and GEOS-Chem model
---------------------------------------------------
For WRF-GC v2.0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Go into the ``WRF`` folder and **delete** the existing WRF-Chem chemistry. Delete the ``chem`` folder entirely.

2. **Clone the WRF-GC repository into the chem folder.**

.. code-block::

	git clone https://github.com/jimmielin/wrf-gc-release.git chem


For WRF-GC v3.0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Go into the ``WRF`` folder and **delete** the existing WRF-Chem chemistry. Delete the ``chem`` folder entirely.

2. Download the code from `our website <https://www.download.atmoschem.org.cn/>`_, create an empty folder named ``chem``, extract the compressed file into ``chem`` folder.

**Make sure you have the right code in the chem folder.** The folder should look like this:

.. code-block::

	WRF/chem$ ls
	gc                config
	chem_driver.F     module_chem_utilities.F    module_input_chem_data.F
	chemics_init.F    module_convection_prep.F   module_data_rrtmgaeropt.F
	wrfgc_convert_state_mod.F ...

Downloading the WPS Pre-Processor
---------------------------------

Go outside the ``WRF`` folder and download :term:`WPS` side-by-side with WPS, from the `wrf-model/WPS GitHub <https://github.com/wrf-model/WPS/releases>`_. Download the version closest to your WRF version (3.9, 4.3, etc.)

Extract the WRF Pre-Processor.

.. warning::
	If you are running simulations after July 2019, **you have to use WPS version 4.0 or above.** It works with WRF v3.9 as well. `Refer to this post for details <https://jimmielin.me/2019/wrf-3x-gfs-ungrib-error/>`_
