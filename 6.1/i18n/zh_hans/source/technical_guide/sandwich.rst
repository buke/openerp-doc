
.. i18n: .. module:: sandwich
.. i18n:     :synopsis: Sandwich Module 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: sandwich
    :synopsis: Sandwich Module 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sandwich"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sandwich"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Sandwich Module (*sandwich*)
.. i18n: ============================
.. i18n: :Module: sandwich
.. i18n: :Name: Sandwich Module
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: sandwich
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   None
..

::

  None

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/sandwich.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/sandwich.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/sandwich.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/sandwich.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`
..

 * :mod:`base`
 * :mod:`product`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Sandwichs order
..

 * Sandwichs order

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Tools
.. i18n:  * Tools/Sandwich
.. i18n:  * Tools/Sandwich/Configuration
.. i18n:  * Tools/Sandwich/Configuration/Type of Product
.. i18n:  * Tools/Sandwich/Configuration/Product
.. i18n:  * Tools/Sandwich/Order Lines
.. i18n:  * Tools/Sandwich/Order Lines/My Order Lines
.. i18n:  * Tools/Sandwich/Order Lines/My Order Lines/My Order Lines of the Day
.. i18n:  * Tools/Sandwich/Order Lines/Order Lines of the Day
.. i18n:  * Tools/Sandwich/Today's Orders
.. i18n:  * Tools/Sandwich/Create Order
..

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

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * sandwich.product.type (form)
.. i18n:  * sandwich.product.type (tree)
.. i18n:  * sandwich.product (tree)
.. i18n:  * sandwich.product (form)
.. i18n:  * sandwich.order.line.tree (tree)
.. i18n:  * sandwich.order.line.form (form)
.. i18n:  * sandwich.order.tree (tree)
.. i18n:  * sandwich.order.form (form)
..

 * sandwich.product.type (form)
 * sandwich.product.type (tree)
 * sandwich.product (tree)
 * sandwich.product (form)
 * sandwich.order.line.tree (tree)
 * sandwich.order.line.form (form)
 * sandwich.order.tree (tree)
 * sandwich.order.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: sandwich.product.type (sandwich.product.type)
.. i18n: #####################################################
..

Object: sandwich.product.type (sandwich.product.type)
#####################################################

.. i18n: :name: Name of the type, char, required
..

:name: Name of the type, char, required

.. i18n: :description: Type's description, char
..

:description: Type's description, char

.. i18n: Object: sandwich.product (sandwich.product)
.. i18n: ###########################################
..

Object: sandwich.product (sandwich.product)
###########################################

.. i18n: :price: Product price, float
..

:price: Product price, float

.. i18n: :name: Product name, char, required
..

:name: Product name, char, required

.. i18n: :product_type_id: Type of product, many2one
..

:product_type_id: Type of product, many2one

.. i18n: Object: sandwich.order (sandwich.order)
.. i18n: #######################################
..

Object: sandwich.order (sandwich.order)
#######################################

.. i18n: :date: Order date, date
..

:date: Order date, date

.. i18n: :note: Notes, text
..

:note: Notes, text

.. i18n: :partner: Partner, many2one, required
..

:partner: Partner, many2one, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :order_lines: Order lines, one2many
..

:order_lines: Order lines, one2many

.. i18n: Object: sandwich.order.line (sandwich.order.line)
.. i18n: #################################################
..

Object: sandwich.order.line (sandwich.order.line)
#################################################

.. i18n: :user_id: User id, many2one, required
..

:user_id: User id, many2one, required

.. i18n: :name: Description, char, required
..

:name: Description, char, required

.. i18n: :order_id: Order, many2one
..

:order_id: Order, many2one

.. i18n: :product_id: Product, many2one
..

:product_id: Product, many2one

.. i18n: :date: Date, date
..

:date: Date, date

.. i18n: :quantity: Quantity, integer, required
..

:quantity: Quantity, integer, required

.. i18n: :product_type_id: Product type, many2one
..

:product_type_id: Product type, many2one
