Manufacturing Orders
====================

Once the bills of materials have been defined, OpenERP is capable of automatically deciding on the manufacturing route according to the needs of the company.

Production orders can be proposed automatically by the system depending on several criteria described in the preceding chapter:

* Using the ``Make to Order`` rules,

* Using the ``Order Point`` (Minimum Stock) rules,

* Using the Production plan.

Of course, you can also start production manually by clicking the button :guilabel:`New` in the menu :menuselection:`Manufacturing --> Manufacturing --> Manufacturing Orders`.

.. figure:: images/mrp_manual.png
   :scale: 75
   :align: center

   *Manufacturing Order*

.. index::
   single: module; mrp_jit

If you have not installed the Just-in-Time planning module :mod:`mrp_jit`, you should start using OpenERP to schedule the Production Orders automatically using the various system rules. To do this, use the menu :menuselection:`Warehouse --> Schedulers --> Compute Schedulers`.

.. tip:: Procurement Exceptions

        Pay attention to the fact that you have to define `minimum stock rules` for each product set as ``Make to Stock``.

Complete Production Workflow
============================

To understand the usefulness and the functioning of the system you should test a complete workflow
on the database installed with the demonstration data. We will show you:

* How to create a sales order,

* The manufacturing workflow for an intermediate product,

* The manufacturing of an ordered product,

* The delivery of products to a customer,

* Invoicing at the end of the month,

* Traceability for after-sales service.

.. tip:: Demonstration data

    To exactly follow the workflow as shown below, you should keep the same quantities as in the
    example and start from a new database. Then you will not run into exceptions resulting from a lack of stock.

This more advanced case of handling problems in procurement will be sorted out later in the chapter.

To be able to do the following step, add ``Sales Management`` through the Reconfigure wizard.

The Sales Order
+++++++++++++++

.. index:: quotation
.. index:: sales order

Begin by encoding a sales (or customer) order through the menu :menuselection:`Sales --> Sales Orders -> New Quotation`. Enter the following information:

* :guilabel:`Customer` : Agrolait,

* :guilabel:`Shipping Policy` : Invoice from the picking (``Other Information`` tab),

* :guilabel:`Sales Order Lines`, click `New`:

  * :guilabel:`Product` : PC2 – Basic PC (assembly on order),

  * :guilabel:`Quantity (UoM)` : 1,

  * :guilabel:`Product UoM` : PCE,

  * :guilabel:`Procurement Method` : on order.

Once the quotation has been entered, you can confirm it immediately by clicking the button
:guilabel:`Confirm Order` at the bottom to the right. Keep note of the order reference because this
follows all through the process. Usually, in a new database, this will be ``SO007`` . At this stage,
you can look at the process linked to your order using the :guilabel:`Question Mark` button next to the ``Sales Orders`` title.

.. figure:: images/mrp_sales_process_new.png
   :scale: 75
   :align: center

   *Process for Handling Sales Order SO007*

Start the requirements calculation using the menu :menuselection:`Manufacturing --> Compute All Schedulers`.

.. index::
   single: semi-finished product

Producing an Intermediate Product
+++++++++++++++++++++++++++++++++

To understand the implications of requirements calculation, you should know the configuration of the sold product. To do this, go to the form for product PC2 and click the link :guilabel:`Product BoM Structure` to the right. You get the scheme shown in :ref:`fig-mrpbomtree` which is the composition of the selected product.

.. _fig-mrpbomtree:

.. figure:: images/mrp_product_bom_tree_new.png
   :scale: 75
   :align: center

   *Composition of PC2*

The PC2 computer has to be manufactured in two steps:

1: The intermediate product: CPU_GEN

2: The finished product using that intermediate product: PC2

The manufacturing supervisor can then consult the production orders using the menu
:menuselection:`Manufacturing --> Manufacturing --> Manufacturing Orders`. You then get a
list of orders to start (``Ready to Produce``) and the estimated start date (``Scheduled Date``) to meet the customer delivery date.

