
.. module:: account_balance_reporting
    :synopsis: Account balance reporting engine 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_balance_reporting"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

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

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`base`
 * :mod:`account`

Reports
-------

 * Generic balance report

 * Generic balance report (non zero lines)

Menus
-------

 * Financial Management/Legal Statements/Account balance reports
 * Financial Management/Legal Statements/Account balance reports/Templates
 * Financial Management/Legal Statements/Account balance reports/Reports

Views
-----

 * account.balance.report.template.form (form)
 * account.balance.report.template.tree (tree)
 * account.balance.report.template.line.form (form)
 * account.balance.report.template.line.tree (tree)
 * account.balance.report.form (form)
 * account.balance.report.tree (tree)
 * account.balance.report.line.form (form)
 * account.balance.report.line.tree (tree)


Objects
-------

Object: account.balance.report.template (account.balance.report.template)
#########################################################################



:description: Description, text





:balance_mode: Balance mode, selection

    *Formula calculation mode: Depending on it, the balance is calculated as follows:
    Mode 0: debit-credit (default);
    Mode 1: debit-credit, credit-debit for accounts in brackets;
    Mode 2: credit-debit;
    Mode 3: credit-debit, debit-credit for accounts in brackets.*



:report_xml_id: Report design, many2one





:line_ids: Lines, one2many





:type: Type, selection





:name: Name, char, required




Object: account.balance.report.template.line (account.balance.report.template.line)
###################################################################################



:code: Code, char, required

    *Concept code, may be used on formulas to reference this line*



:name: Name, char, required

    *Concept name/description*



:sequence: Sequence, char

    *Lines will be sorted/grouped by this field*



:css_class: CSS Class, selection

    *Style-sheet class*



:child_ids: Children, one2many





:negate: Negate, boolean

    *Negate the value (change the sign of the balance)*



:parent_id: Parent, many2one





:current_value: Fiscal year 1 formula, text

    *Value calculation formula: Depending on this formula the final value is calculated as follows:
    Empy template value: sum of (this concept) children values.
    Number with decimal point ("10.2"): that value (constant).
    Account numbers separated by commas ("430,431,(437)"): Sum of the account balances
    (the sign of the balance depends on the balance mode).
    Concept codes separated by "+" ("11000+12000"): Sum of those concepts values.*



:previous_value: Fiscal year 2 formula, text

    *Value calculation formula: Depending on this formula the final value is calculated as follows:
    Empy template value: sum of (this concept) children values.
    Number with decimal point ("10.2"): that value (constant).
    Account numbers separated by commas ("430,431,(437)"): Sum of the account balances
    (the sign of the balance depends on the balance mode).
    Concept codes separated by "+" ("11000+12000"): Sum of those concepts values.*



:report_id: Template, many2one




Object: account.balance.report (account.balance.report)
#######################################################



:name: Name, char, required





:current_fiscalyear_id: Fiscal year 1, many2one, required





:company_id: Company, many2one, required, readonly





:previous_fiscalyear_id: Fiscal year 2, many2one





:state: State, selection





:current_period_ids: Fiscal year 1 periods, many2many





:previous_period_ids: Fiscal year 2 periods, many2many





:line_ids: Lines, one2many





:calc_date: Calculation date, datetime





:template_id: Template, many2one, required




Object: account.balance.report.line (account.balance.report.line)
#################################################################



:code: Code, char, required





:name: Name, char, required





:sequence: Sequence, char





:template_line_id: Line template, many2one





:notes: Notes, text





:child_ids: Children, one2many





:calc_date: Calculation date, datetime





:parent_id: Parent, many2one





:css_class: CSS Class, selection





:current_value: Fiscal year 1, float





:previous_value: Fiscal year 2, float





:report_id: Report, many2one


