
Analytic Accounts
=================

To manage purchases by project, you should use analytic accounts. 
You can set an analytic account on each line of a supplier order. 
The analytic costs linked to this purchase will be managed
by OpenERP from the goods receipt and confirmation of the supplier invoice.

.. index::
   single: module; hr_timesheet_invoice

The :mod:`hr_timesheet_invoice` module lets you re-invoice the analytic costs automatically using
parameters in the analytic accounts such as sale pricelist, associated partner company, and maximum amount.

So you can put an invoice order with a defined invoice workflow in place based on the analytic accounts. If you are
working ``Make to Order``, the workflow will be:

#. Customer Order,

#. Procurement Order on supplier,

#. Receive invoice and goods from the supplier,

#. Delivery and invoicing to the customer.

When re-invoicing based on costs you would get the following workflow:

#. Enter the customer contract conditions from the analytic accounts,

#. Purchase raw materials and write the services performed into the timesheets,

#. Receive the supplier invoice and the products,

#. Invoice these costs to the customer.

.. index::
   single: module; purchase_analytic_plans

.. tip:: Analytic Multi-plans

   If you want several analysis plans, you should install the module :mod:`purchase_analytic_plans`.
   These let you split a line on a supplier purchase order into several accounts and analytic
   plans.
   Look at :ref:`ch-accts` for more information on the use of analytic accounts.

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
