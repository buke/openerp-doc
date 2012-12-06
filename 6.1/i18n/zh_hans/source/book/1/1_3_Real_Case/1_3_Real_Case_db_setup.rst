.. i18n: Database Setup
.. i18n: ==============
..

帐套配置
==============

.. i18n: You will create all the elements in the database that you need to carry out the use case. These are
.. i18n: specified in the functional requirements.
..

You will create all the elements in the database that you need to carry out the use case. These are
specified in the functional requirements.

.. i18n: .. index::
.. i18n:    single: accounts; configuring
.. i18n:    
.. i18n: Configuring Accounts
.. i18n: --------------------
..

.. index::
   single: accounts; configuring
   
配置会计科目
--------------------

.. i18n: You need to start off with a minimal set of accounts, and to do that you will need a couple of
.. i18n: account types. You can structure your accounts into a chart at any time (and, in fact, you can
.. i18n: structure them into several additional charts at the same time as you will see in the chapter
.. i18n: :ref:`ch-configacct`), so you do not need to be concerned unduly about structure.
..

You need to start off with a minimal set of accounts, and to do that you will need a couple of
account types. You can structure your accounts into a chart at any time (and, in fact, you can
structure them into several additional charts at the same time as you will see in the chapter
:ref:`ch-configacct`), so you do not need to be concerned unduly about structure.

.. i18n: .. index::
.. i18n:    single: account types
..

.. index::
   single: account types

.. i18n: Account Types
.. i18n: ^^^^^^^^^^^^^
..

科目类型
^^^^^^^^^^^^^

.. i18n: Create account types using :menuselection:`Accounting --> Configuration --> 
.. i18n: Financial Accounting --> Accounts --> Account Types` and then clicking the
.. i18n: :guilabel:`New` button. You will need the following four types, the first of which is shown
.. i18n: in figure :ref:`fig-oech03accty`.
..

Create account types using :menuselection:`Accounting --> Configuration --> 
Financial Accounting --> Accounts --> Account Types` and then clicking the
:guilabel:`New` button. You will need the following four types, the first of which is shown
in figure :ref:`fig-oech03accty`.

.. i18n: .. table:: Defining Account Types
.. i18n: 
.. i18n:    ============== ======== ================================= ===============
.. i18n:    Acc. Type Name Code     P&L / BS Category                 Deferral Method
.. i18n:    ============== ======== ================================= ===============
.. i18n:    View           view     /                                 None           
.. i18n:    Income         income   Profit & Loss (Income Accounts)   Unreconciled   
.. i18n:    Expense        expense  Profit & Loss (Expense Accounts)  Unreconciled   
.. i18n:    Cash           cash     Balance Sheet (Assets Accounts)   Balance        
.. i18n:    ============== ======== ================================= ===============
..

.. table:: Defining Account Types

   ============== ======== ================================= ===============
   科目类型       类型CODE     P&L / BS Category                 Deferral Method
   ============== ======== ================================= ===============
   View           view     /                                 None           
   Income         income   Profit & Loss (Income Accounts)   Unreconciled   
   Expense        expense  Profit & Loss (Expense Accounts)  Unreconciled   
   Cash           cash     Balance Sheet (Assets Accounts)   Balance        
   ============== ======== ================================= ===============

.. i18n: .. _fig-oech03accty:
.. i18n: 
.. i18n: .. figure::  images/openerp_ch03_acctype.png
.. i18n:    :align: center
.. i18n:    :scale: 80
.. i18n: 
.. i18n:    *New Account Type*
.. i18n:    
.. i18n: Accounts
.. i18n: ^^^^^^^^
..

.. _fig-oech03accty:

.. figure::  images/openerp_ch03_acctype.png
   :align: center
   :scale: 80

   *New Account Type*
   
科目
^^^^^^^^

.. i18n: Create accounts using :menuselection:`Accounting --> Configuration --> 
.. i18n: Financial Accounting --> Accounts --> Accounts` and then clicking the
.. i18n: :guilabel:`New` button. 
..

新建科目 :menuselection:`Accounting --> Configuration --> 
Financial Accounting --> Accounts --> Accounts` and then clicking the
:guilabel:`New` button. 

.. i18n: You need accounts to handle the purchase and sales orders that have not yet been paid,
.. i18n: two more for the receipt and shipping of goods, and one for the payment and receipt of funds. 
.. i18n: And one 'organizing' account that is just a view of the other five. So
.. i18n: you will need the following six accounts, one of which is shown
.. i18n: in :ref:`fig-oech03accts`.
..

You need accounts to handle the purchase and sales orders that have not yet been paid,
two more for the receipt and shipping of goods, and one for the payment and receipt of funds. 
And one 'organizing' account that is just a view of the other five. So
you will need the following six accounts, one of which is shown
in :ref:`fig-oech03accts`.

.. i18n: .. table:: Defining Accounts
.. i18n: 
.. i18n:    ============= ==== ============= =============== ============ =========
.. i18n:    Name          Code Internal Type Parent          Account Type Reconcile
.. i18n:    ============= ==== ============= =============== ============ =========
.. i18n:    Minimal Chart 0    View                          View         unchecked
.. i18n:    Payable       AP   Payable       0 Minimal Chart Expense      checked
.. i18n:    Receivable    AR   Receivable    0 Minimal Chart Income       checked
.. i18n:    Cash          C    Liquidity     0 Minimal Chart Cash         unchecked
.. i18n:    Purchases     P    Regular       0 Minimal Chart Expense      unchecked
.. i18n:    Sales         S    Regular       0 Minimal Chart Income       unchecked
.. i18n:    ============= ==== ============= =============== ============ =========
..

.. table:: Defining Accounts

   ============= ==== ============= =============== ============ =========
   Name          Code Internal Type Parent          Account Type Reconcile
   ============= ==== ============= =============== ============ =========
   Minimal Chart 0    View                          View         unchecked
   Payable       AP   Payable       0 Minimal Chart Expense      checked
   Receivable    AR   Receivable    0 Minimal Chart Income       checked
   Cash          C    Liquidity     0 Minimal Chart Cash         unchecked
   Purchases     P    Regular       0 Minimal Chart Expense      unchecked
   Sales         S    Regular       0 Minimal Chart Income       unchecked
   ============= ==== ============= =============== ============ =========

