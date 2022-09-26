Running specialty simulations
=============================

.. warning::
	Running CO2 and CH4 specialty simulations in WRF-GC is a feature available in WRF-GC 3.0 or later. This version of WRF-GC is currently work in progress and not ready for release.

Installing WRF-GC with specialty simulations
---------------------------------------------

To run WRF-GC specialty simulations, a new set of WRF-GC coupler and GEOS-Chem configuration files need to be installed. **We recommend creating a separate copy of WRF-GC (including WRF) source code for each different type of simulation and not mixing the source code directories.**

To install specialty simulations, **instead of** running ``make install_registry`` in the ``chem`` folder after configuring WRF and before compiling, run:

* ``make install_registry_ch4`` for CH4 simulation;
* ``make install_registry_co2`` for CO2 simulation.

Then, proceed to ``./compile em_real`` as usual.

Preparing necessary input files
--------------------------------

Apart from the emission files specified in ``HEMCO_Config.rc`` for specialty simulations, it is very important to provide the following inputs:

* **Restart files** with initial concentrations for CO2 and CH4. You can input this into WRF-GC after ``real.exe`` using the ``mozbc`` tool. See :doc:`/icbc`. You can use this ``mozbc`` configuration (similarly for CO2):


.. code-block::

	&control

	do_bc     = .true.,
	do_ic     = .true.,
	domain    = 1,

	dir_wrf = '/directory/to/WRF/run/'
	dir_moz = '/directory/to/input/'
	fn_moz  = 'input_data_file_name.nc'

	spc_map = 'ch4 -> CH4',
	/

* (CH4 simulation only) **High-resolution OH and Cl concentrations**. By default, ``HEMCO_Config.rc`` uses 4x5 degree species maps, which greatly degrades the spatial resolution of the run, even if WRF-GC runs at higher resolution. These are specified in ``HEMCO_Config.rc`` here:

.. code-block::

	(((GLOBAL_OH
	* GLOBAL_OH  $ROOT/OH/v2014-09/v5-07-08/OH_3Dglobal.geos5.47L.4x5.nc OH           1985/1-12/1/0 C xyz kg/m3 * - 1 1
	)))GLOBAL_OH
	(((GLOBAL_CL
	* GLOBAL_Cl      $ROOT/GCClassic_Output/13.0.0/$YYYY/GEOSChem.SpeciesConc.$YYYY$MM$DD_0000z.nc4      SpeciesConc_Cl    2010-2019/1-12/1/0 C xyz 1        * - 1 1
	)))GLOBAL_CL
	)))CHEMISTRY_INPUT

We recommend making a high-resolution WRF-GC run with the same domain, extracting the ``oh`` and ``cl`` variables, and converting the units (WRF-GC output is in ppmv):

* ``oh`` unit should be converted from ppmv to kg/m3;
* ``cl`` unit should be converted from ppmv to v/v dry; multiply by 1e-6.
and saving them to a ``netCDF`` file so they can be read. Only the month necessary for the simulation needs to be provided, so for a run in 2019/02 and the concentrations saved out to ``wrfgc_output_oh_cl.nc``, the entries could be:

.. code-block::

	(((GLOBAL_OH
	* GLOBAL_OH  wrfgc_output_oh_cl.nc     oh   2019/2/1/0 C xyz kg/m3 * - 1 1
	)))GLOBAL_OH
	(((GLOBAL_CL
	* GLOBAL_Cl  wrfgc_output_oh_cl.nc     cl   2019/2/1/0 C xyz 1     * - 1 1
	)))GLOBAL_CL
	)))CHEMISTRY_INPUT

To help the conversion of ppmv to kg/m3:
* Pressure from WRF output is ``P`` + ``PB`` (perturbation pressure P + base state pressure PB), in Pa;
* Total potential temperature (Theta) is ``T`` + 300, in K. To get the temperature,
* Temperature = Theta * ((P+PB)/1000)^(2/7), in K.
* Molecular weight of Cl (atomic chlorine) is 35.45 g/mol per the GEOS-Chem species database.

Making outputs smaller
-----------------------

By default, WRF-GC outputs all the species for the full chemistry simulation even in CO2 and CH4 simulations. This can be annoying. Create a file ``outputlist.txt`` in the ``run`` directory with:

