
.. index::
   single: Invoice to Payment

***********************
From Invoice to Payment
***********************

 *This chapter traces the basic accounting workflow in OpenERP, from entering an invoice to
 registering payments. The various operations are described, from the entry of accounting receipts to
 the treatment of the reconciliation process, including payment orders.*

Accounting is at the heart of managing a company: all the company's operations have an impact here.
It has an informational role (how much cash is there? what debts need to be repaid? what is the stock
valuation?) and, because of the information it provides, a reliable and detailed accounting system
can and should have a major decision-making role.

In most companies, accounting is limited to producing statutory reports and satisfying the
directors' curiosity about certain strategic decisions, and to printing the balance sheet and the
income statement several times a year. Even then, there is often several weeks of delay between
reality and the report.

.. note:: Valueing your Accounting Function

        In many small companies, the accounting function is poorly treated.

        Not only do you see the data for documents being entered into the system twice,
        but also the results are often just used to produce legal documents and regular printouts
        of the balance sheet and income statements some weeks after the closing dates.

        By contrast, integrating your accounts with your management system means that you can:

        * reduce data entry effort – you only need to do it once,

        * run your processes with the benefit of financial vision: for example, in managing projects,
          negotiating contracts, and forecasting cash flow,

        * easily get hold of useful information when you need it, such as a customer's credit position.

So accounting is too often underused. The information it brings makes it a very effective tool
for running the company if it is integrated into the management system. Accounting information really
is necessary in all of your company's processes for you to be effective, for example:

* for preparing quotations it is important to know the precise financial position of the client, and
  to see a history of any delays in payment,

* if a given customer has exceeded his credit limit, accounting can automatically stop further
  deliveries to the customer,

* if a project budget is 80% consumed, but the project is only 20% complete, you could renegotiate
  with the client, or review and rein in the objectives of the project,

* if you need to improve your company's cash flow then you could plan your service projects on the
  basis of billing rates and payment terms of the various projects, and not just delivery dates –
  you could work on short-term client projects in preference to R&D projects, for example.

OpenERP's general accounting and analytic accounting handle these needs well because of the close
integration between all of the application modules. Furthermore, the transactions, the actions and
the financial analyses happen in real time, so that you cannot only monitor the situation but also
manage it effectively.

.. index::
   single: module; account

The :mod:`account` module in OpenERP covers general accounting, analytic accounting, and auxiliary
and budgetary accounting. It is double-entry, multi-currency and multi-company.

.. index::
   single: accounting
   single: accounting; financial
   single: accounting; analytical
   single: accounting; auxiliary
   single: accounting; budgetary
   single: asset
   single: liability

.. note:: Accounting

        * General accounting (or financial accounting) is for identifying the assets and liabilities of the
          business. It is managed using double-entry accounting which ensures that each transaction is
          credited to one account and debited from another.

        * Analytical accounting (or management accounting, or cost accounting) is an independent accounting
          system, which reflects the general accounts but is structured along axes that represent the
          company's management needs.

        * Auxiliary accounting reflects the accounts of customers and/or suppliers.

        * Budgetary accounts predefine the expected allocation of resources, usually at the start of a
          financial year.

.. index::
   pair: accounting; multi-company

.. tip:: Multi-company

        There is a choice of methods for integrating OpenERP in a multi-company environment:

        * if the companies hold few documents in common (such as products, or partners - any OpenERP
          resource), you could install separate databases,

        * if the companies share many documents, you can register them in the same database and install
          OpenERP's multi-company documents to finely manage access rights,

        .. index::
           single: module; base_synchro

        * you can synchronize specified document types in several databases using the :mod:`base_synchro`
          module, which is a shared-funding module rather than a module in the standard open repositories.

One of the great advantages of integrating accounts with all of the other modules is in avoiding the
double entry of data into accounting documents. So in OpenERP, an Order automatically generates an
Invoice, and the Invoice automatically generates the accounting entries. These in turn generate tax
submissions, customer reminders, and so on. Such strong integration enables you to:

* reduce data entry work,

* greatly reduce the number of data entry errors,

* get information in real time and enable very fast reaction times (for bill reminders, for
  example),

* exert timely control over all areas of company management.

.. index::
   single: accountant

.. tip:: For Accountants

        You can configure the Accounting application using the information given in the configuration wizard.

        .. figure::  images/config_wiz_account.png
           :scale: 65


        With appropriate rights management, this allows trustees to
        provide customers with real-time access to their data. It also gives them the opportunity to work
        on certain documents that have no direct accounting impact, such as budgets.

        This can provide a value-added service that greatly improves the interaction between trustees and
        their clients.

All the accounts are held in the default currency (which is specified in the company definition),
but each account and/or transaction can also have a secondary currency (which is defined in the
account). The value of multi-currency transactions is then tracked in both currencies.

For this chapter you should start with a fresh database that includes demo data,
with `Sales Management` installed and a generic chart of accounts.

.. raw:: html

    <div class="all-toctree">

.. toctree::

    accounting_workflow
    invoicing
    accounting_entries

.. raw:: html

    </div>



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
