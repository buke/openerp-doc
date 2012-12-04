
.. i18n: .. module:: report_analytic
.. i18n:     :synopsis: Analytic Account Reporting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: report_analytic
    :synopsis: Analytic Account Reporting (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_analytic"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_analytic"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Analytic Account Reporting (*report_analytic*)
.. i18n: ==============================================
.. i18n: :Module: report_analytic
.. i18n: :Name: Analytic Account Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_analytic
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Analytic Account Reporting (*report_analytic*)
==============================================
:Module: report_analytic
:Name: Analytic Account Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_analytic
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
.. i18n:   A module that adds new reports based on analytic accounts.
..

::

  A module that adds new reports based on analytic accounts.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/report_analytic.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/report_analytic.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/report_analytic.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_analytic.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_analytic.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_analytic.zip>`_

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

.. i18n:  * Financial Management/Reporting/Analytic/All Months/Expired analytic accounts
..

 * Financial Management/Reporting/Analytic/All Months/Expired analytic accounts

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * report.analytic.account.close.form (form)
.. i18n:  * report.analytic.account.close.tree (tree)
.. i18n:  * report.analytic.account.close.graph (graph)
..

 * report.analytic.account.close.form (form)
 * report.analytic.account.close.tree (tree)
 * report.analytic.account.close.graph (graph)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Analytic account to close (report.analytic.account.close)
.. i18n: #################################################################
..

Object: Analytic account to close (report.analytic.account.close)
#################################################################

.. i18n: :name: Analytic account, many2one, readonly
..

:name: Analytic account, many2one, readonly

.. i18n: :date_deadline: Deadline, date, readonly
..

:date_deadline: Deadline, date, readonly

.. i18n: :quantity_max: Max. Quantity, float, readonly
..

:quantity_max: Max. Quantity, float, readonly

.. i18n: :state: State, char, readonly
..

:state: State, char, readonly

.. i18n: :balance: Balance, float, readonly
..

:balance: Balance, float, readonly

.. i18n: :partner_id: Partner, many2one, readonly
..

:partner_id: Partner, many2one, readonly

.. i18n: :quantity: Quantity, float, readonly
..

:quantity: Quantity, float, readonly
