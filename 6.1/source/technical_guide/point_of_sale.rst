
.. module:: point_of_sale
    :synopsis: Point Of Sale (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/point_of_sale"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Point Of Sale (*point_of_sale*)
===============================
:Module: point_of_sale
:Name: Point Of Sale
:Version: 5.0.1.0
:Author: Tiny
:Directory: point_of_sale
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Main features :
   - Fast encoding of the sale.
   - Allow to choose one payment mode (the quick way) or to split the payment between several payment mode.
   - Computation of the amount of money to return.
   - Create and confirm picking list automatically.
   - Allow the user to create invoice automatically.
   - Allow to refund former sales.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/point_of_sale.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/point_of_sale.zip>`_


Dependencies
------------

 * :mod:`sale`
 * :mod:`purchase`
 * :mod:`account`
 * :mod:`account_tax_include`

Reports
-------

 * Receipt

 * Invoice

 * Details of Sales

 * Sales (summary)

 * Pos Lines

Menus
-------

 * Point of Sale/Configuration
 * Point of Sale
 * Point of Sale/Point of Sale
 * Point of Sale/Configuration/Default journals
 * Point of Sale/Point of Sale/Orders of the day
 * Point of Sale/Point of Sale/All orders
 * Point of Sale/POS Lines
 * Point of Sale/POS Lines/POS Lines of the day
 * Point of Sale/Reporting
 * Point of Sale/Reporting/Sales of the day
 * Point of Sale/Reporting/Sales of the month
 * Point of Sale/Reporting/All the sales

Views
-----

 * pos.order (form)
 * Sales (tree)
 * Sale lines (tree)
 * Sale line (form)
 * report.trans.pos.user.form (form)
 * Sales by user (tree)


Objects
-------

Object: Point of Sale journal configuration. (pos.config.journal)
#################################################################



:code: Code, char





:name: Description, char





:journal_id: Journal, many2one




Object: Point of Sale (pos.order)
#################################



:sale_journal: Journal, many2one, required, readonly





:date_validity: Validity Date, date, required





:account_move: Account Entry, many2one, readonly





:date_order: Date Ordered, datetime, readonly





:partner_id: Partner, many2one, readonly





:last_out_picking: Last Output Picking, many2one, readonly





:nb_print: Number of Print, integer, readonly





:note: Notes, text





:user_id: Logged in User, many2one, readonly

    *This is the logged in user (not necessarily the salesman).*



:pickings: Picking, one2many, readonly





:invoice_wanted: Create Invoice, boolean





:amount_tax: Taxes, float, readonly





:state: State, selection, readonly





:pricelist_id: Pricelist, many2one, required, readonly





:amount_return: unknown, float, readonly





:account_receivable: Default Receivable, many2one, required, readonly





:amount_paid: unknown, float, readonly





:amount_total: Total, float, readonly





:name: Order Description, char, required, readonly





:invoice_id: Invoice, many2one, readonly





:lines: Order Lines, one2many, readonly





:salesman_id: Salesman, many2one

    *This is the salesman actually making the order.*



:shop_id: Shop, many2one, required, readonly





:payments: Order Payments, one2many, readonly




Object: Lines of Point of Sale (pos.order.line)
###############################################



:create_date: Creation Date, datetime, readonly





:name: Line Description, char





:order_id: Order Ref, many2one





:price_unit: Unit Price, float, required





:price_subtotal: Subtotal, float, readonly





:qty: Quantity, float





:discount: Discount (%), float





:product_id: Product, many2one, required




Object: Pos Payment (pos.payment)
#################################



:payment_id: Payment Term, many2one





:payment_date: Payment Date, date, required





:payment_name: Payment Name, char





:name: Description, char





:order_id: Order Ref, many2one, required





:journal_id: Journal, many2one, required





:amount: Amount, float, required





:payment_nb: Piece Number, char




Object: transaction for the pos (report.transaction.pos)
########################################################



:user_id: User, many2one, readonly





:no_trans: Number of Transaction, float, readonly





:invoice_id: Invoice, many2one, readonly





:journal_id: Journal, many2one, readonly





:date_create: Date, char, readonly





:amount: Amount, float, readonly