.. i18n: .. _fig-oech03accts:
.. i18n: 
.. i18n: .. figure::  images/openerp_ch03_accts.png
.. i18n:    :align: center
.. i18n:    :scale: 80
.. i18n: 
.. i18n:    *New Account*
..

.. _fig-oech03accts:

.. figure::  images/openerp_ch03_accts.png
   :align: center
   :scale: 80

   *New Account*

.. i18n: The :guilabel:`Account Type` entry is taken from the list of types that you just created.
.. i18n: Although it looks a bit like a text box, it does not behave in quite the same way.
.. i18n: A single :kbd:`Del` or :kbd:`Backspace` keystroke is all you need to delete the whole text,
.. i18n: and when you type the name (or part of the name), you still need to associate that text
.. i18n: with the entry by clicking the :guilabel:`Search` icon to the right of the field.
..

The :guilabel:`Account Type` entry is taken from the list of types that you just created.
Although it looks a bit like a text box, it does not behave in quite the same way.
A single :kbd:`Del` or :kbd:`Backspace` keystroke is all you need to delete the whole text,
and when you type the name (or part of the name), you still need to associate that text
with the entry by clicking the :guilabel:`Search` icon to the right of the field.

.. i18n: .. index::
.. i18n:    single: properties; defining
..

.. index::
   single: properties; defining

.. i18n: Properties
.. i18n: ^^^^^^^^^^
..

属性
^^^^^^^^^^

.. i18n: You now define some default properties, so that you do not have to think about
.. i18n: which account is used for which transaction every time you do something.
.. i18n: The main new properties are the four that associate accounts payable and receivable
.. i18n: to partners, and expenses and income to product categories.
..

You now define some default properties, so that you do not have to think about
which account is used for which transaction every time you do something.
The main new properties are the four that associate accounts payable and receivable
to partners, and expenses and income to product categories.

.. i18n: Create properties using :menuselection:`Administration --> Configuration --> 
.. i18n: Parameters --> Configuration Parameters` and then clicking the :guilabel:`New` button.
.. i18n: You may have switch to ``Extended`` view to be able to access this menu.
..

Create properties using :menuselection:`Administration --> Configuration --> 
Parameters --> Configuration Parameters` and then clicking the :guilabel:`New` button.
You may have switch to ``Extended`` view to be able to access this menu.

.. i18n: .. table:: Defining Properties
.. i18n: 
.. i18n:    ============================== ================== ======== ===============================
.. i18n:    Name                           Field              Type     Value                          
.. i18n:    ============================== ================== ======== ===============================
.. i18n:    property_account_payable       Account Payable    Many2One (account.account) AP Payable   
.. i18n:    property_account_receivable    Account Receivable Many2One (account.account) AR Receivable
.. i18n:    property_account_expense_categ Expense Account    Many2One (account.account) P Purchases  
.. i18n:    property_account_income_categ  Income Account     Many2One (account.account) S Sales      
.. i18n:    ============================== ================== ======== ===============================
..

.. table:: Defining Properties

   ============================== ================== ======== ===============================
   Name                           Field              Type     Value                          
   ============================== ================== ======== ===============================
   property_account_payable       Account Payable    Many2One (account.account) AP Payable   
   property_account_receivable    Account Receivable Many2One (account.account) AR Receivable
   property_account_expense_categ Expense Account    Many2One (account.account) P Purchases  
   property_account_income_categ  Income Account     Many2One (account.account) S Sales      
   ============================== ================== ======== ===============================

.. i18n: .. tip:: Mistakes in configuring accounts and properties
.. i18n: 
.. i18n:    It is easy to make mistakes in configuring accounts and their properties, but the consequences
.. i18n:    are not immediately obvious. You will mostly discover mistakes when trying to make a Purchase or
.. i18n:    Sale Order (see later, for example, :ref:`sect-PO`), where the accounts are required fields or,
.. i18n:    if you are diligent, when you set up Partners. 
.. i18n:    
.. i18n:    If you configure them correctly at this stage, then fields will be completed automatically and you will
.. i18n:    never know a thing. If you do not configure all this correctly, then you will not be able to save the
.. i18n:    order form until you have corrected the problem or until you manually set the accounts. 
.. i18n:    
.. i18n:    Since this configuration is quite tedious, you would do best by finding a certified Chart of Accounts
.. i18n:    that has already been set up to meet your needs, if you can find one.
..

.. tip:: Mistakes in configuring accounts and properties

   It is easy to make mistakes in configuring accounts and their properties, but the consequences
   are not immediately obvious. You will mostly discover mistakes when trying to make a Purchase or
   Sale Order (see later, for example, :ref:`sect-PO`), where the accounts are required fields or,
   if you are diligent, when you set up Partners. 
   
   If you configure them correctly at this stage, then fields will be completed automatically and you will
   never know a thing. If you do not configure all this correctly, then you will not be able to save the
   order form until you have corrected the problem or until you manually set the accounts. 
   
   Since this configuration is quite tedious, you would do best by finding a certified Chart of Accounts
   that has already been set up to meet your needs, if you can find one.

.. i18n: .. index::
.. i18n:    single: journals; configuring
..

.. index::
   single: journals; configuring

.. i18n: Configuring Journals
.. i18n: --------------------
..

配置账簿
--------------------

.. i18n: You will also need to configure some journals, which are used to record the transactions from one account
.. i18n: to another when invoices are raised and then paid. Create journals from the menu
.. i18n: :menuselection:`Accounting --> Configuration --> 
.. i18n: Financial Accounting --> Journals --> Journals` and then click the :guilabel:`New` button. 
..

You will also need to configure some journals, which are used to record the transactions from one account
to another when invoices are raised and then paid. Create journals from the menu
:menuselection:`Accounting --> Configuration --> 
Financial Accounting --> Journals --> Journals` and then click the :guilabel:`New` button. 

