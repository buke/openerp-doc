
Testing a Complete Purchase Cycle according to an Example
=========================================================

To familiarize yourself with the system workflow, you will test a purchase-sales workflow in two phases.

The first consists of a product purchase, which requires the following operations:

	#. Place a purchase order with Plumbing Component Suppliers for 10 Titanium Alloy Radiators at a
	   unit price of 56.00.

	#. Receive these products at your Goods In.

	#. Generate a purchase invoice.

	#. Pay your supplier.

Then, you will sell some of these products, using this sequence:

	#. Receive a sales order for 6 Titanium Alloy Radiators from Smith and Sons, sold at a unit price
	   of 130.00.

	#. Dispatch the products.

	#. Invoice the customer.

	#. Receive the payment.

.. _sect-PO:

Purchase Order
--------------

To place a Purchase Order with your supplier, use the menu :menuselection:`Purchases --> Purchase Management -->
Purchase Orders` and click the `New` button.

Complete the following field:

*  :guilabel:`Supplier` : \ ``Plumbing Component Suppliers``\  .

As you complete the :guilabel:`Supplier` field, OpenERP automatically completes the :guilabel:`Address` field and the :guilabel:`Pricelist` field from information it takes from the Partner record.

Enter the following information in the Purchase Order Lines (click `New`):

*  :guilabel:`Product` : \ ``Titanium Alloy Radiator``\   - type in part of this name then press the tab key to complete it, or click the :guilabel:`Search` icon at the end of the line to bring a search box (if product is previously configured)

When you have selected a product on the product line, OpenERP automatically completes the following fields from information it finds in the ``Product`` record:

* :guilabel:`Product UOM` : the unit of measure for this product,

* :guilabel:`Description` : the detailed description of the product,

* :guilabel:`Scheduled Date` : based on the product lead time,

* :guilabel:`Unit Price` : the unit price of the product,

* :guilabel:`Analytic account` : if any account is specified and if you belong to the ``User Group`` `Useability / Analytic Accounting` (see menu :menuselection:`Administration --> Users --> Users`) then it will appear on the order line (it is not in this example),

* :guilabel:`Taxes` : applicable taxes defined in the partner, if specified, otherwise in the
  product, if specified (there are no taxes in this example).

You can edit any of these fields to suit the requirements of the purchase order at the time of entry. Change the:

* :guilabel:`Quantity` : \ ``10``\ ,

* :guilabel:`Unit Price` to \ ``56.00``\ .

Save the order line and close the :guilabel:`Order Line` window by clicking the
:guilabel:`Save & Close` button. You can then save the whole one-line order by clicking :guilabel:`Save`, which makes the form non-editable.

It is now in a state of \ ``Request for Quotation``\. To approve the quotation, click :guilabel:`Convert to Purchase Order`, which corresponds to an approval from a manager or from Accounts within your own company and moves the order into \ ``Approved`` \ state.

If you click the :guilabel:`Delivery & Invoicing` tab you will see the delivery :guilabel:`Destination` is your own company's ``Stock`` location and that the invoice was created from the order.
It is not entirely obvious at this stage, but the invoice is in a draft state so it can be edited and, crucially, it has no accounting impact yet: it is just ready for your accounting group to activate it.

Receiving Goods
---------------

After confirming the order, you would wait for the delivery of the products from your supplier. Typically
this would be somebody in Stores, who would:

	#. Open the menu :menuselection:`Warehouse --> Warehouse Management --> Incoming Shipments`.

	   .. note:: From the Purchase Order

	      You could have clicked the :guilabel:`Receptions` link to the right of the Purchase Order
	      to reach the same screen, but this would confuse the purchasing role with the
	      stores role. That link is very useful during testing and training, however.

	#. When the :guilabel:`Incoming Shipments` window appears, select the name of the entry in the list
	   (\ ``IN/00001``\)   to display the Packing List itself – you would usually do a search for the supplier name
	   or order number in a list that was larger than this – then click :guilabel:`Process` to load the
	   :guilabel:`Process Document` form.

	#. Click :guilabel:`Validate` to indicate that you are receiving the whole quantity of 10 units.

