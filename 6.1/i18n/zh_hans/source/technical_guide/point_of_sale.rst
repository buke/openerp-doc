
.. i18n: .. module:: point_of_sale
.. i18n:     :synopsis: Point Of Sale (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: point_of_sale
    :synopsis: Point Of Sale (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/point_of_sale"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/point_of_sale"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Point Of Sale (*point_of_sale*)
.. i18n: ===============================
.. i18n: :Module: point_of_sale
.. i18n: :Name: Point Of Sale
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: point_of_sale
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Main features :
.. i18n:    - Fast encoding of the sale.
.. i18n:    - Allow to choose one payment mode (the quick way) or to split the payment between several payment mode.
.. i18n:    - Computation of the amount of money to return.
.. i18n:    - Create and confirm picking list automatically.
.. i18n:    - Allow the user to create invoice automatically.
.. i18n:    - Allow to refund former sales.
..

::

  Main features :
   - Fast encoding of the sale.
   - Allow to choose one payment mode (the quick way) or to split the payment between several payment mode.
   - Computation of the amount of money to return.
   - Create and confirm picking list automatically.
   - Allow the user to create invoice automatically.
   - Allow to refund former sales.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/point_of_sale.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/point_of_sale.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/point_of_sale.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/point_of_sale.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`purchase`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`account_tax_include`
..

 * :mod:`sale`
 * :mod:`purchase`
 * :mod:`account`
 * :mod:`account_tax_include`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Receipt
.. i18n: 
.. i18n:  * Invoice
.. i18n: 
.. i18n:  * Details of Sales
.. i18n: 
.. i18n:  * Sales (summary)
.. i18n: 
.. i18n:  * Pos Lines
..

 * Receipt

 * Invoice

 * Details of Sales

 * Sales (summary)

 * Pos Lines

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Point of Sale/Configuration
.. i18n:  * Point of Sale
.. i18n:  * Point of Sale/Point of Sale
.. i18n:  * Point of Sale/Configuration/Default journals
.. i18n:  * Point of Sale/Point of Sale/Orders of the day
.. i18n:  * Point of Sale/Point of Sale/All orders
.. i18n:  * Point of Sale/POS Lines
.. i18n:  * Point of Sale/POS Lines/POS Lines of the day
.. i18n:  * Point of Sale/Reporting
.. i18n:  * Point of Sale/Reporting/Sales of the day
.. i18n:  * Point of Sale/Reporting/Sales of the month
.. i18n:  * Point of Sale/Reporting/All the sales
..

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

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * pos.order (form)
.. i18n:  * Sales (tree)
.. i18n:  * Sale lines (tree)
.. i18n:  * Sale line (form)
.. i18n:  * report.trans.pos.user.form (form)
.. i18n:  * Sales by user (tree)
..

 * pos.order (form)
 * Sales (tree)
 * Sale lines (tree)
 * Sale line (form)
 * report.trans.pos.user.form (form)
 * Sales by user (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Point of Sale journal configuration. (pos.config.journal)
.. i18n: #################################################################
..

Object: Point of Sale journal configuration. (pos.config.journal)
#################################################################

.. i18n: :code: Code, char
..

:code: Code, char

.. i18n: :name: Description, char
..

:name: Description, char

.. i18n: :journal_id: Journal, many2one
..

:journal_id: Journal, many2one

.. i18n: Object: Point of Sale (pos.order)
.. i18n: #################################
..

Object: Point of Sale (pos.order)
#################################

.. i18n: :sale_journal: Journal, many2one, required, readonly
..

:sale_journal: Journal, many2one, required, readonly

.. i18n: :date_validity: Validity Date, date, required
..

:date_validity: Validity Date, date, required

.. i18n: :account_move: Account Entry, many2one, readonly
..

:account_move: Account Entry, many2one, readonly

.. i18n: :date_order: Date Ordered, datetime, readonly
..

:date_order: Date Ordered, datetime, readonly

.. i18n: :partner_id: Partner, many2one, readonly
..

:partner_id: Partner, many2one, readonly

.. i18n: :last_out_picking: Last Output Picking, many2one, readonly
..

:last_out_picking: Last Output Picking, many2one, readonly

.. i18n: :nb_print: Number of Print, integer, readonly
..

:nb_print: Number of Print, integer, readonly

.. i18n: :note: Notes, text
..

:note: Notes, text

.. i18n: :user_id: Logged in User, many2one, readonly
..

:user_id: Logged in User, many2one, readonly

.. i18n:     *This is the logged in user (not necessarily the salesman).*
..

    *This is the logged in user (not necessarily the salesman).*

.. i18n: :pickings: Picking, one2many, readonly
..

:pickings: Picking, one2many, readonly

.. i18n: :invoice_wanted: Create Invoice, boolean
..

:invoice_wanted: Create Invoice, boolean

.. i18n: :amount_tax: Taxes, float, readonly
..

:amount_tax: Taxes, float, readonly

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :pricelist_id: Pricelist, many2one, required, readonly
..

:pricelist_id: Pricelist, many2one, required, readonly

.. i18n: :amount_return: unknown, float, readonly
..

:amount_return: unknown, float, readonly

.. i18n: :account_receivable: Default Receivable, many2one, required, readonly
..

:account_receivable: Default Receivable, many2one, required, readonly

.. i18n: :amount_paid: unknown, float, readonly
..

:amount_paid: unknown, float, readonly

.. i18n: :amount_total: Total, float, readonly
..

:amount_total: Total, float, readonly

.. i18n: :name: Order Description, char, required, readonly
..

:name: Order Description, char, required, readonly

.. i18n: :invoice_id: Invoice, many2one, readonly
..

:invoice_id: Invoice, many2one, readonly

.. i18n: :lines: Order Lines, one2many, readonly
..

:lines: Order Lines, one2many, readonly

.. i18n: :salesman_id: Salesman, many2one
..

:salesman_id: Salesman, many2one

.. i18n:     *This is the salesman actually making the order.*
..

    *This is the salesman actually making the order.*

.. i18n: :shop_id: Shop, many2one, required, readonly
..

:shop_id: Shop, many2one, required, readonly

.. i18n: :payments: Order Payments, one2many, readonly
..

:payments: Order Payments, one2many, readonly

.. i18n: Object: Lines of Point of Sale (pos.order.line)
.. i18n: ###############################################
..

Object: Lines of Point of Sale (pos.order.line)
###############################################

.. i18n: :create_date: Creation Date, datetime, readonly
..

:create_date: Creation Date, datetime, readonly

.. i18n: :name: Line Description, char
..

:name: Line Description, char

.. i18n: :order_id: Order Ref, many2one
..

:order_id: Order Ref, many2one

.. i18n: :price_unit: Unit Price, float, required
..

:price_unit: Unit Price, float, required

.. i18n: :price_subtotal: Subtotal, float, readonly
..

:price_subtotal: Subtotal, float, readonly

.. i18n: :qty: Quantity, float
..

:qty: Quantity, float

.. i18n: :discount: Discount (%), float
..

:discount: Discount (%), float

.. i18n: :product_id: Product, many2one, required
..

:product_id: Product, many2one, required

.. i18n: Object: Pos Payment (pos.payment)
.. i18n: #################################
..

Object: Pos Payment (pos.payment)
#################################

.. i18n: :payment_id: Payment Term, many2one
..

:payment_id: Payment Term, many2one

.. i18n: :payment_date: Payment Date, date, required
..

:payment_date: Payment Date, date, required

.. i18n: :payment_name: Payment Name, char
..

:payment_name: Payment Name, char

.. i18n: :name: Description, char
..

:name: Description, char

.. i18n: :order_id: Order Ref, many2one, required
..

:order_id: Order Ref, many2one, required

.. i18n: :journal_id: Journal, many2one, required
..

:journal_id: Journal, many2one, required

.. i18n: :amount: Amount, float, required
..

:amount: Amount, float, required

.. i18n: :payment_nb: Piece Number, char
..

:payment_nb: Piece Number, char

.. i18n: Object: transaction for the pos (report.transaction.pos)
.. i18n: ########################################################
..

Object: transaction for the pos (report.transaction.pos)
########################################################

.. i18n: :user_id: User, many2one, readonly
..

:user_id: User, many2one, readonly

.. i18n: :no_trans: Number of Transaction, float, readonly
..

:no_trans: Number of Transaction, float, readonly

.. i18n: :invoice_id: Invoice, many2one, readonly
..

:invoice_id: Invoice, many2one, readonly

.. i18n: :journal_id: Journal, many2one, readonly
..

:journal_id: Journal, many2one, readonly

.. i18n: :date_create: Date, char, readonly
..

:date_create: Date, char, readonly

.. i18n: :amount: Amount, float, readonly
..

:amount: Amount, float, readonly