.. i18n: .. table:: Defining Journals
.. i18n: 
.. i18n:    ================ ==== ======== ========================== ================ ===================== ======================
.. i18n:    Journal Name     Code Type     Display Mode               Entry Sequence   Default Debit Account Default Credit Account
.. i18n:    ================ ==== ======== ========================== ================ ===================== ======================
.. i18n:    Purchase Journal PUJ  Purchase Sale/Purchase Journal View Purchase Journal P Purchases           P Purchases
.. i18n:    Sale Journal     SAJ  Sale     Sale/Purchase Journal View Sale Journal     S Sales               S Sales
.. i18n:    Bank Journal     BNK  Cash     Cash Journal View          Account Journal  C Cash                C Cash
.. i18n:    ================ ==== ======== ========================== ================ ===================== ======================
..

.. table:: Defining Journals

   ================ ==== ======== ========================== ================ ===================== ======================
   Journal Name     Code Type     Display Mode               Entry Sequence   Default Debit Account Default Credit Account
   ================ ==== ======== ========================== ================ ===================== ======================
   Purchase Journal PUJ  Purchase Sale/Purchase Journal View Purchase Journal P Purchases           P Purchases
   Sale Journal     SAJ  Sale     Sale/Purchase Journal View Sale Journal     S Sales               S Sales
   Bank Journal     BNK  Cash     Cash Journal View          Account Journal  C Cash                C Cash
   ================ ==== ======== ========================== ================ ===================== ======================

.. i18n: .. tip:: Mistakes in configuring journals
.. i18n: 
.. i18n:    It is easy to make mistakes in configuring the journals, too, and the consequences
.. i18n:    are also not immediately obvious. You will mostly discover mistakes when creating an invoice
.. i18n:    (which happens at different points in the process, depending on your configuration).
.. i18n:    In this example, validating a Purchase Order creates a draft invoice 
.. i18n:    (see later, again for example, :ref:`sect-PO`), where a journal is required. 
.. i18n:    
.. i18n:    As with accounts and properties, if you configure them correctly at this stage, then 
.. i18n:    the fields will be completed automatically and you will never know a thing. 
.. i18n:    If you do not configure all this correctly, then there will be errors with the
.. i18n:    order form or corresponding draft invoice,
.. i18n:    until you have corrected the problem or until you manually set the journal. 
..

.. tip:: Mistakes in configuring journals

   It is easy to make mistakes in configuring the journals, too, and the consequences
   are also not immediately obvious. You will mostly discover mistakes when creating an invoice
   (which happens at different points in the process, depending on your configuration).
   In this example, validating a Purchase Order creates a draft invoice 
   (see later, again for example, :ref:`sect-PO`), where a journal is required. 
   
   As with accounts and properties, if you configure them correctly at this stage, then 
   the fields will be completed automatically and you will never know a thing. 
   If you do not configure all this correctly, then there will be errors with the
   order form or corresponding draft invoice,
   until you have corrected the problem or until you manually set the journal. 

.. i18n: .. _sect-ConfiCo:
.. i18n: 
.. i18n: .. index::
.. i18n:    single: Main Company; configuring
..

.. _sect-ConfiCo:

.. index::
   single: Main Company; configuring

.. i18n: Configuring the Main Company
.. i18n: ----------------------------
..

配置公司信息
----------------------------

.. i18n: In case you had chosen to :guilabel:`Skip Configuration Wizards` when you first created the database, you may configure your company information in the following manner.
.. i18n: Start configuring your database by renaming the :guilabel:`Main Company` from its default of \
.. i18n: ``OpenERP S.A.``\   to the name of your own company or (in this case) another example company. When you
.. i18n: print standard documents such as quotations, orders and invoices you will find this configuration
.. i18n: information used in the document headers and footers.
..

In case you had chosen to :guilabel:`Skip Configuration Wizards` when you first created the database, you may configure your company information in the following manner.
Start configuring your database by renaming the :guilabel:`Main Company` from its default of \
``OpenERP S.A.``\   to the name of your own company or (in this case) another example company. When you
print standard documents such as quotations, orders and invoices you will find this configuration
information used in the document headers and footers.

.. i18n: To do this, click :menuselection:`Sales --> Address Book --> Customers` and click the name of the only company
.. i18n: there, which is \ ``OpenERP S.A.`` \. This gives you a read-only form view of the company, so
.. i18n: make it editable by clicking the :guilabel:`Edit` button to the upper left of the form.
..

To do this, click :menuselection:`Sales --> Address Book --> Customers` and click the name of the only company
there, which is \ ``OpenERP S.A.`` \. This gives you a read-only form view of the company, so
make it editable by clicking the :guilabel:`Edit` button to the upper left of the form.

.. i18n: .. tip:: Editable form in the web interface
.. i18n: 
.. i18n: 	When toggling from the list view to the form view of an item, you can generally click its name in
.. i18n: 	the list view to show a non-editable view, or the pencil icon by the left-hand edge of the line to
.. i18n: 	open it in an editable view. You can toggle between editable and non-editable once you are in form
.. i18n: 	view.
..

.. tip:: Editable form in the web interface

	When toggling from the list view to the form view of an item, you can generally click its name in
	the list view to show a non-editable view, or the pencil icon by the left-hand edge of the line to
	open it in an editable view. You can toggle between editable and non-editable once you are in form
	view.

.. i18n: Change the following:
..

Change the following:

.. i18n: *  :guilabel:`Name` : \ ``Ambitious Plumbing Enterprises``\  ,
.. i18n: 
.. i18n: *  :guilabel:`Contact Name` : \ ``George Turnbull``\  .
..

*  :guilabel:`Name` : \ ``Ambitious Plumbing Enterprises``\  ,

*  :guilabel:`Contact Name` : \ ``George Turnbull``\  .

.. i18n: Before you save this, look at the partner's accounting setup by clicking the tab
.. i18n: :guilabel:`Accounting`. The fields :guilabel:`Account Receivable` and :guilabel:`Account Payable`
.. i18n: have account values in them that were taken from the account properties you just created.
.. i18n: You do not have to accept those values: you can enter any suitable account you like at this stage, 
.. i18n: although OpenERP constrains the selection to ones that make accounting sense.
..

