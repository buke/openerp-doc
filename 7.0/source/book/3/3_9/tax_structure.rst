
.. _tax:

Managing your Tax Structure
===========================

This section deals with statutory taxes and accounts which are legally required from the company:

* the taxation structure provided by Open ERP,

.. index:: tax

You can attach taxes to transactions so that you can:

* add taxes to the amount you pay or receive,

* report on the taxes in various categories that you should pay the tax authorities,

* track taxes in your general accounts,

* manage the payment and refund of taxes using the same mechanisms OpenERP uses for other monetary transactions.

Since the detailed tax structure is a mechanism for carrying out governments' policies, and the collection of taxes so critical to their authorities, tax requirements and reporting can be complex. OpenERP has a flexible mechanism for handling taxation that can be configured to meet the requirements of many tax jurisdictions.

The taxation mechanism can also be used to handle other tax-like financial transactions, such as royalties to authors based on the value of transactions through an account.

From the menu :menuselection:`Accounting --> Configuration --> Financial Accounting --> Taxes` you can define your tax structure. Note that when you use a predefined (localised) chart of accounts, taxes will be configured as well in most cases.

OpenERP's tax system runs around three major concepts:

* :guilabel:`Tax Code` (or :guilabel:`Tax Case`), used for tax reporting, can be set up in a hierarchical
  structure so that multiple codes can be formed into trees in the same way as a ``Chart of Accounts``. The Tax Codes structure is used to define your VAT return; it can be numeric and alphanumeric. You can define tax codes from the menu :menuselection: `Accounting --> Configuration --> Financial Accounting --> Taxes --> Tax Codes`.

* :guilabel:`Taxes`, the basic tax object that contains the rules for calculating tax on the transaction it is attached to, linked to the General Accounts and to the Tax Codes. A tax can contain multiple child taxes and base its calculation on those taxes rather than on the base transaction, providing considerable flexibility.

* the :guilabel:`General Accounts`, which record the taxes owing and paid. Since the general accounts are discussed elsewhere in this part of the book and are not tax-specific, they will not be detailed in this section.

You can attach zero or more :guilabel:`Purchase Taxes` and :guilabel:`Sale Taxes` items to products, so that you can account separately for purchase and sales taxes (or Input and Output VAT – where VAT is Value Added Tax). Because you can attach more than one tax, you can handle a VAT or Sales Tax separately from an Eco Tax on the same product.

To create a new :guilabel:`Tax Code`, use the menu :menuselection:`Accounting --> Configuration --> Financial Accounting --> Taxes --> Tax Codes`. You should define the following fields:

.. figure::  images/account_def_tax_code_form.png
   :scale: 75
   :align: center

   *Tax Code*

*  :guilabel:`Tax Case Name`: a unique name required to identify the tax case, usually taken from your VAT return,

*  :guilabel:`Case Code`: an optional short code for the case,

*  :guilabel:`Parent Code`: a link to a parent Tax Code to create a tree structure which can be displayed from the menu :menuselection:`Accounting --> Charts --> Cgart of Taxes`,

*  :guilabel:`Not Printable in Invoice`: a checkbox allowing you to indicate that any taxes linked to the tax code concerned should not be printed on the invoice,

*  :guilabel:`Coefficient for parent`: choose ``1.00`` to add the total to the parent account or ``-1.00`` to subtract it,

*  :guilabel:`Description`: a free text field for documentation purposes.

You can also see two read-only fields:

*  :guilabel:`Period Sum`: a single figure showing the total accumulated on this case for the current financial period.

*  :guilabel:`Year Sum`: a single figure showing the total accumulated on this case for the financial year.

You will probably need to create two tax codes for each different tax rate that you have to define, one for the tax itself and one for the invoice amount (the so-called base code) the tax is computed from. And you will create tax codes that you will not link to any tax objects (similar to General Account \ ``View``\   types) just to organise the tree (or hierarchical) structure.

To have a look at the structure you have constructed, you can use the menu :menuselection:`Accounting --> Charts --> Chart of Taxes`.
This tree view reflects the structure of the :guilabel:`Tax Codes` and shows the current tax situation for the selected period, or for the complete financial year.

The :guilabel:`Taxes` defined are used to compute taxes on the transactions they are attached to, and they are linked to the corresponding General Accounts (usually VAT accounts) and to Tax Codes, both for the base amount and the tax amount.

To create a new Tax, use the menu :menuselection:`Accounting --> Configuration --> Financial Accounting --> Taxes --> Taxes`.

.. figure::  images/account_define_tax_form.png
   :scale: 75
   :align: center

   *Defining Taxes*

You define the following fields:

