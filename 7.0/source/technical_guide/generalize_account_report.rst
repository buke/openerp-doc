
.. module:: generalize_account_report
    :synopsis: generalize account report module 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/generalize_account_report"></div>
    <script src="http://js-kit.com/ratings.js"></script>

generalize account report module (*generalize_account_report*)
==============================================================
:Module: generalize_account_report
:Name: generalize account report module
:Version: 5.0.0.1
:Author: Tiny/Axelor
:Directory: generalize_account_report
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Module to handle account in generalize manner and print the report.

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`base`
 * :mod:`account_voucher`

Reports
-------

 * Final Horizontal Report

 * Final Vertical Report

Menus
-------

 * Financial Management/Legal Statements/Generalize Account Report
 * Financial Management/Legal Statements/Generalize Account Report/Generalize Account Report

Views
-----

 * generalize_account_report.tree (tree)
 * generalize_account_report.form (form)
 * group.detail.configuration.tree (tree)
 * group.detail.configuration.form (form)


Objects
-------

Object: Generalize Account Report (generalize.account.report)
#############################################################



:name: Name, char, required





:end_date: End Date, date





:gr_detail: Documents, one2many





:Loss_tran_acc: Loss Transfer Account, many2one





:company_id: Company, many2one, required





:fiscal_year: Fiscal Year, many2one, required





:st_date: Start Date, date





:profit_tran_acc: Profit Transfer Account, many2one





:type: Report type, selection, required





:final_type: Final Account Type, selection, required




Object: Group Configuration (group.detail.configuration)
########################################################



:acc_gr_name: Account, many2one, required





:pos_name: Position Name, selection, required





:name: Name, char, required





:gdc_id: Geralize Account, many2one





:sequence: Sequence, integer, required


