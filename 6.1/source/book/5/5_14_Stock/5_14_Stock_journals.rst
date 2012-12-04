
Organize your Deliveries
========================

You can manage stock through journals in the same way as you can manage your accounts
through journals. This approach has the great advantage
that you can define journals in various ways to meet your company's needs.

For example, a large company may want to organize deliveries by department or warehouse. You can
then create a journal and a manager for each department. The different users can work in a
journal as a function of their position in the company. That enables you to better structure your
information.

A company doing a lot of transport could organize its journals by delivery vehicle. The different
delivery orders will then be assigned to a journal representing a particular vehicle. When the
vehicle has left the company, you can confirm all the orders that are found in the journal all at the
same time.

.. index::
   single: stock; journal

The Different Journals
----------------------

.. index::
   single: module; sale_journal

Install the Reconfigure option `Invoicing Journals` for Sales Management or the :mod:`sale_journal` module to work with different journals. This adds two new concepts to OpenERP:

* Invoicing journals,

* Stock journals or Delivery journals.

**Invoicing journals** (:menuselection:`Sales --> Configuration --> Sales --> Invoice Types`) are used to assign purchase orders and/or delivery orders to a given invoicing journal. Everything in the journal can be invoiced in one go, and you can control the amounts by
journal. For example, you can create the following journals: daily invoicing, end-of-week invoicing
and monthly invoicing. It is also possible to show the invoicing journal by default in the partner form.
Set the `Invoicing Method` to ``Grouped`` (one invoice per customer) or ``Non Grouped`` (individual invoices) according to your needs.

**Stock journals** (:menuselection:`Warehouse --> Configuration --> Warehouse Management --> Stock Journals`) allow you to classify the delivery orders in various ways, such as by department, by salesperson or by type. If a salesperson looks for a delivery order in his own journal, he can
easily see the work on current items compared with his own orders.

.. tip:: Default Values

   To enter all the orders in his own stock journal, a salesperson can use the default values that
   are entered in the fields when creating orders.

Finally, the stock journals can also be used as **delivery journals** to post each item into a delivery journal. For example, you
can create journals dated according to customer delivery dates (such as Monday's deliveries, or
afternoon deliveries) or these journals could represent the day's work for delivery vehicles (such
as truck1, truck2).

Using the Journals
------------------

You will now see how to use the journals to organize your stock management in practice. After
installing the module :mod:`sale_journal` look at the list of partners. In the tab :guilabel:`Sales and
Purchases` on any of them you will now see the field :guilabel:`Invoicing Method`.

.. figure:: images/partner_property_view.png
   :scale: 75
   :align: center

   *Partner Form in Invoicing Mode*

You can create a new :guilabel:`Invoicing Journal` for a partner through the menu :menuselection:`Sales --> Configuration --> Sales --> Invoice Types`. You can decide if the invoices should be grouped or not when generating them in the journal. Create a second invoicing journal
``End-of-Month Invoicing`` which you can assign to another partner.

.. figure:: images/invoice_mode.png
   :scale: 75
   :align: center

   *Defining an Invoicing Journal*

Then enter the data for some sales orders for these two partners. After entering sales order data, the
field :guilabel:`Invoicing Mode` in the second tab ``Other Information`` is completed automatically from the partner settings.

Look at the `History` tab of the Sales order, and observe the `Picking List` that has been created. The field :guilabel:`Invoicing Mode` is
automatically shown there. 

.. figure:: images/sales_order_picking.png
   :scale: 75
   :align: center

   *Generated Picking Lists*

At the end of the day, the invoicing supervisor can display the list by journal. Go to the
menu :menuselection:`Sales --> Invoicing --> Lines to Invoice`. Add a New Filter by selecting `Invoice Type contains Daily`, or any other part of the invoice journal you are using. Select the different orders in the list. You can automatically carry out invoicing by clicking the action :guilabel:`Make Invoices` (the gears symbol).

.. tip:: Confirming Invoices

    By default, invoices are generated in the draft state, which enables you to modify them before
    sending them to the customer.
    But you can confirm all the invoices in one go by selecting them all from the list and selecting the
    action `Confirm Draft Invoices`.

At the end of the month the invoicing management does the same work, but in the journal 'month-end invoicing'.

You can also enter a journal to confirm / cancel all the orders in one go. Then you can do several
quotations, assign them to a journal and confirm or cancel them at once.

.. figure:: images/stock_journal_form.png
   :scale: 65
   :align: center

   *View of an Order Journal*

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
