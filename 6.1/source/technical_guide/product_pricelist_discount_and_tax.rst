
.. module:: product_pricelist_discount_and_tax
    :synopsis: Price list discount and tax handling 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_pricelist_discount_and_tax"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Price list discount and tax handling (*product_pricelist_discount_and_tax*)
===========================================================================
:Module: product_pricelist_discount_and_tax
:Name: Price list discount and tax handling
:Version: 5.0.1.1
:Author: Gábor Dukai
:Directory: product_pricelist_discount_and_tax
:Web: http://exploringopenerp.blogspot.com
:Official module: no
:Quality certified: no

Description
-----------

::

  A complete solution for those companies who use discounts and/or 
      product prices with tax included extensively.
      
      This module is like product_visible_discount but improved in many ways:
        -Properly calculates discounts for any price type, not only list_price.
        -It's able to add/subtract tax from the price before calculating the discount.
        This means you can have for example a 'shop price' calculated with tax included
        and define a price list like 'shop price net -5%' easily.
        -It works with product_price_update that module can mass calculate and 
        update product prices with tax included.
        -A simpler override of the SO's product_id_change, 2 browses and 2 reads less.
        -Purchase Orders can also use discounts if the supplier defines his prices
        with discounts.
        -Even PO's generated with MRP will have the discounts defined in the 
        supplier price list.
      
      Compatibility: tested with OpenERP v5.0

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`sale`
 * :mod:`purchase_discount`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT product.price.type.form.pricelist_tax_include (form)
 * \* INHERIT product.pricelist.tree.pricelist_tax_include (form)
 * \* INHERIT product.pricelist.form.pricelist_tax_include1 (form)
 * \* INHERIT product.pricelist.form.pricelist_tax_include2 (form)


Objects
-------

None
