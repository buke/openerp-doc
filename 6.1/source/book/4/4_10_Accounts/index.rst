
.. index::
   single: Analytic Accounts

.. _ch-accts:

*****************
Analytic Accounts
*****************

 *Sitting at the heart of your company's processes, analytic accounts (or cost accounts) are
 indispensable tools for managing your operations well. Unlike your financial accounts, they are for
 more than accountants - they are for general managers and project managers, too.*

You need a common way of referring to each user, service, or document to integrate all your
company's processes effectively. Such a common basis is provided by analytic accounts (or management
accounts, or cost accounts, as they are also called) in OpenERP.

Analytic accounts are often presented as a foundation for strategic enterprise decisions. But
because of all the information they pull together, OpenERP's analytic accounts can be a useful
management tool, at the center of most system processes.

There are several reasons for this:

* they reflect your entire management activity,

* unlike the general accounts, the structure of the analytic accounts is not regulated by legal
  obligations, so each company can adapt it to its needs.

.. note:: Independence from General Accounts

        In some software packages, analytic accounts are managed as an extension of general accounts –
        for example, by using the two last digits of the account code to represent analytic accounts.

        In OpenERP, analytic accounts are linked to general accounts but are treated totally
        independently.
        So you can enter various different analytic operations that have no counterpart in the general
        financial accounts.

While the structure of the general chart of accounts is imposed by law, the analytic chart of
accounts is built to fit a company's needs closely.

Just as in the general accounts, you will find accounting entries in the different analytic accounts.
Each analytic entry can be linked to a general account, or not, as you wish. Conversely, an entry in
a general account can be linked to one, several, or no corresponding analytic accounts.

You will discover many advantages of this independent representation below. For the more impatient,
here are some of those advantages:

* you can manage many different analytic operations,

* you can modify an analytic plan on the fly, during the course of an activity, because of its
  independence,

* you can avoid an explosion in the number of general accounts,

* even those companies that do not use OpenERP's general accounts can use the analytic accounts for
  management.

.. tip:: Who Benefits from Analytic Accounts?

        Unlike general accounts, analytic accounts in OpenERP are not so much an accounting tool for Accounts as a
        management tool for everyone in the company. (That is why they are also called management accounts.)

        The main users of analytic accounts should be the directors, general managers and project managers.

Analytic accounts make up a powerful tool that can be used in different ways. The trick is to create
your own analytic structure for a chart of accounts that closely matches your company's needs.

For this chapter, you should start with a fresh database that includes demo data,
with :mod:`sale` and its dependencies installed, and no particular chart of accounts configured.

.. raw:: html

    <div class="all-toctree">

.. toctree::

    4_10_Accounts_analytic_chart
    4_10_Accounts_record

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

