
.. module:: account_report
    :synopsis: Reporting for accounting (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_report"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Reporting for accounting (*account_report*)
===========================================
:Module: account_report
:Name: Reporting for accounting
:Version: 5.0.1.1
:Author: Tiny
:Directory: account_report
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Financial and accounting reporting
      Fiscal statements
      Indicators

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/account_report.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/account_report.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_report.zip>`_


Dependencies
------------

 * :mod:`account`

Reports
-------

 * Fiscal Statements

 * Indicators

 * Print Indicators in PDF

Menus
-------

 * Financial Management/Configuration/Custom reporting
 * Financial Management/Configuration/Custom reporting/New Reporting Item Formula
 * Financial Management/Reporting/Custom reporting
 * Financial Management/Reporting/Custom reporting/Fiscal Statements reporting
 * Financial Management/Reporting/Custom reporting/Indicators reporting
 * Financial Management/Reporting/Custom reporting/Other reports
 * Financial Management/Reporting/Custom reporting/Print Indicators

Views
-----

 * account.report.report.form (form)
 * account.report.report.tree.simple (tree)
 * account.report.report.tree (tree)
 * account.report.history1 (tree)
 * account.report.history2 (form)
 * account.report.history3 (graph)


Objects
-------

Object: Account reporting (account.report.report)
#################################################



:status: Status, selection, readonly





:note: Note, text





:disp_tree: Display Tree, boolean

    *When the indicators are printed, if one indicator is set with this field to True, then it will display one more graphs with all its children in tree*



:code: Code, char, required





:name: Name, char, required





:sequence: Sequence, integer





:type: Type, selection, required





:child_ids: Children, one2many





:badness_limit: Badness Indicator Limit, float

    *This Value sets the limit of badness.*



:goodness_limit: Goodness Indicator Limit, float

    *This Value sets the limit of goodness.*



:parent_id: Parent, many2one





:amount: Value, float, readonly





:disp_graph: Display As Graph, boolean

    *If the field is set to True, information will be printed as a Graph, otherwise as an array.*



:active: Active, boolean





:expression: Expression, char, required




Object: Indicator (account.report.history)
##########################################



:tmp: temp, integer, readonly





:fiscalyear_id: Fiscal Year, many2one, readonly





:period_id: Period, many2one, readonly





:name: Indicator, many2one, readonly





:val: Value, float, readonly


