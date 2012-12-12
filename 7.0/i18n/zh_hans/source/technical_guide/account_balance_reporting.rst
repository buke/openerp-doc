
.. i18n: .. module:: account_balance_reporting
.. i18n:     :synopsis: Account balance reporting engine 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_balance_reporting
    :synopsis: Account balance reporting engine 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_balance_reporting"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_balance_reporting"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Account balance reporting engine (*account_balance_reporting*)
.. i18n: ==============================================================
.. i18n: :Module: account_balance_reporting
.. i18n: :Name: Account balance reporting engine
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Pexego
.. i18n: :Directory: account_balance_reporting
.. i18n: :Web: http://www.pexego.es
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Account balance reporting engine (*account_balance_reporting*)
==============================================================
:Module: account_balance_reporting
:Name: Account balance reporting engine
:Version: 5.0.0.1
:Author: Pexego
:Directory: account_balance_reporting
:Web: http://www.pexego.es
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   The module allows the user to create account balance reports and templates,
.. i18n:   comparing the values of 'accounting concepts' between two fiscal years
.. i18n:   or a set of fiscal periods.
.. i18n:   
.. i18n:   Accounting concepts values can be calculated as the sum of some account balances,
.. i18n:   the sum of its children, other account concepts or constant values.
.. i18n:   
.. i18n:   Generated reports are stored as objects on the server,
.. i18n:   so you can check them anytime later or edit them
.. i18n:   (to add notes for example) before printing.
.. i18n:   
.. i18n:   The module lets the user add new templates of the reports concepts,
.. i18n:   and associate them a specific "XML reports" (OpenERP RML files for example)
.. i18n:   with the design used when printing.
.. i18n:   So it is very easy to add predefined country-specific official reports.
.. i18n:   
.. i18n:   The user interface has been designed to be as much user-friendly as it can be.
.. i18n:   
.. i18n:   Note: It has been designed to meet Spanish/Spain localization needs,
.. i18n:   but it might be used as a generic accounting report engine.
..

::

  The module allows the user to create account balance reports and templates,
  comparing the values of 'accounting concepts' between two fiscal years
  or a set of fiscal periods.
  
  Accounting concepts values can be calculated as the sum of some account balances,
  the sum of its children, other account concepts or constant values.
  
  Generated reports are stored as objects on the server,
  so you can check them anytime later or edit them
  (to add notes for example) before printing.
  
  The module lets the user add new templates of the reports concepts,
  and associate them a specific "XML reports" (OpenERP RML files for example)
  with the design used when printing.
  So it is very easy to add predefined country-specific official reports.
  
  The user interface has been designed to be as much user-friendly as it can be.
  
  Note: It has been designed to meet Spanish/Spain localization needs,
  but it might be used as a generic accounting report engine.

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

.. i18n:  * Generic balance report
.. i18n: 
.. i18n:  * Generic balance report (non zero lines)
..

 * Generic balance report

 * Generic balance report (non zero lines)

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Financial Management/Legal Statements/Account balance reports
.. i18n:  * Financial Management/Legal Statements/Account balance reports/Templates
.. i18n:  * Financial Management/Legal Statements/Account balance reports/Reports
..

 * Financial Management/Legal Statements/Account balance reports
 * Financial Management/Legal Statements/Account balance reports/Templates
 * Financial Management/Legal Statements/Account balance reports/Reports

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * account.balance.report.template.form (form)
.. i18n:  * account.balance.report.template.tree (tree)
.. i18n:  * account.balance.report.template.line.form (form)
.. i18n:  * account.balance.report.template.line.tree (tree)
.. i18n:  * account.balance.report.form (form)
.. i18n:  * account.balance.report.tree (tree)
.. i18n:  * account.balance.report.line.form (form)
.. i18n:  * account.balance.report.line.tree (tree)
..

 * account.balance.report.template.form (form)
 * account.balance.report.template.tree (tree)
 * account.balance.report.template.line.form (form)
 * account.balance.report.template.line.tree (tree)
 * account.balance.report.form (form)
 * account.balance.report.tree (tree)
 * account.balance.report.line.form (form)
 * account.balance.report.line.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: account.balance.report.template (account.balance.report.template)
.. i18n: #########################################################################
..

Object: account.balance.report.template (account.balance.report.template)
#########################################################################

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: :balance_mode: Balance mode, selection
..

:balance_mode: Balance mode, selection

.. i18n:     *Formula calculation mode: Depending on it, the balance is calculated as follows:
.. i18n:     Mode 0: debit-credit (default);
.. i18n:     Mode 1: debit-credit, credit-debit for accounts in brackets;
.. i18n:     Mode 2: credit-debit;
.. i18n:     Mode 3: credit-debit, debit-credit for accounts in brackets.*
..

    *Formula calculation mode: Depending on it, the balance is calculated as follows:
    Mode 0: debit-credit (default);
    Mode 1: debit-credit, credit-debit for accounts in brackets;
    Mode 2: credit-debit;
    Mode 3: credit-debit, debit-credit for accounts in brackets.*

.. i18n: :report_xml_id: Report design, many2one
..

:report_xml_id: Report design, many2one

.. i18n: :line_ids: Lines, one2many
..

:line_ids: Lines, one2many

.. i18n: :type: Type, selection
..

:type: Type, selection

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: account.balance.report.template.line (account.balance.report.template.line)
.. i18n: ###################################################################################
..