Before you save this, look at the partner's accounting setup by clicking the tab
:guilabel:`Accounting`. The fields :guilabel:`Account Receivable` and :guilabel:`Account Payable`
have account values in them that were taken from the account properties you just created.
You do not have to accept those values: you can enter any suitable account you like at this stage, 
although OpenERP constrains the selection to ones that make accounting sense.

.. i18n: Back at the first tab, :guilabel:`General`, change any other fields you like, 
.. i18n: such as the address and phone numbers, then :guilabel:`Save`. This
.. i18n: changes one Contact for the Partner, which is sufficient for the example.
..

Back at the first tab, :guilabel:`General`, change any other fields you like, 
such as the address and phone numbers, then :guilabel:`Save`. This
changes one Contact for the Partner, which is sufficient for the example.

.. i18n: From the :guilabel:`MAIN MENU`, click :menuselection:`Administration --> Companies --> Companies`
.. i18n: and edit the only entry there:
..

From the :guilabel:`MAIN MENU`, click :menuselection:`Administration --> Companies --> Companies`
and edit the only entry there:

.. i18n: *  :guilabel:`Company Name` : \ ``AmbiPlum``\  ,
.. i18n: 
.. i18n: *  :guilabel:`Partner` : should already show \ ``Ambitious Plumbing Enterprises``\  ,
.. i18n: 
.. i18n: *  :guilabel:`Report Header` : \ ``Ambitious Plumbing``\  ,
.. i18n: 
.. i18n: *  :guilabel:`Report Footer 1` : \ ``Best Plumbing Services, Great Prices``\  ,
.. i18n: 
.. i18n: *  :guilabel:`Report Footer 2` : \ ``Ambitious – our Registered Company Details``\  .
..

*  :guilabel:`Company Name` : \ ``AmbiPlum``\  ,

*  :guilabel:`Partner` : should already show \ ``Ambitious Plumbing Enterprises``\  ,

*  :guilabel:`Report Header` : \ ``Ambitious Plumbing``\  ,

*  :guilabel:`Report Footer 1` : \ ``Best Plumbing Services, Great Prices``\  ,

*  :guilabel:`Report Footer 2` : \ ``Ambitious – our Registered Company Details``\  .

.. i18n: Figure :ref:`fig-oech03co` shows the effect of this.
.. i18n: You can also change various other company-wide parameters for reports and scheduling in the other tabs,
.. i18n: and you can upload a company logo of a specific size for the reports. Click :guilabel:`Save` to store this.
..

Figure :ref:`fig-oech03co` shows the effect of this.
You can also change various other company-wide parameters for reports and scheduling in the other tabs,
and you can upload a company logo of a specific size for the reports. Click :guilabel:`Save` to store this.

.. i18n: .. _fig-oech03co:
.. i18n: 
.. i18n: .. figure::  images/openerp_ch03_co.png
.. i18n:    :align: center
.. i18n:    :scale: 75
.. i18n: 
.. i18n:    *Changing company details*
..

.. _fig-oech03co:

.. figure::  images/openerp_ch03_co.png
   :align: center
   :scale: 75

   *Changing company details*

.. i18n: You can leave the currency at its default setting of \ ``EUR`` \ for this example. Or you can
.. i18n: change it in this Company and the two default Pricelists (:menuselection:`Sales --> Configuration --> Pricelists --> Pricelists`) if you feel compelled to do that.
..

You can leave the currency at its default setting of \ ``EUR`` \ for this example. Or you can
change it in this Company and the two default Pricelists (:menuselection:`Sales --> Configuration --> Pricelists --> Pricelists`) if you feel compelled to do that.

.. i18n: .. note::  Currency
.. i18n: 
.. i18n: 	The examples in this book are in USD and EUR. You, the reader, could use your home currency
.. i18n: 	(perhaps CAD, CNY, GBP, or Rs) in their place.
..

.. note::  Currency

	The examples in this book are in USD and EUR. You, the reader, could use your home currency
	(perhaps CAD, CNY, GBP, or Rs) in their place.

.. i18n: .. index::
.. i18n:    single: partner
.. i18n:    pair: partner; category
.. i18n:    pair: partner; contact
..

.. index::
   single: partner
   pair: partner; category
   pair: partner; contact

.. i18n: Creating Partner Categories, Partners and their Contacts
.. i18n: --------------------------------------------------------
..

新建业务伙伴,伙伴分类及伙伴联系人
--------------------------------------------------------

.. i18n: You will now create a suppliers category and a customers category. Partner categories are useful for
.. i18n: organizing groups of partners but have no special behavior that affects partners, so you can assign
.. i18n: them as you like. Then you will define one supplier and one customer, with a contact for each.
..

You will now create a suppliers category and a customers category. Partner categories are useful for
organizing groups of partners but have no special behavior that affects partners, so you can assign
them as you like. Then you will define one supplier and one customer, with a contact for each.

.. i18n: To do this, use the menu :menuselection:`Sales --> Configuration --> Address Book --> Partner Categories` and
.. i18n: click :guilabel:`New` to open a new form for defining :guilabel:`Partner Categories`.
.. i18n: Define the two categories that follow by just entering their :guilabel:`Category Name` and saving
.. i18n: them:
..

To do this, use the menu :menuselection:`Sales --> Configuration --> Address Book --> Partner Categories` and
click :guilabel:`New` to open a new form for defining :guilabel:`Partner Categories`.
Define the two categories that follow by just entering their :guilabel:`Category Name` and saving
them:

.. i18n: * \ ``Suppliers``\  ,
.. i18n: 
.. i18n: * \ ``Customers``\  .
..

* \ ``Suppliers``\  ,

* \ ``Customers``\  .

.. i18n: Then create two partners from the menu :menuselection:`Sales --> Address Book --> Customers`. Click on the
.. i18n: :guilabel:`New` button to open a blank form and then add the following data for the first partner
.. i18n: first:
..

Then create two partners from the menu :menuselection:`Sales --> Address Book --> Customers`. Click on the
:guilabel:`New` button to open a blank form and then add the following data for the first partner
first:

