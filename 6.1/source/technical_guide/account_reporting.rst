
.. module:: account_reporting
    :synopsis: Reporting of Balancesheet for accounting (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_reporting"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Reporting of Balancesheet for accounting (*account_reporting*)
==============================================================
:Module: account_reporting
:Name: Reporting of Balancesheet for accounting
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_reporting
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Financial and accounting reporting
      Balance Sheet Report

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_reporting.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_reporting.zip>`_


Dependencies
------------

 * :mod:`account`

Reports
-------

None


Menus
-------

 * Financial Management/Configuration/Balance Sheet Report
 * Financial Management/Configuration/Balance Sheet Report/Balance Sheet Report
 * Financial Management/Configuration/Balance Sheet Report/Balance Sheet Report Form

Views
-----

 * account.report.bs.form (form)
 * account.report.report.tree.bs (tree)


Objects
-------

Object: Rml Colors (color.rml)
##############################



:code: code, char, required





:name: Name, char, required




Object: Account reporting for Balance Sheet (account.report.bs)
###############################################################



:font_style: Font, selection





:account_id: Accounts, many2many





:sequence: Sequence, integer





:note: Note, text





:parent_id: Parent, many2one





:code: Code, char, required





:report_type: Report Type, selection





:child_id: Children, one2many





:color_back: Back Color, many2one





:color_font: Font Color, many2one





:name: Name, char, required


