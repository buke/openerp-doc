
.. module:: report_intrastat
    :synopsis: Intrastat Reporting - Reporting (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_intrastat"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Intrastat Reporting - Reporting (*report_intrastat*)
====================================================
:Module: report_intrastat
:Name: Intrastat Reporting - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_intrastat
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  A module that adds intrastat reports.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_intrastat.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_intrastat.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_intrastat.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`product`
 * :mod:`stock`
 * :mod:`sale`
 * :mod:`purchase`

Reports
-------

 * Invoice Intrastat

Menus
-------

 * Products/Configuration/Intrastat Code
 * Stock Management/Reporting/This Month
 * Stock Management/Reporting/This Month/Intrastat (this month)
 * Stock Management/Reporting/All Months
 * Stock Management/Reporting/All Months/Intrastat

Views
-----

 * \* INHERIT res.country.tree (form)
 * \* INHERIT res.country.form (form)
 * \* INHERIT product.normal.form (form)
 * report.intrastat.code.tree (tree)
 * report.intrastat.code.form (form)
 * report.intrastat.view (tree)


Objects
-------

Object: Intrastat code (report.intrastat.code)
##############################################



:name: Intrastat Code, char





:description: Description, char




Object: Intrastat report (report.intrastat)
###########################################



:code: Country code, char, readonly





:name: Period, many2one, readonly





:weight: Weight, float, readonly





:type: Type, selection





:value: Value, float, readonly





:currency_id: Currency, many2one, readonly





:intrastat_id: Intrastat code, many2one, readonly





:ref: Origin, char, readonly





:supply_units: Supply Units, float, readonly