Object: account.balance.report.template.line (account.balance.report.template.line)
###################################################################################

.. i18n: :code: Code, char, required
..

:code: Code, char, required

.. i18n:     *Concept code, may be used on formulas to reference this line*
..

    *Concept code, may be used on formulas to reference this line*

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n:     *Concept name/description*
..

    *Concept name/description*

.. i18n: :sequence: Sequence, char
..

:sequence: Sequence, char

.. i18n:     *Lines will be sorted/grouped by this field*
..

    *Lines will be sorted/grouped by this field*

.. i18n: :css_class: CSS Class, selection
..

:css_class: CSS Class, selection

.. i18n:     *Style-sheet class*
..

    *Style-sheet class*

.. i18n: :child_ids: Children, one2many
..

:child_ids: Children, one2many

.. i18n: :negate: Negate, boolean
..

:negate: Negate, boolean

.. i18n:     *Negate the value (change the sign of the balance)*
..

    *Negate the value (change the sign of the balance)*

.. i18n: :parent_id: Parent, many2one
..

:parent_id: Parent, many2one

.. i18n: :current_value: Fiscal year 1 formula, text
..

:current_value: Fiscal year 1 formula, text

.. i18n:     *Value calculation formula: Depending on this formula the final value is calculated as follows:
.. i18n:     Empy template value: sum of (this concept) children values.
.. i18n:     Number with decimal point ("10.2"): that value (constant).
.. i18n:     Account numbers separated by commas ("430,431,(437)"): Sum of the account balances
.. i18n:     (the sign of the balance depends on the balance mode).
.. i18n:     Concept codes separated by "+" ("11000+12000"): Sum of those concepts values.*
..

    *Value calculation formula: Depending on this formula the final value is calculated as follows:
    Empy template value: sum of (this concept) children values.
    Number with decimal point ("10.2"): that value (constant).
    Account numbers separated by commas ("430,431,(437)"): Sum of the account balances
    (the sign of the balance depends on the balance mode).
    Concept codes separated by "+" ("11000+12000"): Sum of those concepts values.*

.. i18n: :previous_value: Fiscal year 2 formula, text
..

:previous_value: Fiscal year 2 formula, text

.. i18n:     *Value calculation formula: Depending on this formula the final value is calculated as follows:
.. i18n:     Empy template value: sum of (this concept) children values.
.. i18n:     Number with decimal point ("10.2"): that value (constant).
.. i18n:     Account numbers separated by commas ("430,431,(437)"): Sum of the account balances
.. i18n:     (the sign of the balance depends on the balance mode).
.. i18n:     Concept codes separated by "+" ("11000+12000"): Sum of those concepts values.*
..

    *Value calculation formula: Depending on this formula the final value is calculated as follows:
    Empy template value: sum of (this concept) children values.
    Number with decimal point ("10.2"): that value (constant).
    Account numbers separated by commas ("430,431,(437)"): Sum of the account balances
    (the sign of the balance depends on the balance mode).
    Concept codes separated by "+" ("11000+12000"): Sum of those concepts values.*

.. i18n: :report_id: Template, many2one
..

:report_id: Template, many2one

.. i18n: Object: account.balance.report (account.balance.report)
.. i18n: #######################################################
..

Object: account.balance.report (account.balance.report)
#######################################################

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :current_fiscalyear_id: Fiscal year 1, many2one, required
..

:current_fiscalyear_id: Fiscal year 1, many2one, required

.. i18n: :company_id: Company, many2one, required, readonly
..

:company_id: Company, many2one, required, readonly

.. i18n: :previous_fiscalyear_id: Fiscal year 2, many2one
..

:previous_fiscalyear_id: Fiscal year 2, many2one

.. i18n: :state: State, selection
..

:state: State, selection

.. i18n: :current_period_ids: Fiscal year 1 periods, many2many
..

:current_period_ids: Fiscal year 1 periods, many2many

.. i18n: :previous_period_ids: Fiscal year 2 periods, many2many
..

:previous_period_ids: Fiscal year 2 periods, many2many

.. i18n: :line_ids: Lines, one2many
..

:line_ids: Lines, one2many

.. i18n: :calc_date: Calculation date, datetime
..

:calc_date: Calculation date, datetime

.. i18n: :template_id: Template, many2one, required
..

:template_id: Template, many2one, required

.. i18n: Object: account.balance.report.line (account.balance.report.line)
.. i18n: #################################################################
..

Object: account.balance.report.line (account.balance.report.line)
#################################################################

.. i18n: :code: Code, char, required
..

:code: Code, char, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :sequence: Sequence, char
..

:sequence: Sequence, char

.. i18n: :template_line_id: Line template, many2one
..

:template_line_id: Line template, many2one

.. i18n: :notes: Notes, text
..

:notes: Notes, text

.. i18n: :child_ids: Children, one2many
..

:child_ids: Children, one2many

.. i18n: :calc_date: Calculation date, datetime
..

:calc_date: Calculation date, datetime

.. i18n: :parent_id: Parent, many2one
..

:parent_id: Parent, many2one

.. i18n: :css_class: CSS Class, selection
..

:css_class: CSS Class, selection

.. i18n: :current_value: Fiscal year 1, float
..

:current_value: Fiscal year 1, float

.. i18n: :previous_value: Fiscal year 2, float
..

:previous_value: Fiscal year 2, float

.. i18n: :report_id: Report, many2one
..

:report_id: Report, many2one
