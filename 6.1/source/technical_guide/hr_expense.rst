
.. module:: hr_expense
    :synopsis: Human Resources Expenses Tracking (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_expense"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Human Resources Expenses Tracking (*hr_expense*)
================================================
:Module: hr_expense
:Name: Human Resources Expenses Tracking
:Version: 5.0.1.0
:Author: Tiny
:Directory: hr_expense
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module aims to manage employee's expenses.
  
      The whole workflow is implemented:
      * Draft expense
      * Confirmation of the sheet by the employee
      * Validation by his manager
      * Validation by the accountant and invoice creation
      * Payment of the invoice to the employee
  
      This module also use the analytic accounting and is compatible with
      the invoice on timesheet module so that you will be able to automatically
      re-invoice your customer's expenses if your work by project.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/hr_expense.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_expense.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_expense.zip>`_


Dependencies
------------

 * :mod:`hr`
 * :mod:`account`
 * :mod:`account_tax_include`

Reports
-------

 * Print HR expenses

Menus
-------

 * Human Resources/Expenses
 * Human Resources/Expenses/All expenses
 * Human Resources/Expenses/All expenses/Draft expenses
 * Human Resources/Expenses/All expenses/Expenses waiting validation
 * Human Resources/Expenses/All expenses/Expenses waiting invoice
 * Human Resources/Expenses/All expenses/Expenses waiting payment
 * Human Resources/Expenses/My Expenses
 * Human Resources/Expenses/New Expenses Sheet
 * Human Resources/Expenses/My Expenses/My Draft expenses
 * Human Resources/Expenses/My Expenses/My expenses waiting validation

Views
-----

 * hr.expense.line.tree (tree)
 * hr.expense.expense.tree (tree)
 * hr.expense.form (form)
 * \* INHERIT product.product.expense.form (form)


Objects
-------

Object: Expense (hr.expense.expense)
####################################



:note: Note, text





:employee_id: Employee, many2one, required





:user_id: User, many2one, required





:name: Expense Sheet, char, required





:account_move_id: Account Move, many2one





:invoice_id: Invoice, many2one





:journal_id: Force Journal, many2one





:id: Sheet ID, integer, readonly





:currency_id: Currency, many2one, required





:user_valid: Validation User, many2one





:state: State, selection, readonly





:date_valid: Date Validated, date





:date: Date, date





:line_ids: Expense Lines, one2many, readonly





:amount: Total Amount, float, readonly





:ref: Reference, char





:date_confirm: Date Confirmed, date




Object: Expense Line (hr.expense.line)
######################################



:product_id: Product, many2one





:sequence: Sequence, integer





:description: Description, text





:name: Short Description, char, required





:date_value: Date, date, required





:uom_id: UoM, many2one





:expense_id: Expense, many2one





:unit_amount: Unit Price, float





:unit_quantity: Quantities, float





:ref: Reference, char





:analytic_account: Analytic account, many2one





:total_amount: Total, float, readonly


