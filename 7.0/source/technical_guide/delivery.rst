
.. module:: delivery
    :synopsis: Carriers and deliveries (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/delivery"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Carriers and deliveries (*delivery*)
====================================
:Module: delivery
:Name: Carriers and deliveries
:Version: 5.0.1.0
:Author: Tiny
:Directory: delivery
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Allows you to add delivery methods in sales orders and packing. You can define your own carrier and delivery grids for prices. When creating invoices from picking, OpenERP is able to add and compute the shipping line.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/delivery.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/delivery.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/delivery.zip>`_


Dependencies
------------

 * :mod:`sale`
 * :mod:`purchase`
 * :mod:`stock`

Reports
-------

None


Menus
-------

 * Stock Management/Configuration/Delivery
 * Stock Management/Configuration/Delivery/Delivery Method
 * Stock Management/Configuration/Delivery/Delivery Pricelist
 * Stock Management/Outgoing Products/Packing to be invoiced
 * Stock Management/Incoming Products/Generate Draft Invoices On Receptions

Views
-----

 * delivery.carrier.tree (tree)
 * delivery.carrier.form (form)
 * delivery.grid.tree (tree)
 * delivery.grid.form (form)
 * delivery.grid.line.form (form)
 * delivery.grid.line.tree (tree)
 * \* INHERIT delivery.sale.order_withcarrier.form.view (form)
 * \* INHERIT delivery.stock.picking_withcarrier.out.form.view (form)
 * \* INHERIT stock.picking_withweight.in.form.view (form)
 * \* INHERIT stock.picking_withweight.internal.form.view (form)
 * \* INHERIT delivery.stock.picking_withcarrier.delivery.form.view (form)
 * \* INHERIT res.partner.carrier.property.form.inherit (form)


Objects
-------

Object: Carrier and delivery grids (delivery.carrier)
#####################################################



:product_id: Delivery Product, many2one, required





:price: Price, float, readonly





:grids_id: Delivery Grids, one2many





:active: Active, boolean





:partner_id: Carrier Partner, many2one, required





:name: Carrier, char, required




Object: Delivery Grid (delivery.grid)
#####################################



:name: Grid Name, char, required





:sequence: Sequence, integer, required





:state_ids: States, many2many





:country_ids: Countries, many2many





:carrier_id: Carrier, many2one, required





:active: Active, boolean





:zip_from: Start Zip, char





:line_ids: Grid Line, one2many





:zip_to: To Zip, char




Object: Delivery line of grid (delivery.grid.line)
##################################################



:list_price: Sale Price, float, required





:name: Name, char, required





:price_type: Price Type, selection, required





:max_value: Maximum Value, float, required





:standard_price: Cost Price, float, required





:grid_id: Grid, many2one, required





:variable_factor: Variable Factor, selection, required





:operator: Operator, selection, required





:type: Variable, selection, required


