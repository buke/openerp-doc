
.. index::
   single: journal; configuring

Journals
========

All your accounting entries need to appear in an accounting journal. So you should create a Sales Journal for customer invoices, a Sales Refund journal for customer credit notes, a Purchase Journal for supplier invoices, a Purchase Refund journal for supplier credit notes and a Bank Journal for bank transactions.

Configuring a Journal
---------------------

To view, edit or create new journals use the menu :menuselection:`Accounting --> Configuration --> Financial Accounting --> Journals --> Journals`.

.. figure::  images/account_journal_form.png
   :scale: 75
   :align: center

   *Defining an Accounting Journal*

Blue fields are mandatory fields. When you select a journal type, some configuration parameters will be preset. The journal type will tell the system where the journal concerned can be used.

Each journal has a specific way of displaying data. The type of journal determines the journal view, which indicates the fields that need to be visible and are required to enter accounting data in that journal. The view determines both the order of the fields and the properties of each field. For example, the field :guilabel:`Statement` has to appear when entering data in the bank journal, but not in the other journals.

You can also create your own journal views. However, before creating a new view for a journal, check whether there is nothing similar already defined. You should only create a new view for new types of journals.

You can create a sequence for each journal. This sequence determines the automatic numbering for accounting entries. Several journals can use the same sequence if you want to define one for them all, and if your legislation allows this.

.. tip:: Sequences

    Sequences can also be created from the :menuselection:`Settings --> Configuration --> Sequences & Identifiers --> Sequences`.
    By default, OpenERP has only one sequence in the journal definition. If you need two separate sequences to be kept for the journal, you can install the module :mod:`account_sequence`.

The default credit and debit account allow the software to automatically generate counterpart entries when you are entering data through :guilabel:`Journal Items`. In some journals, debit and credit accounts are mandatory. For example, in a bank journal you should put an associated bank account, so that you do not have to create counterparts for each transaction manually.

A journal can be marked as being centralised. When you do this, the counterpart entries will not be owned by each entry, but will be global for the given journal and period. You will then have a credit line and a debit line centralized for each entry in one of these journals, meaning that both credit and debit appear on the same line. This option is used when posting opening entries in a situation journal.

.. note:: Bank Journal, Easy Configuration

    A bank journal can automatically be created from the bank account(s) you define for your company. Go to :menuselection:`Accounting --> Configuration --> Financial Accounting --> Accounts --> Setup your Bank Accounts`. Here you create the bank account or IBAN number of your company's bank account(s). Fill in the Bank Name, and when you save the entry, your Bank Journal will automatically be created with the Bank Name and the Account Number. The general ledger account for this bank will also be created for you.

Controls and Tips for Data Entry
--------------------------------

You can carry out two types of control on journals in OpenERP – controls over the accounts and access controls for groups of users. In addition to these controls, you can also apply all of the standard user rights management.

To avoid entering account data in wrong accounts, you can put conditions on the general accounts about which journal can use a given account. To do this, you have to list all the accounts or valid account types in the second tab, :guilabel:`Entry Controls`. If you have not added any accounts there, OpenERP applies no restriction on the accounts for that journal. If you list accounts and/or the types of accounts that can be used in a journal, OpenERP prevents you from using any account or account type not in that list. This verification step starts from the moment you enter data. You can only select allowed accounts or account types.

This functionality is useful for limiting possible data entry errors by restricting the accounts to be used in a journal.

.. tip:: Control of Data Entry

        In accounting it is not a good idea to allow a data entry directly from bank account A to bank
        account B.
        If you enter a transaction from bank A to bank B, the transaction will be accounted for twice.

        To prevent this problem, pass the transaction through intermediate account C.
        At the time of data entry, the system checks the type of account that is accepted in the bank
        journal: only accounts that are not of type ``Bank`` are accepted.

        If your accountant defines this control properly, non-accounting users are prevented from
        transferring payments from one bank to another, reducing your risks.

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
