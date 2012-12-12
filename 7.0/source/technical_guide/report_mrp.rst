
.. module:: report_mrp
    :synopsis: MRP Management - Reporting (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_mrp"></div>
    <script src="http://js-kit.com/ratings.js"></script>

MRP Management - Reporting (*report_mrp*)
=========================================
:Module: report_mrp
:Name: MRP Management - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_mrp
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  A module that adds new reports based on MRP cases.
      Workcenter loads, Weekly Stock value variation

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_mrp.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_mrp.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_mrp.zip>`_


Dependencies
------------

 * :mod:`mrp`

Reports
-------

None


Menus
-------

 * Manufacturing/Reporting
 * Manufacturing/Reporting/Workcenter Loads
 * Manufacturing/Reporting/Weekly Stock Value Variation

Views
-----

 * report.workcenter.load.tree (tree)
 * report.workcenter.load.graph (graph)
 * report.workcenter.load.form (form)
 * report.mrp.inout.tree (tree)
 * report.mrp.inout.form (form)
 * report.mrp.inout.graph (graph)


Objects
-------

Object: Workcenter Load (report.workcenter.load)
################################################



:workcenter_id: Workcenter, many2one, required





:name: Week, char, required





:hour: Nbr of hour, float





:cycle: Nbr of cycle, float




Object: Stock value variation (report.mrp.inout)
################################################



:date: Week, char, required





:value: Stock value, float, required


