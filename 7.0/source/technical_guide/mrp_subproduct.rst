
.. module:: mrp_subproduct
    :synopsis: MRP Sub Product (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/mrp_subproduct"></div>
    <script src="http://js-kit.com/ratings.js"></script>

MRP Sub Product (*mrp_subproduct*)
==================================
:Module: mrp_subproduct
:Name: MRP Sub Product
:Version: 5.0.1.0
:Author: Tiny
:Directory: mrp_subproduct
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module allows you to produce several products from one production order.
  You can configure sub-products in the bill of material.
  Without this module:
      A + B + C -> D
  With this module:
      A + B + C -> D + E

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/mrp_subproduct.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/mrp_subproduct.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`mrp`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT mrp.bom.sub.product (form)


Objects
-------

Object: Mrp Sub Product (mrp.subproduct)
########################################



:bom_id: BoM, many2one





:subproduct_type: Quantity Type, selection, required





:product_id: Product, many2one, required





:product_uom: Product UOM, many2one, required





:product_qty: Product Qty, float, required


