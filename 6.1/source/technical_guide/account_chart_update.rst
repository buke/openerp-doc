
.. module:: account_chart_update
    :synopsis: Update account chart from template 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_chart_update"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Update account chart from template (*account_chart_update*)
===========================================================
:Module: account_chart_update
:Name: Update account chart from template
:Version: 5.0.1.0
:Author: Zikzakmedia SL
:Directory: account_chart_update
:Web: www.zikzakmedia.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Adds a wizard to update a company account chart from a template:
    * Generates the new accounts from the template and assigns them to the right company
    * Generates the new taxes and tax codes, changing account assignations
    * Generates the new fiscal positions, changing account and taxes assignations
  
  Before creating the new accounts, taxes, tax codes and fiscal positions, the user can select
  which ones must be created.
  
  The user can also choose to update the existing accounts, taxes, tax codes and fiscal positions
  from a template.
  
  The problems occurred during the creation/updating of the account chart are shown in the last step.
  
  It is useful when the account law has changed and you want to transfer the new accounts, taxes and
  fiscal positions included in the account chart template to an existing company account chart.
  
  Note: Due to the memory limitation of the osv_memory OpenERP objects, only a maximum number of 
  objects can be created each time. If a lot of new accounts, taxes, tax codes or fiscal positions
  must be created, the wizard should be run several times.

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`account`

Reports
-------

None


Menus
-------

 * Financial Management/Configuration/Financial Accounting/Templates/Update Chart of Accounts from a Chart Template

Views
-----

 * Update Chart of Accounts from a Chart Template (form)


Objects
-------

Object: wizard.update.charts.accounts (wizard.update.charts.accounts)
#####################################################################



:update_tax_code: Update tax codes, boolean

    *Existing tax codes are updated. Tax codes are searched by name.*



:code_digits: # of Digits, integer, required

    *No. of Digits to use for account code. Make sure it is the same number as existing accounts.*



:fiscal_position_ids: Fiscal positions, one2many





:logs: Logs, text, readonly





:new_fp: Create - Fiscal positions, integer, readonly





:chart_template_id: Chart Template, many2one, required





:company_id: Company, many2one, required





:tax_code_ids: Tax codes, one2many





:update_account: Update accounts, boolean

    *Existing accounts are updated. Accounts are searched by code.*



:update_fiscal_position: Update fiscal positions, boolean

    *Existing fiscal positions are updated. Fiscal positions are searched by name.*



:state: Status, selection, readonly





:update_tax: Update taxes, boolean

    *Existing taxes are updated. Taxes are searched by name.*



:updated_tax: Update - Taxes, integer, readonly





:account_ids: Accounts, one2many





:new_account: Create - Accounts, integer, readonly





:updated_fp: Update - Fiscal positions, integer, readonly





:updated_tax_code: Update - Tax codes, integer, readonly





:updated_account: Update - Accounts, integer, readonly





:new_tax_code: Create - Tax codes, integer, readonly





:new_tax: Create - Taxes, integer, readonly





:tax_ids: Taxes, one2many




Object: wizard.update.charts.accounts.tax.code (wizard.update.charts.accounts.tax.code)
#######################################################################################



:tax_code_id: Tax codes, many2one, required





:update_chart_wizard_id: Update chart wizard, many2one, required




Object: wizard.update.charts.accounts.tax (wizard.update.charts.accounts.tax)
#############################################################################



:update_chart_wizard_id: Update chart wizard, many2one, required





:tax_id: Taxes, many2one, required




Object: wizard.update.charts.accounts.account (wizard.update.charts.accounts.account)
#####################################################################################



:update_chart_wizard_id: Update chart wizard, many2one, required





:account_id: Accounts, many2one, required




Object: wizard.update.charts.accounts.fiscal.position (wizard.update.charts.accounts.fiscal.position)
#####################################################################################################



:update_chart_wizard_id: Update chart wizard, many2one, required





:fiscal_position_id: Fiscal positions, many2one, required