.. i18n: * :guilabel:`Name` : \ ``Plumbing Component Suppliers``\  ,
.. i18n: 
.. i18n: * :guilabel:`Customer` checkbox : \ ``unchecked``\  ,
.. i18n: 
.. i18n: * :guilabel:`Supplier` checkbox : \ ``checked``\  ,
.. i18n: 
.. i18n: * :guilabel:`Contact Name` : \ ``Jean Poolley``\  ,
.. i18n: 
.. i18n: * :guilabel:`Address Type` : \ ``Default``\  ,
.. i18n: 
.. i18n: * add \ ``Suppliers``\   to the :guilabel:`Partner Categories` field by selecting it from the Search Partner Categories list,
.. i18n: 
.. i18n: * then save the partner by clicking the :guilabel:`Save` button. 
..

* :guilabel:`Name` : \ ``Plumbing Component Suppliers``\  ,

* :guilabel:`Customer` checkbox : \ ``unchecked``\  ,

* :guilabel:`Supplier` checkbox : \ ``checked``\  ,

* :guilabel:`Contact Name` : \ ``Jean Poolley``\  ,

* :guilabel:`Address Type` : \ ``Default``\  ,

* add \ ``Suppliers``\   to the :guilabel:`Partner Categories` field by selecting it from the Search Partner Categories list,

* then save the partner by clicking the :guilabel:`Save` button. 

.. i18n: Figure :ref:`fig-oech03part` shows the result. 
..

Figure :ref:`fig-oech03part` shows the result. 

.. i18n: .. _fig-oech03part:
.. i18n: 
.. i18n: .. figure::  images/openerp_03_part.png
.. i18n:    :align: center
.. i18n:    :scale: 80
.. i18n: 
.. i18n:    *New Partner Form*
..

.. _fig-oech03part:

.. figure::  images/openerp_03_part.png
   :align: center
   :scale: 80

   *New Partner Form*

.. i18n: .. note:: Contact Types
.. i18n: 
.. i18n: 	If you have recorded several contacts for the same partner you can specify which contact is used for
.. i18n: 	various documents by specifying the Address Type.
.. i18n: 
.. i18n: 	For example the delivery address can differ from the invoice address for a partner. If the Address
.. i18n: 	Types are correctly assigned, then OpenERP can automatically select the appropriate address
.. i18n: 	during the creation of the document – an invoice is addressed to the contact that has been assigned
.. i18n: 	the Address Type of Invoice, otherwise to the Default address.
..

.. note:: Contact Types

	If you have recorded several contacts for the same partner you can specify which contact is used for
	various documents by specifying the Address Type.

	For example the delivery address can differ from the invoice address for a partner. If the Address
	Types are correctly assigned, then OpenERP can automatically select the appropriate address
	during the creation of the document – an invoice is addressed to the contact that has been assigned
	the Address Type of Invoice, otherwise to the Default address.

.. i18n: For the second partner, proceed just as you did for the first, with the following data:
..

For the second partner, proceed just as you did for the first, with the following data:

.. i18n: * :guilabel:`Name` : \ ``Smith and Offspring``\ ,
.. i18n: 
.. i18n: * :guilabel:`Customer` checkbox : \ ``checked``\ ,
.. i18n: 
.. i18n: * :guilabel:`Supplier` checkbox : \ ``unchecked``\ ,
.. i18n: 
.. i18n: * :guilabel:`Contact Name` : \ ``Stephen Smith``\ ,
.. i18n: 
.. i18n: * :guilabel:`Address Type` : \ ``Default``\ ,
.. i18n: 
.. i18n: * add \ ``Customers``\   in the :guilabel:`Categories` field,
.. i18n: 
.. i18n: * :guilabel:`Save` the form.
..

* :guilabel:`Name` : \ ``Smith and Offspring``\ ,

* :guilabel:`Customer` checkbox : \ ``checked``\ ,

* :guilabel:`Supplier` checkbox : \ ``unchecked``\ ,

* :guilabel:`Contact Name` : \ ``Stephen Smith``\ ,

* :guilabel:`Address Type` : \ ``Default``\ ,

* add \ ``Customers``\   in the :guilabel:`Categories` field,

* :guilabel:`Save` the form.

.. i18n: To check
.. i18n: your work, you can go to the menu :menuselection:`Sales --> Configuration --> Address Book --> Partner Categories`
.. i18n: and click on each category in turn to see the companies in the category.
..

To check
your work, you can go to the menu :menuselection:`Sales --> Configuration --> Address Book --> Partner Categories`
and click on each category in turn to see the companies in the category.

.. i18n: .. note:: Multiple Partner Categories
.. i18n: 
.. i18n: 	If this partner was also a supplier, then you would add ``Suppliers`` to the categories as well, but there is
.. i18n: 	no need to do so in this example. You can assign a partner to multiple categories at all levels of
.. i18n: 	the hierarchy.
..

.. note:: Multiple Partner Categories

	If this partner was also a supplier, then you would add ``Suppliers`` to the categories as well, but there is
	no need to do so in this example. You can assign a partner to multiple categories at all levels of
	the hierarchy.

.. i18n: .. index::
.. i18n:    single: product
.. i18n:    pair: product; category
..

.. index::
   single: product
   pair: product; category

.. i18n: .. _log-product:
.. i18n: 
.. i18n: Creating Products and their Categories
.. i18n: --------------------------------------
..

.. _log-product:

新建商品信息及其分类
--------------------------------------

.. i18n: Unlike partner categories and their assigned partners, product categories do have an effect on the
.. i18n: products assigned to them – and a product may belong to only one category. Under the main menu link
.. i18n: :menuselection:`Warehouse` or :menuselection:`Sale`, select the menu
.. i18n: :menuselection:`Configuration --> Products --> Products Categories` and click :guilabel:`New` to get
.. i18n: an empty form for defining a product category.
..

Unlike partner categories and their assigned partners, product categories do have an effect on the
products assigned to them – and a product may belong to only one category. Under the main menu link
:menuselection:`Warehouse` or :menuselection:`Sale`, select the menu
:menuselection:`Configuration --> Products --> Products Categories` and click :guilabel:`New` to get
an empty form for defining a product category.

