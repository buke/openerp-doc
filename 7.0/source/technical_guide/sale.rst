
.. module:: sale
    :synopsis: Sales Management (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Sales Management (*sale*)
=========================
:Module: sale
:Name: Sales Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: sale
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  The base module to manage quotations and sales orders.
  
      * Workflow with validation steps:
          - Quotation -> Sale order -> Invoice
      * Invoicing methods:
          - Invoice on order (before or after shipping)
          - Invoice on delivery
          - Invoice on timesheets
          - Advance invoice
      * Partners preferences (shipping, invoicing, incoterm, ...)
      * Products stocks and prices
      * Delivery methods:
          - all at once, multi-parcel
          - delivery costs

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/sale.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/sale.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/sale.zip>`_


Dependencies
------------

 * :mod:`product`
 * :mod:`stock`
 * :mod:`mrp`
 * :mod:`process`

Reports
-------

 * Quotation / Order

Menus
-------

 * Sales Management/Configuration
 * Sales Management
 * Sales Management/Configuration/Shop
 * Sales Management/Sales Orders
 * Sales Management/Sales Orders/My Sales Order
 * Sales Management/Sales Orders/All Sales Order
 * Sales Management/Sales Orders/New Quotation
 * Sales Management/Sales Orders/All Sales Order/Sales in Exception
 * Sales Management/Sales Orders/All Sales Order/Sales Order To Be Invoiced
 * Sales Management/Sales Orders/All Sales Order/Sales Order in Progress
 * Sales Management/Sales Orders/All Sales Order/All Quotations
 * Sales Management/Sales Orders/My Sales Order/My sales in shipping exception
 * Sales Management/Sales Orders/My Sales Order/My sales order waiting Invoice
 * Sales Management/Sales Orders/My Sales Order/My sales order in progress
 * Sales Management/Sales Orders/My Sales Order/My Quotations
 * Sales Management/Sales Order Lines
 * Sales Management/Sales Order Lines/Uninvoiced Lines
 * Sales Management/Sales Order Lines/Uninvoiced Lines/Uninvoiced and Delivered Lines

Views
-----

 * sale.shop (form)
 * sale.shop (tree)
 * sale.order.calendar (calendar)
 * sale.order.graph (graph)
 * sale.order.tree (tree)
 * sale.order.form (form)
 * sale.order.line.graph (graph)
 * sale.order.line.tree (tree)
 * sale.order.line.form2 (form)
 * Configure Picking Policy for Sale Order  (form)
 * \* INHERIT stock.picking.form (form)


Objects
-------

Object: Sale Shop (sale.shop)
#############################



:payment_account_id: Payment Accounts, many2many





:name: Shop Name, char, required





:warehouse_id: Warehouse, many2one





:pricelist_id: Pricelist, many2one





:project_id: Analytic Account, many2one





:payment_default_id: Default Payment Term, many2one, required




Object: Sale Order (sale.order)
###############################



:origin: Origin, char





:order_line: Order Lines, one2many, readonly





:picking_policy: Packing Policy, selection, required

    *If you don't have enough stock available to deliver all at once, do you accept partial shipments or not?*



:order_policy: Shipping Policy, selection, required, readonly

    *The Shipping Policy is used to synchronise invoice and delivery operations.
    - The 'Pay before delivery' choice will first generate the invoice and then generate the packing order after the payment of this invoice.
    - The 'Shipping & Manual Invoice' will create the packing order directly and wait for the user to manually click on the 'Invoice' button to generate the draft invoice.
    - The 'Invoice on Order After Delivery' choice will generate the draft invoice based on sale order after all packing lists have been finished.
    - The 'Invoice from the packing' choice is used to create an invoice during the packing process.*



:invoice_ids: Invoices, many2many

    *This is the list of invoices that have been generated for this sale order. The same sale order may have been invoiced in several times (by line for example).*



:shop_id: Shop, many2one, required, readonly





:client_order_ref: Customer Ref, char





:date_order: Date Ordered, date, required, readonly





:partner_id: Customer, many2one, required, readonly





:invoiced: Paid, boolean, readonly





:amount_tax: Taxes, float, readonly





:fiscal_position: Fiscal Position, many2one





:amount_untaxed: Untaxed Amount, float, readonly





:payment_term: Payment Term, many2one





:note: Notes, text





:state: Order State, selection, readonly

    *Gives the state of the quotation or sale order. The exception state is automatically set when a cancel operation occurs in the invoice validation (Invoice Exception) or in the packing list process (Shipping Exception). The 'Waiting Schedule' state is set when the invoice is confirmed but waiting for the scheduler to run on the date 'Date Ordered'.*



:invoiced_rate: Invoiced, float, readonly





:pricelist_id: Pricelist, many2one, required, readonly





:project_id: Analytic Account, many2one, readonly





:incoterm: Incoterm, selection





:partner_order_id: Ordering Contact, many2one, required, readonly

    *The name and address of the contact that requested the order or quotation.*



:picked_rate: Picked, float, readonly





:partner_invoice_id: Invoice Address, many2one, required, readonly





:user_id: Salesman, many2one





:picking_ids: Related Packing, one2many, readonly

    *This is the list of picking list that have been generated for this invoice*



:amount_total: Total, float, readonly





:name: Order Reference, char, required





:partner_shipping_id: Shipping Address, many2one, required, readonly





:shipped: Picked, boolean, readonly





:invoice_quantity: Invoice on, selection, required

    *The sale order will automatically create the invoice proposition (draft invoice). Ordered and delivered quantities may not be the same. You have to choose if you invoice based on ordered or shipped quantities. If the product is a service, shipped quantities means hours spent on the associated tasks.*


Object: Sale Order line (sale.order.line)
#########################################



:property_ids: Properties, many2many, readonly





:product_uos_qty: Quantity (UoS), float, readonly





:product_uom: Product UoM, many2one, required, readonly





:sequence: Sequence, integer





:price_unit: Unit Price, float, required, readonly





:product_uom_qty: Quantity (UoM), float, required, readonly





:price_subtotal: Subtotal, float, readonly





:product_uos: Product UoS, many2one





:number_packages: Number Packages, integer, readonly





:invoiced: Invoiced, boolean, readonly





:move_ids: Inventory Moves, one2many, readonly





:delay: Delivery Lead Time, float, required, readonly

    *Number of days between the order confirmation and the shipping of the products to the customer*



:state: Status, selection, required, readonly





:order_partner_id: Customer, many2one





:product_packaging: Packaging, many2one





:tax_id: Taxes, many2many, readonly





:type: Procure Method, selection, required, readonly





:procurement_id: Procurement, many2one





:order_id: Order Ref, many2one, required, readonly





:discount: Discount (%), float, readonly





:price_net: Net Price, float, readonly





:product_id: Product, many2one





:name: Description, char, required, readonly





:invoice_lines: Invoice Lines, many2many, readonly





:notes: Notes, text





:th_weight: Weight, float, readonly





:address_allotment_id: Allotment Partner, many2one




Object: sale.config.picking_policy (sale.config.picking_policy)
###############################################################



:picking_policy: Packing Default Policy, selection, required





:order_policy: Shipping Default Policy, selection, required





:step: Steps To Deliver a Sale Order, selection, required

    *By default, OpenERP is able to manage complex routing and paths of products in your warehouse and partner locations. This will configure the most common and simple methods to deliver products to the customer in one or two operations by the worker.*



:name: Name, char


