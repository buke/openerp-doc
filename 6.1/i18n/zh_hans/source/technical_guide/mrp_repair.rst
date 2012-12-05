
.. i18n: .. module:: mrp_repair
.. i18n:     :synopsis: Products Repairs Module (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: mrp_repair
    :synopsis: Products Repairs Module (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:       <br />
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />
..

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: .. tip:: This module is part of the OpenERP software, the leading Open Source 
.. i18n:   enterprise management system. If you want to discover OpenERP, check our 
.. i18n:   `screencasts <http://openerp.tv>`_ or download 
.. i18n:   `OpenERP <http://openerp.com>`_ directly.
..

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/mrp_repair"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/mrp_repair"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Products Repairs Module (*mrp_repair*)
.. i18n: ======================================
.. i18n: :Module: mrp_repair
.. i18n: :Name: Products Repairs Module
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: mrp_repair
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   The aim is to have a complete module to manage all products repairs. The following topics should be covered by this module:
.. i18n:              * Add/remove products in the reparation
.. i18n:              * Impact for stocks
.. i18n:              * Invoicing (products and/or services)
.. i18n:              * Warranty concept
.. i18n:              * Repair quotation report
.. i18n:              * Notes for the technician and for the final customer
..

::

  The aim is to have a complete module to manage all products repairs. The following topics should be covered by this module:
             * Add/remove products in the reparation
             * Impact for stocks
             * Invoicing (products and/or services)
             * Warranty concept
             * Repair quotation report
             * Notes for the technician and for the final customer

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/mrp_repair.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/mrp_repair.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/mrp_repair.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/mrp_repair.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/mrp_repair.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/mrp_repair.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`account`
..

 * :mod:`base`
 * :mod:`sale`
 * :mod:`account`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Quotation / Order
..

 * Quotation / Order

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Manufacturing/Repairs
.. i18n:  * Manufacturing/Repairs/Repairs in quotation
.. i18n:  * Manufacturing/Repairs/Repairs in progress
.. i18n:  * Manufacturing/Repairs/Repairs Ready to Start
.. i18n:  * Manufacturing/Repairs/Repairs to be invoiced
.. i18n:  * Manufacturing/Repairs/New Repair
..

 * Manufacturing/Repairs
 * Manufacturing/Repairs/Repairs in quotation
 * Manufacturing/Repairs/Repairs in progress
 * Manufacturing/Repairs/Repairs Ready to Start
 * Manufacturing/Repairs/Repairs to be invoiced
 * Manufacturing/Repairs/New Repair

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * mrp.repair.form (form)
.. i18n:  * mrp.repair.tree (tree)
..

 * mrp.repair.form (form)
 * mrp.repair.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Repairs Order (mrp.repair)
.. i18n: ##################################
..

Object: Repairs Order (mrp.repair)
##################################

.. i18n: :operations: Operation Lines, one2many, readonly
..

:operations: Operation Lines, one2many, readonly

.. i18n: :address_id: Delivery Address, many2one
..

:address_id: Delivery Address, many2one

.. i18n: :internal_notes: Internal Notes, text
..

:internal_notes: Internal Notes, text

.. i18n: :quotation_notes: Quotation Notes, text
..

:quotation_notes: Quotation Notes, text

.. i18n: :partner_id: Partner, many2one
..

:partner_id: Partner, many2one

.. i18n:     *This field allow you to choose the partner that will be invoiced and delivered*
..

    *This field allow you to choose the partner that will be invoiced and delivered*

.. i18n: :invoiced: Invoiced, boolean, readonly
..

:invoiced: Invoiced, boolean, readonly

.. i18n: :amount_untaxed: Untaxed Amount, float, readonly
..

:amount_untaxed: Untaxed Amount, float, readonly

.. i18n: :location_id: Current Location, many2one, required, readonly
..

:location_id: Current Location, many2one, required, readonly

.. i18n: :amount_tax: Taxes, float, readonly
..

:amount_tax: Taxes, float, readonly

.. i18n: :state: Repair State, selection, readonly
..

:state: Repair State, selection, readonly

.. i18n:     *Gives the state of the Repair Order*
..

    *Gives the state of the Repair Order*

.. i18n: :pricelist_id: Pricelist, many2one
..

:pricelist_id: Pricelist, many2one

.. i18n:     *The pricelist comes from the selected partner, by default.*
..

    *The pricelist comes from the selected partner, by default.*

.. i18n: :amount_total: Total, float, readonly
..

:amount_total: Total, float, readonly

.. i18n: :prodlot_id: Lot Number, many2one
..

:prodlot_id: Lot Number, many2one

.. i18n: :partner_invoice_id: Invoicing Address, many2one
..

:partner_invoice_id: Invoicing Address, many2one

.. i18n: :move_id: Move, many2one, required, readonly
..

:move_id: Move, many2one, required, readonly

.. i18n: :name: Repair Ref, char, required
..

:name: Repair Ref, char, required

.. i18n: :product_id: Product to Repair, many2one, required, readonly
..

:product_id: Product to Repair, many2one, required, readonly

.. i18n: :guarantee_limit: Guarantee limit, date
..

:guarantee_limit: Guarantee limit, date

.. i18n:     *The guarantee limit is computed as: last move date + warranty defined on selected product. If the current date is below the guarantee limit, each operation and fee you add will be set as 'not to invoiced' by default. Note you can manually change this later.*
..

    *The guarantee limit is computed as: last move date + warranty defined on selected product. If the current date is below the guarantee limit, each operation and fee you add will be set as 'not to invoiced' by default. Note you can manually change this later.*

.. i18n: :deliver_bool: Deliver, boolean
..

:deliver_bool: Deliver, boolean

.. i18n:     *Check this box if you want to manage the delivery once the product is repaired. If checked, it will create a packing with selected product. Note that you can select the locations in the Info tab, if you have the extended view.*
..

    *Check this box if you want to manage the delivery once the product is repaired. If checked, it will create a packing with selected product. Note that you can select the locations in the Info tab, if you have the extended view.*

.. i18n: :invoice_method: Invoice Method, selection, required, readonly
..

:invoice_method: Invoice Method, selection, required, readonly

.. i18n:     *This field allow you to change the workflow of the repair order. If value selected is different from 'No Invoice', it also allow you to select the pricelist and invoicing address.*
..

    *This field allow you to change the workflow of the repair order. If value selected is different from 'No Invoice', it also allow you to select the pricelist and invoicing address.*

.. i18n: :location_dest_id: Delivery Location, many2one, readonly
..

:location_dest_id: Delivery Location, many2one, readonly

.. i18n: :invoice_id: Invoice, many2one, readonly
..

:invoice_id: Invoice, many2one, readonly

.. i18n: :fees_lines: Fees Lines, one2many, readonly
..

:fees_lines: Fees Lines, one2many, readonly

.. i18n: :repaired: Repaired, boolean, readonly
..

:repaired: Repaired, boolean, readonly

.. i18n: :picking_id: Packing, many2one, readonly
..

:picking_id: Packing, many2one, readonly

.. i18n: Object: Repair Operations Lines (mrp.repair.line)
.. i18n: #################################################
..

Object: Repair Operations Lines (mrp.repair.line)
#################################################

.. i18n: :name: Description, char, required
..

:name: Description, char, required

.. i18n: :product_uom: Product UoM, many2one, required
..

:product_uom: Product UoM, many2one, required

.. i18n: :repair_id: Repair Order Ref, many2one
..

:repair_id: Repair Order Ref, many2one

.. i18n: :type: Type, selection, required
..

:type: Type, selection, required

.. i18n: :price_unit: Unit Price, float, required
..

:price_unit: Unit Price, float, required

.. i18n: :product_uom_qty: Quantity (UoM), float, required
..

:product_uom_qty: Quantity (UoM), float, required

.. i18n: :price_subtotal: Subtotal, float, readonly
..

:price_subtotal: Subtotal, float, readonly

.. i18n: :to_invoice: To Invoice, boolean
..

:to_invoice: To Invoice, boolean

.. i18n: :state: Status, selection, required, readonly
..

:state: Status, selection, required, readonly

.. i18n: :product_id: Product, many2one, required
..

:product_id: Product, many2one, required

.. i18n: :location_dest_id: Dest. Location, many2one, required
..

:location_dest_id: Dest. Location, many2one, required

.. i18n: :invoiced: Invoiced, boolean, readonly
..

:invoiced: Invoiced, boolean, readonly

.. i18n: :location_id: Source Location, many2one, required
..

:location_id: Source Location, many2one, required

.. i18n: :invoice_line_id: Invoice Line, many2one, readonly
..

:invoice_line_id: Invoice Line, many2one, readonly

.. i18n: :move_id: Inventory Move, many2one, readonly
..

:move_id: Inventory Move, many2one, readonly

.. i18n: :tax_id: Taxes, many2many
..

:tax_id: Taxes, many2many

.. i18n: Object: Repair Fees line (mrp.repair.fee)
.. i18n: #########################################
..

Object: Repair Fees line (mrp.repair.fee)
#########################################

.. i18n: :name: Description, char, required
..

:name: Description, char, required

.. i18n: :product_uom: Product UoM, many2one, required
..

:product_uom: Product UoM, many2one, required

.. i18n: :repair_id: Repair Order Ref, many2one, required
..

:repair_id: Repair Order Ref, many2one, required

.. i18n: :price_unit: Unit Price, float, required
..

:price_unit: Unit Price, float, required

.. i18n: :product_uom_qty: Quantity, float, required
..

:product_uom_qty: Quantity, float, required

.. i18n: :price_subtotal: Subtotal, float, readonly
..

:price_subtotal: Subtotal, float, readonly

.. i18n: :to_invoice: To Invoice, boolean
..

:to_invoice: To Invoice, boolean

.. i18n: :invoiced: Invoiced, boolean, readonly
..

:invoiced: Invoiced, boolean, readonly

.. i18n: :tax_id: Taxes, many2many
..

:tax_id: Taxes, many2many

.. i18n: :invoice_line_id: Invoice Line, many2one, readonly
..

:invoice_line_id: Invoice Line, many2one, readonly

.. i18n: :product_id: Product, many2one
..

:product_id: Product, many2one
