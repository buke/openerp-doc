
.. i18n: .. module:: report_purchase
.. i18n:     :synopsis: Purchase Management - Reporting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: report_purchase
    :synopsis: Purchase Management - Reporting (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_purchase"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_purchase"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Purchase Management - Reporting (*report_purchase*)
.. i18n: ===================================================
.. i18n: :Module: report_purchase
.. i18n: :Name: Purchase Management - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_purchase
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module to add views like
.. i18n:       Purchase By Product, Purchase By Category of Product, All Months, Current Month.
..

::

  Module to add views like
      Purchase By Product, Purchase By Category of Product, All Months, Current Month.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/report_purchase.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/report_purchase.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/report_purchase.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_purchase.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_purchase.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_purchase.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`purchase`
..

 * :mod:`purchase`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n: None
..

None

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Purchase Management/Reporting
.. i18n:  * Purchase Management/Reporting/This Month
.. i18n:  * Purchase Management/Reporting/This Month/Purchases by Products (this month)
.. i18n:  * Purchase Management/Reporting/All Months
.. i18n:  * Purchase Management/Reporting/All Months/Purchases by Products
.. i18n:  * Purchase Management/Reporting/This Month/Purchases by Category of Product (this month)
.. i18n:  * Purchase Management/Reporting/All Months/Purchases by Category of Products
..

 * Purchase Management/Reporting
 * Purchase Management/Reporting/This Month
 * Purchase Management/Reporting/This Month/Purchases by Products (this month)
 * Purchase Management/Reporting/All Months
 * Purchase Management/Reporting/All Months/Purchases by Products
 * Purchase Management/Reporting/This Month/Purchases by Category of Product (this month)
 * Purchase Management/Reporting/All Months/Purchases by Category of Products

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * report.purchase.order.product.form (form)
.. i18n:  * product.month.graph (graph)
.. i18n:  * report.purchase.order.product.tree (tree)
.. i18n:  * report.purchase.order.category.form (form)
.. i18n:  * product.category.graph (graph)
.. i18n:  * report.purchase.order.category.tree (tree)
..

 * report.purchase.order.product.form (form)
 * product.month.graph (graph)
 * report.purchase.order.product.tree (tree)
 * report.purchase.order.category.form (form)
 * product.category.graph (graph)
 * report.purchase.order.category.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Purchases Orders by Products (report.purchase.order.product)
.. i18n: ####################################################################
..

Object: Purchases Orders by Products (report.purchase.order.product)
####################################################################

.. i18n: :count: # of Lines, integer, readonly
..

:count: # of Lines, integer, readonly

.. i18n: :price_total: Total Price, float, readonly
..

:price_total: Total Price, float, readonly

.. i18n: :name: Month, date, readonly
..

:name: Month, date, readonly

.. i18n: :state: Order State, selection, readonly
..

:state: Order State, selection, readonly

.. i18n: :price_average: Average Price, float, readonly
..

:price_average: Average Price, float, readonly

.. i18n: :product_id: Product, many2one, readonly
..

:product_id: Product, many2one, readonly

.. i18n: :quantity: # of Products, float, readonly
..

:quantity: # of Products, float, readonly

.. i18n: Object: Purchases Orders by Categories (report.purchase.order.category)
.. i18n: #######################################################################
..

Object: Purchases Orders by Categories (report.purchase.order.category)
#######################################################################

.. i18n: :count: # of Lines, integer, readonly
..

:count: # of Lines, integer, readonly

.. i18n: :price_total: Total Price, float, readonly
..

:price_total: Total Price, float, readonly

.. i18n: :name: Month, date, readonly
..

:name: Month, date, readonly

.. i18n: :state: Order State, selection, readonly
..

:state: Order State, selection, readonly

.. i18n: :price_average: Average Price, float, readonly
..

:price_average: Average Price, float, readonly

.. i18n: :category_id: Categories, many2one, readonly
..

:category_id: Categories, many2one, readonly

.. i18n: :quantity: # of Products, float, readonly
..

:quantity: # of Products, float, readonly
