
.. module:: nan_product_pack
    :synopsis: Product Pack 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/nan_product_pack"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Product Pack (*nan_product_pack*)
=================================
:Module: nan_product_pack
:Name: Product Pack
:Version: 5.0.0.1
:Author: NaN for Trod y Avia, S.L.
:Directory: nan_product_pack
:Web: http://www.NaN-tic.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Allows configuring products as a collection of other products. If such a product is added in a sale order, all the products of the pack will be added automatically (when storing the order) as children of the pack product.

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`sale`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT product.product.pack.form (form)
 * product.pack.line.form (form)
 * product.pack.line.tree (tree)


Objects
-------

Object: product.pack.line (product.pack.line)
#############################################



:product_id: Product, many2one, required





:parent_product_id: Parent Product, many2one, required





:quantity: Quantity, float, required


