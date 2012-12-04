
Control Deliveries and Invoicing
================================

Configuring Orders
------------------

.. index:: 
   pair: control; delivery
   pair: control; invoicing

The way the order is configured will determine its future behaviour:

* :guilabel:`Picking Policy` : ``Partial Delivery`` or ``Complete Delivery``,

* :guilabel:`Shipping Policy` : ``Shipping & Manual Invoice``, ``Payment Before Delivery``,
  ``Invoice on Order After Delivery``, and ``Invoice from Delivery``,

* :guilabel:`Invoice on` : ``Ordered Quantities`` or ``Shipped Quantities``.

  .. tip::  Configuring your Interface

     If you work in the ``Simplified`` view mode, only the :guilabel:`Shipping Policy` field is visible
     in the second order tab.
     To get to the ``Extended`` view mode, go to the :guilabel:`Edit Preferences` link and select the interface of your choice.
     You can also use the :guilabel:`Reconfigure` wizard and configure your interface as :guilabel:`Extended`, or assign the group
     :guilabel:`Usability – Extended View` to the current user.

Picking Mode
------------

The picking mode determines the way the storesperson will do the picking. If the order is put
into :guilabel:`Partial Delivery` mode, the picking order will appear in the list of things for the
storesperson to do as soon as any of the products on the order is available. To get the list of
items to be done, you can use the menu :menuselection:`Warehouse --> Outgoing Deliveries`.
By default, the :guilabel:`Available` filter button is selected, so you immediately see the list of available pickings.

The storesperson will then be able to make a partial delivery of the quantities actually available
and do a second picking operation later when the remaining products are available in stock.

If the picking mode is :guilabel:`Complete Delivery`, the picking order will not appear in the list of
pickings to do until all of the products are available in stock. This way, there will only be a
single delivery for any such order.

If the storesperson wants to do so, the delivery mode can be modified on each picking list even after the
order has been confirmed.

In the case of invoicing from picking, the cost of delivering the products will be
calculated according to multiple deliveries. This risks incurring a higher cost because of
the separate deliveries. If invoicing is done from the order, the customer will only be invoiced
once for the whole delivery, even if the delivery of several items has already been made.

.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium
