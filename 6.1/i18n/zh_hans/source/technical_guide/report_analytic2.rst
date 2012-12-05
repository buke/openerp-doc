
.. i18n: .. module:: report_analytic2
.. i18n:     :synopsis: Analytic Accounts - Reporting 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: report_analytic2
    :synopsis: Analytic Accounts - Reporting 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_analytic2"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_analytic2"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Analytic Accounts - Reporting (*report_analytic2*)
.. i18n: ==================================================
.. i18n: :Module: report_analytic2
.. i18n: :Name: Analytic Accounts - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: OpenErp
.. i18n: :Directory: report_analytic2
.. i18n: :Web: http://www.openerp.com/
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Reporting for data related to analytic accounts
..

::

  Reporting for data related to analytic accounts

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/report_analytic2.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/report_analytic2.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/report_analytic2.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_analytic2.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account`
.. i18n:  * :mod:`hr_timesheet`
.. i18n:  * :mod:`hr_timesheet_invoice`
..

 * :mod:`account`
 * :mod:`hr_timesheet`
 * :mod:`hr_timesheet_invoice`

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

.. i18n:  * Financial Management/Reporting/Analytic/All Months/Analytic Amount by year
.. i18n:  * Financial Management/Reporting/Analytic/All Months/Analytic Amounts by month
.. i18n:  * Financial Management/Reporting/Analytic/All Months/Analytic Amounts by product
..

 * Financial Management/Reporting/Analytic/All Months/Analytic Amount by year
 * Financial Management/Reporting/Analytic/All Months/Analytic Amounts by month
 * Financial Management/Reporting/Analytic/All Months/Analytic Amounts by product

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * Amounts by year (tree)
.. i18n:  * Amounts by year (form)
.. i18n:  * Amounts by months (tree)
.. i18n:  * Amounts by month (form)
.. i18n:  * Amounts By products (tree)
.. i18n:  * Amounts by products (form)
..

 * Amounts by year (tree)
 * Amounts by year (form)
 * Amounts by months (tree)
 * Amounts by month (form)
 * Amounts By products (tree)
 * Amounts by products (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Reporting by accounts/ by year (report.analytic.by.year)
.. i18n: ################################################################
..

Object: Reporting by accounts/ by year (report.analytic.by.year)
################################################################

.. i18n: :amount: Amount, float, readonly
..

:amount: Amount, float, readonly

.. i18n: :year: Year, integer, readonly
..

:year: Year, integer, readonly

.. i18n: Object: Reporting by accounts/ by month (report.analytic.by.month)
.. i18n: ##################################################################
..

Object: Reporting by accounts/ by month (report.analytic.by.month)
##################################################################

.. i18n: :amount: Amount, float, readonly
..

:amount: Amount, float, readonly

.. i18n: :year: Year, integer, readonly
..

:year: Year, integer, readonly

.. i18n: :month: Month, integer, readonly
..

:month: Month, integer, readonly

.. i18n: Object: Reporting by accounts/ by product (report.analytic.by.product)
.. i18n: ######################################################################
..

Object: Reporting by accounts/ by product (report.analytic.by.product)
######################################################################

.. i18n: :amount: Amount, float, readonly
..

:amount: Amount, float, readonly

.. i18n: :name: Product Name, char, readonly
..

:name: Product Name, char, readonly

.. i18n: :year: Year, integer, readonly
..

:year: Year, integer, readonly
