
.. module:: personal_base
    :synopsis: Personal Base 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/personal_base"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Personal Base (*personal_base*)
===============================
:Module: personal_base
:Name: Personal Base
:Version: 5.0.1.1
:Author: Sandas
:Directory: personal_base
:Web: www.sandas.eu
:Official module: no
:Quality certified: no

Description
-----------

::

  Sandas Personal Financials base module.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/personal_base.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/personal_base.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`

Reports
-------

None


Menus
-------

 * Administration/Personal
 * Financial Management/Account Entries
 * Financial Management/Account Entries/New Account Entry
 * Financial Management/Account Entries/Confirmed Account Entries
 * Financial Management/Account Entries/Draft Account Entries
 * Financial Management/Account Entries/Confirmed Account Entries/Confirmed Account Lines
 * Financial Management/Accounts Definition
 * Financial Management/Chart of Accounts
 * Administration/Personal/Account Types
 * Administration/Personal/Create Account Types
 * Administration/Personal/Actions After Login

Views
-----

 * personal.base.account.entry.tree (tree)
 * personal.base.account.entry.form (form)
 * personal.base.account.entry.line.tree (tree)
 * personal.base.account.entry.line.tree (tree)
 * personal.base.account.entry.line.form (form)
 * personal.base.account.form (form)
 * personal.base.account.tree (tree)
 * personal.base.account.tree (tree)
 * personal.base.account.type.tree (tree)
 * personal.base.account.type.form (form)


Objects
-------

Object: Account Type (personal.base.account.type)
#################################################



:name: Acc. Type Name, char, required





:sign: Sign, selection, required




Object: Account (personal.base.account)
#######################################



:currency_id: Currency, many2one, required





:user_id: User, many2one, required





:name: Name, char, required





:type_id: Account Type, many2one, required





:child_ids: Childs Codes, one2many





:note: Note, text





:parent_id: Parent Code, many2one





:unit_test: unit_test, boolean





:balance: Balance, float, readonly




Object: Account Entry (personal.base.account.entry)
###################################################



:currency_id: Currency, many2one





:created_in_model_id: Created in Model, many2one, required, readonly





:user_id: User, many2one, required





:name: Description, char, required





:note: Note, text





:state: State, selection, required, readonly





:unit_test: unit_test, boolean





:date: Date, date, required





:line_ids: Entries, one2many




Object: Account Entry Line (personal.base.account.entry.line)
#############################################################



:user_id: User, many2one, required





:account_id: Account, many2one, required





:debit_amount: Debit Amount, float





:credit_amount: Credit Amount, float





:amount_base_with_sign: Amount, float, readonly





:amount_base: Amount Base, float





:currency_id: Currency, many2one, required





:parent_id: Entry, many2one, required





:state: State, selection, required, readonly





:unit_test: unit_test, boolean





:currency_rate: Currency Rate, float, required





:date: Date, date, required





:balance: Balance, float, readonly





:name: Description, char




Object: personal.base.action.login (personal.base.action.login)
###############################################################



:name: Name, char





:action_id: Action, many2one, required


