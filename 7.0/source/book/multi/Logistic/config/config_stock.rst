Managing the Storage
--------------------

In our configuration, we have to define the way in which we will store the products.

The stock will be managed by OpenERP Belgium that will share the products with the other companies. OpenERP France will manage the 
sales part for these products. 

OpenERP France will "transfer" the sales order to OpenERP Belgium that will ship the goods to the customer.

By default, OpenERP creates some locations and warehouses for the first company. As a consequence, we have to create 
the other warehouses and locations for our child companies. We will start by creating the warehouses, then we will define 
specific locations and we will finish by setting up the of shops.

Warehouses
^^^^^^^^^^

In OpenERP, a warehouse represents your places of physical stock. A warehouse can be structured into several locations at multiple 
levels.

We have to create three new warehouses. One for OpenERP, one for OpenERP Belgium and one for OpenERP France. 

.. figure:: images/warehouse.png
   :scale: 75
   :align: center
   
   *Warehouses*

Go to :menuselection:`Warehouse --> Configuration --> Warehouse Management --> Warehouses` and create the different warehouses
according to the parameters shown in picture :ref:`fig-wareh`.

.. _fig-wareh:

.. figure:: images/warehouse_fr.png
   :scale: 75
   :align: center
   
   *Warehouse Parameters*

Locations
^^^^^^^^^

Locations are used to manage all types of storage places, such as at the customer and production counterparts.

In order to store products, we will create one location for the two child companies. It will support the flow of goods between 
those companies.

.. figure:: images/locations.png
   :scale: 75
   :align: center
   
   *Locations*

Go to :menuselection:`Warehouse --> Configuration --> Warehouse Management --> Locations` and create the different locations with 
the parameters defined in the picture :ref:`fig-loc`.

.. _fig-loc:

.. figure:: images/location_fr.png
   :scale: 75
   :align: center
   
   *Location Parameters*

Shops
^^^^^

OpenERP France needs a shop. The objective of this shop is to allow OpenERP France to receive orders from customers and then send 
it to OpenERP Belgium for the delivery of the products.

.. figure:: images/shop_fr.png
   :scale: 75
   :align: center
   
   *Defining a Shop*

Go to :menuselection:`Sales --> Configuration --> Sales --> Shop` to define a shop for OpenERP France.

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
