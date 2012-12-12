
.. module:: sale_margin
    :synopsis: Margins (amount and percent) in Sale Orders 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_margin"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Margins (amount and percent) in Sale Orders (*sale_margin*)
============================================================
:Module: sale_margin
:Name: Margins (amount and percent) in Sale Orders
:Version: 5.0.1.0
:Author: Everlibre & SYLEAM
:Directory: sale_margin
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  None

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/sale_margin.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/sale_margin.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/sale_margin.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`sale`
 * :mod:`account`

Reports
-------

None


Menus
-------

 * Financial Management/Reporting/Invoice
 * Financial Management/Reporting/Invoice/This Month
 * Financial Management/Reporting/Invoice/This Month/Invoices by Product
 * Financial Management/Reporting/Invoice/All Months
 * Financial Management/Reporting/Invoice/All Months/Invoices by Product
 * Financial Management/Reporting/Invoice/This Month/Invoices by Category
 * Financial Management/Reporting/Invoice/All Months/Invoices by Category
 * Financial Management/Reporting/Invoice/This Month/Invoices by Partner
 * Financial Management/Reporting/Invoice/All Months/Invoices by Partner
 * Financial Management/Reporting/Invoice/This Month/Invoices by Partner and Product
 * Financial Management/Reporting/Invoice/All Months/Invoices by Partner and Product
 * Financial Management/Reporting/Invoice/This Month/Invoices
 * Financial Management/Reporting/Invoice/All Months/Invoices

Views
-----

 * \* INHERIT sale.order.margin.view.form (form)
 * \* INHERIT sale.order.margin.view.tree (tree)
 * \* INHERIT sale.order.margin.view.form (form)
 * \* INHERIT sale.order.margin.view.form2 (form)
 * \* INHERIT sale.order.margin.view.form3 (form)
 * \* INHERIT sale.order.margin.view.form4 (form)
 * \* INHERIT sale.order.margin.line.view.tree (tree)
 * \* INHERIT picking.margin.view.form (form)
 * report.account.invoice.product.tree (tree)
 * report.account.invoice.category.tree (tree)
 * report.account.invoice.partner.tree (tree)
 * report.account.invoice.partner.product.tree (tree)
 * report.account.invoice (tree)


Objects
-------

Object: report.account.invoice.product (report.account.invoice.product)
#######################################################################



:product_id: Product, many2one, readonly





:margin: Margin, float, readonly





:state: State, selection, readonly





:name: Month, date, readonly





:amount: Amount, float, readonly





:quantity: Quantity, float, readonly





:type: Type, selection, readonly





:cost_price: Cost Price, float, readonly




Object: report.account.invoice.category (report.account.invoice.category)
#########################################################################



:name: Month, date, readonly





:categ_id: Categories, many2one, readonly





:state: State, selection, readonly





:amount: Amount, float, readonly





:margin: Margin, float, readonly





:quantity: Quantity, float, readonly





:type: Type, selection, readonly





:cost_price: Cost Price, float, readonly




Object: report.account.invoice.partner (report.account.invoice.partner)
#######################################################################



:name: Month, date, readonly





:partner_id: Partner, many2one, readonly





:state: State, selection, readonly





:amount: Amount, float, readonly





:margin: Margin, float, readonly





:quantity: Quantity, float, readonly





:type: Type, selection, readonly





:cost_price: Cost Price, float, readonly




Object: report.account.invoice.partner.product (report.account.invoice.partner.product)
#######################################################################################



:product_id: Product, many2one, readonly





:quantity: Quantity, float, readonly





:partner_id: Partner, many2one, readonly





:state: State, selection, readonly





:amount: Amount, float, readonly





:margin: Margin, float, readonly





:cost_price: Cost Price, float, readonly





:type: Type, selection, readonly





:name: Month, date, readonly




Object: report.account.invoice (report.account.invoice)
#######################################################



:name: Month, date, readonly





:margin: Margin, float, readonly





:amount: Amount, float, readonly





:state: State, selection, readonly





:quantity: Quantity, float, readonly





:type: Type, selection, readonly





:cost_price: Cost Price, float, readonly


