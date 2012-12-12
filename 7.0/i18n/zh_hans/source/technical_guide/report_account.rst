
.. i18n: .. module:: report_account
.. i18n:     :synopsis: Account Reporting - Reporting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: report_account
    :synopsis: Account Reporting - Reporting (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_account"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_account"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Account Reporting - Reporting (*report_account*)
.. i18n: ================================================
.. i18n: :Module: report_account
.. i18n: :Name: Account Reporting - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_account
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Account Reporting - Reporting (*report_account*)
================================================
:Module: report_account
:Name: Account Reporting - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_account
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   A module that adds new reports based on the account module.
..

::

  A module that adds new reports based on the account module.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/report_account.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/report_account.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/report_account.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_account.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_account.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_account.zip>`_

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

.. i18n:  * Financial Management/Reporting/Balance by Type of Account
..

 * Financial Management/Reporting/Balance by Type of Account

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * report.account.receivable.graph (graph)
.. i18n:  * report.account.receivable.tree (tree)
.. i18n:  * report.account.receivable.form (form)
.. i18n:  * report.aged.receivable.graph (graph)
.. i18n:  * report.aged.receivable.tree (tree)
.. i18n:  * report.invoice.created.tree (tree)
..

 * report.account.receivable.graph (graph)
 * report.account.receivable.tree (tree)
 * report.account.receivable.form (form)
 * report.aged.receivable.graph (graph)
 * report.aged.receivable.tree (tree)
 * report.invoice.created.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Receivable accounts (report.account.receivable)
.. i18n: #######################################################
..

Object: Receivable accounts (report.account.receivable)
#######################################################

.. i18n: :credit: Credit, float, readonly
..

:credit: Credit, float, readonly

.. i18n: :balance: Balance, float, readonly
..

:balance: Balance, float, readonly

.. i18n: :type: Account Type, selection, required
..

:type: Account Type, selection, required

.. i18n: :name: Week of Year, char, readonly
..

:name: Week of Year, char, readonly

.. i18n: :debit: Debit, float, readonly
..

:debit: Debit, float, readonly

.. i18n: Object: A Temporary table used for Dashboard view (temp.range)
.. i18n: ##############################################################
..

Object: A Temporary table used for Dashboard view (temp.range)
##############################################################

.. i18n: :name: Range, char
..

:name: Range, char

.. i18n: Object: Aged Receivable Till Today (report.aged.receivable)
.. i18n: ###########################################################
..

Object: Aged Receivable Till Today (report.aged.receivable)
###########################################################

.. i18n: :balance: Balance, float, readonly
..

:balance: Balance, float, readonly

.. i18n: :name: Month Range, char, readonly
..

:name: Month Range, char, readonly

.. i18n: Object: Report of Invoices Created within Last 15 days (report.invoice.created)
.. i18n: ###############################################################################
..

Object: Report of Invoices Created within Last 15 days (report.invoice.created)
###############################################################################

.. i18n: :origin: Origin, char, readonly
..

:origin: Origin, char, readonly

.. i18n: :currency_id: Currency, many2one, readonly
..

:currency_id: Currency, many2one, readonly

.. i18n: :date_due: Due Date, date, readonly
..

:date_due: Due Date, date, readonly

.. i18n: :create_date: Create Date, datetime, readonly
..

:create_date: Create Date, datetime, readonly

.. i18n: :name: Description, char, readonly
..

:name: Description, char, readonly

.. i18n: :partner_id: Partner, many2one, readonly
..

:partner_id: Partner, many2one, readonly

.. i18n: :residual: Residual, float, readonly
..

:residual: Residual, float, readonly

.. i18n: :number: Invoice Number, char, readonly
..

:number: Invoice Number, char, readonly

.. i18n: :date_invoice: Date Invoiced, date, readonly
..

:date_invoice: Date Invoiced, date, readonly

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :amount_untaxed: Untaxed, float, readonly
..

:amount_untaxed: Untaxed, float, readonly

.. i18n: :type: Type, selection, readonly
..

:type: Type, selection, readonly

.. i18n: :amount_total: Total, float, readonly
..

:amount_total: Total, float, readonly
