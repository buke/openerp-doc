.. index::
   pair: service; contract

Managing Service Contracts
==========================

Contracts can take different forms within OpenERP, depending on their nature. So you can have
several distinct types of service contracts, such as:

* fixed-price contracts,

* cost-reimbursement contracts, invoiced when services are completed,

* fixed-price contracts, invoiced monthly as services are carried out.

.. tip:: Contract Quotations

	Some companies commit to contracts on the basis of a requested volume at a certain price for a
	defined period.
	In such a case, the contract is represented by a pricelist for that specific customer.

	The pricelist is linked in the :guilabel:`Sales and Purchases` tab of the :guilabel:`Customers` form,
	so that it is brought up whenever anything is bought from or sold to this partner
	(depending on whether it is a purchase or sales agreement).
	OpenERP automatically selects the price based on this agreed pricelist.

Fixed Price Contracts
---------------------

Fixed price contracts for the sale of services are represented in OpenERP by a Sales Order. In
this case, the supply of services is managed just like all other stockable or consumable products.

You can add new orders using the menu :menuselection:`Sales --> Sales --> Sales Orders`.

The new Sales Order document starts in the \ ``Quotation`` \ state, so the estimate has no
accounting impact on the system until it is confirmed. When you confirm the order, your estimate
moves into the state \ ``Manual In Progress`` \.

.. figure::  images/service_sale_workflow.png
   :scale: 55
   :align: center

   *Process for handling a Sales Order*

Once the order has been approved, OpenERP will automatically generate an invoice and/or a delivery
document proposal based on the parameters you set in the order.

The invoice will be managed by the system depending on the setting of the field :guilabel:`Shipping
Policy` on the order's second tab :guilabel:`Other Information`:

*  :guilabel:`Payment Before Delivery` : OpenERP creates an invoice in the \ ``Draft`` \ state.
   Once this is confirmed and paid, the delivery is activated.

*  :guilabel:`Invoice on Order After Delivery` : the delivery order is produced when the order is
   validated. A draft invoice is then created when the delivery has been completed.

*  :guilabel:`Shipping & Manual Invoice` : OpenERP starts the delivery from the confirmation of
   the order, and adds a button which you manually click when you are ready to create an invoice.

*  :guilabel:`Invoice From The Picking` : invoices are created from the picking stage.

.. index:: delivery

.. note:: Delivery of an Order

	The term 'delivery' should be taken in the broadest sense in OpenERP.
	The effect of a delivery depends on the configuration of the sold product.

	If its type is either ``Stockable Product`` or ``Consumable``, OpenERP will make a request for it to be
	sent for picking.
	If the product's type is ``Service``, OpenERP's scheduler will create a task in the project management
	system,
	or create a subcontract purchase order if the product's `Procurement Method` is ``Make to Order``.

	``Invoicing after delivery`` does as it says: invoicing for the services when the tasks have been
	closed.

When you sign a new contract, you can just enter the order into the system and OpenERP will track
the order.

This works well for small orders. But for large valued service orders, you might want to invoice
several times through the contract, for example:

* 30% on order,

* 40% on completion,

* 30% one month after the system has gone into production.

In this case you should create several invoices for the one Sales Order. You have two options for this:

* Do not handle invoicing automatically from the Sales Order but carry out manual invoicing instead,

* Create draft invoices and then link to them in the third tab :guilabel:`History` of the
  Sales Order, in the :guilabel:`Related
  Invoices` section. When you create an invoice from the order, OpenERP deducts the amounts of the
  invoices already linked to the order to calculate the proposed invoice value.

Cost-reimbursement Contracts
----------------------------

Some contracts are not invoiced from a price fixed on the order but from the cost of the services
carried out. That is usually what happens in the building sector or in large projects.

.. index::
   single: module; hr_timesheet_invoice

The approach you use for this is totally different because instead of using the sales order as the
basis of the invoice you use the analytic accounts. For this you have to install the module
:mod:`hr_timesheet_invoice`.

An analytic account is created for each new contract. The following fields must be completed in this
analytic account:

*  :guilabel:`Partner` : partner associated with the contract,

*  :guilabel:`Sale Pricelist`,

*  :guilabel:`Invoicing`.

The selection of an invoicing rate is an indirect way of specifying that the project will be
invoiced on the basis of analytic costs. This can take different forms, such as delivery of
services, purchase of raw materials, and expense reimbursements.

.. index::
   single: pricelist
..

.. note:: Pricelists and Billing Rates

	You can select a pricelist on the analytic account without having to use it to specify billing
	rates.

	An example of this is a client project that is to be invoiced only indirectly from the analytic
	costs.
	Putting the pricelist on the analytic account makes it possible to compare the actual sales with
	a best case situation where all the services would be invoiced.
	To get this comparison you have to print the analytic balance from the analytic account.

