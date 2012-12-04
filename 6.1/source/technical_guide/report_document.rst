
.. module:: report_document
    :synopsis: Document Management - Reporting (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_document"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Document Management - Reporting (*report_document*)
===================================================
:Module: report_document
:Name: Document Management - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_document
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Reporting for the Document Management module:
      * My Files
      * All users Files

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/report_document.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_document.zip>`_


Dependencies
------------

 * :mod:`document`

Reports
-------

None


Menus
-------

 * Document Management
 * Document Management/Reporting
 * Document Management/Reporting/This Month
 * Document Management/Reporting/This Month/My files
 * Document Management/Reporting/All Months
 * Document Management/Reporting/All Months/My files
 * Document Management/Reporting/This Month/All Users files
 * Document Management/Reporting/All Months/All Users files
 * Document Management/Reporting/Wall of Shame

Views
-----

 * report.document.user.form (form)
 * report.document.user.tree (tree)
 * report.document.wall.form (form)
 * report.document.wall.tree (tree)
 * report.document.resource.graph (graph)
 * report.document.user.graph (graph)
 * report.document.user.tree (tree)
 * report.file.month.graph (graph)
 * report.file.month.tree (tree)
 * report.document.user.graph (graph)
 * view.files.partner.graph (graph)
 * view.files.partner.tree (tree)


Objects
-------

Object: Files details by Users (report.document.user)
#####################################################



:partner: Partner, char, readonly





:file_title: File Name, char, readonly





:user_id: Owner, integer, readonly





:name: Month, date, readonly





:nbr: # of Files, integer, readonly





:month: Month, char, readonly





:directory: Directory, char, readonly





:user: User, char, readonly





:file_size: File Size, integer, readonly





:change_date: Modified Date, datetime, readonly





:create_date: Date Created, datetime, readonly





:type: Directory Type, char, readonly




Object: Files details by Partners (report.files.partner)
########################################################



:file_title: File Name, char, readonly





:create_date: Date Created, datetime, readonly





:name: Month, date, readonly





:nbr: # of Files, integer, readonly





:change_date: Modified Date, datetime, readonly





:file_size: File Size, integer, readonly





:directory: Directory, char, readonly





:partner: Partner, char, readonly





:type: Directory Type, char, readonly




Object: Files details by Directory (report.document.file)
#########################################################



:nbr: # of Files, integer, readonly





:month: Month, char, readonly





:file_size: File Size, integer, readonly




Object: Users that did not inserted documents since one month (report.document.wall)
####################################################################################



:user_id: Owner, many2one, readonly





:name: Month, date, readonly





:file_name: Last Posted File Name, char, readonly





:month: Month, char, readonly





:user: User, char, readonly





:last: Last Posted Time, datetime, readonly


