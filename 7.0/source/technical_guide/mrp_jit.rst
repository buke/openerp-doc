
.. module:: mrp_jit
    :synopsis: MRP JIT (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/mrp_jit"></div>
    <script src="http://js-kit.com/ratings.js"></script>

MRP JIT (*mrp_jit*)
===================
:Module: mrp_jit
:Name: MRP JIT
:Version: 5.0.1.0
:Author: Tiny
:Directory: mrp_jit
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module allows Just In Time computation of all procurement.
  
      If you install this module, you will not have to run the regular procurement 
      scheduler anymore (but you still need to run the minimum order point rule 
      scheduler, or for example let it run daily.)
      All procurement orders will be processed immediately, which could in some
      cases entail a small performance impact.
  
      It may also increase your stock size because products are reserved as soon
      as possible and the scheduler time range is not taken into account anymore. 
      In that case, you can not use priorities any more on the different picking.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/mrp_jit.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/mrp_jit.zip>`_


Dependencies
------------

 * :mod:`mrp`
 * :mod:`sale`

Reports
-------

None


Menus
-------


None


Views
-----


None



Objects
-------

None