.. figure:: images/mrp_production_list_new.png
   :scale: 75
   :align: center

   *List of Manufacturing Orders*

You will see the production order for CPU_GEN, but not the one for PC2 because it depends on an intermediate product that has to be produced first. Return to the production order for CPU_GEN and click it. If there are several of them, select the one corresponding to your order using the source document that contains your order number (in this example ``SO007`` ).

.. figure:: images/mrp_production_form_new.png
   :scale: 75
   :align: center

   *Details of a Production Order*

The system shows you that you have to manufacture product CPU_GEN using the components: MB1, CPU1, FAN, RAM. You can then confirm the production twice:

Start production: consumption of raw materials,

Produce: manufacturing of finished product.

Click the ``Start Production`` button, then click the ``Edit`` button, and edit the line for the product MB1. Enter a lot number for it by putting the cursor in the field :guilabel:`Production Lot` and pressing :kbd:`<F1>` to create a new lot. Enter an internal reference, for example: ``MB1345678``. The system may then show you a warning because this lot is not in stock, but you can ignore this message.

Click the ``Produce`` button to manufacture the finished product.

The production order has to be in the closed state as shown in the figure :ref:`fig-mrpprdfrm`.

.. _fig-mrpprdfrm:

.. figure:: images/mrp_production_form_end_new.png
   :scale: 75
   :align: center

   *Production Order after the Different Stages*

Finished Product Manufacturing
++++++++++++++++++++++++++++++

Having manufactured the intermediate product CPU_GEN, OpenERP automatically proposes the manufacturing
of the computer PC2 using the order created earlier. Return to the Manufacturing Orders menu and look at the orders Ready to Produce through  :menuselection:`Manufacturing --> Manufacturing --> Manufacturing Orders`.

You will find computer PC2 which has been sold to the customer (source document SO007), as shown in the figure hereafter.

.. figure:: images/mrp_production_list_end_new.png
    :scale: 75
    :align: center
    
    *Completed Production for PC2*

Now that the production has been completed, the product sold to the customer has been manufactured and the raw materials have been consumed and taken out of stock.
 
.. tip:: Automatic Actions

    As well as managing the use of materials and the production of stocks, manufacturing can have the following
    automatic effects which are detailed further on in the chapter:
    
    * adding value to stock,
    * generating operations for assembly staff,
    * automatically creating analytical accounting entries.

Subproduct Production
+++++++++++++++++++++

If you need to manage subproducts, you should install the module :mod:`mrp_subproduct` (Reconfigure wizard, MRP Sub-
products). The normal behaviour of manufacturing in OpenERP enables you to manufacture several units of the
same finished product from raw materials (A + B > C). With Subproduct management, the manufacturing result can be to have both finished products and secondary products (A + B > C + D).

.. note:: Subproduct Material

    In OpenERP, subproduct material corresponds to secondary products that are a by-product of the main manufacturing
    process. For example, cutting planks of timber will produce other planks but these bits of timber are too small 
    (or the offcuts may have value for the company if they can be used elsewhere).

If the module :mod:`mrp_subproduct` has been installed, you get a new tab Sub products in the Bill of Material
that lets you set secondary products resulting from the manufacturing of the finished product.

.. figure:: images/mrp_bom_subproduct.png
    :scale: 75
    :align: center
    
    *Definition of Subproducts*

When OpenERP generates a production order based on a bill of materials that uses a secondary product, you pick
up the list of all products in the second tab of the production order ``Finished Products``.
    
.. figure:: images/mrp_production.png
    :scale: 75
    :align: center
    
    *Production Order producing Several Finished Products*

Secondary products enable you to generate several types of products from the same raw materials and manufacturing methods - only these are not used in the calculation of requirements. Then, if you need the secondary products, OpenERP will not ask you to manufacture another product to use the waste products and secondary products of this production. In this case, you should enter another production order for the secondary product.

