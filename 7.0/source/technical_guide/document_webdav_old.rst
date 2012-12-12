
.. module:: document_webdav_old
    :synopsis: Integrated Document Management System 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/document_webdav_old"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Integrated Document Management System (*document_webdav_old*)
=============================================================
:Module: document_webdav_old
:Name: Integrated Document Management System
:Version: 5.0.1.0
:Author: Tiny
:Directory: document_webdav_old
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This is a complete document management system:
  	* WebDav Interface
  	* User Authentication
  	* Document Indexation

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/document_webdav_old.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/document_webdav_old.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Document Management
 * Document Management/Configuration/Directories
 * Document Management/Directorie's Structure
 * Document Management/Search a File

Views
-----

 * document.directory (form)
 * document.directory (tree)
 * ir.attachment (form)
 * ir.attachment (tree)
 * \* INHERIT ir.attachment.view.inherit (form)


Objects
-------

Object: Document directory (document.directory)
###############################################



:create_uid: Creator, many2one, readonly





:domain: Domain, char





:group_ids: Groups, many2many





:create_date: Date Created, datetime, readonly





:ressource_type_id: Resource Model, many2one





:ressource_tree: Tree Structure, boolean





:file_type: Content Type, char





:content_ids: Virtual Files, one2many





:child_ids: Childs, one2many





:file_ids: Files, one2many





:write_uid: Last Modification User, many2one, readonly





:parent_id: Parent Item, many2one





:write_date: Date Modified, datetime, readonly





:user_id: Owner, many2one





:ressource_id: Resource ID, integer





:type: Type, selection, required





:name: Name, char, required




Object: Directory Content (document.directory.content)
######################################################



:suffix: Suffix, char





:extension: Extension, selection, required





:sequence: Sequence, integer





:name: Content Name, char, required





:directory_id: Directory, many2one





:versioning: Versioning, boolean





:report_id: Report, many2one, required


