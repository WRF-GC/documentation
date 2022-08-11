Downloading WRF-GC
===================

This section discusses:

* Downloading the :term:`WRF` model.
* Downloading the WRF-GC coupler and the :term:`GEOS-Chem` model.
* Downloading the :term:`WPS` (WRF Pre-Processor).

.. note::
	Currently, the GEOS-Chem model is included within the WRF-GC coupler. In the future, we plan to distribute these separately.

	However, the GEOS-Chem model version within the WRF-GC coupler, located within the ``gc`` folder, **is unmodified.** You can change this copy of GEOS-Chem just as you would change any other copy of GEOS-Chem, for your research.

Choose a folder to store your WRF-GC model, then proceed with the steps below.

Downloading WRF
----------------

Obtain the WRF model from `the NCAR/WRFV3 GitHub <https://github.com/NCAR/WRFV3/releases>`_ (version 3.9.1.1 for WRF-GC v1.0 and v2.0) or `the wrf-model/WRF GitHub <https://github.com/wrf-model/WRF/releases>`_ (version 4.0 and above for WRF-GC v3.0)

**The currently supported version is WRF v3.9.1.1 (for WRF-GC v1.0 and v2.0).**

.. note::
	If you would like to use WRF version 4, please contact the WRF-GC team for an experimental version.

.. code-block::

	wget https://github.com/NCAR/WRFV3/archive/refs/tags/V3.9.1.1.zip
	unzip V3.9.1.1.zip

Extract WRF into the ``WRFV3`` folder (version 3) or ``WRF`` folder (version 4). For simplicity, we refer to these folders as ``WRF`` below.

Downloading the WRF-GC coupler and GEOS-Chem model
---------------------------------------------------

1. Go into the ``WRF`` folder and **delete** the existing WRF-Chem chemistry. Delete the ``chem`` folder entirely.

2. **Clone the WRF-GC repository into the chem folder.**

.. code-block::

	git clone https://github.com/jimmielin/wrf-gc-release.git chem

**Make sure you have cloned this into the chem folder.**

Downloading the WPS Pre-Processor
---------------------------------

Go outside the ``WRF`` folder and download :term:`WPS` side-by-side with WPS, from the `wrf-model/WPS GitHub <https://github.com/wrf-model/WPS/releases>`_. Download the version closest to your WRF version (3.9, 4.3, etc.)

Extract the WRF Pre-Processor.

.. warning::
	If you are running simulations after July 2019, **you have to use WPS version 4.0 or above.** It works with WRF v3.9 as well. `Refer to this post for details <https://jimmielin.me/2019/wrf-3x-gfs-ungrib-error/>`_