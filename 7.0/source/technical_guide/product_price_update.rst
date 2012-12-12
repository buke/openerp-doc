
.. module:: product_price_update
    :synopsis: Product price update 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_price_update"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Product price update (*product_price_update*)
=============================================
:Module: product_price_update
:Name: Product price update
:Version: 5.0.1.1
:Author: Gábor Dukai
:Directory: product_price_update
:Web: http://exploringopenerp.blogspot.com
:Official module: no
:Quality certified: no

Description
-----------

::

  You can think of this module as product_listprice_upgrade v2.
  
      The aim of this module is to allow the automatic update of the price fields of products.
      * added a new pricelist type called 'Internal Pricelist' (currently, we have only 2 pricelist types: Sale and Purchase Pricelist)
      * Created a wizard button in the menu Products>Pricelist called 'Update Product Prices'
      * After filling in the wizard form and clicking on 'Update', it will change the selected price field of all products in the categories that we were selected in the wizard.
  
      Compatibility: tested with OpenERP v5.0

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_price_update.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_price_update.zip>`_


Dependencies
------------

 * :mod:`product`
 * :mod:`product_pricelist_discount_and_tax`

Reports
-------

None


Menus
-------

 * Products/Pricelists/Update Product Prices

Views
-----

 * Updated the price of products (form)
 * Update Product Prices (form)


Objects
-------

Object: product.price.update.wizard (product.price.update.wizard)
#################################################################



:pricelist_id: Select a Pricelist, many2one, required





:upgrade: Update child categories, boolean





:categ_ids: Select Product Categories, many2many, required





:price_type_id: Price to Update, many2one, required




Object: product.price.update.wizard.done (product.price.update.wizard.done)
###########################################################################



:updated_field: Updated price type, char, readonly





:updated_products: Number of updated products, float, readonly


