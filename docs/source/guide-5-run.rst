Running WRF-GC
===============

This section discusses:

* Running WRF-GC (``wrf.exe``)
* How to monitor progress.

This section assumes that all input data and configuration are ready. For configuration, refer to the previous sections.

Configuring WRF-GC
-------------------

Refer to :doc:`/guide-4-wps-domain-real`'s relevant sections. Usually, you need to configure most options before running ``real.exe``.

Running WRF-GC (``wrf.exe``)
-------------------------

Run it similarly to ``real.exe``:

.. code-block::

	mpirun -np 32 ./wrf.exe

In a cluster you may want to use a batch script to do this. On a standalone Linux system you may want to do this within ``screen``.

Track progress using ``tail -f rsl.out.0000``. For troubleshooting, see the note at the top of :doc:`/common-errors`.