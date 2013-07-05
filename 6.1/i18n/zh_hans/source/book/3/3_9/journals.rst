.. i18n: .. index::
.. i18n:    single: journal; configuring
..

.. index::
   single: journal; configuring

.. i18n: Journals
.. i18n: ========
..

账簿
========

.. i18n: All your accounting entries need to appear in an accounting journal. So you should create a Sales Journal for customer invoices, a Sales Refund journal for customer credit notes, a Purchase Journal for supplier invoices, a Purchase Refund journal for supplier credit notes and a Bank Journal for bank transactions.
..

所有的会计分录需要由会计帐簿来显示。因此您应该为销售发票创建销售分类帐， a Sales Refund journal for customer credit notes, 为供应商发票创建采购分类帐， a Purchase Refund journal for supplier credit notes and a Bank Journal for bank transactions.

.. i18n: Configuring a Journal
.. i18n: ---------------------
..

配置账簿
---------------------

.. i18n: To view, edit or create new journals use the menu :menuselection:`Accounting --> Configuration --> Financial Accounting --> Journals --> Journals`.
..

要查看，编辑或创建新分类帐，使用菜单 :menuselection:`Accounting --> Configuration --> Financial Accounting --> Journals --> Journals`.

.. i18n: .. figure::  images/account_journal_form.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Defining an Accounting Journal*
..

.. figure::  images/account_journal_form.png
   :scale: 75
   :align: center

   *定义会计分类帐*

.. i18n: Blue fields are mandatory fields. When you select a journal type, some configuration parameters will be preset. The journal type will tell the system where the journal concerned can be used.
..

蓝色字段均为必填字段。当您选择了分类帐类型，将被预置一些配置参数。 The journal type will tell the system where the journal concerned can be used.

.. i18n: Each journal has a specific way of displaying data. The type of journal determines the journal view, which indicates the fields that need to be visible and are required to enter accounting data in that journal. The view determines both the order of the fields and the properties of each field. For example, the field :guilabel:`Statement` has to appear when entering data in the bank journal, but not in the other journals.
..

每一分类帐都有显示数据的特殊方式。 The type of journal determines the journal view, which indicates the fields that need to be visible and are required to enter accounting data in that journal. The view determines both the order of the fields and the properties of each field. For example, the field :guilabel:`Statement` has to appear when entering data in the bank journal, but not in the other journals.

.. i18n: You can also create your own journal views. However, before creating a new view for a journal, check whether there is nothing similar already defined. You should only create a new view for new types of journals.
..

You can also create your own journal views. However, before creating a new view for a journal, check whether there is nothing similar already defined. You should only create a new view for new types of journals.

.. i18n: You can create a sequence for each journal. This sequence determines the automatic numbering for accounting entries. Several journals can use the same sequence if you want to define one for them all, and if your legislation allows this.
..

You can create a sequence for each journal. This sequence determines the automatic numbering for accounting entries. Several journals can use the same sequence if you want to define one for them all, and if your legislation allows this.

.. i18n: .. tip:: Sequences
.. i18n: 
.. i18n:     Sequences can also be created from the :menuselection:`Settings --> Configuration --> Sequences & Identifiers --> Sequences`.
.. i18n:     By default, OpenERP has only one sequence in the journal definition. If you need two separate sequences to be kept for the journal, you can install the module :mod:`account_sequence`.
..

.. tip:: 序号编码

    Sequences can also be created from the :menuselection:`Settings --> Configuration --> Sequences & Identifiers --> Sequences`.
    By default, OpenERP has only one sequence in the journal definition. If you need two separate sequences to be kept for the journal, you can install the module :mod:`account_sequence`.

.. i18n: The default credit and debit account allow the software to automatically generate counterpart entries when you are entering data through :guilabel:`Journal Items`. In some journals, debit and credit accounts are mandatory. For example, in a bank journal you should put an associated bank account, so that you do not have to create counterparts for each transaction manually.
..

The default credit and debit account allow the software to automatically generate counterpart entries when you are entering data through :guilabel:`Journal Items`. In some journals, debit and credit accounts are mandatory. For example, in a bank journal you should put an associated bank account, so that you do not have to create counterparts for each transaction manually.