*  :guilabel:`Tax Name`: a unique name required for this tax (such as \ ``21% Purchase VAT``\  ),

*  :guilabel:`Tax Code`: an optional code for this tax (such as \ ``VAT IN IC``\  ),

*  :guilabel:`Tax Application`: defines whether the tax is applicable to ``Sale``, ``Purchase`` or ``All`` transactions,

*  :guilabel:`Tax Included in Price`: when checked, the price shown in the product or invoice is inclusive of this tax,

*  :guilabel:`Tax Type`: a required field indicating how tax should be calculated: ``Percentage``,
   ``Fixed Amount``, ``None``, ``Balance`` or ``Python Code``, (the latter is found in the :guilabel:`Compute Code`
   field in the :guilabel:`Special Computation` tab),

*  :guilabel:`Amount`: a required field whose meaning depends on the Tax Type, being a multiplier of the base amount when the :guilabel:`Tax
   Type` is \ ``Percentage``\ and a fixed amount added to the base amount when the :guilabel:`Tax Type` is \ ``Fixed Amount``\,

*  :guilabel:`Invoice Tax Account`: a General Account used to record invoiced tax amounts, which may be the same for several taxes or split according to percentage so that one tax is allocated to one account,

*  :guilabel:`Refund Tax Account`: a General Account used to record invoiced tax refunds, which may be the same as the Invoice Tax Account or, in some tax jurisdictions, has to be separated,

*  :guilabel:`Tax on Children`: when checked, the tax calculation is applied to the output from other tax calculations specified in the :guilabel:`Child Tax Accounts` field (so you can have taxes on taxes), otherwise the calculation is applied to the base amount of the transaction,

*  :guilabel:`Include in base amount`: when checked, the tax is added to the base amount and not shown separately, such as Eco taxes,

*  :guilabel:`Child Tax Accounts`: other taxes that can be used to supply the figure for taxation.

.. tip:: Using Child Taxes

    You can use child taxes when you have a complex tax situation requiring several tax codes to be used.

The fields above apply the taxes that you specify and record them in the general accounts, but do not provide you with the information that your tax authorities might need. Use the :guilabel:`Tax Definition` tab, parts Tax Declaration: Invoices and Credit Notes to define to which tax codes the tax should be assigned:

*  :guilabel:`Account Base Code`: tax code to record the invoiced amount (exclusive of taxes) the tax is calculated on,

*  :guilabel:`Account Tax Code`: tax code to record the calculated tax amount,

*  :guilabel:`Refund Base Code`: tax code to record the refund amount (exclusive of taxes) the tax is calculated on,

*  :guilabel:`Refund Tax Code`: tax code to record the refund tax amount.

When you have created a tax structure consisting of taxe codes and taxes, you can use the taxes in your various business objects so that transactions can be associated with taxes and tax-like charges, such as Eco Taxes (Recupel and Bebat, for instance).

.. tip:: Retail Customers

    When you are retailing to end users rather than selling to a business,
    you may want to (or be required to) show tax-inclusive prices on your invoicing documents rather
    than a tax-exclusive price plus tax.

You can assign multiple taxes to a Product. Assuming you have set up the appropriate taxes, you would use the menu :menuselection:`Sales --> Products --> Products` to open and edit a :guilabel:`Product` definition, then:

* select one or more :guilabel:`Sale Taxes` for any products that you might sell, which may
  include a \ ``Sales Tax``\   or \ ``Output VAT``\  and a \ ``Sales Eco Tax``\  ,

* select one or more :guilabel:`Purchase Taxes` for any products that you might purchase, which may
  include a \ ``Purchase Tax``\   or \ ``Input VAT``\  and a \ ``Purchase Eco Tax``\  .

Generally, when you make a purchase or sales, the taxes assigned to the product are used to calculate the taxes owing or owed.

You can also assign multiple taxes to an account, so that when you transfer money through the account you attract a tax amount. This principle can easily be used when posting purchase invoices for which no products are required.

.. index:: fiscal position

Taxes on Products and Accounts will usually be national taxes. OpenERP is capable of automatically converting national taxes to intracommunal or export taxes through the concept of ``Fiscal Positions``.

Go to the menu :menuselection:`Accounting --> Configuration -_> Financial Accounting --> Taxes --> Fiscal Positions`. You can use the fiscal positions to automatically convert national taxes to the required intracommunal or export taxes, according to the fiscal position specified for the customer or supplier.

Fiscal positions allow you to make a mapping from national taxes to intracommunal or export taxes, or to map your accounts according to these criteria. You can link fiscal positions to your customers and suppliers to ensure automatic and easy VAT conversion when posting entries.