.. i18n: Enter \ ``Radiators``\   in the :guilabel:`Name` field. You will see that other fields, specifically those
.. i18n: in the :guilabel:`Accounting Properties` section, have been automatically filled in with values of
.. i18n: accounts and journals. These are the values that will affect products – equivalent fields in a
.. i18n: product will take on these values if they, too, are blank when their form is saved.
.. i18n: Click :guilabel:`Save`.
..

Enter \ ``Radiators``\   in the :guilabel:`Name` field. You will see that other fields, specifically those
in the :guilabel:`Accounting Properties` section, have been automatically filled in with values of
accounts and journals. These are the values that will affect products – equivalent fields in a
product will take on these values if they, too, are blank when their form is saved.
Click :guilabel:`Save`.

.. i18n: .. note:: Property Fields
.. i18n: 
.. i18n: 	Properties have a rather unusual behavior. They are defined by parameters in the menus in 
.. i18n: 	:menuselection:`Administration --> Configuration --> Parameters --> Configuration Parameters`,
.. i18n: 	and they update fields only when a form
.. i18n: 	is saved, and only when the fields are empty at the time the form is saved. You can manually
.. i18n: 	override any of these properties as you need.
.. i18n: 
.. i18n: 	Property fields are used all over the OpenERP system and particularly extensively in a multi-
.. i18n: 	company environment. There, property fields in a partner form can be populated with different
.. i18n: 	values depending on the user's company.
.. i18n: 
.. i18n: 	For example, the payment conditions for a partner could differ depending on the company from which
.. i18n: 	it is addressed.
..

.. note:: Property Fields

	Properties have a rather unusual behavior. They are defined by parameters in the menus in 
	:menuselection:`Administration --> Configuration --> Parameters --> Configuration Parameters`,
	and they update fields only when a form
	is saved, and only when the fields are empty at the time the form is saved. You can manually
	override any of these properties as you need.

	Property fields are used all over the OpenERP system and particularly extensively in a multi-
	company environment. There, property fields in a partner form can be populated with different
	values depending on the user's company.

	For example, the payment conditions for a partner could differ depending on the company from which
	it is addressed.

.. i18n: .. note:: UOM
.. i18n: 
.. i18n: 	UOM is an abbreviation for Unit of Measure. OpenERP manages multiple units of measure for each
.. i18n: 	product: you can buy in tons and sell in kgs, for example. The conversion between each category is
.. i18n: 	made automatically (so long as you have set up the conversion rate in the product form first).
..

.. note:: UOM

	UOM is an abbreviation for Unit of Measure. OpenERP manages multiple units of measure for each
	product: you can buy in tons and sell in kgs, for example. The conversion between each category is
	made automatically (so long as you have set up the conversion rate in the product form first).

.. i18n: .. tip::  Managing Double Units of Measure
.. i18n: 
.. i18n: 	The whole management of stock can be carried out with double units of measure (UOM and UOS – for
.. i18n: 	Unit of Sale). For example, an agro-food company can stock and sell ham by piece, but buy and value
.. i18n: 	it by weight. There is no direct relationship between these two units, so a weighing operation has to
.. i18n: 	be done.
.. i18n: 
.. i18n: 	This functionality is crucial in the agro-food industry, and can be equally important in
.. i18n: 	fabrication, chemicals and many other industries.
..

.. tip::  Managing Double Units of Measure

	The whole management of stock can be carried out with double units of measure (UOM and UOS – for
	Unit of Sale). For example, an agro-food company can stock and sell ham by piece, but buy and value
	it by weight. There is no direct relationship between these two units, so a weighing operation has to
	be done.

	This functionality is crucial in the agro-food industry, and can be equally important in
	fabrication, chemicals and many other industries.

.. i18n: Now create a new product through the :menuselection:`Warehouse` or :menuselection:`Sale` menu:
..

Now create a new product through the :menuselection:`Warehouse` or :menuselection:`Sale` menu:

.. i18n: #.	Go to :menuselection:`Product --> Products` and click :guilabel:`New`.
.. i18n: 
.. i18n: #.	Create a product – type \ ``Titanium Alloy Radiator``\  in the :guilabel:`Name` field.
.. i18n: 
.. i18n: #.	Click the :guilabel:`Search` icon to the right of the :guilabel:`Category` field to select the
.. i18n: 	:guilabel:`Radiators` category.
.. i18n: 
.. i18n: #.	The :guilabel:`Product Type` field should be assigned as \ ``Stockable Product``\.
.. i18n: 	The fields :guilabel:`Procurement Method`, :guilabel:`Supply method`, :guilabel:`Default Unit Of Measure`, 
.. i18n: 	and :guilabel:`Purchase Unit Of Measure` should
.. i18n: 	also stay at their default values.
.. i18n: 
.. i18n: #.	Enter \ ``57.50``\  into the :guilabel:`Cost Price`
.. i18n: 	field and \ ``132.50``\  into the :guilabel:`Sale Price` field.
..

#.	Go to :menuselection:`Product --> Products` and click :guilabel:`New`.

#.	Create a product – type \ ``Titanium Alloy Radiator``\  in the :guilabel:`Name` field.

#.	Click the :guilabel:`Search` icon to the right of the :guilabel:`Category` field to select the
	:guilabel:`Radiators` category.

#.	The :guilabel:`Product Type` field should be assigned as \ ``Stockable Product``\.
	The fields :guilabel:`Procurement Method`, :guilabel:`Supply method`, :guilabel:`Default Unit Of Measure`, 
	and :guilabel:`Purchase Unit Of Measure` should
	also stay at their default values.

#.	Enter \ ``57.50``\  into the :guilabel:`Cost Price`
	field and \ ``132.50``\  into the :guilabel:`Sale Price` field.

.. i18n: 	.. figure:: images/product.png
.. i18n: 	   :align: center
.. i18n: 	   :scale: 75
.. i18n:            
.. i18n: 	   *Product Form*
..

	.. figure:: images/product.png
	   :align: center
	   :scale: 75
           
	   *Product Form*