.. note:: Services in Manufacturing

    Unlike most software for production management, OpenERP manages services as well as stockable products. So
    it is possible to put products of type Service in a bill of materials. These do not appear in the production 
    order, but their requirements will be taken into account.
    
    If they are defined as Make to Order, OpenERP will generate a task for the manufacturing or a subcontract
    order for the operations. The behaviour will depend on the Supply Method configured in the product form: Buy
    or Produce.

Scrapping
+++++++++

If you have to scrap the final product before it is finished, you will have to scrap every component allowed for this product. 

.. figure:: images/mo_scrap.png
    :scale: 75
    :align: center
    
    *Scrapping a Product to Finish*

If you scrap a Product to Finish, you will get the situation illustrated in the previous figure. A finished product will be *created* and put in the scrapped virtual location. A new Product to Finish has been added to the manufacturing order.

.. tip:: Scrap a product

    To scrap a product, you have to edit the manufacturing order and then select the product to be
    scrapped by clicking the little pencil at the left of the item.

This new product has been added for the following reason: when you have to manufacture a product and if this product
has to be scrapped, you have to produce another product to replace the scrapped one. The reason why 
you have to scrap each component manually is that the production problem can come from one component.

If the production process is finished and you see that you have to scrap the finished product, you will
not have to scrap the different components. They are already *consumed*. They are not available anymore
for further manufacturing orders; they have been moved to the production Stock Location.

Production Orders
+++++++++++++++++

To open a Production Order, use the menu :menuselection:`Manufacturing --> Manufacturing --> Manufacturing Orders` and click the `New` button.
You get a blank form to enter a new production order as shown in the figure :ref:`fig-mrpprdnew`.

.. _fig-mrpprdnew:

.. figure:: images/mrp_production_new.png
   :scale: 75
   :align: center

   *New Production Order*

The production order follows the process given by the figure :ref:`fig-mrpprdproc`.

.. _fig-mrpprdproc:

.. figure:: images/mrp_production_processus.png
   :scale: 75
   :align: center

   *Process for Handling a Production Order*

The `Scheduled date` , `Product Qty` and `Reference`, are automatically completed when the form is first opened.
Enter the product that you want to produce, and the quantity required. The :guilabel:`Product UOM` by
default is completed automatically by OpenERP when the product is first selected.

You then have to set two locations:

	* The location from which the required raw materials should be found, and

	* The location for depositing the finished products.

For simplicity, put the ``Stock`` location in both places. The field :guilabel:`Bill of Materials` will
automatically be completed by OpenERP when you select the product. You can then overwrite it with another BoM to specify something else to use for this specific manufacturing, then click the button :guilabel:`Compute Data`.

The tabs :guilabel:`Scheduled Products` and :guilabel:`Work Orders` are also completed automatically when you click
:guilabel:`Compute Data` (in the :guilabel:`Work Orders` or :guilabel:`Scheduled Products` tabs). 
You will find the raw materials there that are required for the production and the operations needed by the assembly staff.

If you want to start production, click the button :guilabel:`Confirm Production`, and OpenERP automatically completes the :guilabel:`Products to Consume` field in the :guilabel:`Consumed Products` tab and :guilabel:`Products to Finish` field in :guilabel:`Finished Products` tab.

The information in the :guilabel:`Consumed Products` tab can be changed if:

* you want to enter a serial number for raw materials,

* you want to change the quantities consumed (lost during production).

For traceability, you can set lot numbers on the raw materials used, or on the finished
products.
Note the :guilabel:`Production Lot` and :guilabel:`Pack` numbers.

Once the order is confirmed, you should force the reservation of materials
using the :guilabel:`Force Reservation` button. This means that you do not have
to wait for the scheduler to assign and reserve the raw materials from your stock for this
production run. This shortens the procurement process.

If you do not want to change the priorities, just leave the production order in this state and the scheduler will create a plan based on the priority and your planned date.

To start the production of products, click :guilabel:`Start Production`. The raw materials are then consumed automatically from stock, which means that the draft ( ``Waiting`` ) movements become ``Done``.

Once the production is complete, click :guilabel:`Produce`. The finished products are now moved into stock.


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