.. code-block::
	-:h:0:a3o2,acet,acta,ald2,alk4,aromp4,aromp5,aromro2,ato2,atooh,b3o2,bald,benz,benzo,benzo2,benzp,bro2,bzco3,bzco3h,bzpan,br,br2,brcl,brno2,brno3,bro,c2h2,c2h4,c2h6,c3h8,c4hvp1,c4hvp2,ccl4,cfc11,cfc113,cfc114,cfc115,cfc12,ch2br2,ch2cl2,ch2i2,ch2ibr,ch2icl,ch2o,ch2oo,ch3br,ch3ccl3,ch3choo,ch3cl,ch3i,chbr3,chcl3,clock,co,csl,cl,cl2,cl2o2,clno2,clno3,clo,cloo,eoh,ethln,ethn,ethp,etno3,eto,eto2,etoo,etp,glyc,glyx,h,h1211,h1301,h2,h2402,h2o,h2o2,hac,hbr,hc5a,hcfc123,hcfc141b,hcfc142b,hcfc22,hcooh,hcl,hi,hmhp,hmml,hms,hno2,hno3,hno4,ho2,hobr,hocl,hoi,honit,hpald1,hpald1oo,hpald2,hpald2oo,hpald3,hpald4,hpethnl,i,i2,i2o2,i2o3,i2o4,ibr,iche,ichoo,icn,icnoo,icpdh,icl,idc,idchp,idhdp,idhnboo,idhndoo1,idhndoo2,idhpe,idn,idnoo,iepoxa,iepoxaoo,iepoxb,iepoxboo,iepoxd,ihn1,ihn2,ihn3,ihn4,ihoo1,ihoo4,ihpnboo,ihpndoo,ihpoo1,ihpoo2,ihpoo3,ina,ino,ino2b,ino2d,inpb,inpd,io,iono,iono2,iprno3,isop,isopnoo1,isopnoo2,itcn,ithn,ko2,lbro2h,lbro2n,lch4,lco,limo,limo2,lisopno3,lisopoh,lnro2h,lnro2n,lox,ltro2h,ltro2n,lvoc,lvocoa,lxro2h,lxro2n,macr,macr1oo,macr1ooh,macrno2,map,mco3,mcrdh,mcrenol,mcrhn,mcrhnb,mcrhp,mcrohoo,mct,mek,meno3,mgly,mo2,moh,monits,monitu,mp,mpan,mpn,mtpa,mtpo,mvk,mvkdh,mvkhc,mvkhcb,mvkhp,mvkn,mvkohoo,mvkpc,n,n2,n2o,n2o5,nap,nh3,no,no2,no3,nphen,nprno3,nro2,o,o1d,o2,o3,ocs,oclo,oh,oio,olnd,olnn,othro2,pan,pco,ph2o2,phen,pio2,pip,po2,pox,pp,ppn,prn1,propnn,prpe,prpn,pso4,pyac,r4n1,r4n2,r4o2,r4p,ra3p,rb3p,rcho,rco3,rcooh,ripa,ripb,ripc,ripd,roh,rp,salacl,salccl,so2,tolu,tro2,xro2,xyle,aeri,aonita,asoa1,asoa2,asoa3,asoan,asog1,asog2,asog3,bcpi,bcpo,brsala,brsalc,dms,dst1,dst2,dst3,dst4,indiol,ionita,isala,isalc,monita,msa,nh4,nit,nits,ocpi,ocpo,sala,salaal,salc,salcal,so4,so4s,soagx,soaie,soap,soas,tsoa0,tsoa1,tsoa2,tsoa3,tsog0,tsog1,tsog2,tsog3,pfe,diag_so4_a1,diag_so4_a2,diag_so4_a3,diag_so4_a4,diag_nit_a1,diag_nit_a2,diag_nit_a3,diag_nit_a4,diag_nh4_a1,diag_nh4_a2,diag_nh4_a3,diag_nh4_a4,diag_ocpi_a1,diag_ocpi_a2,diag_ocpi_a3,diag_ocpi_a4,diag_ocpo_a1,diag_ocpo_a2,diag_ocpo_a3,diag_ocpo_a4,diag_bcpi_a1,diag_bcpi_a2,diag_bcpi_a3,diag_bcpi_a4,diag_bcpo_a1,diag_bcpo_a2,diag_bcpo_a3,diag_bcpo_a4,diag_seas_a1,diag_seas_a2,diag_seas_a3,diag_seas_a4,diag_dst_a1,diag_dst_a2,diag_dst_a3,diag_dst_a4,diag_soas_a1,diag_soas_a2,diag_soas_a3,diag_soas_a4,diag_so4_cw1,diag_so4_cw2,diag_so4_cw3,diag_so4_cw4,diag_nit_cw1,diag_nit_cw2,diag_nit_cw3,diag_nit_cw4,diag_nh4_cw1,diag_nh4_cw2,diag_nh4_cw3,diag_nh4_cw4,diag_ocpi_cw1,diag_ocpi_cw2,diag_ocpi_cw3,diag_ocpi_cw4,diag_ocpo_cw1,diag_ocpo_cw2,diag_ocpo_cw3,diag_ocpo_cw4,diag_bcpi_cw1,diag_bcpi_cw2,diag_bcpi_cw3,diag_bcpi_cw4,diag_bcpo_cw1,diag_bcpo_cw2,diag_bcpo_cw3,diag_bcpo_cw4,diag_seas_cw1,diag_seas_cw2,diag_seas_cw3,diag_seas_cw4,diag_dst_cw1,diag_dst_cw2,diag_dst_cw3,diag_dst_cw4,diag_soas_cw1,diag_soas_cw2,diag_soas_cw3,diag_soas_cw4,diag_water_a1,diag_water_a2,diag_water_a3,diag_water_a4,diag_num_a1,diag_num_a2,diag_num_a3,diag_num_a4,diag_num_cw1,diag_num_cw2,diag_num_cw3,diag_num_cw4

Go to ``namelist.input`` and in ``&time_control`` section, add:

.. code-block::
	iofields_filename = 'outputlist.txt',

This will exclude all the full-chemistry species from the specialty WRF-GC simuulation output.