.. i18n: #.	Click the :guilabel:`Accounting` tab, then click :guilabel:`Save` and observe that
.. i18n: 	:guilabel:`Accounting Properties` here remain empty. When product
.. i18n: 	transactions occur, the Income and Expense accounts that you have just defined in the Product
.. i18n: 	Category are used by the Product unless an account is specified here, directly in the product, to
.. i18n: 	override that.
.. i18n: 
.. i18n: #.	Once the product is saved, it changes to a non-editable state. If you had entered data
.. i18n: 	incorrectly or left a required field blank, an error message would pop-up, the form would have
.. i18n: 	stayed editable and you would need to
.. i18n: 	click from tab to tab to find a field colored red that would have
.. i18n: 	to be correctly filled in.
..

#.	Click the :guilabel:`Accounting` tab, then click :guilabel:`Save` and observe that
	:guilabel:`Accounting Properties` here remain empty. When product
	transactions occur, the Income and Expense accounts that you have just defined in the Product
	Category are used by the Product unless an account is specified here, directly in the product, to
	override that.

#.	Once the product is saved, it changes to a non-editable state. If you had entered data
	incorrectly or left a required field blank, an error message would pop-up, the form would have
	stayed editable and you would need to
	click from tab to tab to find a field colored red that would have
	to be correctly filled in.

.. i18n: .. index::
.. i18n:    single: stock; location
..

.. index::
   single: stock; location

.. i18n: .. _log-loc:
.. i18n: 
.. i18n: Stock Locations
.. i18n: ---------------
..

.. _log-loc:

配置库位信息
---------------

.. i18n: Click :menuselection:`Warehouse --> Inventory Control --> Location Structure` to see the hierarchy of stock
.. i18n: locations. These locations have been defined by the minimal default data loaded when the database
.. i18n: was created. You will use this default structure in this example.
..

Click :menuselection:`Warehouse --> Inventory Control --> Location Structure` to see the hierarchy of stock
locations. These locations have been defined by the minimal default data loaded when the database
was created. You will use this default structure in this example.

.. i18n: OpenERP has three predefined top-level location types , ``Physical Locations`` and ``Partner Locations``
.. i18n: that act as their names suggest, and ``Virtual Locations`` that are used by OpenERP for its own purposes.
..

OpenERP has three predefined top-level location types , ``Physical Locations`` and ``Partner Locations``
that act as their names suggest, and ``Virtual Locations`` that are used by OpenERP for its own purposes.

