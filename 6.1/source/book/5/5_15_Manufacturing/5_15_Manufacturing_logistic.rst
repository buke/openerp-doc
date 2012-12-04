Logistics and Manufacturing
===========================

Manufacturing Stock Locations
+++++++++++++++++++++++++++++

OpenERP allows you to define a specific location to keep track of your manufacturing moves. 

To get an overview of all stock moves, go to :menuselection:`Warehouse --> Traceability --> Stock Moves`. You can enter your Production location in the ``Location`` search field and then group by Source or Destination according to the moves you would like to check.

Traceability
++++++++++++

With traceability you can easily track your production lots in the software. With this functionality you can
quickly find where your products are in your warehouse. In counterpart, you will be forced to mention a
number of lot to each product to be able to track it in the system.

To enable traceability in the manufacturing process, go to :menuselection:`Warehouse --> Product --> Products`. In the ``Product`` form, you have to select the box :guilabel:`Track Manufacturing Lots` in the :guilabel:`Lots` section on the ``Information`` tab.

In the manufacturing order, you have to mention a production lot number in order to continue the process.
You can select the production lot in the :guilabel:`Manufacturing Order` form on the second tab, called :guilabel:`Finished Products`. You have to click the Products to Finish you want to trace, a new window will open. In the :guilabel:`Production Lot` field, click to link the manufacturing order to a production lot.

.. figure:: images/prod_lot.png
    :scale: 75
    :align: center
    
    *Tracking a Manufacturing Order*

When you have linked some manufacturing orders to production lots, you can trace them from the menu :menuselection:`Warehouse --> Traceability --> Production Lots`. In this view, you see the different production lots linked to a product. If you select one lot, you will have the possibility to choose between :guilabel:`Upstream Traceability` or :guilabel:`Downstream Traceability`.

.. figure:: images/production_lots.png
    :scale: 75
    :align: center
    
    *Choosing between Upstream and Downstream Traceability*
    
.. tip:: Traceability
    
    **Upstream Traceability**: It starts from the raw materials received from the supplier and follows 
    the chain to the finished products delivered to customers. Note that the name is confusing - this 
    would often be considered a downstream direction. Think of it as **Where Used**.
    
    **Downstream Traceability**: It follows the product in the other direction, from customer to the different 
    suppliers of raw material. Note that the name is confusing - this would often be considered an upstream 
    direction. Think of it as **Where Supplied**.

        
.. figure:: images/upstream_trace.png
    :scale: 75
    :align: center
    
    *Upstream Traceability*

The different lines show the stock moves attached to the production of the product. There are several
stock moves that are traced due to the Bill of Materials attached to the product *[PC1] Basic PC*.
    
        
.. figure:: images/downstream_trace.png
    :scale: 75
    :align: center
    
    *Downstream Traceability*        

In this window, you only see the move for the finished product. This is related to the definition of the  concept of Downstream Traceability, which only shows the flow from the customer to the supplier of raw materials.

Managing Repairs: from Repair to Invoicing and Stock Movements
==============================================================

.. index::
   single: module; mrp_repair

The management of repairs is carried out through the module :mod:`mrp_repair`. Once installed, this module adds a new :menuselection:`Manufacturing --> Manufacturing --> Repair Orders` menu under the ``Manufacturing`` menu to create repair jobs and review repairs in progress.

.. tip:: Repairs

        To install this module, you can also use the ``Reconfigure`` wizard. In the *MRP Application Configuration* screen, check the ``Repairs`` option.

In OpenERP, a repair will have the following effects:

* Use of materials: items for replacement,

* Production of products: items replaced from reserved stock,

* Quality control: tracking the reasons for repair,

* Accounting entries: following stock moves,

* Receipt and delivery of product from and to the end user,

* Adding operations that can be seen in the product's traceability,

* Invoicing items used and/or free for repairs.

Entering Data for a New Repair
++++++++++++++++++++++++++++++

Use the menu :menuselection:`Manufacturing --> Manufacturing --> Repair Orders` to enter a new repair into
the system. You will see a blank form for the repair data, as shown in the figure :ref:`fig-mrprepnew2` below.

.. _fig-mrprepnew2:

.. figure:: images/mrp_repair_new.png
   :scale: 75
   :align: center

   *Entering a New Repair*

First enter the product to repair, then identify the product that will be repaired using the *product lot number*. OpenERP then automatically completes fields from the selected lot – the partner fields, address, delivery location and stock move.

If a warranty period has been defined in the product description, in months, OpenERP completes the field :guilabel:`Guarantee limit` with the correct warranty date.

Now you have to specify the components that you will be adding, replacing or removing in the *Operations* part. On each line, you should specify the following:

