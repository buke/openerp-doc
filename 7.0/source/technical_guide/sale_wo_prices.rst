
.. module:: sale_wo_prices
    :synopsis: Sales without prices 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_wo_prices"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Sales without prices (*sale_wo_prices*)
=======================================
:Module: sale_wo_prices
:Name: Sales without prices
:Version: 5.0.1.0
:Author: Zikzakmedia SL
:Directory: sale_wo_prices
:Web: www.zikzakmedia.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Hides prices in sales and product forms. Only sale manager can see them. Normal salesmen can do sales without seeing the product prices.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/sale_wo_prices.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/sale_wo_prices.zip>`_


Dependencies
------------

 * :mod:`sale`
 * :mod:`product`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT product.normal.form.wop1 (form)
 * \* INHERIT product.product.tree.wop1 (tree)
 * \* INHERIT product.product.tree.wop2 (tree)
 * \* INHERIT product.product.tree.wop3 (tree)
 * \* INHERIT sale.order.form.wop1 (form)
 * \* INHERIT sale.order.form.wop2 (form)
 * \* INHERIT sale.order.form.wop3 (form)
 * \* INHERIT sale.order.form.wop4 (form)
 * \* INHERIT sale.order.form.wop5 (form)
 * \* INHERIT sale.order.form.wop6 (form)
 * \* INHERIT sale.order.tree.wop1 (tree)


Objects
-------

None