.. i18n: #.	From the :guilabel:`Main Menu` click on :menuselection:`Warehouse --> Configuration -->
.. i18n: 	Warehouse Management --> Locations` to reach a list view of the locations (not the tree view).
.. i18n: 
.. i18n: #.	Click on the name of a location, such as \ ``Physical Locations/OpenERP S.A.`` \ to open a
.. i18n: 	descriptive form view. Each
.. i18n: 	location has a :guilabel:`Location Type` and a :guilabel:`Parent Location` that defines the hierarchical structure.
.. i18n: 	While you are here you should change 
.. i18n: 	the location's name to ``Ambitious Plumbing Enterprises`` , since it was named before you changed the
.. i18n: 	company name.
.. i18n: 
.. i18n: #.	From the :menuselection:`Main Menu` click :menuselection:`Warehouse --> Configuration
.. i18n: 	Warehouse Management --> Warehouses` to view a list of warehouses. There is only the one at the moment, which
.. i18n: 	should also be renamed from ``OpenERP S.A.`` to ``Ambitious Plumbing Enterprises`` .
..

#.	From the :guilabel:`Main Menu` click on :menuselection:`Warehouse --> Configuration -->
	Warehouse Management --> Locations` to reach a list view of the locations (not the tree view).

#.	Click on the name of a location, such as \ ``Physical Locations/OpenERP S.A.`` \ to open a
	descriptive form view. Each
	location has a :guilabel:`Location Type` and a :guilabel:`Parent Location` that defines the hierarchical structure.
	While you are here you should change 
	the location's name to ``Ambitious Plumbing Enterprises`` , since it was named before you changed the
	company name.

#.	From the :menuselection:`Main Menu` click :menuselection:`Warehouse --> Configuration
	Warehouse Management --> Warehouses` to view a list of warehouses. There is only the one at the moment, which
	should also be renamed from ``OpenERP S.A.`` to ``Ambitious Plumbing Enterprises`` .

.. i18n: A Warehouse contains an input location, a stock location and an output location for sold products.
.. i18n: You can associate a warehouse with a partner to give the warehouse an address. That does not have to
.. i18n: be your own company (although it can be); you can easily specify another partner who may be holding
.. i18n: stock on your behalf.
..

A Warehouse contains an input location, a stock location and an output location for sold products.
You can associate a warehouse with a partner to give the warehouse an address. That does not have to
be your own company (although it can be); you can easily specify another partner who may be holding
stock on your behalf.

.. i18n: .. index::
.. i18n:    single: location structure
..

.. index::
   single: location structure

.. i18n: .. note:: Location Structure
.. i18n: 
.. i18n: 	Each warehouse is composed of three locations :guilabel:`Location Input`, :guilabel:`Location Output`, and 
.. i18n: 	:guilabel:`Location Stock`. Your available stock is given by the contents of the :guilabel:`Location Stock` 
.. i18n: 	and its child locations.
.. i18n: 
.. i18n: 	So the :guilabel:`Location Input` can be placed as a child of the :guilabel:`Location Stock`, which means 
.. i18n: 	that when :guilabel:`Location Stock` is interrogated for product quantities, it also takes account of the 
.. i18n: 	contents of the :guilabel:`Location Input`. :guilabel:`Location Input` could be used as a goods-in QC location.
.. i18n: 	The :guilabel:`Location Output` must never be placed as a child of :guilabel:`Location Stock`, 
.. i18n: 	since items in :guilabel:`Location Output`, which can be considered to be
.. i18n: 	packed ready for customer shipment, should not be thought of as available for sale elsewhere.
..

.. note:: Location Structure

	Each warehouse is composed of three locations :guilabel:`Location Input`, :guilabel:`Location Output`, and 
	:guilabel:`Location Stock`. Your available stock is given by the contents of the :guilabel:`Location Stock` 
	and its child locations.

	So the :guilabel:`Location Input` can be placed as a child of the :guilabel:`Location Stock`, which means 
	that when :guilabel:`Location Stock` is interrogated for product quantities, it also takes account of the 
	contents of the :guilabel:`Location Input`. :guilabel:`Location Input` could be used as a goods-in QC location.
	The :guilabel:`Location Output` must never be placed as a child of :guilabel:`Location Stock`, 
	since items in :guilabel:`Location Output`, which can be considered to be
	packed ready for customer shipment, should not be thought of as available for sale elsewhere.

.. i18n: .. index::
.. i18n:    single: account; chart
.. i18n:    single: chart of accounts
..

.. index::
   single: account; chart
   single: chart of accounts

.. i18n: Setting up a Chart of Accounts
.. i18n: ------------------------------
..

设置会计科目表
------------------------------

.. i18n: You can set up a chart of accounts during the creation of a database, but for this exercise you will
.. i18n: start with the minimal chart that you created (just a handful of required
.. i18n: accounts without hierarchy, tax or subtotals).
..

You can set up a chart of accounts during the creation of a database, but for this exercise you will
start with the minimal chart that you created (just a handful of required
accounts without hierarchy, tax or subtotals).

.. i18n: A number of account charts have been predefined for OpenERP, some of which meet the needs of
.. i18n: national authorities (the number of those created for OpenERP is growing as various contributors
.. i18n: create and freely publish them). You can take one of those without changing it if it is suitable, or
.. i18n: you can take anything as your starting point and design a complete chart of accounts to meet your
.. i18n: exact needs, including accounts for inventory, asset depreciation, equity and taxation.
..

A number of account charts have been predefined for OpenERP, some of which meet the needs of
national authorities (the number of those created for OpenERP is growing as various contributors
create and freely publish them). You can take one of those without changing it if it is suitable, or
you can take anything as your starting point and design a complete chart of accounts to meet your
exact needs, including accounts for inventory, asset depreciation, equity and taxation.

.. i18n: You can also run multiple charts of accounts in parallel – so you can put all of your transaction
.. i18n: accounts into several charts, with different arrangements for taxation and depreciation, aggregated
.. i18n: differently for various needs.
..

You can also run multiple charts of accounts in parallel – so you can put all of your transaction
accounts into several charts, with different arrangements for taxation and depreciation, aggregated
differently for various needs.

.. i18n: Before you can use any chart of accounts for anything, you need to specify a Fiscal Year. This
.. i18n: defines the different time periods available for accounting transactions. An initial Fiscal Year
.. i18n: was created during the database setup, so you do not need to do any more on this.
.. i18n: You can also create a Fiscal Year manually from :menuselection:`Accounting --> Configuration --> Financial Accounting --> Periods --> Fiscal Years`.
..

Before you can use any chart of accounts for anything, you need to specify a Fiscal Year. This
defines the different time periods available for accounting transactions. An initial Fiscal Year
was created during the database setup, so you do not need to do any more on this.
You can also create a Fiscal Year manually from :menuselection:`Accounting --> Configuration --> Financial Accounting --> Periods --> Fiscal Years`.

.. i18n: Click :menuselection:`Accounting --> Charts --> Charts of Accounts` to open a :guilabel:`Chart of Accounts`
.. i18n: form where you define exactly what you want to see.
.. i18n: Click :guilabel:`Open Charts` to accept the defaults and see a
.. i18n: hierarchical structure of the accounts.
..

Click :menuselection:`Accounting --> Charts --> Charts of Accounts` to open a :guilabel:`Chart of Accounts`
form where you define exactly what you want to see.
Click :guilabel:`Open Charts` to accept the defaults and see a
hierarchical structure of the accounts.

.. i18n: .. index::
.. i18n:    pair: database; backup
..

.. index::
   pair: database; backup

.. i18n: Make a Backup of the Database
.. i18n: -----------------------------
..

备份数据库帐套
-----------------------------

.. i18n: If you know the super-administrator password, make a backup of your database using the procedure
.. i18n: described in :ref:`sect-dbmanage`. Then restore it to a new database: \ ``testing``\  .
..

If you know the super-administrator password, make a backup of your database using the procedure
described in :ref:`sect-dbmanage`. Then restore it to a new database: \ ``testing``\  .

.. i18n: This operation enables you to test the new configuration on \ ``testing``\   so that you can be sure
.. i18n: everything works as designed. Then if the tests are successful, you can make a new database from \
.. i18n: ``openerp_ch03``\  , perhaps called \ ``live``\ or  \ ``production``\ , for your real work.
..

This operation enables you to test the new configuration on \ ``testing``\   so that you can be sure
everything works as designed. Then if the tests are successful, you can make a new database from \
``openerp_ch03``\  , perhaps called \ ``live``\ or  \ ``production``\ , for your real work.

.. i18n: From here on, connect to this new \ ``testing``\   database logged in as \ ``admin``\   if you can.
.. i18n: If you have to make corrections, do that on \ ``openerp_ch03``\   and copy it to a new \
.. i18n: ``testing``\   database to continue checking it.
..

From here on, connect to this new \ ``testing``\   database logged in as \ ``admin``\   if you can.
If you have to make corrections, do that on \ ``openerp_ch03``\   and copy it to a new \
``testing``\   database to continue checking it.

.. i18n: Or you can just continue working with the \ ``openerp_ch03``\   database to get through this
.. i18n: chapter. You can recreate \ ``openerp_ch03``\   quite quickly if something goes wrong and you cannot
.. i18n: recover from it but, again, you would need to know your super-administrator password for that.
..

Or you can just continue working with the \ ``openerp_ch03``\   database to get through this
chapter. You can recreate \ ``openerp_ch03``\   quite quickly if something goes wrong and you cannot
recover from it but, again, you would need to know your super-administrator password for that.

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
