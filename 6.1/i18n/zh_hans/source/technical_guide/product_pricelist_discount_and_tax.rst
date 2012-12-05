
.. i18n: .. module:: product_pricelist_discount_and_tax
.. i18n:     :synopsis: Price list discount and tax handling 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: product_pricelist_discount_and_tax
    :synopsis: Price list discount and tax handling 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_pricelist_discount_and_tax"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_pricelist_discount_and_tax"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Price list discount and tax handling (*product_pricelist_discount_and_tax*)
.. i18n: ===========================================================================
.. i18n: :Module: product_pricelist_discount_and_tax
.. i18n: :Name: Price list discount and tax handling
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Gábor Dukai
.. i18n: :Directory: product_pricelist_discount_and_tax
.. i18n: :Web: http://exploringopenerp.blogspot.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   A complete solution for those companies who use discounts and/or 
.. i18n:       product prices with tax included extensively.
.. i18n:       
.. i18n:       This module is like product_visible_discount but improved in many ways:
.. i18n:         -Properly calculates discounts for any price type, not only list_price.
.. i18n:         -It's able to add/subtract tax from the price before calculating the discount.
.. i18n:         This means you can have for example a 'shop price' calculated with tax included
.. i18n:         and define a price list like 'shop price net -5%' easily.
.. i18n:         -It works with product_price_update that module can mass calculate and 
.. i18n:         update product prices with tax included.
.. i18n:         -A simpler override of the SO's product_id_change, 2 browses and 2 reads less.
.. i18n:         -Purchase Orders can also use discounts if the supplier defines his prices
.. i18n:         with discounts.
.. i18n:         -Even PO's generated with MRP will have the discounts defined in the 
.. i18n:         supplier price list.
.. i18n:       
.. i18n:       Compatibility: tested with OpenERP v5.0
..

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

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n: (No download links available)
..

(No download links available)

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`purchase_discount`
..

 * :mod:`sale`
 * :mod:`purchase_discount`

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

.. i18n: None
..

None

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT product.price.type.form.pricelist_tax_include (form)
.. i18n:  * \* INHERIT product.pricelist.tree.pricelist_tax_include (form)
.. i18n:  * \* INHERIT product.pricelist.form.pricelist_tax_include1 (form)
.. i18n:  * \* INHERIT product.pricelist.form.pricelist_tax_include2 (form)
..

 * \* INHERIT product.price.type.form.pricelist_tax_include (form)
 * \* INHERIT product.pricelist.tree.pricelist_tax_include (form)
 * \* INHERIT product.pricelist.form.pricelist_tax_include1 (form)
 * \* INHERIT product.pricelist.form.pricelist_tax_include2 (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
