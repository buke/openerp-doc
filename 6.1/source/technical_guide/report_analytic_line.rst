
.. module:: report_analytic_line
    :synopsis: Analytic lines - Reporting (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_analytic_line"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Analytic lines - Reporting (*report_analytic_line*)
===================================================
:Module: report_analytic_line
:Name: Analytic lines - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_analytic_line
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  A report on analytic lines, costs by products, months and accounts.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_analytic_line.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_analytic_line.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_analytic_line.zip>`_


Dependencies
------------

 * :mod:`account`
 * :mod:`hr_timesheet_invoice`

Reports
-------

None


Menus
-------

 * Financial Management/Reporting/Analytic/All Months/Analytic Lines to Invoice

Views
-----

 * report.account.analytic.line.to.invoice (form)
 * report.account.analytic.line.to.invoice (tree)
 * report.account.analytic.line.to.invoice.graph (graph)


Objects
-------

Object: Analytic lines to invoice report (report.account.analytic.line.to.invoice)
##################################################################################



:account_id: Analytic account, many2one, readonly





:product_uom_id: UoM, many2one, readonly





:amount: Amount, float, readonly





:product_id: Product, many2one, readonly





:unit_amount: Units, float, readonly





:sale_price: Sale price, float, readonly





:name: Month, date, readonly


