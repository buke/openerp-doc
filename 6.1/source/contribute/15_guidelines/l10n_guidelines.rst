
.. _l10n-guidelines-link:

=======================
Localization Guidelines
=======================

OpenERP Localization is the process of writing the necessary configuration
or the customizations required to make OpenERP suitable for a general purpose
use in a particular country.

Usually the first step for creating a localization (a.k.a. *l10n*) is to
configure one (or more) Chart(s) of Accounts for the country, with the related
dependencies: Account types, Taxes, etc.

This section gives a few guidelines to assist in the creation of a correct
``l10n_XXX`` module. Once the new l10n module meets the following requirements,
it can be considered for inclusion in the official OpenERP addons, via a
merge proposal process (as described in :ref:`merge_proposals`).


.. tip:: Reference and Examples

        Have a look at the Belgian localization module (``l10n_be``) to get
        started, and for references and examples of how a localization module
        is structured

Contents of a localization module
---------------------------------

In order to have a localization module fully complete, you should ensure
that the following features are present in your module:

 * chart  of account and chart of taxes are mandatory, and must meet the
   guidelines defined below. It's quite possible to put multiple chart
   templates in the same l10n module
 * bank interfaces (import - export)
 * legal reports (no business reports, these could be in a separate module)

Most of the time it's preferable that localization modules do not contain
any Python code that would interfere with the normal behavior of OpenERP's
core (such as inherited/overridden methods).
It's also preferable that they do not reimplement existing
features (e.g. don't add a wizard to generate the chart of account, use the
existing one).

If you think the OpenERP accounting report engine does not fit the legal
requirements for your country, you can make a merge proposal (see :ref:`merge_proposals`)
to improve the core accounting engine.

The next sections provide guidelines for writing the most critical parts of
you l10n modules, in the preferred order of writing.

Generic Guidelines
------------------

 * The module must be named ``l10n_XX`` where XX is the lower case country code,
   taken from http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
 * The l10n_XX module must be hosted on Launchpad, like all OpenERP modules
 * The l10n_XX module must be in a bzr branch which is: 

    * either a branch of ``lp:openobject-addons``
    * or a branch containing this module only (in that case it will need to be added
      to a branch of ``lp:openobject-addons`` in order to make a merge proposal
      to include it in official addons).

 * The module must not define charts but *charts templates*
 * the whole localization must be contained in one and only one module that contains
   legal requirements:

    * chart of accounts
    * tax structure
    * taxes
    * legal statements (reports), if any
    * tax declarations, if any
    * bank import/export features, if any

* Extra features which are not legal requirements but best practices of the country
  can be in separate modules (such as special kind of discounts, some special tax for
  very specific situations, etc.)

Account Types Guidelines (account.account.type)
-----------------------------------------------
Example
 Assets, Liabilities...

Description
 The type contains more information about the account and its specifics.

It's important to pay attention to the deferral method field (named
``close_method``) because it will define the way your accounts will create or not
new entries when opening a new fiscal year. You should choose:

  * ``detail`` for accounts that you want to fully report (even reconciled entries)
  * ``none`` for accounts that you don't want to report at all

Make also sure to give a corresponding value for the new field ``report_type``
(new as of v6) because it's used in balance sheet and P&L report to know in
which column to display it.
You must have at least one account with report_type ``'/'`` (net profit).

Chart of Accounts Guidelines (account.account.template)
-------------------------------------------------------
When creating your chart of account, the principal information you should take
care of is the internal type field (named ``type``), because that field will
be used by OpenERP in many places:

    * ``receivable`` type is used for customer accounts
    * ``payable`` is used for supplier accounts
    * ``view`` is used for non-leaf accounts, used to organize the Chart of
      Accounts in a suitable tree of accounts. OpenERP won't accept any entries
      in ``view`` accounts.
    * ``liquidity`` is used for cash/bank accounts (new as of v6)

For any other accounts (regular ones), you should chose the internal type ``other``.

**Important**: Create templates of charts of accounts, not real charts of accounts,
as the Chart Of Accounts is not global, it's a template that needs to be applied
for each company.

This is also the place where you'll have to make the categorization of your
accounts in the account types (as explained in previous section), via the
``user_type`` field.

Be sure the chart of account has a hierarchical tree structure.


