
.. i18n: .. module:: document
.. i18n:     :synopsis: Integrated Document Management System (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: document
    :synopsis: Integrated Document Management System (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/document"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/document"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Integrated Document Management System (*document*)
.. i18n: ==================================================
.. i18n: :Module: document
.. i18n: :Name: Integrated Document Management System
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: document
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This is a complete document management system:
.. i18n:       * FTP Interface
.. i18n:       * User Authentication
.. i18n:       * Document Indexation
.. i18n:   
.. i18n:       ATTENTION: 
.. i18n:       - When you install this module in a running company that already has PDF files stored in the database, 
.. i18n:         you will lose them all. 
.. i18n:       - After installing this module PDF's are no longer stored in the database, 
.. i18n:         but in the server's filesystem like /server/bin/filestore.
..

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

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/document.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/document.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/document.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/document.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`process`
..

 * :mod:`base`
 * :mod:`process`

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
.. i18n:  * Document Management/Document Configuration
.. i18n:  * Document Management/Document Configuration/Directories
.. i18n:  * Document Management/Document Configuration/Directorie's Structure
.. i18n:  * Document Management/Browse Files Using FTP
.. i18n:  * Document Management/Search a File
..

 * Document Management
 * Document Management/Document Configuration
 * Document Management/Document Configuration/Directories
 * Document Management/Document Configuration/Directorie's Structure
 * Document Management/Browse Files Using FTP
 * Document Management/Search a File

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * document.directory (form)
.. i18n:  * document.directory (tree)
.. i18n:  * ir.attachment (form)
.. i18n:  * ir.attachment (tree)
.. i18n:  * \* INHERIT ir.attachment.view.inherit (form)
.. i18n:  * \* INHERIT process.node.form (form)
.. i18n:  * \* INHERIT process.process.form (form)
.. i18n:  * Auto Configure Directory (form)
..

 * document.directory (form)
 * document.directory (tree)
 * ir.attachment (form)
 * ir.attachment (tree)
 * \* INHERIT ir.attachment.view.inherit (form)
 * \* INHERIT process.node.form (form)
 * \* INHERIT process.process.form (form)
 * Auto Configure Directory (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Document directory (document.directory)
.. i18n: ###############################################
..

Object: Document directory (document.directory)
###############################################

.. i18n: :create_uid: Creator, many2one, readonly
..

:create_uid: Creator, many2one, readonly

.. i18n: :domain: Domain, char
..

:domain: Domain, char

.. i18n:     *Use a domain if you want to apply an automatic filter on visible resources.*
..

    *Use a domain if you want to apply an automatic filter on visible resources.*

.. i18n: :group_ids: Groups, many2many
..

:group_ids: Groups, many2many

.. i18n: :create_date: Date Created, datetime, readonly
..

:create_date: Date Created, datetime, readonly

.. i18n: :ressource_type_id: Directories Mapped to Objects, many2one
..

:ressource_type_id: Directories Mapped to Objects, many2one

.. i18n:     *Select an object here and OpenERP will create a mapping for each of these objects, using the given domain, when browsing through FTP.*
..

    *Select an object here and OpenERP will create a mapping for each of these objects, using the given domain, when browsing through FTP.*

.. i18n: :ressource_tree: Tree Structure, boolean
..

:ressource_tree: Tree Structure, boolean

.. i18n:     *Check this if you want to use the same tree structure as the object selected in the system.*
..

    *Check this if you want to use the same tree structure as the object selected in the system.*

.. i18n: :file_type: Content Type, char
..

:file_type: Content Type, char

.. i18n: :content_ids: Virtual Files, one2many
..

:content_ids: Virtual Files, one2many

.. i18n: :child_ids: Children, one2many
..

:child_ids: Children, one2many

.. i18n: :file_ids: Files, one2many
..

:file_ids: Files, one2many

.. i18n: :write_uid: Last Modification User, many2one, readonly
..

:write_uid: Last Modification User, many2one, readonly

.. i18n: :parent_id: Parent Item, many2one
..

:parent_id: Parent Item, many2one

.. i18n: :ressource_parent_type_id: Parent Model, many2one
..

:ressource_parent_type_id: Parent Model, many2one

.. i18n:     *If you put an object here, this directory template will appear bellow all of these objects. Don't put a parent directory if you select a parent model.*
..

    *If you put an object here, this directory template will appear bellow all of these objects. Don't put a parent directory if you select a parent model.*

.. i18n: :write_date: Date Modified, datetime, readonly
..

:write_date: Date Modified, datetime, readonly

.. i18n: :user_id: Owner, many2one
..

:user_id: Owner, many2one

.. i18n: :ressource_id: Resource ID, integer
..

:ressource_id: Resource ID, integer

.. i18n: :type: Type, selection, required
..

:type: Type, selection, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: Directory Content Type (document.directory.content.type)
.. i18n: ################################################################
..

Object: Directory Content Type (document.directory.content.type)
################################################################

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :code: Extension, char
..

:code: Extension, char

.. i18n: :name: Content Type, char, required
..

:name: Content Type, char, required

.. i18n: Object: Directory Content (document.directory.content)
.. i18n: ######################################################
..

Object: Directory Content (document.directory.content)
######################################################

.. i18n: :suffix: Suffix, char
..

:suffix: Suffix, char

.. i18n: :extension: Document Type, selection, required
..

:extension: Document Type, selection, required

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :name: Content Name, char, required
..

:name: Content Name, char, required

.. i18n: :directory_id: Directory, many2one
..

:directory_id: Directory, many2one

.. i18n: :include_name: Include Record Name, boolean
..

:include_name: Include Record Name, boolean

.. i18n:     *Check this field if you want that the name of the file start by the record name.*
..

    *Check this field if you want that the name of the file start by the record name.*

.. i18n: :report_id: Report, many2one
..

:report_id: Report, many2one

.. i18n: Object: document.configuration.wizard (document.configuration.wizard)
.. i18n: #####################################################################
..

Object: document.configuration.wizard (document.configuration.wizard)
#####################################################################

.. i18n: :host: Server Address, char, required
..

:host: Server Address, char, required

.. i18n:     *Put here the server address or IP. Keep localhost if you don't know what to write.*
..

    *Put here the server address or IP. Keep localhost if you don't know what to write.*
