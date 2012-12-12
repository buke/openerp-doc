
.. i18n: .. module:: sale_supplier_direct_delivery
.. i18n:     :synopsis: Automates direct delivery between a supplier and a customer 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: sale_supplier_direct_delivery
    :synopsis: Automates direct delivery between a supplier and a customer 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_supplier_direct_delivery"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_supplier_direct_delivery"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Automates direct delivery between a supplier and a customer (*sale_supplier_direct_delivery*)
.. i18n: =============================================================================================
.. i18n: :Module: sale_supplier_direct_delivery
.. i18n: :Name: Automates direct delivery between a supplier and a customer
.. i18n: :Version: 5.0.0.9
.. i18n: :Author: Smile.fr for Loyalty Expert
.. i18n: :Directory: sale_supplier_direct_delivery
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Automates direct delivery between a supplier and a customer (*sale_supplier_direct_delivery*)
=============================================================================================
:Module: sale_supplier_direct_delivery
:Name: Automates direct delivery between a supplier and a customer
:Version: 5.0.0.9
:Author: Smile.fr for Loyalty Expert
:Directory: sale_supplier_direct_delivery
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
.. i18n:   Enable to send goods directly form supplier to customer taking special care of:
.. i18n:   - making only one picking from supplier location to customer location and using that picking in the sale_order workflow
.. i18n:   - copying the sale order shipping address to the generate purchase order line (so merging purchase orders later on will still work)
.. i18n:   
.. i18n:   Also take note of the following points:
.. i18n:   1) We set automatically a Sale Order line to direct delivery if there isn't enough product in the stock.
.. i18n:   2) We don't try to split such a line, but we set it entirely to direct delivery even if some products are available
.. i18n:   3) In a sale order, some lines can be set to direct while some others are on stock at the same time
.. i18n:   4) When we look if there is enough product on virtual stock for a line, we look at the time the sale order is confirmed,
.. i18n:   we don't try to anticipate if there will be enough virtual stock is the future if the sale order is planned for later.
..

::

  Enable to send goods directly form supplier to customer taking special care of:
  - making only one picking from supplier location to customer location and using that picking in the sale_order workflow
  - copying the sale order shipping address to the generate purchase order line (so merging purchase orders later on will still work)
  
  Also take note of the following points:
  1) We set automatically a Sale Order line to direct delivery if there isn't enough product in the stock.
  2) We don't try to split such a line, but we set it entirely to direct delivery even if some products are available
  3) In a sale order, some lines can be set to direct while some others are on stock at the same time
  4) When we look if there is enough product on virtual stock for a line, we look at the time the sale order is confirmed,
  we don't try to anticipate if there will be enough virtual stock is the future if the sale order is planned for later.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/sale_supplier_direct_delivery.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/sale_supplier_direct_delivery.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/sale_supplier_direct_delivery.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/sale_supplier_direct_delivery.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`purchase`
..

 * :mod:`base`
 * :mod:`product`
 * :mod:`sale`
 * :mod:`purchase`

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

.. i18n:  * Stock Management/Supplier Direct Delivery
..

 * Stock Management/Supplier Direct Delivery

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT product.supplierinfo.tree.direct_delivery.inherit (tree)
.. i18n:  * \* INHERIT product.supplierinfo.form.direct_delivery.inherit (form)
.. i18n:  * \* INHERIT sale.order.tree.direct_delivery (tree)
.. i18n:  * \* INHERIT sale.order.line.form.direct_delivery (form)
.. i18n:  * \* INHERIT sale.order.line.tree.direct_delivery (form)
.. i18n:  * \* INHERIT purchase.order.tree.direct_delivery (tree)
.. i18n:  * \* INHERIT purchase.order.line.form.direct_delivery (form)
.. i18n:  * \* INHERIT purchase.order.line.tree.direct_delivery (tree)
..

 * \* INHERIT product.supplierinfo.tree.direct_delivery.inherit (tree)
 * \* INHERIT product.supplierinfo.form.direct_delivery.inherit (form)
 * \* INHERIT sale.order.tree.direct_delivery (tree)
 * \* INHERIT sale.order.line.form.direct_delivery (form)
 * \* INHERIT sale.order.line.tree.direct_delivery (form)
 * \* INHERIT purchase.order.tree.direct_delivery (tree)
 * \* INHERIT purchase.order.line.form.direct_delivery (form)
 * \* INHERIT purchase.order.line.tree.direct_delivery (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
