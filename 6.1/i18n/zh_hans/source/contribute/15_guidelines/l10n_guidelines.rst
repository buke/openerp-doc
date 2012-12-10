.. i18n: .. _l10n-guidelines-link:
.. i18n: 
.. i18n: =======================
.. i18n: Localization Guidelines
.. i18n: =======================
..

.. _l10n-guidelines-link:

=======================
本地化指南
=======================

.. i18n: OpenERP Localization is the process of writing the necessary configuration
.. i18n: or the customizations required to make OpenERP suitable for a general purpose
.. i18n: use in a particular country.
..

OpenERP Localization is the process of writing the necessary configuration
or the customizations required to make OpenERP suitable for a general purpose
use in a particular country.

.. i18n: Usually the first step for creating a localization (a.k.a. *l10n*) is to
.. i18n: configure one (or more) Chart(s) of Accounts for the country, with the related
.. i18n: dependencies: Account types, Taxes, etc.
..

Usually the first step for creating a localization (a.k.a. *l10n*) is to
configure one (or more) Chart(s) of Accounts for the country, with the related
dependencies: Account types, Taxes, etc.

.. i18n: This section gives a few guidelines to assist in the creation of a correct
.. i18n: ``l10n_XXX`` module. Once the new l10n module meets the following requirements,
.. i18n: it can be considered for inclusion in the official OpenERP addons, via a
.. i18n: merge proposal process (as described in :ref:`merge_proposals`).
..

This section gives a few guidelines to assist in the creation of a correct
``l10n_XXX`` module. Once the new l10n module meets the following requirements,
it can be considered for inclusion in the official OpenERP addons, via a
merge proposal process (as described in :ref:`merge_proposals`).

.. i18n: .. tip:: Reference and Examples
.. i18n: 
.. i18n:         Have a look at the Belgian localization module (``l10n_be``) to get
.. i18n:         started, and for references and examples of how a localization module
.. i18n:         is structured
..

.. tip:: Reference and Examples

        Have a look at the Belgian localization module (``l10n_be``) to get
        started, and for references and examples of how a localization module
        is structured

.. i18n: Contents of a localization module
.. i18n: ---------------------------------
..

本地化模块的内容
---------------------------------

.. i18n: In order to have a localization module fully complete, you should ensure
.. i18n: that the following features are present in your module:
..

In order to have a localization module fully complete, you should ensure
that the following features are present in your module:

.. i18n:  * chart  of account and chart of taxes are mandatory, and must meet the
.. i18n:    guidelines defined below. It's quite possible to put multiple chart
.. i18n:    templates in the same l10n module
.. i18n:  * bank interfaces (import - export)
.. i18n:  * legal reports (no business reports, these could be in a separate module)
..

 * chart  of account and chart of taxes are mandatory, and must meet the
   guidelines defined below. It's quite possible to put multiple chart
   templates in the same l10n module
 * bank interfaces (import - export)
 * legal reports (no business reports, these could be in a separate module)

.. i18n: Most of the time it's preferable that localization modules do not contain
.. i18n: any Python code that would interfere with the normal behavior of OpenERP's
.. i18n: core (such as inherited/overridden methods).
.. i18n: It's also preferable that they do not reimplement existing
.. i18n: features (e.g. don't add a wizard to generate the chart of account, use the
.. i18n: existing one).
..

Most of the time it's preferable that localization modules do not contain
any Python code that would interfere with the normal behavior of OpenERP's
core (such as inherited/overridden methods).
It's also preferable that they do not reimplement existing
features (e.g. don't add a wizard to generate the chart of account, use the
existing one).

.. i18n: If you think the OpenERP accounting report engine does not fit the legal
.. i18n: requirements for your country, you can make a merge proposal (see :ref:`merge_proposals`)
.. i18n: to improve the core accounting engine.
..

If you think the OpenERP accounting report engine does not fit the legal
requirements for your country, you can make a merge proposal (see :ref:`merge_proposals`)
to improve the core accounting engine.

.. i18n: The next sections provide guidelines for writing the most critical parts of
.. i18n: you l10n modules, in the preferred order of writing.
..

The next sections provide guidelines for writing the most critical parts of
you l10n modules, in the preferred order of writing.

.. i18n: Generic Guidelines
.. i18n: ------------------
..

通用指南
------------------

