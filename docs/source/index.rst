Welcome to WRF-GC!
===================

**WRF-GC** (WRF coupled with GEOS-Chem chemistry) is an online coupled model based on the regional meteorology model, WRF (Weather Research and Forecasting Model), and the GEOS-Chem chemical transport model.

This is the new web-based WRF-GC documentation. We are actively working on adding content.

Check out `the WRF-GC website <https://fugroup.org/index.php/WRF-GC>`_ at the `Atmospheric Chemistry and Climate Group at SUSTech <https://fugroup.org/>`_.

.. note::

   This documentation is under active development. Some content may still be under the old documentation, with step-to-step instructions, `in this PDF <https://fugroup.org/wrf-gc/WRF-GC_Documentation_updated_for_v2_Feb2021.pdf>`_.

The key references for WRF-GC are:

* **Lin et al., 2020**: Lin, H., Feng, X., Fu, T.-M., Tian, H., Ma, Y., Zhang, L., Jacob, D. J., Yantosca, R. M., Sulprizio, M. P., Lundgren, E. W., Zhuang, J., Zhang, Q., Lu, X., Zhang, L., Shen, L., Guo, J., Eastham, S. D., and Keller, C. A.: *WRF-GC (v1.0): online coupling of WRF (v3.9.1.1) and GEOS-Chem (v12.2.1) for regional atmospheric chemistry modeling – Part 1: Description of the one-way model*, Geosci. Model Dev., 13, 3241–3265, https://doi.org/10.5194/gmd-13-3241-2020, 2020. 
* **Feng et al., 2021**: Feng, X., Lin, H., Fu, T.-M., Sulprizio, M. P., Zhuang, J., Jacob, D. J., Tian, H., Ma, Y., Zhang, L., Wang, X., Chen, Q., and Han, Z.: *WRF-GC (v2.0): online two-way coupling of WRF (v3.9.1.1) and GEOS-Chem (v12.7.2) for modeling regional atmospheric chemistry–meteorology interactions*, Geosci. Model Dev., 14, 3741–3768, https://doi.org/10.5194/gmd-14-3741-2021, 2021. 

Most useful pages
------------------

* :doc:`/faq` about WRF-GC.
* :doc:`/common-errors` for when you run into errors. ``Ctrl+F`` (``Command+F``) will be your friend in this comprehensive page.
* The :doc:`/preflight-checklist` has a list of all steps you have to go through for a successful WRF-GC run. Make sure you follow all steps.

Table of contents
------------------

.. toctree::
   :maxdepth: 1
   :caption: Introduction

   key-concepts.rst
   faq.rst

.. toctree::
   :maxdepth: 1
   :caption: Getting started

   getting-started.rst
   guide-1-system-requirements.rst
   guide-2-downloading.rst
   guide-3-compiling.rst
   guide-4-wps-domain-real.rst
   icbc.rst
   guide-5-run.rst
   guide-6-outputs.rst
   preflight-checklist.rst

.. toctree::
   :maxdepth: 2
   :caption: Diving deeper

   common-errors.rst
   nudging.rst
   extra-diagnostics.rst
   newspecies.rst
   lightnox.rst

.. toctree::
   :maxdepth: 1
   :caption: Help & Reference

   resources.rst
