
.. module:: sale_supplier_direct_delivery
    :synopsis: Automates direct delivery between a supplier and a customer 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_supplier_direct_delivery"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

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

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/sale_supplier_direct_delivery.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/sale_supplier_direct_delivery.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`product`
 * :mod:`sale`
 * :mod:`purchase`

Reports
-------

None


Menus
-------

 * Stock Management/Supplier Direct Delivery

Views
-----

 * \* INHERIT product.supplierinfo.tree.direct_delivery.inherit (tree)
 * \* INHERIT product.supplierinfo.form.direct_delivery.inherit (form)
 * \* INHERIT sale.order.tree.direct_delivery (tree)
 * \* INHERIT sale.order.line.form.direct_delivery (form)
 * \* INHERIT sale.order.line.tree.direct_delivery (form)
 * \* INHERIT purchase.order.tree.direct_delivery (tree)
 * \* INHERIT purchase.order.line.form.direct_delivery (form)
 * \* INHERIT purchase.order.line.tree.direct_delivery (tree)


Objects
-------

None
