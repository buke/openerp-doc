
.. module:: electronic_report_intrastat
    :synopsis: Electronic Intrastat Reporting - To export intrastat data into .SDV format 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/electronic_report_intrastat"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Electronic Intrastat Reporting - To export intrastat data into .SDV format (*electronic_report_intrastat*)
==========================================================================================================
:Module: electronic_report_intrastat
:Name: Electronic Intrastat Reporting - To export intrastat data into .SDV format
:Version: 5.0.1.0
:Author: Tiny
:Directory: electronic_report_intrastat
:Web: http://tinyerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  A module that export intrastat data into .SDV format

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/electronic_report_intrastat.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/electronic_report_intrastat.zip>`_


Dependencies
------------

 * :mod:`report_intrastat`

Reports
-------

None


Menus
-------

 * Stock Management/Reporting/Intrastat Export Logs

Views
-----

 * report.intrastat.export.log.form (form)
 * export.log.tree (tree)


Objects
-------

Object: report.intrastat.export.log (report.intrastat.export.log)
#################################################################



:date_create: Export Time, datetime





:nbr: Total lines Exported, integer





:note: Notes, text





:user_id: User, many2one





:name: Name, char


