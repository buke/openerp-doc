
.. module:: product_extended
    :synopsis: Product extension to track sales and purchases 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_extended"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Product extension to track sales and purchases (*product_extended*)
===================================================================
:Module: product_extended
:Name: Product extension to track sales and purchases
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_extended
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Product extension. This module adds:
    * Last purchase order for each product supplier 
    * New functional field: Available stock (real+outgoing stock)
    * Computes standard price from the BoM of the product (optional for each product)
    * Standard price is shown in the BoM and it can be computed with a wizard

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_extended.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_extended.zip>`_


Dependencies
------------

 * :mod:`product`
 * :mod:`purchase`
 * :mod:`sale`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT product_extended.supplierinfo.form.view (form)
 * \* INHERIT product_extended.supplierinfo.tree.view (tree)
 * \* INHERIT product_extended.product.form.view (form)
 * \* INHERIT product_extended.product.form.view (form)
 * \* INHERIT mrp.bom.form.product_extended (form)
 * \* INHERIT mrp.bom.tree.product_extended (tree)


Objects
-------

None
