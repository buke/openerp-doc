
.. i18n: .. module:: account_chart_update
.. i18n:     :synopsis: Update account chart from template 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_chart_update
    :synopsis: Update account chart from template 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_chart_update"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_chart_update"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Update account chart from template (*account_chart_update*)
.. i18n: ===========================================================
.. i18n: :Module: account_chart_update
.. i18n: :Name: Update account chart from template
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Zikzakmedia SL
.. i18n: :Directory: account_chart_update
.. i18n: :Web: www.zikzakmedia.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Adds a wizard to update a company account chart from a template:
.. i18n:     * Generates the new accounts from the template and assigns them to the right company
.. i18n:     * Generates the new taxes and tax codes, changing account assignations
.. i18n:     * Generates the new fiscal positions, changing account and taxes assignations
.. i18n:   
.. i18n:   Before creating the new accounts, taxes, tax codes and fiscal positions, the user can select
.. i18n:   which ones must be created.
.. i18n:   
.. i18n:   The user can also choose to update the existing accounts, taxes, tax codes and fiscal positions
.. i18n:   from a template.
.. i18n:   
.. i18n:   The problems occurred during the creation/updating of the account chart are shown in the last step.
.. i18n:   
.. i18n:   It is useful when the account law has changed and you want to transfer the new accounts, taxes and
.. i18n:   fiscal positions included in the account chart template to an existing company account chart.
.. i18n:   
.. i18n:   Note: Due to the memory limitation of the osv_memory OpenERP objects, only a maximum number of 
.. i18n:   objects can be created each time. If a lot of new accounts, taxes, tax codes or fiscal positions
.. i18n:   must be created, the wizard should be run several times.
..

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

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n: (No download links available)
..

(No download links available)

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account`
..

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

.. i18n:  * Financial Management/Configuration/Financial Accounting/Templates/Update Chart of Accounts from a Chart Template
..

 * Financial Management/Configuration/Financial Accounting/Templates/Update Chart of Accounts from a Chart Template

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * Update Chart of Accounts from a Chart Template (form)
..

 * Update Chart of Accounts from a Chart Template (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: wizard.update.charts.accounts (wizard.update.charts.accounts)
.. i18n: #####################################################################
..

Object: wizard.update.charts.accounts (wizard.update.charts.accounts)
#####################################################################

.. i18n: :update_tax_code: Update tax codes, boolean
..

:update_tax_code: Update tax codes, boolean

.. i18n:     *Existing tax codes are updated. Tax codes are searched by name.*
..

    *Existing tax codes are updated. Tax codes are searched by name.*

.. i18n: :code_digits: # of Digits, integer, required
..

:code_digits: # of Digits, integer, required

.. i18n:     *No. of Digits to use for account code. Make sure it is the same number as existing accounts.*
..

    *No. of Digits to use for account code. Make sure it is the same number as existing accounts.*

.. i18n: :fiscal_position_ids: Fiscal positions, one2many
..

:fiscal_position_ids: Fiscal positions, one2many

.. i18n: :logs: Logs, text, readonly
..

:logs: Logs, text, readonly

.. i18n: :new_fp: Create - Fiscal positions, integer, readonly
..

:new_fp: Create - Fiscal positions, integer, readonly

.. i18n: :chart_template_id: Chart Template, many2one, required
..

:chart_template_id: Chart Template, many2one, required

.. i18n: :company_id: Company, many2one, required
..

:company_id: Company, many2one, required

.. i18n: :tax_code_ids: Tax codes, one2many
..

:tax_code_ids: Tax codes, one2many

.. i18n: :update_account: Update accounts, boolean
..

:update_account: Update accounts, boolean

.. i18n:     *Existing accounts are updated. Accounts are searched by code.*
..

    *Existing accounts are updated. Accounts are searched by code.*

.. i18n: :update_fiscal_position: Update fiscal positions, boolean
..

:update_fiscal_position: Update fiscal positions, boolean

.. i18n:     *Existing fiscal positions are updated. Fiscal positions are searched by name.*
..

    *Existing fiscal positions are updated. Fiscal positions are searched by name.*

.. i18n: :state: Status, selection, readonly
..

:state: Status, selection, readonly

.. i18n: :update_tax: Update taxes, boolean
..

:update_tax: Update taxes, boolean

.. i18n:     *Existing taxes are updated. Taxes are searched by name.*
..

    *Existing taxes are updated. Taxes are searched by name.*

.. i18n: :updated_tax: Update - Taxes, integer, readonly
..

:updated_tax: Update - Taxes, integer, readonly

.. i18n: :account_ids: Accounts, one2many
..

:account_ids: Accounts, one2many

.. i18n: :new_account: Create - Accounts, integer, readonly
..

:new_account: Create - Accounts, integer, readonly

.. i18n: :updated_fp: Update - Fiscal positions, integer, readonly
..

:updated_fp: Update - Fiscal positions, integer, readonly

.. i18n: :updated_tax_code: Update - Tax codes, integer, readonly
..

:updated_tax_code: Update - Tax codes, integer, readonly

.. i18n: :updated_account: Update - Accounts, integer, readonly
..

:updated_account: Update - Accounts, integer, readonly

.. i18n: :new_tax_code: Create - Tax codes, integer, readonly
..

:new_tax_code: Create - Tax codes, integer, readonly

.. i18n: :new_tax: Create - Taxes, integer, readonly
..

:new_tax: Create - Taxes, integer, readonly

.. i18n: :tax_ids: Taxes, one2many
..

:tax_ids: Taxes, one2many

.. i18n: Object: wizard.update.charts.accounts.tax.code (wizard.update.charts.accounts.tax.code)
.. i18n: #######################################################################################
..

Object: wizard.update.charts.accounts.tax.code (wizard.update.charts.accounts.tax.code)
#######################################################################################

.. i18n: :tax_code_id: Tax codes, many2one, required
..

:tax_code_id: Tax codes, many2one, required

.. i18n: :update_chart_wizard_id: Update chart wizard, many2one, required
..

:update_chart_wizard_id: Update chart wizard, many2one, required

.. i18n: Object: wizard.update.charts.accounts.tax (wizard.update.charts.accounts.tax)
.. i18n: #############################################################################
..

Object: wizard.update.charts.accounts.tax (wizard.update.charts.accounts.tax)
#############################################################################

.. i18n: :update_chart_wizard_id: Update chart wizard, many2one, required
..

:update_chart_wizard_id: Update chart wizard, many2one, required

.. i18n: :tax_id: Taxes, many2one, required
..

:tax_id: Taxes, many2one, required

.. i18n: Object: wizard.update.charts.accounts.account (wizard.update.charts.accounts.account)
.. i18n: #####################################################################################
..

Object: wizard.update.charts.accounts.account (wizard.update.charts.accounts.account)
#####################################################################################

.. i18n: :update_chart_wizard_id: Update chart wizard, many2one, required
..

:update_chart_wizard_id: Update chart wizard, many2one, required

.. i18n: :account_id: Accounts, many2one, required
..

:account_id: Accounts, many2one, required

.. i18n: Object: wizard.update.charts.accounts.fiscal.position (wizard.update.charts.accounts.fiscal.position)
.. i18n: #####################################################################################################
..

Object: wizard.update.charts.accounts.fiscal.position (wizard.update.charts.accounts.fiscal.position)
#####################################################################################################

.. i18n: :update_chart_wizard_id: Update chart wizard, many2one, required
..

:update_chart_wizard_id: Update chart wizard, many2one, required

.. i18n: :fiscal_position_id: Fiscal positions, many2one, required
..

:fiscal_position_id: Fiscal positions, many2one, required
