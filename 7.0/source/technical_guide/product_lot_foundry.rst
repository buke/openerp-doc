
.. module:: product_lot_foundry
    :synopsis: Products Lot Foundry 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_lot_foundry"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Products Lot Foundry (*product_lot_foundry*)
============================================
:Module: product_lot_foundry
:Name: Products Lot Foundry
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_lot_foundry
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Lots management for a metal company: cutting, heatcode, sizes

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_lot_foundry.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_lot_foundry.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`
 * :mod:`stock`
 * :mod:`sale`

Reports
-------

None


Menus
-------

 * Inventory Control
 * Inventory Control/Heat Codes
 * Inventory Control/Heat Codes/Draft Heat Codes

Views
-----

 * \* INHERIT stock.production.lot.form (form)
 * product.lot.foundry.heatcode.tree (tree)
 * product.lot.foundry.heatcode.form (form)
 * \* INHERIT product.normal.form (form)
 * sale.order.form (form)


Objects
-------

Object: Heat Code (product.lot.foundry.heatcode)
################################################



:name: Heat Code, char, required





:lot_ids: Lots, one2many





:mecanical_ids: Mechanical Properties, one2many





:state: State, selection, required





:date: Date, date, required





:chemical_ids: Chemical Properties, one2many




Object: Mechanical Properties (product.lot.foundry.heatcode.mecanical)
######################################################################



:heatcode_id: Heatcode, many2one





:name: Property, char, required





:value: Value, char, required




Object: Chemical Properties (product.lot.foundry.heatcode.chemical)
###################################################################



:heatcode_id: Heatcode, many2one





:name: Property, char, required





:value: Value, char, required




Object: stock.production.lot.reservation (stock.production.lot.reservation)
###########################################################################



:name: Reservation, char





:size_x: Width, float





:size_y: Length, float





:size_z: Thickness, float





:date: Date, date





:lot_id: Lot, many2one, required




Object: stock.production.lot.all (stock.production.lot.all)
###########################################################



:lot_id: Lot, many2one





:name: Quantity, float





:line_id: Order Line, many2one