Services are then entered onto timesheets by the various people who work on the project.
Periodically the project manager or account manager uses the following menu to prepare an invoice
:menuselection:`Accounting --> Periodical Processing --> Billing -->
Bill Tasks Works`.

OpenERP then displays all of the costs that have not yet been invoiced. You can filter the proposed
list and click the appropriate action button to generate the corresponding invoices. You can select
the level of detail which is reported on the invoice, such as the date and details of the services.

.. figure::  images/service_timesheet_invoice.png
   :scale: 75
   :align: center

   *Screen for invoicing services*

.. index::
   single: module; account_analytic_analysis

.. note:: Project Management and Analytic Accounts

	:guilabel:`Analytic Accounts` is only available once you have
	installed the module :mod:`account_analytic_analysis`.
	It provides various global financial and operational views of a project manager's projects.

Select an entry and click :guilabel:`Invoice analytic lines` link on the right of the form.
You can then invoice the selected entry by clicking :guilabel:`Create Invoices`.

Fixed-price Contracts Invoiced as Services are Worked
-----------------------------------------------------

For large-valued projects, fixed-price invoicing based on the sales order is not always appropriate.
In the case of a services project planned to run for about six months, invoicing could be based on
the following:

* 30% on order,

* 30% at the project mid-point,

* 40% at delivery.

Such an approach is often used in a company but there are other options. This method of invoicing
can pose many problems for the organization and invoicing of the project:

* It is extremely difficult to determine if the project is on track or not. The endpoint is fuzzy,
  which can result in a tricky discussion with the client at the moment of final invoicing.

* If the project takes more or less time than forecast, it will effectively result in under- or
  over-invoicing during the project.

* Whether you get a proper return can depend on the client. For example, if the client takes a long
  time to sign off on project acceptance, you cannot invoice the remaining 40% even though you might
  have supplied the agreed service properly.

* The account manager and the project manager are often different people.
  The project manager has to
  alert the account manager about the moment that the client can be invoiced, but that moment can easily be
  forgotten or mistaken.

* The project can be fixed for service costs but have agreed extras, such as reimbursement for
  travel expenses. Invoicing from the order does not adapt well to such an approach.

OpenERP provides a third method for invoicing services that can be useful on long projects. This
consists of invoicing the project periodically on the basis of time worked up to a fixed amount that
cannot be exceeded. At the end of the project, a final invoice or a credit note is generated to meet
the total amount of value fixed for the project.

To configure such a project you must set an invoicing rate, a pricelist and a maximum amount on the
analytic account for the project. The services are then invoiced throughout the project by the
different project or account managers, just like projects that are invoiced by time used. The
managers can apply a refund on the final invoice if the project takes more time to complete than
permitted under the contract.

When the project is finished you can generate the closing invoice using the  *Final Invoice*  button
on the analytic account. This automatically calculates the final balance of the bill, taking the
amounts already charged into account. If the amount already invoiced is greater than the maximum
agreed amount, then OpenERP generates a draft credit note.

This approach offers many advantages compared with the traditional methods of invoicing in phases
for fixed-price contracts:

* Fixed-price contracts and cost-reimbursable contracts are invoiced in the same way, which makes
  the company's invoicing process quite simple and systematic even when the projects are mixed.

* Everything is invoiced on the basis of worked time, making it easy to forecast invoicing from
  plans linked to the different analytical accounts.

* This method of proceeding educates project managers just as much as the client because refunds
  have to be given for work done if the project slips.

* Invoicing follows the course of the project and avoids a supplier's dependence on the goodwill of
  the client in approving certain phases.

* Invoicing of expenses follows the same workflow and is therefore very simple.

.. note:: Negotiating contracts

	In contract negotiation, invoicing conditions are often neglected by the client.
	So it can often be straightforward to apply this method of invoicing.

Contracts Limited to a Quantity
-------------------------------

.. index::
   single: module; account_analytic_analysis

Finally, certain contracts are expressed in terms of a quantity rather than a fixed amount. Support
contracts comprising a number of prepaid hours are a case in point. To generate such contracts in
OpenERP you should start by installing the module :mod:`account_analytic_analysis`.

Then you can set a maximum number of hours for each analytic account. When employees enter their
time worked on the support contract in the timesheets, the hours are automatically deducted from the
maximum set on each analytic account.

You must also name someone in the company responsible for renewing expired contracts. They become
responsible for searching through the list of accounts showing negative remaining hours.

The client contract can be limited to a certain quantity of hours, and it can also be limited in
time. For that, you set an end date for the corresponding analytic account.

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

