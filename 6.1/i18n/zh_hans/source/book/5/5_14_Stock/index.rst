
.. i18n: .. index::
.. i18n:    single: Logistics
.. i18n:    single: Stock Management
..

.. index::
   single: Logistics
   single: Stock Management

.. i18n: .. _ch-stocks:
.. i18n: 
.. i18n: **************
.. i18n: Your Warehouse
.. i18n: **************
..

.. _ch-stocks:

**************
Your Warehouse
**************

.. i18n:  *OpenERP's stock management is at once very simple, flexible and complete.
.. i18n:  It is based on the concept of double entry that revolutionized accounting.
.. i18n:  The system can be described by Lavoisier's maxim “nothing lost, everything changed” or, better,
.. i18n:  “everything moved”. In OpenERP you do not talk of disappearance, consumption or loss of products:
.. i18n:  instead you speak only of stock moves from one place to another.*
..

 *OpenERP's stock management is at once very simple, flexible and complete.
 It is based on the concept of double entry that revolutionized accounting.
 The system can be described by Lavoisier's maxim “nothing lost, everything changed” or, better,
 “everything moved”. In OpenERP you do not talk of disappearance, consumption or loss of products:
 instead you speak only of stock moves from one place to another.*

.. i18n: Just as in accounting, the OpenERP system manages counterparts to each of its main operations such as
.. i18n: receipts from suppliers, deliveries to customers, profit and loss from inventory, and consumption
.. i18n: of raw materials. Stock movements are always made from one location to another. To satisfy the need
.. i18n: for a counterpart to each stock movement, the software supports different types of stock locations:
..

Just as in accounting, the OpenERP system manages counterparts to each of its main operations such as
receipts from suppliers, deliveries to customers, profit and loss from inventory, and consumption
of raw materials. Stock movements are always made from one location to another. To satisfy the need
for a counterpart to each stock movement, the software supports different types of stock locations:

.. i18n: * Physical stock locations,
.. i18n: 
.. i18n: * Partner locations,
.. i18n: 
.. i18n: * Virtual locations as counterparts for procurement, production and inventory.
..

* Physical stock locations,

* Partner locations,

* Virtual locations as counterparts for procurement, production and inventory.

.. i18n: Physical locations represent warehouses and their hierarchical structure. These are generally the
.. i18n: locations that are managed by traditional stock management systems.
..

Physical locations represent warehouses and their hierarchical structure. These are generally the
locations that are managed by traditional stock management systems.

.. i18n: Partner locations represent your customers' and suppliers' stocks. To reconcile them with your
.. i18n: accounts, these stores play the role of third-party accounts. Reception from a supplier can be shown
.. i18n: by the movement of goods from a partner location to a physical location in your own company. As you
.. i18n: see, supplier locations usually show negative stocks and customer locations usually show positive
.. i18n: stocks.
..

Partner locations represent your customers' and suppliers' stocks. To reconcile them with your
accounts, these stores play the role of third-party accounts. Reception from a supplier can be shown
by the movement of goods from a partner location to a physical location in your own company. As you
see, supplier locations usually show negative stocks and customer locations usually show positive
stocks.

.. i18n: Virtual locations as counterparts for production are used in manufacturing operations. Manufacturing is
.. i18n: characterized by the consumption of raw materials and the production of finished products. Virtual
.. i18n: locations are used for the counterparts of these two operations.
..

Virtual locations as counterparts for production are used in manufacturing operations. Manufacturing is
characterized by the consumption of raw materials and the production of finished products. Virtual
locations are used for the counterparts of these two operations.

.. i18n: Inventory locations are counterparts of the stock operations that represent your company's profit
.. i18n: and loss in terms of your stocks.
..

Inventory locations are counterparts of the stock operations that represent your company's profit
and loss in terms of your stocks.

.. i18n: The figure :ref:`fig-stloctree` shows the initial configuration of the locations when the software is
.. i18n: installed (:menuselection:`Warehouse --> Warehouse Management --> Locations`).
..

The figure :ref:`fig-stloctree` shows the initial configuration of the locations when the software is
installed (:menuselection:`Warehouse --> Warehouse Management --> Locations`).

.. i18n: .. _fig-stloctree:
.. i18n: 
.. i18n: .. figure:: images/stock_location_tree.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Location Structure when OpenERP has just been installed*
..

.. _fig-stloctree:

