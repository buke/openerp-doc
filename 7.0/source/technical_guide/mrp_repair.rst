
.. module:: mrp_repair
    :synopsis: Products Repairs Module (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/mrp_repair"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Products Repairs Module (*mrp_repair*)
======================================
:Module: mrp_repair
:Name: Products Repairs Module
:Version: 5.0.1.0
:Author: Tiny
:Directory: mrp_repair
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  The aim is to have a complete module to manage all products repairs. The following topics should be covered by this module:
             * Add/remove products in the reparation
             * Impact for stocks
             * Invoicing (products and/or services)
             * Warranty concept
             * Repair quotation report
             * Notes for the technician and for the final customer

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/mrp_repair.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/mrp_repair.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/mrp_repair.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`sale`
 * :mod:`account`

Reports
-------

 * Quotation / Order

Menus
-------

 * Manufacturing/Repairs
 * Manufacturing/Repairs/Repairs in quotation
 * Manufacturing/Repairs/Repairs in progress
 * Manufacturing/Repairs/Repairs Ready to Start
 * Manufacturing/Repairs/Repairs to be invoiced
 * Manufacturing/Repairs/New Repair

Views
-----

 * mrp.repair.form (form)
 * mrp.repair.tree (tree)


Objects
-------

Object: Repairs Order (mrp.repair)
##################################



:operations: Operation Lines, one2many, readonly





:address_id: Delivery Address, many2one





:internal_notes: Internal Notes, text





:quotation_notes: Quotation Notes, text





:partner_id: Partner, many2one

    *This field allow you to choose the partner that will be invoiced and delivered*



:invoiced: Invoiced, boolean, readonly





:amount_untaxed: Untaxed Amount, float, readonly





:location_id: Current Location, many2one, required, readonly





:amount_tax: Taxes, float, readonly





:state: Repair State, selection, readonly

    *Gives the state of the Repair Order*



:pricelist_id: Pricelist, many2one

    *The pricelist comes from the selected partner, by default.*



:amount_total: Total, float, readonly





:prodlot_id: Lot Number, many2one





:partner_invoice_id: Invoicing Address, many2one





:move_id: Move, many2one, required, readonly





:name: Repair Ref, char, required





:product_id: Product to Repair, many2one, required, readonly





:guarantee_limit: Guarantee limit, date

    *The guarantee limit is computed as: last move date + warranty defined on selected product. If the current date is below the guarantee limit, each operation and fee you add will be set as 'not to invoiced' by default. Note you can manually change this later.*



:deliver_bool: Deliver, boolean

    *Check this box if you want to manage the delivery once the product is repaired. If checked, it will create a packing with selected product. Note that you can select the locations in the Info tab, if you have the extended view.*



:invoice_method: Invoice Method, selection, required, readonly

    *This field allow you to change the workflow of the repair order. If value selected is different from 'No Invoice', it also allow you to select the pricelist and invoicing address.*



:location_dest_id: Delivery Location, many2one, readonly





:invoice_id: Invoice, many2one, readonly





:fees_lines: Fees Lines, one2many, readonly





:repaired: Repaired, boolean, readonly





:picking_id: Packing, many2one, readonly




Object: Repair Operations Lines (mrp.repair.line)
#################################################



:name: Description, char, required





:product_uom: Product UoM, many2one, required





:repair_id: Repair Order Ref, many2one





:type: Type, selection, required





:price_unit: Unit Price, float, required





:product_uom_qty: Quantity (UoM), float, required





:price_subtotal: Subtotal, float, readonly





:to_invoice: To Invoice, boolean





:state: Status, selection, required, readonly





:product_id: Product, many2one, required





:location_dest_id: Dest. Location, many2one, required





:invoiced: Invoiced, boolean, readonly





:location_id: Source Location, many2one, required





:invoice_line_id: Invoice Line, many2one, readonly





:move_id: Inventory Move, many2one, readonly





:tax_id: Taxes, many2many




Object: Repair Fees line (mrp.repair.fee)
#########################################



:name: Description, char, required





:product_uom: Product UoM, many2one, required





:repair_id: Repair Order Ref, many2one, required





:price_unit: Unit Price, float, required





:product_uom_qty: Quantity, float, required





:price_subtotal: Subtotal, float, readonly





:to_invoice: To Invoice, boolean





:invoiced: Invoiced, boolean, readonly





:tax_id: Taxes, many2many





:invoice_line_id: Invoice Line, many2one, readonly





:product_id: Product, many2one