.. i18n: A journal can be marked as being centralised. When you do this, the counterpart entries will not be owned by each entry, but will be global for the given journal and period. You will then have a credit line and a debit line centralized for each entry in one of these journals, meaning that both credit and debit appear on the same line. This option is used when posting opening entries in a situation journal.
..

A journal can be marked as being centralised. When you do this, the counterpart entries will not be owned by each entry, but will be global for the given journal and period. You will then have a credit line and a debit line centralized for each entry in one of these journals, meaning that both credit and debit appear on the same line. This option is used when posting opening entries in a situation journal.

.. i18n: .. note:: Bank Journal, Easy Configuration
.. i18n: 
.. i18n:     A bank journal can automatically be created from the bank account(s) you define for your company. Go to :menuselection:`Accounting --> Configuration --> Financial Accounting --> Accounts --> Setup your Bank Accounts`. Here you create the bank account or IBAN number of your company's bank account(s). Fill in the Bank Name, and when you save the entry, your Bank Journal will automatically be created with the Bank Name and the Account Number. The general ledger account for this bank will also be created for you.
..

.. note:: Bank Journal, Easy Configuration

    A bank journal can automatically be created from the bank account(s) you define for your company. Go to :menuselection:`Accounting --> Configuration --> Financial Accounting --> Accounts --> Setup your Bank Accounts`. Here you create the bank account or IBAN number of your company's bank account(s). Fill in the Bank Name, and when you save the entry, your Bank Journal will automatically be created with the Bank Name and the Account Number. The general ledger account for this bank will also be created for you.

.. i18n: Controls and Tips for Data Entry
.. i18n: --------------------------------
..

数据录入的控制和提示
--------------------------------

.. i18n: You can carry out two types of control on journals in OpenERP – controls over the accounts and access controls for groups of users. In addition to these controls, you can also apply all of the standard user rights management.
..

You can carry out two types of control on journals in OpenERP – controls over the accounts and access controls for groups of users. In addition to these controls, you can also apply all of the standard user rights management.

.. i18n: To avoid entering account data in wrong accounts, you can put conditions on the general accounts about which journal can use a given account. To do this, you have to list all the accounts or valid account types in the second tab, :guilabel:`Entry Controls`. If you have not added any accounts there, OpenERP applies no restriction on the accounts for that journal. If you list accounts and/or the types of accounts that can be used in a journal, OpenERP prevents you from using any account or account type not in that list. This verification step starts from the moment you enter data. You can only select allowed accounts or account types.
..

To avoid entering account data in wrong accounts, you can put conditions on the general accounts about which journal can use a given account. To do this, you have to list all the accounts or valid account types in the second tab, :guilabel:`Entry Controls`. If you have not added any accounts there, OpenERP applies no restriction on the accounts for that journal. If you list accounts and/or the types of accounts that can be used in a journal, OpenERP prevents you from using any account or account type not in that list. This verification step starts from the moment you enter data. You can only select allowed accounts or account types.

.. i18n: This functionality is useful for limiting possible data entry errors by restricting the accounts to be used in a journal.
..

This functionality is useful for limiting possible data entry errors by restricting the accounts to be used in a journal.

.. i18n: .. tip:: Control of Data Entry
.. i18n: 
.. i18n:         In accounting it is not a good idea to allow a data entry directly from bank account A to bank
.. i18n:         account B.
.. i18n:         If you enter a transaction from bank A to bank B, the transaction will be accounted for twice.
.. i18n: 
.. i18n:         To prevent this problem, pass the transaction through intermediate account C.
.. i18n:         At the time of data entry, the system checks the type of account that is accepted in the bank
.. i18n:         journal: only accounts that are not of type ``Bank`` are accepted.
.. i18n: 
.. i18n:         If your accountant defines this control properly, non-accounting users are prevented from
.. i18n:         transferring payments from one bank to another, reducing your risks.
..

.. tip:: 数据录入控制

        In accounting it is not a good idea to allow a data entry directly from bank account A to bank
        account B.
        If you enter a transaction from bank A to bank B, the transaction will be accounted for twice.

        To prevent this problem, pass the transaction through intermediate account C.
        At the time of data entry, the system checks the type of account that is accepted in the bank
        journal: only accounts that are not of type ``Bank`` are accepted.

        If your accountant defines this control properly, non-accounting users are prevented from
        transferring payments from one bank to another, reducing your risks.

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
