
.. i18n: .. module:: product_extended
.. i18n:     :synopsis: Product extension to track sales and purchases 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: product_extended
    :synopsis: Product extension to track sales and purchases 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_extended"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_extended"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Product extension to track sales and purchases (*product_extended*)
.. i18n: ===================================================================
.. i18n: :Module: product_extended
.. i18n: :Name: Product extension to track sales and purchases
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: product_extended
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Product extension. This module adds:
.. i18n:     * Last purchase order for each product supplier 
.. i18n:     * New functional field: Available stock (real+outgoing stock)
.. i18n:     * Computes standard price from the BoM of the product (optional for each product)
.. i18n:     * Standard price is shown in the BoM and it can be computed with a wizard
..

::

  Product extension. This module adds:
    * Last purchase order for each product supplier 
    * New functional field: Available stock (real+outgoing stock)
    * Computes standard price from the BoM of the product (optional for each product)
    * Standard price is shown in the BoM and it can be computed with a wizard

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/product_extended.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/product_extended.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_extended.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_extended.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`product`
.. i18n:  * :mod:`purchase`
.. i18n:  * :mod:`sale`
..

 * :mod:`product`
 * :mod:`purchase`
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

.. i18n:  * \* INHERIT product_extended.supplierinfo.form.view (form)
.. i18n:  * \* INHERIT product_extended.supplierinfo.tree.view (tree)
.. i18n:  * \* INHERIT product_extended.product.form.view (form)
.. i18n:  * \* INHERIT product_extended.product.form.view (form)
.. i18n:  * \* INHERIT mrp.bom.form.product_extended (form)
.. i18n:  * \* INHERIT mrp.bom.tree.product_extended (tree)
..

 * \* INHERIT product_extended.supplierinfo.form.view (form)
 * \* INHERIT product_extended.supplierinfo.tree.view (tree)
 * \* INHERIT product_extended.product.form.view (form)
 * \* INHERIT product_extended.product.form.view (form)
 * \* INHERIT mrp.bom.form.product_extended (form)
 * \* INHERIT mrp.bom.tree.product_extended (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
