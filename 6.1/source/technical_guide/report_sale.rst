
.. module:: report_sale
    :synopsis: Sales Management - Reporting (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_sale"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Sales Management - Reporting (*report_sale*)
============================================
:Module: report_sale
:Name: Sales Management - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_sale
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Reporting for the sale module:
      * Sales order by product (my/this month/all)
      * Sales order by category of product (my/this month/all)
  
      Some predefined lists:
      * Sales of the month
      * Open quotations
      * Uninvoiced Sales
      * Uninvoiced but shipped Sales

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_sale.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_sale.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_sale.zip>`_


Dependencies
------------

 * :mod:`sale`

Reports
-------

None


Menus
-------

 * Sales Management/Reporting
 * Sales Management/Reporting/This Month
 * Sales Management/Reporting/This Month/Sales by Product (this month)
 * Sales Management/Reporting/All Months
 * Sales Management/Reporting/All Months/Sales by Product
 * Sales Management/Reporting/This Month/Sales by Category of Product (this month)
 * Sales Management/Reporting/All Months/Sales by Category of Products
 * Sales Management/Reporting/This Month/Sales of the Month
 * Sales Management/Reporting/All Months/Graphs
 * Sales Management/Reporting/All Months/Graphs/Monthly Sales Turnover Over One Year
 * Sales Management/Reporting/All Months/Graphs/Daily Sales Turnover Over One Year
 * Sales Management/Reporting/All Months/Graphs/Monthly Cumulated Sales Turnover Over One Year

Views
-----

 * report.sale.order.product.form (form)
 * report.sale.order.product.tree (tree)
 * report.sale.order.product.graph (graph)
 * report.sale.order.category.form (form)
 * report.sale.order.category.tree (tree)
 * report.sale.order.category.graph (graph)
 * sale.order.graph (graph)
 * sale.order.dashboard.graph (graph)
 * report.turnover.per.month.tree (tree)
 * report.turnover.per.month.graph (graph)
 * report.turnover.per.product.tree (tree)
 * report.turnover.per.product.graph (graph)
 * report.sale.order.created.tree (tree)


Objects
-------

Object: Sales Orders by Products (report.sale.order.product)
############################################################



:count: # of Lines, integer, readonly





:price_total: Total Price, float, readonly





:name: Month, date, readonly





:state: Order State, selection, readonly





:price_average: Average Price, float, readonly





:product_id: Product, many2one, readonly





:quantity: # of Products, float, readonly




Object: Sales Orders by Categories (report.sale.order.category)
###############################################################



:count: # of Lines, integer, readonly





:price_total: Total Price, float, readonly





:name: Month, date, readonly





:state: Order State, selection, readonly





:price_average: Average Price, float, readonly





:category_id: Categories, many2one, readonly





:quantity: # of Products, float, readonly




Object: Turnover Per Month (report.turnover.per.month)
######################################################



:name: Month, date, readonly





:turnover: Total Turnover, float, readonly




Object: Turnover Per Product (report.turnover.per.product)
##########################################################



:product_id: Product, many2one, readonly





:turnover: Total Turnover, float, readonly




Object: Report of Created Sale Order (report.sale.order.created)
################################################################



:create_date: Create Date, datetime





:name: Order Reference, char, readonly





:partner_shipping_id: Shipping Address, many2one, readonly





:state: Order State, selection, readonly





:amount_untaxed: Untaxed Amount, float, readonly





:date_order: Date Ordered, date, readonly





:partner_id: Customer, many2one, readonly


