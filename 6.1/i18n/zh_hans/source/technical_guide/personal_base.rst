
.. i18n: .. module:: personal_base
.. i18n:     :synopsis: Personal Base 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: personal_base
    :synopsis: Personal Base 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:       <br />
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />
..

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: .. tip:: This module is part of the OpenERP software, the leading Open Source 
.. i18n:   enterprise management system. If you want to discover OpenERP, check our 
.. i18n:   `screencasts <http://openerp.tv>`_ or download 
.. i18n:   `OpenERP <http://openerp.com>`_ directly.
..

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/personal_base"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/personal_base"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Personal Base (*personal_base*)
.. i18n: ===============================
.. i18n: :Module: personal_base
.. i18n: :Name: Personal Base
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Sandas
.. i18n: :Directory: personal_base
.. i18n: :Web: www.sandas.eu
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Sandas Personal Financials base module.
..

::

  Sandas Personal Financials base module.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/personal_base.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/personal_base.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/personal_base.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/personal_base.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
..

 * :mod:`base`
 * :mod:`account`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n: None
..

None

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Administration/Personal
.. i18n:  * Financial Management/Account Entries
.. i18n:  * Financial Management/Account Entries/New Account Entry
.. i18n:  * Financial Management/Account Entries/Confirmed Account Entries
.. i18n:  * Financial Management/Account Entries/Draft Account Entries
.. i18n:  * Financial Management/Account Entries/Confirmed Account Entries/Confirmed Account Lines
.. i18n:  * Financial Management/Accounts Definition
.. i18n:  * Financial Management/Chart of Accounts
.. i18n:  * Administration/Personal/Account Types
.. i18n:  * Administration/Personal/Create Account Types
.. i18n:  * Administration/Personal/Actions After Login
..

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

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * personal.base.account.entry.tree (tree)
.. i18n:  * personal.base.account.entry.form (form)
.. i18n:  * personal.base.account.entry.line.tree (tree)
.. i18n:  * personal.base.account.entry.line.tree (tree)
.. i18n:  * personal.base.account.entry.line.form (form)
.. i18n:  * personal.base.account.form (form)
.. i18n:  * personal.base.account.tree (tree)
.. i18n:  * personal.base.account.tree (tree)
.. i18n:  * personal.base.account.type.tree (tree)
.. i18n:  * personal.base.account.type.form (form)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Account Type (personal.base.account.type)
.. i18n: #################################################
..

Object: Account Type (personal.base.account.type)
#################################################

.. i18n: :name: Acc. Type Name, char, required
..

:name: Acc. Type Name, char, required

.. i18n: :sign: Sign, selection, required
..

:sign: Sign, selection, required

.. i18n: Object: Account (personal.base.account)
.. i18n: #######################################
..

Object: Account (personal.base.account)
#######################################

.. i18n: :currency_id: Currency, many2one, required
..

:currency_id: Currency, many2one, required

.. i18n: :user_id: User, many2one, required
..

:user_id: User, many2one, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :type_id: Account Type, many2one, required
..

:type_id: Account Type, many2one, required

.. i18n: :child_ids: Childs Codes, one2many
..

:child_ids: Childs Codes, one2many

.. i18n: :note: Note, text
..

:note: Note, text

.. i18n: :parent_id: Parent Code, many2one
..

:parent_id: Parent Code, many2one

.. i18n: :unit_test: unit_test, boolean
..

:unit_test: unit_test, boolean

.. i18n: :balance: Balance, float, readonly
..

:balance: Balance, float, readonly

.. i18n: Object: Account Entry (personal.base.account.entry)
.. i18n: ###################################################
..

Object: Account Entry (personal.base.account.entry)
###################################################

.. i18n: :currency_id: Currency, many2one
..

:currency_id: Currency, many2one

.. i18n: :created_in_model_id: Created in Model, many2one, required, readonly
..

:created_in_model_id: Created in Model, many2one, required, readonly

.. i18n: :user_id: User, many2one, required
..

:user_id: User, many2one, required

.. i18n: :name: Description, char, required
..

:name: Description, char, required

.. i18n: :note: Note, text
..

:note: Note, text

.. i18n: :state: State, selection, required, readonly
..

:state: State, selection, required, readonly

.. i18n: :unit_test: unit_test, boolean
..

:unit_test: unit_test, boolean

.. i18n: :date: Date, date, required
..

:date: Date, date, required

.. i18n: :line_ids: Entries, one2many
..

:line_ids: Entries, one2many

.. i18n: Object: Account Entry Line (personal.base.account.entry.line)
.. i18n: #############################################################
..

Object: Account Entry Line (personal.base.account.entry.line)
#############################################################

.. i18n: :user_id: User, many2one, required
..

:user_id: User, many2one, required

.. i18n: :account_id: Account, many2one, required
..

:account_id: Account, many2one, required

.. i18n: :debit_amount: Debit Amount, float
..

:debit_amount: Debit Amount, float

.. i18n: :credit_amount: Credit Amount, float
..

:credit_amount: Credit Amount, float

.. i18n: :amount_base_with_sign: Amount, float, readonly
..

:amount_base_with_sign: Amount, float, readonly

.. i18n: :amount_base: Amount Base, float
..

:amount_base: Amount Base, float

.. i18n: :currency_id: Currency, many2one, required
..

:currency_id: Currency, many2one, required

.. i18n: :parent_id: Entry, many2one, required
..

:parent_id: Entry, many2one, required

.. i18n: :state: State, selection, required, readonly
..

:state: State, selection, required, readonly

.. i18n: :unit_test: unit_test, boolean
..

:unit_test: unit_test, boolean

.. i18n: :currency_rate: Currency Rate, float, required
..

:currency_rate: Currency Rate, float, required

.. i18n: :date: Date, date, required
..

:date: Date, date, required

.. i18n: :balance: Balance, float, readonly
..

:balance: Balance, float, readonly

.. i18n: :name: Description, char
..

:name: Description, char

.. i18n: Object: personal.base.action.login (personal.base.action.login)
.. i18n: ###############################################################
..

Object: personal.base.action.login (personal.base.action.login)
###############################################################

.. i18n: :name: Name, char
..

:name: Name, char

.. i18n: :action_id: Action, many2one, required
..

:action_id: Action, many2one, required
