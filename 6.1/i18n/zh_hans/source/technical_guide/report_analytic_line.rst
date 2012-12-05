
.. i18n: .. module:: report_analytic_line
.. i18n:     :synopsis: Analytic lines - Reporting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: report_analytic_line
    :synopsis: Analytic lines - Reporting (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_analytic_line"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_analytic_line"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Analytic lines - Reporting (*report_analytic_line*)
.. i18n: ===================================================
.. i18n: :Module: report_analytic_line
.. i18n: :Name: Analytic lines - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_analytic_line
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   A report on analytic lines, costs by products, months and accounts.
..

::

  A report on analytic lines, costs by products, months and accounts.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/report_analytic_line.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/report_analytic_line.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/report_analytic_line.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_analytic_line.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_analytic_line.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_analytic_line.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account`
.. i18n:  * :mod:`hr_timesheet_invoice`
..

 * :mod:`account`
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

.. i18n:  * Financial Management/Reporting/Analytic/All Months/Analytic Lines to Invoice
..

 * Financial Management/Reporting/Analytic/All Months/Analytic Lines to Invoice

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * report.account.analytic.line.to.invoice (form)
.. i18n:  * report.account.analytic.line.to.invoice (tree)
.. i18n:  * report.account.analytic.line.to.invoice.graph (graph)
..

 * report.account.analytic.line.to.invoice (form)
 * report.account.analytic.line.to.invoice (tree)
 * report.account.analytic.line.to.invoice.graph (graph)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Analytic lines to invoice report (report.account.analytic.line.to.invoice)
.. i18n: ##################################################################################
..

Object: Analytic lines to invoice report (report.account.analytic.line.to.invoice)
##################################################################################

.. i18n: :account_id: Analytic account, many2one, readonly
..

:account_id: Analytic account, many2one, readonly

.. i18n: :product_uom_id: UoM, many2one, readonly
..

:product_uom_id: UoM, many2one, readonly

.. i18n: :amount: Amount, float, readonly
..

:amount: Amount, float, readonly

.. i18n: :product_id: Product, many2one, readonly
..

:product_id: Product, many2one, readonly

.. i18n: :unit_amount: Units, float, readonly
..

:unit_amount: Units, float, readonly

.. i18n: :sale_price: Sale price, float, readonly
..

:sale_price: Sale price, float, readonly

.. i18n: :name: Month, date, readonly
..

:name: Month, date, readonly