.. i18n:  * The module must be named ``l10n_XX`` where XX is the lower case country code,
.. i18n:    taken from http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
.. i18n:  * The l10n_XX module must be hosted on Launchpad, like all OpenERP modules
.. i18n:  * The l10n_XX module must be in a bzr branch which is: 
.. i18n: 
.. i18n:     * either a branch of ``lp:openobject-addons``
.. i18n:     * or a branch containing this module only (in that case it will need to be added
.. i18n:       to a branch of ``lp:openobject-addons`` in order to make a merge proposal
.. i18n:       to include it in official addons).
.. i18n: 
.. i18n:  * The module must not define charts but *charts templates*
.. i18n:  * the whole localization must be contained in one and only one module that contains
.. i18n:    legal requirements:
.. i18n: 
.. i18n:     * chart of accounts
.. i18n:     * tax structure
.. i18n:     * taxes
.. i18n:     * legal statements (reports), if any
.. i18n:     * tax declarations, if any
.. i18n:     * bank import/export features, if any
.. i18n: 
.. i18n: * Extra features which are not legal requirements but best practices of the country
.. i18n:   can be in separate modules (such as special kind of discounts, some special tax for
.. i18n:   very specific situations, etc.)
..

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

.. i18n: Account Types Guidelines (account.account.type)
.. i18n: -----------------------------------------------
.. i18n: Example
.. i18n:  Assets, Liabilities...
..

科目类型指南 (account.account.type)
-----------------------------------------------
Example
 Assets, Liabilities...

.. i18n: Description
.. i18n:  The type contains more information about the account and its specifics.
..

Description
 The type contains more information about the account and its specifics.

.. i18n: It's important to pay attention to the deferral method field (named
.. i18n: ``close_method``) because it will define the way your accounts will create or not
.. i18n: new entries when opening a new fiscal year. You should choose:
..

It's important to pay attention to the deferral method field (named
``close_method``) because it will define the way your accounts will create or not
new entries when opening a new fiscal year. You should choose:

.. i18n:   * ``detail`` for accounts that you want to fully report (even reconciled entries)
.. i18n:   * ``none`` for accounts that you don't want to report at all
..

  * ``detail`` for accounts that you want to fully report (even reconciled entries)
  * ``none`` for accounts that you don't want to report at all

.. i18n: Make also sure to give a corresponding value for the new field ``report_type``
.. i18n: (new as of v6) because it's used in balance sheet and P&L report to know in
.. i18n: which column to display it.
.. i18n: You must have at least one account with report_type ``'/'`` (net profit).
..

Make also sure to give a corresponding value for the new field ``report_type``
(new as of v6) because it's used in balance sheet and P&L report to know in
which column to display it.
You must have at least one account with report_type ``'/'`` (net profit).

.. i18n: Chart of Accounts Guidelines (account.account.template)
.. i18n: -------------------------------------------------------
.. i18n: When creating your chart of account, the principal information you should take
.. i18n: care of is the internal type field (named ``type``), because that field will
.. i18n: be used by OpenERP in many places:
..

科目表指南 (account.account.template)
-------------------------------------------------------
When creating your chart of account, the principal information you should take
care of is the internal type field (named ``type``), because that field will
be used by OpenERP in many places:

.. i18n:     * ``receivable`` type is used for customer accounts
.. i18n:     * ``payable`` is used for supplier accounts
.. i18n:     * ``view`` is used for non-leaf accounts, used to organize the Chart of
.. i18n:       Accounts in a suitable tree of accounts. OpenERP won't accept any entries
.. i18n:       in ``view`` accounts.
.. i18n:     * ``liquidity`` is used for cash/bank accounts (new as of v6)
..

    * ``receivable`` type is used for customer accounts
    * ``payable`` is used for supplier accounts
    * ``view`` is used for non-leaf accounts, used to organize the Chart of
      Accounts in a suitable tree of accounts. OpenERP won't accept any entries
      in ``view`` accounts.
    * ``liquidity`` is used for cash/bank accounts (new as of v6)

.. i18n: For any other accounts (regular ones), you should chose the internal type ``other``.
..

For any other accounts (regular ones), you should chose the internal type ``other``.

.. i18n: **Important**: Create templates of charts of accounts, not real charts of accounts,
.. i18n: as the Chart Of Accounts is not global, it's a template that needs to be applied
.. i18n: for each company.
..

**Important**: Create templates of charts of accounts, not real charts of accounts,
as the Chart Of Accounts is not global, it's a template that needs to be applied
for each company.

.. i18n: This is also the place where you'll have to make the categorization of your
.. i18n: accounts in the account types (as explained in previous section), via the
.. i18n: ``user_type`` field.
..

This is also the place where you'll have to make the categorization of your
accounts in the account types (as explained in previous section), via the
``user_type`` field.

.. i18n: Be sure the chart of account has a hierarchical tree structure.
..