Add or remove a component of the finished product:

* `Product`,

* `Qty`,

* `UoM`,

* `Unit Price`,

* `To Invoice` or not.

Once the component has been selected, OpenERP automatically completes most of the fields:

* :guilabel:`Qty`: 1,

* :guilabel:`UoM`: unit for managing stock defined in the product form,

* :guilabel:`Unit Price`: calculated from the customer list price,

* :guilabel:`Source Location`: given by the stock management,

* :guilabel:`To Invoice`: depends on the actual date and the guarantee period.

This information is automatically proposed by the system, but you can modify it all yourself.

On the second tab of the ``Repair`` form, ``Invoicing``, you can select whether the repair has to be invoiced or not, and if invoiced whether it should be before or after the repair. You can also select the applicable list price, a specific address and encode additional charges that need to be added to the repair invoice.

.. figure:: images/mrp_repair_tab2.png
   :scale: 75
   :align: center

   *Repair Form, Invoicing Tab*

The third tab, ``Extra Info`` shows information about linked invoice and picking. You receive information about the current location, and you can change the ``Delivery Location``. The ``Notes`` tab allows you to register internal notes and information that should be written on the Quotation.

Repair Workflow
+++++++++++++++

A defined process handles a repair order – both the repair itself and the customer invoicing. The figure :ref:`fig-mrprepflow2` shows this repair process.

.. _fig-mrprepflow2:

.. figure:: images/mrp_repair_workflow.png
   :scale: 65
   :align: center

   *Process to Handle a Repair*

Once a repair has been entered in the system, it is in the ``Quotation`` state. In this state, a repair order has no impact on the rest of the system. You can print a quotation through the action `Quotation / Order`.

On the second tab, you can specify the `Invoice Method`:

* ``No Invoice``,

* ``Before Repair``,

* ``After Repair``.

You can then confirm the repair operation or create an invoice for the customer depending on the Invoice Method.

The repair quotation can now be sent to the customer. Once the customer approves the repair, click the `Confirm Repair` button. From the menu :menuselection:`Manufacturing --> Manufacturing --> Repair Orders` you can easily find the confirmed repair orders by selecting the ``Confirmed`` button. Click `Start Repair` to indicate that you can start working on the repair. The Repair order will now be in the ``Under Repair`` state. When you finish the repair, click the ``End Repair`` button.

.. index::
   pair: invoicing; repair

Invoicing the Repair
++++++++++++++++++++

When the repair is to be invoiced, a draft invoice is generated by the system. For an After Repair invoice, you can click the ``Make Invoice`` button. OpenERP will then show the draft invoice created at the top of the repair order (red text). You can easily go to that invoice simply by clicking the corresponding red text. This invoice contains the raw materials used (replaced components) and any other costs such as the time used for the repair. These other costs are entered on the second tab of the *Repair* form. Any information you entered for the quotation on the ``Notes`` tab will also be displayed on the invoice.

If the product to be repaired is still under guarantee, OpenERP automatically suggests that the components themselves are not invoiced, but will still use any other defined costs. You can override any of these default values while entering the data.

.. note:: Extra Info

        The link to the generated invoice is shown on the ``Extra Info``tab of the repair document. To open the invoice, simply click the ``Invoice`` field.

Stock Movements and Repairs
+++++++++++++++++++++++++++

When the repair has been carried out, OpenERP automatically carries out stock movements for components that have been removed, added or replaced on the finished product. From the menu :menuselection:`Warehouse --> Traceability --> Stock Moves`, you can for instance enter the production lot to see all moves for the repaired product.

The move operations are carried out using the locations shown in the first tab of the ``Repair`` form. If a destination location has been specified, OpenERP automatically handles the final customer delivery order when the repair has been completed. This also lets you manage the delivery of the repaired products.

For example, take the case of the shelf that was produced at the start of this chapter. If you have to replace the shelf SIDEPAN, you should enter data for the repair as shown in figure :ref:`fig-mrpreppan2`.

.. _fig-mrpreppan2:

.. figure:: images/mrp_repair_panlat.png
   :scale: 75
   :align: center

   *Repair for a Side Panel*

In this example, you would carry out the following operations:

* Remove a SIDEPAN shelf in the cabinet and put the faulty shelf in the *Scrapped* location,

* Place a new SIDEPAN shelf that has been taken from stock.

When the repair is ready to be confirmed, OpenERP will generate the following stock moves:

* Put faulty SIDEPAN into suitable stock location *Default Production > Scrapped*,

* Consume SIDEPAN: *Stock > Production*.

If you analyze the traceability of this lot number, you will see all the repair operations in the
upstream and downstream traceability lists of the products concerned.


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
