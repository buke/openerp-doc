
.. i18n: Managing the Storage
.. i18n: --------------------
..

Managing the Storage
--------------------

.. i18n: In our configuration, we have to define the way in which we will store the products.
..

In our configuration, we have to define the way in which we will store the products.

.. i18n: The stock will be managed by OpenERP Belgium that will share the products with the other companies. OpenERP France will manage the 
.. i18n: sales part for these products. 
..

The stock will be managed by OpenERP Belgium that will share the products with the other companies. OpenERP France will manage the 
sales part for these products. 

.. i18n: OpenERP France will "transfer" the sales order to OpenERP Belgium that will ship the goods to the customer.
..

OpenERP France will "transfer" the sales order to OpenERP Belgium that will ship the goods to the customer.

.. i18n: By default, OpenERP creates some locations and warehouses for the first company. As a consequence, we have to create 
.. i18n: the other warehouses and locations for our child companies. We will start by creating the warehouses, then we will define 
.. i18n: specific locations and we will finish by setting up the of shops.
..

By default, OpenERP creates some locations and warehouses for the first company. As a consequence, we have to create 
the other warehouses and locations for our child companies. We will start by creating the warehouses, then we will define 
specific locations and we will finish by setting up the of shops.

.. i18n: Warehouses
.. i18n: ^^^^^^^^^^
..

Warehouses
^^^^^^^^^^

.. i18n: In OpenERP, a warehouse represents your places of physical stock. A warehouse can be structured into several locations at multiple 
.. i18n: levels.
..

In OpenERP, a warehouse represents your places of physical stock. A warehouse can be structured into several locations at multiple 
levels.

.. i18n: We have to create three new warehouses. One for OpenERP, one for OpenERP Belgium and one for OpenERP France. 
..

We have to create three new warehouses. One for OpenERP, one for OpenERP Belgium and one for OpenERP France. 

.. i18n: .. figure:: images/warehouse.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n:    
.. i18n:    *Warehouses*
..

.. figure:: images/warehouse.png
   :scale: 75
   :align: center
   
   *Warehouses*

.. i18n: Go to :menuselection:`Warehouse --> Configuration --> Warehouse Management --> Warehouses` and create the different warehouses
.. i18n: according to the parameters shown in picture :ref:`fig-wareh`.
..

Go to :menuselection:`Warehouse --> Configuration --> Warehouse Management --> Warehouses` and create the different warehouses
according to the parameters shown in picture :ref:`fig-wareh`.

.. i18n: .. _fig-wareh:
.. i18n: 
.. i18n: .. figure:: images/warehouse_fr.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n:    
.. i18n:    *Warehouse Parameters*
..

.. _fig-wareh:

.. figure:: images/warehouse_fr.png
   :scale: 75
   :align: center
   
   *Warehouse Parameters*

.. i18n: Locations
.. i18n: ^^^^^^^^^
..

Locations
^^^^^^^^^

.. i18n: Locations are used to manage all types of storage places, such as at the customer and production counterparts.
..

Locations are used to manage all types of storage places, such as at the customer and production counterparts.

.. i18n: In order to store products, we will create one location for the two child companies. It will support the flow of goods between 
.. i18n: those companies.
..

In order to store products, we will create one location for the two child companies. It will support the flow of goods between 
those companies.

.. i18n: .. figure:: images/locations.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n:    
.. i18n:    *Locations*
..

.. figure:: images/locations.png
   :scale: 75
   :align: center
   
   *Locations*

.. i18n: Go to :menuselection:`Warehouse --> Configuration --> Warehouse Management --> Locations` and create the different locations with 
.. i18n: the parameters defined in the picture :ref:`fig-loc`.
..

Go to :menuselection:`Warehouse --> Configuration --> Warehouse Management --> Locations` and create the different locations with 
the parameters defined in the picture :ref:`fig-loc`.

.. i18n: .. _fig-loc:
.. i18n: 
.. i18n: .. figure:: images/location_fr.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n:    
.. i18n:    *Location Parameters*
..

.. _fig-loc:

.. figure:: images/location_fr.png
   :scale: 75
   :align: center
   
   *Location Parameters*

.. i18n: Shops
.. i18n: ^^^^^
..

Shops
^^^^^

.. i18n: OpenERP France needs a shop. The objective of this shop is to allow OpenERP France to receive orders from customers and then send 
.. i18n: it to OpenERP Belgium for the delivery of the products.
..

OpenERP France needs a shop. The objective of this shop is to allow OpenERP France to receive orders from customers and then send 
it to OpenERP Belgium for the delivery of the products.

.. i18n: .. figure:: images/shop_fr.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n:    
.. i18n:    *Defining a Shop*
..

.. figure:: images/shop_fr.png
   :scale: 75
   :align: center
   
   *Defining a Shop*

.. i18n: Go to :menuselection:`Sales --> Configuration --> Sales --> Shop` to define a shop for OpenERP France.
..

Go to :menuselection:`Sales --> Configuration --> Sales --> Shop` to define a shop for OpenERP France.

.. i18n: .. Copyright © Open Object Press. All rights reserved.
..

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.
..

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the OpenERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.
..

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.
..

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.
..

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.
..

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium
..

.. Published by Open Object Press, Grand Rosière, Belgium