At this point you have accepted 10 units into your company, in a location that you have already seen.

Using the menu :menuselection:`Purchases --> Products --> Products` you can find the product `Titanium Alloy Radiators`
with `Real Stock` and `Virtual Stock` 10. Open the product form, and click the `Stock by Location` link at the right side of the screen to see the `Real Stock` and `Virtual Stock` of this product in various locations. Now select the checkbox in front of the Stock and Suppliers locations. The right side menu appears. Click the `Location Inventory Overview` report to see the inventory valuation for each of these two locations.

.. _fig-lotsbyloc:

.. figure::  images/lots_by_location_pdf.png
   :scale: 65
   :align: center

   *List of Products and their Stock Levels*

.. tip:: Traceability in Double-Entry

   OpenERP operates a double-entry stock transfer scheme similar to double-entry accounting.
   Because of this you can carry out various analyses of stock levels in your warehouse,
   along with the corresponding levels in Partner Location at your Supplier.
   The double-entry system, similar to that of accounting, enables you to keep track
   of stock movements quite easily, and to resolve any errors that occur.

Invoice Control
---------------

When you have received an invoice from your supplier (which would usually be sent to your Accounts department),
go to the menu :menuselection:`Accounting --> Suppliers --> Supplier Invoices`
to open a list of supplier invoices waiting for receipt.
These invoices enable your Accounts Department to match the price and quantities
ordered against the price and quantities on the supplier's invoice (and since it is not uncommon to receive
an invoice showing details more favourable to the supplier than those agreed at the time of
purchase, this is a useful function).

In this example, you created an invoice automatically when you confirmed the supplier's Purchase
Order. That is because the :guilabel:`Invoicing Control` field on the order was set to \ ``From Order``\ (the default option). Other options enable you to create invoices at the time of receiving goods or manually. The initial state of an invoice is \ ``Draft``\  .

Now click the invoice for your order \ ``PO00001``\  to display its contents. You can compare the
goods that you have recorded there with the invoice received from your supplier. If there is a
difference, it is possible to change the invoice lines to, for example, add a delivery charge. Select the correct `Invoice Date` and click
:guilabel:`Approve` to confirm the invoice and put it into the \ ``Open`` \ state.

Accounting entries are generated automatically once the invoice is validated. You can check the entry from the ``Other Info`` tab, in the `Journal Entry` field. To see the effects on your chart of accounts, go to the menu :menuselection:`Accounting --> Charts --> Chart of
Accounts`, and click :guilabel:`Open Charts` at the :guilabel:`Chart of Accounts` page to see that you
have a debit of ``560.00`` in the ``Purchases`` account and a credit of ``560.00`` in the ``Payable`` account.

.. tip:: Invoice Control

        Should your purchase invoice have to be checked by the purchaser first, he can go to the menu :menuselection:`Purchases --> Invoice Control --> Supplier Invoices to Receive` to check whether the invoice corresponds with the order (or the goods receipt according to the Invoice Control settings).

Paying the Supplier
-------------------

Select the menu :menuselection:`Accounting --> Suppliers --> Supplier Invoices` and click the :guilabel:`Unpaid` button
for a list of supplier invoices that have not yet been paid. In practice, you would search for the invoice by order number or,
more generally, for invoices nearing their payment date. You can type ``PO00001`` in the `Source Document` box to find the invoice.

Open the invoice and click the :guilabel:`Pay Invoice` button. It opens the :guilabel:`Pay Invoice` window in new tab with a description of the payment.

``Supplier`` and ``Date`` comes automatically from invoice. You just have to enter the ``Payment Method`` (i.e. the corresponding bank journal). When you select the payment method, you will notice that the corresponding invoice is displayed in Supplier Invoices and Outstanding Transactions, and that the Amount is filled automatically. Then click the :guilabel:`Validate` button to post this entry and consider the invoice as Paid.

