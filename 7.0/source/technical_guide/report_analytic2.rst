
.. module:: report_analytic2
    :synopsis: Analytic Accounts - Reporting 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_analytic2"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Analytic Accounts - Reporting (*report_analytic2*)
==================================================
:Module: report_analytic2
:Name: Analytic Accounts - Reporting
:Version: 5.0.1.0
:Author: OpenErp
:Directory: report_analytic2
:Web: http://www.openerp.com/
:Official module: no
:Quality certified: no

Description
-----------

::

  Reporting for data related to analytic accounts

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/report_analytic2.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_analytic2.zip>`_


Dependencies
------------

 * :mod:`account`
 * :mod:`hr_timesheet`
 * :mod:`hr_timesheet_invoice`

Reports
-------

None


Menus
-------

 * Financial Management/Reporting/Analytic/All Months/Analytic Amount by year
 * Financial Management/Reporting/Analytic/All Months/Analytic Amounts by month
 * Financial Management/Reporting/Analytic/All Months/Analytic Amounts by product

Views
-----

 * Amounts by year (tree)
 * Amounts by year (form)
 * Amounts by months (tree)
 * Amounts by month (form)
 * Amounts By products (tree)
 * Amounts by products (form)


Objects
-------

Object: Reporting by accounts/ by year (report.analytic.by.year)
################################################################



:amount: Amount, float, readonly





:year: Year, integer, readonly




Object: Reporting by accounts/ by month (report.analytic.by.month)
##################################################################



:amount: Amount, float, readonly





:year: Year, integer, readonly





:month: Month, integer, readonly




Object: Reporting by accounts/ by product (report.analytic.by.product)
######################################################################



:amount: Amount, float, readonly





:name: Product Name, char, readonly





:year: Year, integer, readonly


