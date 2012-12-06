.. i18n: .. index::
.. i18n:    single: Invoice to Payment
..

.. index::
   single: Invoice to Payment

.. i18n: ***********************
.. i18n: From Invoice to Payment
.. i18n: ***********************
..

***********************
从开票到支付
***********************

.. i18n:  *This chapter traces the basic accounting workflow in OpenERP, from entering an invoice to
.. i18n:  registering payments. The various operations are described, from the entry of accounting receipts to
.. i18n:  the treatment of the reconciliation process, including payment orders.*
..

 *This chapter traces the basic accounting workflow in OpenERP, from entering an invoice to
 registering payments. The various operations are described, from the entry of accounting receipts to
 the treatment of the reconciliation process, including payment orders.*

.. i18n: Accounting is at the heart of managing a company: all the company's operations have an impact here.
.. i18n: It has an informational role (how much cash is there? what debts need to be repaid? what is the stock
.. i18n: valuation?) and, because of the information it provides, a reliable and detailed accounting system
.. i18n: can and should have a major decision-making role.
..

Accounting is at the heart of managing a company: all the company's operations have an impact here.
It has an informational role (how much cash is there? what debts need to be repaid? what is the stock
valuation?) and, because of the information it provides, a reliable and detailed accounting system
can and should have a major decision-making role.

.. i18n: In most companies, accounting is limited to producing statutory reports and satisfying the
.. i18n: directors' curiosity about certain strategic decisions, and to printing the balance sheet and the
.. i18n: income statement several times a year. Even then, there is often several weeks of delay between
.. i18n: reality and the report.
..

In most companies, accounting is limited to producing statutory reports and satisfying the
directors' curiosity about certain strategic decisions, and to printing the balance sheet and the
income statement several times a year. Even then, there is often several weeks of delay between
reality and the report.

.. i18n: .. note:: Valueing your Accounting Function
.. i18n: 
.. i18n:         In many small companies, the accounting function is poorly treated.
.. i18n: 
.. i18n:         Not only do you see the data for documents being entered into the system twice,
.. i18n:         but also the results are often just used to produce legal documents and regular printouts
.. i18n:         of the balance sheet and income statements some weeks after the closing dates.
.. i18n: 
.. i18n:         By contrast, integrating your accounts with your management system means that you can:
.. i18n: 
.. i18n:         * reduce data entry effort – you only need to do it once,
.. i18n: 
.. i18n:         * run your processes with the benefit of financial vision: for example, in managing projects,
.. i18n:           negotiating contracts, and forecasting cash flow,
.. i18n: 
.. i18n:         * easily get hold of useful information when you need it, such as a customer's credit position.
..

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

.. i18n: So accounting is too often underused. The information it brings makes it a very effective tool
.. i18n: for running the company if it is integrated into the management system. Accounting information really
.. i18n: is necessary in all of your company's processes for you to be effective, for example:
..

So accounting is too often underused. The information it brings makes it a very effective tool
for running the company if it is integrated into the management system. Accounting information really
is necessary in all of your company's processes for you to be effective, for example:

.. i18n: * for preparing quotations it is important to know the precise financial position of the client, and
.. i18n:   to see a history of any delays in payment,
.. i18n: 
.. i18n: * if a given customer has exceeded his credit limit, accounting can automatically stop further
.. i18n:   deliveries to the customer,
.. i18n: 
.. i18n: * if a project budget is 80% consumed, but the project is only 20% complete, you could renegotiate
.. i18n:   with the client, or review and rein in the objectives of the project,
.. i18n: 
.. i18n: * if you need to improve your company's cash flow then you could plan your service projects on the
.. i18n:   basis of billing rates and payment terms of the various projects, and not just delivery dates –
.. i18n:   you could work on short-term client projects in preference to R&D projects, for example.
..

* for preparing quotations it is important to know the precise financial position of the client, and
  to see a history of any delays in payment,

* if a given customer has exceeded his credit limit, accounting can automatically stop further
  deliveries to the customer,

* if a project budget is 80% consumed, but the project is only 20% complete, you could renegotiate
  with the client, or review and rein in the objectives of the project,

* if you need to improve your company's cash flow then you could plan your service projects on the
  basis of billing rates and payment terms of the various projects, and not just delivery dates –
  you could work on short-term client projects in preference to R&D projects, for example.

.. i18n: OpenERP's general accounting and analytic accounting handle these needs well because of the close
.. i18n: integration between all of the application modules. Furthermore, the transactions, the actions and
.. i18n: the financial analyses happen in real time, so that you cannot only monitor the situation but also
.. i18n: manage it effectively.
..

OpenERP's general accounting and analytic accounting handle these needs well because of the close
integration between all of the application modules. Furthermore, the transactions, the actions and
the financial analyses happen in real time, so that you cannot only monitor the situation but also
manage it effectively.

.. i18n: .. index::
.. i18n:    single: module; account
..

.. index::
   single: module; account

.. i18n: The :mod:`account` module in OpenERP covers general accounting, analytic accounting, and auxiliary
.. i18n: and budgetary accounting. It is double-entry, multi-currency and multi-company.
..

The :mod:`account` module in OpenERP covers general accounting, analytic accounting, and auxiliary
and budgetary accounting. It is double-entry, multi-currency and multi-company.