.. index::
   single: module; account

.. note:: Payment of an Invoice

	The method described here is for companies that do not use their accounting system to pay bills, but
	just to record the payments.
	If you are using the :mod:`account` module with all its features, other, more efficient, methods let you manage payments,
	such as entering bank statements, reconciling paperwork, using tools for preparing payments,
	interfacing with banks.

You can monitor the accounting impact of paying the invoice through the chart of accounts available
from the menu :menuselection:`Accounting --> Charts --> Chart of Accounts`. OpenERP
automatically creates accounting entries from the payment, and can reconcile the payment to the
invoice. You now have a new transaction that has debited the ``Payable`` account with ``560.00`` and
credited the ``Bank`` account.

If you look in :menuselection:`Accounting --> Journal Entries --> Journal Entries` you will see both
accounting transactions, one in the ``Purchase`` Journal and another one in the ``Bank`` Journal, both with the ``Posted`` state.

Testing a Complete Sales Cycle according to an Example
======================================================

Sales Order
-----------

In OpenERP, sales proposals and sales orders are managed using documents that are based on the
same common functionality as purchase orders, so you will recognize the following documents in general
but see changes to their detail and to their workflows. To create a new sales proposal, use the
menu :menuselection:`Sales --> Sales --> Sales Orders` and click the `New` button which creates a new order as a \
``Quotation``\  , then:

	#. Select the :guilabel:`Customer` \ ``Smith and Offspring`` \. This has the effect of automatically
	   completing several other fields: :guilabel:`Ordering Contact`, :guilabel:`Invoice Address`,
	   :guilabel:`Shipping Address`, and the :guilabel:`Pricelist` \ ``Public Pricelist (EUR)``\.  They are
	   all only defaults, so these fields can be modified as you need.

	#. Click the :guilabel:`New` button in :guilabel:`Sales Order Lines` section to open a :guilabel:`Sales Order Lines` window.

	#. Select the product \ ``Titanium Alloy Radiator`` \. Although the :guilabel:`Product` field is not
	   itself required, it is used by OpenERP to select the specific product so that several other fields
	   can be automatically completed on the order line of the quotation, such as :guilabel:`Description`,
	   :guilabel:`Unit of Measure`, :guilabel:`Unit Price`, :guilabel:`Procurement Method`,
	   :guilabel:`Delivery Lead Time`, and :guilabel:`Taxes`.

	#. Change the :guilabel:`Quantity (UoM)` to \ ``6``\  and the :guilabel:`Unit Price` to \ ``130.00``\.
	   Then click :guilabel:`Save & Close` and the line appears on the quotation form.

	#. On the :guilabel:`Other Information` tab of this Sales Order, select a
	   :guilabel:`Picking Policy` of ``Complete Delivery`` and a
	   :guilabel:`Shipping Policy` of ``Invoice on Order After Delivery`` from the dropdown menu lists.

	#. Return to the first tab :guilabel:`Sales Order` and validate the document by clicking
	   :guilabel:`Confirm Order` which calculates prices and changes the order's state from \
	   ``Quotation``\  to \ ``In Progress`` \ as shown in screenshot :ref:`fig-ch03ord`.
	   If you were in negotiation with the prospective customer, you would click :guilabel:`Compute` and :guilabel:`Save`,
	   to keep the document in \ ``Quotation``\  state for as long as necessary.

	   .. _fig-ch03ord:

	   .. figure:: images/so.png
	      :scale: 75
	      :align: center

	      *Sales Order Form*

	#. In the last tab of the order :guilabel:`History`, you can see the :guilabel:`Picking List`
	   that has been created and you will be able to see any invoices that relate to this order when they are
	   generated.