.. figure:: images/stock_location_tree.png
   :scale: 75
   :align: center

   *Location Structure when OpenERP has just been installed*

.. i18n: .. note::  Hierarchical Stock Locations
.. i18n: 
.. i18n:     In OpenERP, locations are structured hierarchically.
.. i18n:     You can structure your locations as a tree, dependent on a parent-child relationship.
.. i18n:     This gives you more detailed levels of analysis of your stock operations and the organization of
.. i18n:     your warehouses.
..

.. note::  Hierarchical Stock Locations

    In OpenERP, locations are structured hierarchically.
    You can structure your locations as a tree, dependent on a parent-child relationship.
    This gives you more detailed levels of analysis of your stock operations and the organization of
    your warehouses.

.. i18n: .. tip:: Locations and Warehouses
.. i18n: 
.. i18n:     In OpenERP a **Warehouse** represents the place where your physical stock is stored.
.. i18n:     A warehouse can be structured into several locations at multiple levels.
.. i18n:     Locations are used to manage all types of storage places, such as at the customer and production
.. i18n:     counterparts.
..

.. tip:: Locations and Warehouses

    In OpenERP a **Warehouse** represents the place where your physical stock is stored.
    A warehouse can be structured into several locations at multiple levels.
    Locations are used to manage all types of storage places, such as at the customer and production
    counterparts.

.. i18n: For this chapter you can continue using the database with demo data from a previous chapter or start with a fresh database that includes demo data,
.. i18n: with Warehouse Management and its dependencies installed and any chart of accounts configured.
..

For this chapter you can continue using the database with demo data from a previous chapter or start with a fresh database that includes demo data,
with Warehouse Management and its dependencies installed and any chart of accounts configured.

.. i18n: In this chapter, the following modules will be used:
..

In this chapter, the following modules will be used:

.. i18n: .. table:: List of modules
.. i18n: 
.. i18n:    ======================================= ===================================================================
.. i18n:    Name                                    Description
.. i18n:    ======================================= ===================================================================
.. i18n:    :mod:`stock`                            to handle the stock functions
.. i18n:    :mod:`stock_planning`                   to define planning on products
.. i18n:    :mod:`stock_location`                   to define pull and push flows
.. i18n:    :mod:`delivery`                         to define delivery methods and costs
.. i18n:    :mod:`account_anglo_saxon`              to illustrate the valuation according to the anglo-saxon principles
.. i18n:    :mod:`sale_journal`                     to handle stock by journal
.. i18n:    :mod:`mrp_jit`                          to illustrate the just-in-time functionality
.. i18n:    :mod:`sale_supplier_direct_delivery`    to directly deliver the product from the supplier to the customer
.. i18n:    ======================================= ===================================================================
..

.. table:: List of modules

   ======================================= ===================================================================
   Name                                    Description
   ======================================= ===================================================================
   :mod:`stock`                            to handle the stock functions
   :mod:`stock_planning`                   to define planning on products
   :mod:`stock_location`                   to define pull and push flows
   :mod:`delivery`                         to define delivery methods and costs
   :mod:`account_anglo_saxon`              to illustrate the valuation according to the anglo-saxon principles
   :mod:`sale_journal`                     to handle stock by journal
   :mod:`mrp_jit`                          to illustrate the just-in-time functionality
   :mod:`sale_supplier_direct_delivery`    to directly deliver the product from the supplier to the customer
   ======================================= ===================================================================

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="all-toctree">
..

.. raw:: html

    <div class="all-toctree">

.. i18n: .. toctree::
.. i18n: 
.. i18n:     5_14_Stock_illustration
.. i18n:     5_14_Stock_inv
.. i18n:     5_14_Stock_mvts
.. i18n:     5_14_Stock_production
.. i18n:     5_14_Stock_traceability
.. i18n:     5_14_Stock_financial
.. i18n:     5_14_Stock_journals
.. i18n:     5_14_Stock_delivery_date
.. i18n:     5_14_Stock_import
.. i18n:     5_14_Stock_Location_Ex
..

.. toctree::

    5_14_Stock_illustration
    5_14_Stock_inv
    5_14_Stock_mvts
    5_14_Stock_production
    5_14_Stock_traceability
    5_14_Stock_financial
    5_14_Stock_journals
    5_14_Stock_delivery_date
    5_14_Stock_import
    5_14_Stock_Location_Ex

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     </div>
..

.. raw:: html

    </div>

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
