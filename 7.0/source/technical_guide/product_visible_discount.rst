
.. module:: product_visible_discount
    :synopsis: Visible Discount 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_visible_discount"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Visible Discount (*product_visible_discount*)
=============================================
:Module: product_visible_discount
:Name: Visible Discount
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_visible_discount
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  This module lets you calculate discounts on Sale Order lines and Invoice lines base on the partner's pricelist.
      To this end, a new check box named "Visible Discount" is added to the pricelist form.
      Example:
          For the product PC1 and the partner "Asustek": if listprice=450, and the price calculated using Asustek's pricelist is 225
          If the check box is checked, we will have on the sale order line: Unit price=450, Discount=50,00, Net price=225
          If the check box is unchecked, we will have on Sale Order and Invoice lines: Unit price=225, Discount=0,00, Net price=225

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_visible_discount.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_visible_discount.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`product`
 * :mod:`account`
 * :mod:`sale`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT product.pricelist.tree (form)
 * \* INHERIT product.pricelist.form (form)


Objects
-------

None
