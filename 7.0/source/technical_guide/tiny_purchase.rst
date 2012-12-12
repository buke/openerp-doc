
.. module:: tiny_purchase
    :synopsis: Tiny purchase 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/tiny_purchase"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Tiny purchase (*tiny_purchase*)
===============================
:Module: tiny_purchase
:Name: Tiny purchase
:Version: 5.0.0.1
:Author: Tiny
:Directory: tiny_purchase
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Very simple purchase module.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/tiny_purchase.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/tiny_purchase.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

 * Print Order

Menus
-------

 * Tools
 * Tools/Tiny Purchase
 * Tools/Tiny Purchase/Purchase line
 * Tools/Tiny Purchase/Configuration
 * Tools/Tiny Purchase/Configuration/Purchase product
 * Tools/Tiny Purchase/Purchase Order

Views
-----

 * tiny_purchase.line.form (form)
 * tiny_purchase.product.form (form)
 * tiny_purchase.order.form (form)


Objects
-------

Object: tiny_purchase.product (tiny_purchase.product)
#####################################################



:price: Price, float





:name: Name, char




Object: tiny_purchase.order (tiny_purchase.order)
#################################################



:line_ids: Lines, one2many





:state: State, selection





:user_id: User, many2one, required





:name: Date, date




Object: tiny_purchase.line (tiny_purchase.line)
###############################################



:order_id: Order, many2one, required





:price: Price, float, readonly





:product_id: Product, many2one, required





:comments: Comments, text





:quantity: Quantity, integer