Be sure the chart of account has a hierarchical tree structure.

.. i18n: Chart of Tax Codes Guidelines (account.tax.code.template)
.. i18n: ---------------------------------------------------------
.. i18n: This object is the same in v5 and v6. The hierarchical structure of the
.. i18n: Chart of Tax Codes should allow you to compute the sum/totals easily
.. i18n: as legally required in your country.
..

税码表指南 (account.tax.code.template)
---------------------------------------------------------
This object is the same in v5 and v6. The hierarchical structure of the
Chart of Tax Codes should allow you to compute the sum/totals easily
as legally required in your country.

.. i18n: The code of each tax code must respect legal statements.
..

The code of each tax code must respect legal statements.

.. i18n: Here is an example of minimal chart of taxes structure:
..

Here is an example of minimal chart of taxes structure:

.. i18n:     * Tax Balance to Pay
.. i18n: 
.. i18n:         * Tax Paid
.. i18n: 
.. i18n:             * Tax Paid 21%
.. i18n:             * Tax Paid 0%
.. i18n: 
.. i18n:         * Tax Received
.. i18n: 
.. i18n:             * Tax Received 21%
.. i18n:             * Tax Received 0%
.. i18n: 
.. i18n:         * Tax Bases
.. i18n: 
.. i18n:             * Base of Taxable Sales
.. i18n:             * Base Tax Sales 21%
.. i18n:             * Base of Taxable Purchases
.. i18n:             * Base Tax Purchases 21%
..

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

.. i18n: The code of each tax code must be the code of the tax section/cell
.. i18n: for this amount in your monthly/yearly legal tax declaration.
.. i18n: Leave the tax code empty if you don't want that code to appear
.. i18n: in the legal tax statement (i.e. for chart structure purposes)
..

The code of each tax code must be the code of the tax section/cell
for this amount in your monthly/yearly legal tax declaration.
Leave the tax code empty if you don't want that code to appear
in the legal tax statement (i.e. for chart structure purposes)

.. i18n: Chart Template Guidelines account.chart.template
.. i18n: ------------------------------------------------
..

科目表指南 account.chart.template
------------------------------------------------

.. i18n: Once all above objects are created, you can focus on the Chart Template.
.. i18n: It specifies the required information for generating the proper chart
.. i18n: of account, taxes, etc. when you install this chart via the
.. i18n: Chart of Account installation wizard.
..

Once all above objects are created, you can focus on the Chart Template.
It specifies the required information for generating the proper chart
of account, taxes, etc. when you install this chart via the
Chart of Account installation wizard.

.. i18n: This information includes:
..

This information includes:

.. i18n:  * chart of account: the ``account_root_id`` field provides the root account
.. i18n:    (with ``parent_id = False``) of your chart
.. i18n:  * chart of tax: the ``tax_code_root_id`` field provides the root tax code
.. i18n:    (with ``parent_id = False``) of your chart
.. i18n:  * parent of the bank/cash accounts: the ``bank_account_view_id`` field selects
.. i18n:    the account (within your chart) under which the bank and cash accounts will be
.. i18n:    created by OpenERP
.. i18n:  * default receivable account: the ``property_account_receivable`` field
.. i18n:    selects the account of your chart that will be used by default as customer
.. i18n:    account for each new partner
.. i18n:  * default payable account: the ``property_account_payable`` field selects
.. i18n:    the account of your chart that will be used by default for the supplier account
.. i18n:    of new partners
.. i18n:  * default expense accounts: the ``property_account_expense_categ`` field selects
.. i18n:    the account of your chart that will be used by default for the expense account
.. i18n:    of each new product
.. i18n:  * default income account: the ``property_account_income_categ`` selects the account
.. i18n:    of your chart that will be used by default for the income account of each new
.. i18n:    product
.. i18n:  * As of v6, a new field has been introduced for Reserve and Profit/Loss Account,
.. i18n:    named ``property_reserve_and_surplus_account``. This fields select the account
.. i18n:    used for transferring amounts from Profit & Loss Report.
..

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

.. i18n: Taxes Guidelines (account.tax.template)
.. i18n: ---------------------------------------
.. i18n: The only change in that object for v6 is the removal of the ``tax_group``
.. i18n: field which was unused. When testing the taxes, you should make sure that:
..

税项指南 (account.tax.template)
---------------------------------------
The only change in that object for v6 is the removal of the ``tax_group``
field which was unused. When testing the taxes, you should make sure that:

.. i18n:  * the accounting entries created for it are correct: right accounts, debit
.. i18n:    and credit
.. i18n:  * the vat amounts that are put in the tax code are correct
..

 * the accounting entries created for it are correct: right accounts, debit
   and credit
 * the vat amounts that are put in the tax code are correct

.. i18n: This should be verified for both invoices and refunds.
..

This should be verified for both invoices and refunds.

.. i18n: Use the ``chart_template_id`` to link the taxes to the
.. i18n: ``account.chart.template`` object defined above.
..

Use the ``chart_template_id`` to link the taxes to the
``account.chart.template`` object defined above.

.. i18n: Check that each tax is linked to an account, a tax code and a base tax code.
..

Check that each tax is linked to an account, a tax code and a base tax code.

.. i18n: Fiscal positions Guidelines (account.fiscal.position.template)
.. i18n: --------------------------------------------------------------
.. i18n: Fiscal position objects stay the same in v6. They're used to
.. i18n: automatically map the default tax/account for a product
.. i18n: according to Partner-specific situations (for invoices, sale
.. i18n: and purchase orders).
..

财务结构指南 (account.fiscal.position.template)
--------------------------------------------------------------
Fiscal position objects stay the same in v6. They're used to
automatically map the default tax/account for a product
according to Partner-specific situations (for invoices, sale
and purchase orders).

.. i18n: In Europe we need at least 3 fiscal positions:
..

In Europe we need at least 3 fiscal positions:

.. i18n:   * national customers
.. i18n:   * foreign customers, within Europe
.. i18n:   * foreign customers, outside Europe
..

  * national customers
  * foreign customers, within Europe
  * foreign customers, outside Europe

.. i18n: This tax and account mapping will allow you to keep a generic VAT,
.. i18n: let's say 21% (Belgian VAT), and a corresponding income account 
.. i18n: "sales in Belgium"  on your products. When invoicing a
.. i18n: customer that has the fiscal  position 'in Europe', those values
.. i18n: will be automatically changed into (for example) the corresponding
.. i18n: 0% VAT and "sales in Europe" account.
..

This tax and account mapping will allow you to keep a generic VAT,
let's say 21% (Belgian VAT), and a corresponding income account 
"sales in Belgium"  on your products. When invoicing a
customer that has the fiscal  position 'in Europe', those values
will be automatically changed into (for example) the corresponding
0% VAT and "sales in Europe" account.

.. i18n: Use the ``chart_template_id`` field to link the fiscal positions
.. i18n: to the ``account.chart.template`` object defined above.
..

Use the ``chart_template_id`` field to link the fiscal positions
to the ``account.chart.template`` object defined above.

.. i18n: Check that each l10n module has at least two fiscal positions
.. i18n: defined:
..

Check that each l10n module has at least two fiscal positions
defined:

.. i18n:  * one for the national customers
.. i18n:  * one or more for foreign customers
..

 * one for the national customers
 * one or more for foreign customers

.. i18n: Modules dependencies Guidelines
.. i18n: -------------------------------
.. i18n: If the module is from an European country, it should
.. i18n: depend on the ``base_vat`` module.
..

模块依赖指南
-------------------------------
If the module is from an European country, it should
depend on the ``base_vat`` module.

.. i18n: Avoid to put specific features in your l10n_XX module if it's not related
.. i18n: to legal requirement. New accounting features (example: discount on payment, etc.)
.. i18n: must be in another and generic module, not in a l10n_XX  module.
.. i18n: Also, the l10n_XX module should not depend (require) on these other modules,
.. i18n: which may not be included into official addons.
..

Avoid to put specific features in your l10n_XX module if it's not related
to legal requirement. New accounting features (example: discount on payment, etc.)
must be in another and generic module, not in a l10n_XX  module.
Also, the l10n_XX module should not depend (require) on these other modules,
which may not be included into official addons.

.. i18n: For legal requirements that are specific to your country
.. i18n: (e.g.: mandatory electronic tax declaration system), you can add the features
.. i18n: in the l10n_XX  module directly.
..

For legal requirements that are specific to your country
(e.g.: mandatory electronic tax declaration system), you can add the features
in the l10n_XX  module directly.

.. i18n: Specific reports Guidelines
.. i18n: ---------------------------
.. i18n: If there is any specific report legally required in your country
.. i18n: (such as the VAT report that generates XML files in l10n_be), the
.. i18n: localization module of that country is the right place to put it.
..

特定报表指南
---------------------------
If there is any specific report legally required in your country
(such as the VAT report that generates XML files in l10n_be), the
localization module of that country is the right place to put it.

.. i18n: As a reminder: look at l10n_be for examples or for references.
..

As a reminder: look at l10n_be for examples or for references.
