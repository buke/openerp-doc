
.. module:: report_analytic
    :synopsis: Analytic Account Reporting (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_analytic"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  A module that adds new reports based on analytic accounts.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_analytic.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_analytic.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_analytic.zip>`_


Dependencies
------------

 * :mod:`account`
 * :mod:`hr_timesheet_invoice`

Reports
-------

None


Menus
-------

 * Financial Management/Reporting/Analytic/All Months/Expired analytic accounts

Views
-----

 * report.analytic.account.close.form (form)
 * report.analytic.account.close.tree (tree)
 * report.analytic.account.close.graph (graph)


Objects
-------

Object: Analytic account to close (report.analytic.account.close)
#################################################################



:name: Analytic account, many2one, readonly





:date_deadline: Deadline, date, readonly





:quantity_max: Max. Quantity, float, readonly





:state: State, char, readonly





:balance: Balance, float, readonly





:partner_id: Partner, many2one, readonly





:quantity: Quantity, float, readonly


