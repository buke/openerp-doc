
.. module:: report_purchase
    :synopsis: Purchase Management - Reporting (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_purchase"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Purchase Management - Reporting (*report_purchase*)
===================================================
:Module: report_purchase
:Name: Purchase Management - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_purchase
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Module to add views like
      Purchase By Product, Purchase By Category of Product, All Months, Current Month.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_purchase.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_purchase.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_purchase.zip>`_


Dependencies
------------

 * :mod:`purchase`

Reports
-------

None


Menus
-------

 * Purchase Management/Reporting
 * Purchase Management/Reporting/This Month
 * Purchase Management/Reporting/This Month/Purchases by Products (this month)
 * Purchase Management/Reporting/All Months
 * Purchase Management/Reporting/All Months/Purchases by Products
 * Purchase Management/Reporting/This Month/Purchases by Category of Product (this month)
 * Purchase Management/Reporting/All Months/Purchases by Category of Products

Views
-----

 * report.purchase.order.product.form (form)
 * product.month.graph (graph)
 * report.purchase.order.product.tree (tree)
 * report.purchase.order.category.form (form)
 * product.category.graph (graph)
 * report.purchase.order.category.tree (tree)


Objects
-------

Object: Purchases Orders by Products (report.purchase.order.product)
####################################################################



:count: # of Lines, integer, readonly





:price_total: Total Price, float, readonly





:name: Month, date, readonly





:state: Order State, selection, readonly





:price_average: Average Price, float, readonly





:product_id: Product, many2one, readonly





:quantity: # of Products, float, readonly




Object: Purchases Orders by Categories (report.purchase.order.category)
#######################################################################



:count: # of Lines, integer, readonly





:price_total: Total Price, float, readonly





:name: Month, date, readonly





:state: Order State, selection, readonly





:price_average: Average Price, float, readonly





:category_id: Categories, many2one, readonly





:quantity: # of Products, float, readonly