Go to :menuselection:`Sales --> Products --> Products` to display a list of
products: just the one, \ ``Titanium Alloy Radiator``\  , currently exists in this example. Its
:guilabel:`Real Stock` still shows \ ``10.00``\   but its :guilabel:`Virtual Stock` now shows \
``4.00``\  to reflect the new future requirement of 6 units for dispatch.

Preparing Goods for Shipping to Customers
-----------------------------------------

The stores manager selects the menu :menuselection:`Warehouse --> Warehouse Management -->
Delivery Orders` to get a list of orders to dispatch. For this example, find the Delivery Order related
to the sales order which you have created. You should click the ``Available`` button, to see all delivery orders, because your delivery order will be in ``Confirmed`` state and not yet in ``Available`` state. Open the Delivery Order concerned.

.. index::
   single: module; mrp_jit

.. tip::  Running Schedulers

	At the moment, your Sales Order is waiting for products to be reserved to fulfil it.
	A stock reservation activity takes place periodically to calculate the needs,
	which also takes customer priorities into account.
	The calculation can be started from the menu :menuselection:`Warehouse --> Schedulers --> Compute Schedulers`.
	Running this automatically reserves products (i.e. the status will be set to Available if the products are in stock).

	If you do not want to have to work out your stock needs but have a lean workflow you can install the
	:mod:`mrp_jit` (Just In Time) module.

Although OpenERP has automatically been made aware that items on this order will need to be dispatched, it has not yet assigned any specific items from any location to fulfil it. It is ready to move \ ``6.00``\  \ ``Titanium Alloy Radiators``\   from the :guilabel:`Stock` location to the :guilabel:`Customers` location, so start this process by clicking :guilabel:`Check Availability`. The :guilabel:`Move` line has now changed from the \ ``Confirmed``\   state to the \ ``Available``\   state.

Then click the :guilabel:`Process` button to reach the :guilabel:`Process Document` window, where
you click the :guilabel:`Validate` button to transfer the 6 radiators to the customer.

To analyze stock movements that you have made during these operations, go to :menuselection:`Warehouse --> Product --> Products` and select the radiator by clicking the checkbox in front of it, then click the action `Stock by Location` which is at the right most side to see that your stocks have reduced to 4 radiators and the generic ``Customers`` location has a level of 6 radiators.

Invoicing Goods
---------------

Use the menu :menuselection:`Accounting --> Customers --> Customer Invoices` to open a list of Sales invoices generated by OpenERP. If they are in the \ ``Draft`` \ state, it means that they do not yet have any impact on the accounting system. You will find a
draft invoice has been created for the order \ ``SO001``\   once you have dispatched the goods
because you had selected \ ``Invoice on Order After Delivery``\  .

Once you confirm an invoice, OpenERP assigns it a unique number, and all of the corresponding
accounting entries are generated. So open the invoice and click :guilabel:`Validate` to do that and
move the invoice into an \ ``Open``\   state with a number of ``SAJ/2011/0001``.

You can send your customer the invoice for payment at this stage. Click :guilabel:`Print Invoice`
to get a PDF document that can be printed or emailed to the customer.

The PDF of your invoice will automatically be added as an attachment. This gives you a permanent non-editable record of your invoice on the OpenERP system.

Review your chart of accounts to check the impact of these activities on your accounting. You will see
the new revenue line from the invoice.

Customer Payment
----------------

Registering an invoice payment by a customer is essentially the same as the process of paying a
supplier. From the menu :menuselection:`Accounting --> Customers --> Customer Invoices`,
click the name of the invoice that you want to mark as paid:

	#. Use the :guilabel:`Payment` button which opens a new window `Pay Invoice`.

	#. Select the :guilabel:`Payment Method`, for this example select ``Bank Journal`` then validate the entry.

.. _fig_ch03faminv:

.. figure::  images/cust_inv.png
   :scale: 75
   :align: center

   *Invoice Form*

Check your Chart of Accounts as before to see that you now have a healthy bank balance in the \
``Bank``\   account.

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

