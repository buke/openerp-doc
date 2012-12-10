
.. i18n: .. module:: report_document
.. i18n:     :synopsis: Document Management - Reporting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: report_document
    :synopsis: Document Management - Reporting (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_document"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_document"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Document Management - Reporting (*report_document*)
.. i18n: ===================================================
.. i18n: :Module: report_document
.. i18n: :Name: Document Management - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_document
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Reporting for the Document Management module:
.. i18n:       * My Files
.. i18n:       * All users Files
..

::

  Reporting for the Document Management module:
      * My Files
      * All users Files

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/report_document.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/report_document.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/report_document.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_document.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`document`
..

 * :mod:`document`

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

.. i18n:  * Document Management
.. i18n:  * Document Management/Reporting
.. i18n:  * Document Management/Reporting/This Month
.. i18n:  * Document Management/Reporting/This Month/My files
.. i18n:  * Document Management/Reporting/All Months
.. i18n:  * Document Management/Reporting/All Months/My files
.. i18n:  * Document Management/Reporting/This Month/All Users files
.. i18n:  * Document Management/Reporting/All Months/All Users files
.. i18n:  * Document Management/Reporting/Wall of Shame
..

 * Document Management
 * Document Management/Reporting
 * Document Management/Reporting/This Month
 * Document Management/Reporting/This Month/My files
 * Document Management/Reporting/All Months
 * Document Management/Reporting/All Months/My files
 * Document Management/Reporting/This Month/All Users files
 * Document Management/Reporting/All Months/All Users files
 * Document Management/Reporting/Wall of Shame

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * report.document.user.form (form)
.. i18n:  * report.document.user.tree (tree)
.. i18n:  * report.document.wall.form (form)
.. i18n:  * report.document.wall.tree (tree)
.. i18n:  * report.document.resource.graph (graph)
.. i18n:  * report.document.user.graph (graph)
.. i18n:  * report.document.user.tree (tree)
.. i18n:  * report.file.month.graph (graph)
.. i18n:  * report.file.month.tree (tree)
.. i18n:  * report.document.user.graph (graph)
.. i18n:  * view.files.partner.graph (graph)
.. i18n:  * view.files.partner.tree (tree)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Files details by Users (report.document.user)
.. i18n: #####################################################
..

Object: Files details by Users (report.document.user)
#####################################################

.. i18n: :partner: Partner, char, readonly
..

:partner: Partner, char, readonly

.. i18n: :file_title: File Name, char, readonly
..

:file_title: File Name, char, readonly

.. i18n: :user_id: Owner, integer, readonly
..

:user_id: Owner, integer, readonly

.. i18n: :name: Month, date, readonly
..

:name: Month, date, readonly

.. i18n: :nbr: # of Files, integer, readonly
..

:nbr: # of Files, integer, readonly

.. i18n: :month: Month, char, readonly
..

:month: Month, char, readonly

.. i18n: :directory: Directory, char, readonly
..

:directory: Directory, char, readonly

.. i18n: :user: User, char, readonly
..

:user: User, char, readonly

.. i18n: :file_size: File Size, integer, readonly
..

:file_size: File Size, integer, readonly

.. i18n: :change_date: Modified Date, datetime, readonly
..

:change_date: Modified Date, datetime, readonly

.. i18n: :create_date: Date Created, datetime, readonly
..

:create_date: Date Created, datetime, readonly

.. i18n: :type: Directory Type, char, readonly
..

:type: Directory Type, char, readonly

.. i18n: Object: Files details by Partners (report.files.partner)
.. i18n: ########################################################
..

Object: Files details by Partners (report.files.partner)
########################################################

.. i18n: :file_title: File Name, char, readonly
..

:file_title: File Name, char, readonly

.. i18n: :create_date: Date Created, datetime, readonly
..

:create_date: Date Created, datetime, readonly

.. i18n: :name: Month, date, readonly
..

:name: Month, date, readonly

.. i18n: :nbr: # of Files, integer, readonly
..

:nbr: # of Files, integer, readonly

.. i18n: :change_date: Modified Date, datetime, readonly
..

:change_date: Modified Date, datetime, readonly

.. i18n: :file_size: File Size, integer, readonly
..

:file_size: File Size, integer, readonly

.. i18n: :directory: Directory, char, readonly
..

:directory: Directory, char, readonly

.. i18n: :partner: Partner, char, readonly
..

:partner: Partner, char, readonly

.. i18n: :type: Directory Type, char, readonly
..

:type: Directory Type, char, readonly

.. i18n: Object: Files details by Directory (report.document.file)
.. i18n: #########################################################
..

Object: Files details by Directory (report.document.file)
#########################################################

.. i18n: :nbr: # of Files, integer, readonly
..

:nbr: # of Files, integer, readonly

.. i18n: :month: Month, char, readonly
..

:month: Month, char, readonly

.. i18n: :file_size: File Size, integer, readonly
..

:file_size: File Size, integer, readonly

.. i18n: Object: Users that did not inserted documents since one month (report.document.wall)
.. i18n: ####################################################################################
..

Object: Users that did not inserted documents since one month (report.document.wall)
####################################################################################

.. i18n: :user_id: Owner, many2one, readonly
..

:user_id: Owner, many2one, readonly

.. i18n: :name: Month, date, readonly
..

:name: Month, date, readonly

.. i18n: :file_name: Last Posted File Name, char, readonly
..

:file_name: Last Posted File Name, char, readonly

.. i18n: :month: Month, char, readonly
..

:month: Month, char, readonly

.. i18n: :user: User, char, readonly
..

:user: User, char, readonly

.. i18n: :last: Last Posted Time, datetime, readonly
..

:last: Last Posted Time, datetime, readonly