.. i18n: .. index::
.. i18n:    single: accounting
.. i18n:    single: accounting; financial
.. i18n:    single: accounting; analytical
.. i18n:    single: accounting; auxiliary
.. i18n:    single: accounting; budgetary
.. i18n:    single: asset
.. i18n:    single: liability
..

.. index::
   single: accounting
   single: accounting; financial
   single: accounting; analytical
   single: accounting; auxiliary
   single: accounting; budgetary
   single: asset
   single: liability

.. i18n: .. note:: Accounting
.. i18n: 
.. i18n:         * General accounting (or financial accounting) is for identifying the assets and liabilities of the
.. i18n:           business. It is managed using double-entry accounting which ensures that each transaction is
.. i18n:           credited to one account and debited from another.
.. i18n: 
.. i18n:         * Analytical accounting (or management accounting, or cost accounting) is an independent accounting
.. i18n:           system, which reflects the general accounts but is structured along axes that represent the
.. i18n:           company's management needs.
.. i18n: 
.. i18n:         * Auxiliary accounting reflects the accounts of customers and/or suppliers.
.. i18n: 
.. i18n:         * Budgetary accounts predefine the expected allocation of resources, usually at the start of a
.. i18n:           financial year.
..

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

.. i18n: .. index::
.. i18n:    pair: accounting; multi-company
..

.. index::
   pair: accounting; multi-company

.. i18n: .. tip:: Multi-company
.. i18n: 
.. i18n:         There is a choice of methods for integrating OpenERP in a multi-company environment:
.. i18n: 
.. i18n:         * if the companies hold few documents in common (such as products, or partners - any OpenERP
.. i18n:           resource), you could install separate databases,
.. i18n: 
.. i18n:         * if the companies share many documents, you can register them in the same database and install
.. i18n:           OpenERP's multi-company documents to finely manage access rights,
.. i18n: 
.. i18n:         .. index::
.. i18n:            single: module; base_synchro
.. i18n: 
.. i18n:         * you can synchronize specified document types in several databases using the :mod:`base_synchro`
.. i18n:           module, which is a shared-funding module rather than a module in the standard open repositories.
..

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

.. i18n: One of the great advantages of integrating accounts with all of the other modules is in avoiding the
.. i18n: double entry of data into accounting documents. So in OpenERP, an Order automatically generates an
.. i18n: Invoice, and the Invoice automatically generates the accounting entries. These in turn generate tax
.. i18n: submissions, customer reminders, and so on. Such strong integration enables you to:
..

One of the great advantages of integrating accounts with all of the other modules is in avoiding the
double entry of data into accounting documents. So in OpenERP, an Order automatically generates an
Invoice, and the Invoice automatically generates the accounting entries. These in turn generate tax
submissions, customer reminders, and so on. Such strong integration enables you to:

.. i18n: * reduce data entry work,
.. i18n: 
.. i18n: * greatly reduce the number of data entry errors,
.. i18n: 
.. i18n: * get information in real time and enable very fast reaction times (for bill reminders, for
.. i18n:   example),
.. i18n: 
.. i18n: * exert timely control over all areas of company management.
..

* reduce data entry work,

* greatly reduce the number of data entry errors,

* get information in real time and enable very fast reaction times (for bill reminders, for
  example),

* exert timely control over all areas of company management.

.. i18n: .. index::
.. i18n:    single: accountant
..

.. index::
   single: accountant

.. i18n: .. tip:: For Accountants
.. i18n: 
.. i18n:         You can configure the Accounting application using the information given in the configuration wizard.
.. i18n: 
.. i18n:         .. figure::  images/config_wiz_account.png
.. i18n:            :scale: 65
.. i18n: 
.. i18n:         With appropriate rights management, this allows trustees to
.. i18n:         provide customers with real-time access to their data. It also gives them the opportunity to work
.. i18n:         on certain documents that have no direct accounting impact, such as budgets.
.. i18n: 
.. i18n:         This can provide a value-added service that greatly improves the interaction between trustees and
.. i18n:         their clients.
..

.. tip:: For Accountants

        You can configure the Accounting application using the information given in the configuration wizard.

        .. figure::  images/config_wiz_account.png
           :scale: 65

        With appropriate rights management, this allows trustees to
        provide customers with real-time access to their data. It also gives them the opportunity to work
        on certain documents that have no direct accounting impact, such as budgets.

        This can provide a value-added service that greatly improves the interaction between trustees and
        their clients.

.. i18n: All the accounts are held in the default currency (which is specified in the company definition),
.. i18n: but each account and/or transaction can also have a secondary currency (which is defined in the
.. i18n: account). The value of multi-currency transactions is then tracked in both currencies.
..

All the accounts are held in the default currency (which is specified in the company definition),
but each account and/or transaction can also have a secondary currency (which is defined in the
account). The value of multi-currency transactions is then tracked in both currencies.

.. i18n: For this chapter you should start with a fresh database that includes demo data,
.. i18n: with `Sales Management` installed and a generic chart of accounts.
..

For this chapter you should start with a fresh database that includes demo data,
with `Sales Management` installed and a generic chart of accounts.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="all-toctree">
..

.. raw:: html

    <div class="all-toctree">

.. i18n: .. toctree::
.. i18n: 
.. i18n:     accounting_workflow
.. i18n:     invoicing
.. i18n:     accounting_entries
..

.. toctree::

    accounting_workflow
    invoicing
    accounting_entries

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
