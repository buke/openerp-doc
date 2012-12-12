
Keeping Track of Open Orders
============================

.. index::
   single: module; sale_delivery

In some industries, customers commonly place orders for a certain volume of products and ask for regular
deliveries from an order up to the total amount on it. This principle, called open orders, is managed
by the :mod:`sale_delivery` module in OpenERP.

OpenERP handles open orders easily. An open order is an order for a
certain quantity of products but whose deliveries are planned for various dates over a period of
time.

To do that, you should install the :mod:`sale_delivery` module (in ``extra-addons`` at the time of writing). 
A Sales Order is entered as a normal order, but you also set the total quantity that will be delivered on each order line.

Then you can use the new tab :guilabel:`Deliveries` on the order to plan the quantities sold and enter your
delivery planning there.

.. figure:: images/sale_delivery_form.png
   :scale: 75
   :align: center

   *Managing Open Orders, Planning Forecasts*

In the order lines, OpenERP shows you the quantity planned in addition to the quantity sold. This way, you
can verify whether the quantities sold equal the quantities to be delivered. On confirmation of the sales order, OpenERP no longer generates a single delivery order, but plans scheduled dispatches.

.. tip:: Invoicing Mode

   If you work with Open Orders, you should set :guilabel:`Invoice Control` to the mode ``Shipped Quantities``.
   Then the storesperson will be able to re-plan and change the quantities of the forecast deliveries
   in the system.

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
