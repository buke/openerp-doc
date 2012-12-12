
.. module:: sandwich
    :synopsis: Sandwich Module 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sandwich"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Sandwich Module (*sandwich*)
============================
:Module: sandwich
:Name: Sandwich Module
:Version: 5.0.1.0
:Author: Tiny
:Directory: sandwich
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

  * `5.0 <http://www.openerp.com/download/modules/5.0/sandwich.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/sandwich.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`product`

Reports
-------

 * Sandwichs order

Menus
-------

 * Tools
 * Tools/Sandwich
 * Tools/Sandwich/Configuration
 * Tools/Sandwich/Configuration/Type of Product
 * Tools/Sandwich/Configuration/Product
 * Tools/Sandwich/Order Lines
 * Tools/Sandwich/Order Lines/My Order Lines
 * Tools/Sandwich/Order Lines/My Order Lines/My Order Lines of the Day
 * Tools/Sandwich/Order Lines/Order Lines of the Day
 * Tools/Sandwich/Today's Orders
 * Tools/Sandwich/Create Order

Views
-----

 * sandwich.product.type (form)
 * sandwich.product.type (tree)
 * sandwich.product (tree)
 * sandwich.product (form)
 * sandwich.order.line.tree (tree)
 * sandwich.order.line.form (form)
 * sandwich.order.tree (tree)
 * sandwich.order.form (form)


Objects
-------

Object: sandwich.product.type (sandwich.product.type)
#####################################################



:name: Name of the type, char, required





:description: Type's description, char




Object: sandwich.product (sandwich.product)
###########################################



:price: Product price, float





:name: Product name, char, required





:product_type_id: Type of product, many2one




Object: sandwich.order (sandwich.order)
#######################################



:date: Order date, date





:note: Notes, text





:partner: Partner, many2one, required





:name: Name, char, required





:order_lines: Order lines, one2many




Object: sandwich.order.line (sandwich.order.line)
#################################################



:user_id: User id, many2one, required





:name: Description, char, required





:order_id: Order, many2one





:product_id: Product, many2one





:date: Date, date





:quantity: Quantity, integer, required





:product_type_id: Product type, many2one


