
.. module:: account_coda_2_1_d
    :synopsis: Account CODA Version 2.1 D - Helps to import bank statements from .csv file. 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_coda_2_1_d"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Account CODA Version 2.1 D - Helps to import bank statements from .csv file. (*account_coda_2_1_d*)
===================================================================================================
:Module: account_coda_2_1_d
:Name: Account CODA Version 2.1 D - Helps to import bank statements from .csv file.
:Version: 5.0.1.0.1
:Author: OpenERP
:Directory: account_coda_2_1_d
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Module provides functionality to import
      bank statements from .csv file.
      Import coda file wizard is used to import bank statements.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_coda_2_1_d.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_coda_2_1_d.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`account_report`
 * :mod:`base_iban`

Reports
-------

None


Menus
-------

 * Financial Management/Reporting/Coda Statements
 * Financial Management/Periodical Processing/Import Coda Statements

Views
-----

 * account.coda.form (form)
 * account.coda.tree (tree)


Objects
-------

Object: CODA Format For Account (account.coda)
##############################################



:user_id: User, many2one, readonly





:name: Coda File, binary, readonly





:journal_id: Bank Journal, many2one, readonly





:note: Import Log, text, readonly





:date: Import Date, date, readonly





:statement_id: Generated Bank Statement, many2one, readonly


