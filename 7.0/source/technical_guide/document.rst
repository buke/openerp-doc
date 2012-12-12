
.. module:: document
    :synopsis: Integrated Document Management System (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/document"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Integrated Document Management System (*document*)
==================================================
:Module: document
:Name: Integrated Document Management System
:Version: 5.0.1.0
:Author: Tiny
:Directory: document
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This is a complete document management system:
      * FTP Interface
      * User Authentication
      * Document Indexation
  
      ATTENTION: 
      - When you install this module in a running company that already has PDF files stored in the database, 
        you will lose them all. 
      - After installing this module PDF's are no longer stored in the database, 
        but in the server's filesystem like /server/bin/filestore.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/document.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/document.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`process`

Reports
-------

None


Menus
-------

 * Document Management
 * Document Management/Document Configuration
 * Document Management/Document Configuration/Directories
 * Document Management/Document Configuration/Directorie's Structure
 * Document Management/Browse Files Using FTP
 * Document Management/Search a File

Views
-----

 * document.directory (form)
 * document.directory (tree)
 * ir.attachment (form)
 * ir.attachment (tree)
 * \* INHERIT ir.attachment.view.inherit (form)
 * \* INHERIT process.node.form (form)
 * \* INHERIT process.process.form (form)
 * Auto Configure Directory (form)


Objects
-------

Object: Document directory (document.directory)
###############################################



:create_uid: Creator, many2one, readonly





:domain: Domain, char

    *Use a domain if you want to apply an automatic filter on visible resources.*



:group_ids: Groups, many2many





:create_date: Date Created, datetime, readonly





:ressource_type_id: Directories Mapped to Objects, many2one

    *Select an object here and OpenERP will create a mapping for each of these objects, using the given domain, when browsing through FTP.*



:ressource_tree: Tree Structure, boolean

    *Check this if you want to use the same tree structure as the object selected in the system.*



:file_type: Content Type, char





:content_ids: Virtual Files, one2many





:child_ids: Children, one2many





:file_ids: Files, one2many





:write_uid: Last Modification User, many2one, readonly





:parent_id: Parent Item, many2one





:ressource_parent_type_id: Parent Model, many2one

    *If you put an object here, this directory template will appear bellow all of these objects. Don't put a parent directory if you select a parent model.*



:write_date: Date Modified, datetime, readonly





:user_id: Owner, many2one





:ressource_id: Resource ID, integer





:type: Type, selection, required





:name: Name, char, required




Object: Directory Content Type (document.directory.content.type)
################################################################



:active: Active, boolean





:code: Extension, char





:name: Content Type, char, required




Object: Directory Content (document.directory.content)
######################################################



:suffix: Suffix, char





:extension: Document Type, selection, required





:sequence: Sequence, integer





:name: Content Name, char, required





:directory_id: Directory, many2one





:include_name: Include Record Name, boolean

    *Check this field if you want that the name of the file start by the record name.*



:report_id: Report, many2one




Object: document.configuration.wizard (document.configuration.wizard)
#####################################################################



:host: Server Address, char, required

    *Put here the server address or IP. Keep localhost if you don't know what to write.*