Chart of Tax Codes Guidelines (account.tax.code.template)
---------------------------------------------------------
This object is the same in v5 and v6. The hierarchical structure of the
Chart of Tax Codes should allow you to compute the sum/totals easily
as legally required in your country.

The code of each tax code must respect legal statements.

Here is an example of minimal chart of taxes structure:

    * Tax Balance to Pay

        * Tax Paid

            * Tax Paid 21%
            * Tax Paid 0%

        * Tax Received

            * Tax Received 21%
            * Tax Received 0%

        * Tax Bases

            * Base of Taxable Sales
            * Base Tax Sales 21%
            * Base of Taxable Purchases
            * Base Tax Purchases 21%



The code of each tax code must be the code of the tax section/cell
for this amount in your monthly/yearly legal tax declaration.
Leave the tax code empty if you don't want that code to appear
in the legal tax statement (i.e. for chart structure purposes)


Chart Template Guidelines account.chart.template
------------------------------------------------

Once all above objects are created, you can focus on the Chart Template.
It specifies the required information for generating the proper chart
of account, taxes, etc. when you install this chart via the
Chart of Account installation wizard.

This information includes:

 * chart of account: the ``account_root_id`` field provides the root account
   (with ``parent_id = False``) of your chart
 * chart of tax: the ``tax_code_root_id`` field provides the root tax code
   (with ``parent_id = False``) of your chart
 * parent of the bank/cash accounts: the ``bank_account_view_id`` field selects
   the account (within your chart) under which the bank and cash accounts will be
   created by OpenERP
 * default receivable account: the ``property_account_receivable`` field
   selects the account of your chart that will be used by default as customer
   account for each new partner
 * default payable account: the ``property_account_payable`` field selects
   the account of your chart that will be used by default for the supplier account
   of new partners
 * default expense accounts: the ``property_account_expense_categ`` field selects
   the account of your chart that will be used by default for the expense account
   of each new product
 * default income account: the ``property_account_income_categ`` selects the account
   of your chart that will be used by default for the income account of each new
   product
 * As of v6, a new field has been introduced for Reserve and Profit/Loss Account,
   named ``property_reserve_and_surplus_account``. This fields select the account
   used for transferring amounts from Profit & Loss Report.


Taxes Guidelines (account.tax.template)
---------------------------------------
The only change in that object for v6 is the removal of the ``tax_group``
field which was unused. When testing the taxes, you should make sure that:

 * the accounting entries created for it are correct: right accounts, debit
   and credit
 * the vat amounts that are put in the tax code are correct

This should be verified for both invoices and refunds.

Use the ``chart_template_id`` to link the taxes to the
``account.chart.template`` object defined above.

Check that each tax is linked to an account, a tax code and a base tax code.


Fiscal positions Guidelines (account.fiscal.position.template)
--------------------------------------------------------------
Fiscal position objects stay the same in v6. They're used to
automatically map the default tax/account for a product
according to Partner-specific situations (for invoices, sale
and purchase orders).

In Europe we need at least 3 fiscal positions:

  * national customers
  * foreign customers, within Europe
  * foreign customers, outside Europe

This tax and account mapping will allow you to keep a generic VAT,
let's say 21% (Belgian VAT), and a corresponding income account 
"sales in Belgium"  on your products. When invoicing a
customer that has the fiscal  position 'in Europe', those values
will be automatically changed into (for example) the corresponding
0% VAT and "sales in Europe" account.

Use the ``chart_template_id`` field to link the fiscal positions
to the ``account.chart.template`` object defined above.

Check that each l10n module has at least two fiscal positions
defined:

 * one for the national customers
 * one or more for foreign customers


Modules dependencies Guidelines
-------------------------------
If the module is from an European country, it should
depend on the ``base_vat`` module.

Avoid to put specific features in your l10n_XX module if it's not related
to legal requirement. New accounting features (example: discount on payment, etc.)
must be in another and generic module, not in a l10n_XX  module.
Also, the l10n_XX module should not depend (require) on these other modules,
which may not be included into official addons.

For legal requirements that are specific to your country
(e.g.: mandatory electronic tax declaration system), you can add the features
in the l10n_XX  module directly.


Specific reports Guidelines
---------------------------
If there is any specific report legally required in your country
(such as the VAT report that generates XML files in l10n_be), the
localization module of that country is the right place to put it.

As a reminder: look at l10n_be for examples or for references.
