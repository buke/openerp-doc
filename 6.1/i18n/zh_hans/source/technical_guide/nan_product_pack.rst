
.. i18n: .. module:: nan_product_pack
.. i18n:     :synopsis: Product Pack 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: nan_product_pack
    :synopsis: Product Pack 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/nan_product_pack"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/nan_product_pack"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Product Pack (*nan_product_pack*)
.. i18n: =================================
.. i18n: :Module: nan_product_pack
.. i18n: :Name: Product Pack
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: NaN for Trod y Avia, S.L.
.. i18n: :Directory: nan_product_pack
.. i18n: :Web: http://www.NaN-tic.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Allows configuring products as a collection of other products. If such a product is added in a sale order, all the products of the pack will be added automatically (when storing the order) as children of the pack product.
..

::

  Allows configuring products as a collection of other products. If such a product is added in a sale order, all the products of the pack will be added automatically (when storing the order) as children of the pack product.

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
..

 * :mod:`sale`

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

.. i18n:  * \* INHERIT product.product.pack.form (form)
.. i18n:  * product.pack.line.form (form)
.. i18n:  * product.pack.line.tree (tree)
..

 * \* INHERIT product.product.pack.form (form)
 * product.pack.line.form (form)
 * product.pack.line.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: product.pack.line (product.pack.line)
.. i18n: #############################################
..

Object: product.pack.line (product.pack.line)
#############################################

.. i18n: :product_id: Product, many2one, required
..

:product_id: Product, many2one, required

.. i18n: :parent_product_id: Parent Product, many2one, required
..

:parent_product_id: Parent Product, many2one, required

.. i18n: :quantity: Quantity, float, required
..

:quantity: Quantity, float, required
