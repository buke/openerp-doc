Managing Lots and Traceability
==============================

The double-entry management in OpenERP enables you to run very advanced traceability. All
operations are formalized in terms of stock moves, so it is very easy to search for the cause of any
gaps in stock moves.

.. index::
   single: traceability; upstream
   single: traceability; downstream

.. note:: Upstream Traceability

    It runs from the raw materials received from the supplier and follows the
    chain to the finished products delivered to customers.
    (Note that the name is confusing - this would often be considered a downstream direction.
    Think of it as **Where Used**.)
    
.. note:: Downstream Traceability

    It follows the product in the other direction, from customer to the
    different suppliers of raw material.
    (Note that the name is confusing - this would often be considered an upstream direction.
    Think of it as **Where Supplied**.)

Stock Moves
-----------

Use the menu :menuselection:`Warehouse --> Traceability --> Stock Moves`
to track past stock transactions for a product or a given location. All the operations
are available. You can filter on the various fields to retrieve the operations about an order,
or a production activity, or a source location, or any given destination.

.. figure:: images/stock_move_tree.png
   :scale: 65
   :align: center

   *History of Stock Movements*

Each stock move is in a given state. The various states are:

* ``Draft`` : the move so far has no effect in the system. The transaction has not yet been confirmed,

* ``Not available``: the move will be done, so it will be counted in the calculations of virtual stock. But
  you do not know whether it will be done without problem because the products have not been reserved for
  the move,

* ``Available`` : the move will be done and the necessary raw materials have been reserved for the
  transaction,

* ``Done`` : the stock move (picking) has been done, and entered into the calculations of real stock,

* ``Waiting`` : in the case of transactions ``From Order``, this state shows that the stock move is blocked
  waiting for the end of another move,

* ``Cancelled`` : the stock move was not carried out, so it is not taken into account in either real stock or
  virtual stock.

Delivery orders, goods receipts and internal picking lists are just documents that group a set of
stock moves. You can also consult the history of these documents using the menu
:menuselection:`Warehouse --> Traceability --> Packs`.

Lots
----

OpenERP can also manage product lots. Two lot types are defined:

* Production lots (batch numbers) are represented by a unique product or an assembly of identical
  products leaving the same production area. They are usually identified by bar codes stuck on the
  products. The batch can be marked with a supplier number or your own company numbers.

* Tracking numbers are logistical lots to identify the container for a set of
  products. This corresponds, for example, to the pallet numbers on which several different products
  are stocked.

These lots can be encoded onto all stock moves and, specifically, on incoming shipments lines, internal moves
and outgoing deliveries.

.. figure:: images/picking_form_line.png
   :scale: 75
   :align: center

   *Entering a Line for Production Receipt*

To enter the lot number in an operation, you can use an existing lot number or create a new pack. A
production lot (batch number) is used for a single product. A tracking number can be
used several times for different products, so you can mix different products on a pallet or in a box.

.. note:: Simplified View

    In the ``Simplified`` view, the tracking numbers cannot be seen: the field is hidden.
    To get to ``Extended`` view mode, assign the group
    :guilabel:`Useability / Extended View` to the current user, or change the User Preferences.

You can also specify on the product form the operations in which a lot number is
required. You can then compel the user to set a lot number for manufacturing operations, goods
receipt, or customer packing.

You do not have to encode the lot numbers one by one to assign a unique lot number to a set of several items.
You only need to take a stock move for several products line and click the button
:guilabel:`Split in Production Lots`. You can then give a lot number prefix (if you want) and OpenERP will
complete the prefix in the wizard with a continuing sequence number. This sequence number
might correspond to a set of pre-printed barcodes that you stick on each product.

.. figure:: images/picking_split_lot.png
   :scale: 75
   :align: center

   *Splitting a Lot into uniquely Identified Parts*

.. index:: traceability (stock)

Traceability
------------

If you key in the lot numbers for stock moves as described above, you can investigate the traceability of any
given lot number. Go to the menu :menuselection:`Warehouse --> Traceability -->
Production Lots` or :menuselection:`Warehouse --> Traceability --> Packs`.

.. tip:: Product Shortcuts

    From the product form, the toolbar to the right offers useful information:

    * :guilabel:`Minimum Stock Rules`,

    * :guilabel:`Stock by Location`,

    * :guilabel:`Product Sales`,

    * :guilabel:`Bills of Material`.

Search for a particular lot using the filters for the lot number, the date or the product. Once you
can see the form about this lot, several actions can be performed:

* :guilabel:`Upstream Traceability`: from supplier through to customers,

* :guilabel:`Downstream Traceability`: from customer back to suppliers,

* Stock in all the physical and virtual locations.

.. figure:: images/stock_traceability_upstream.png
   :scale: 75
   :align: center

   *Tracing Upstream in Make to Order*

.. figure:: images/stock_traceability_downstream.png
   :scale: 75
   :align: center

   *Tracing Downstream in Make to Stock*

Finally, on a lot, you can enter data on all the operations that have been done for the product. That
keeps a useful history of the pre-sales operations.


Scrapping Products
==================

In OpenERP, there are many ways to handle scrap products. 

#. :menuselection:`Warehouse --> Product Moves --> Receive Products`

#. :menuselection:`Warehouse --> Product Moves --> Deliver Products`

#. :menuselection:`Warehouse --> Warehouse Management --> Incoming Shipments`

    .. figure:: images/incoming_scrap.png
	   :scale: 75
	   :align: center
	
	   *Scrapping from an Incoming Shipment*

#. :menuselection:`Warehouse --> Warehouse Management --> Internal Moves`

   .. figure:: images/internal_scrap.png
	  :scale: 75
	  :align: center
	
	  *Scrapping from an Internal Move*	

#. :menuselection:`Warehouse --> Warehouse Management --> Delivery Orders`

.. figure:: images/delivery_scrap.png
	  :scale: 75
	  :align: center
	
	  *Scrapping from a Delivery Order*	

When you decide to scrap some products, they are transferred to the :guilabel:`Scrap` location.
To display the content of this :guilabel:`Virtual Location`, go to :menuselection:
`Warehouse --> Inventory Control --> Location Structure`, then select the virtual locations and display the
:guilabel:`Scrap` location.

If you want to transfer the products to another location, you can create a new one and check the 
:guilabel:`Scrap Location` in the additional information.

Identifying Products and Locations with Barcodes and RFID Devices
=================================================================

You can the barcode in the product form in the field :guilabel:`EAN13`.


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

