
.. i18n: .. module:: document_webdav_old
.. i18n:     :synopsis: Integrated Document Management System 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: document_webdav_old
    :synopsis: Integrated Document Management System 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/document_webdav_old"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/document_webdav_old"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Integrated Document Management System (*document_webdav_old*)
.. i18n: =============================================================
.. i18n: :Module: document_webdav_old
.. i18n: :Name: Integrated Document Management System
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: document_webdav_old
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This is a complete document management system:
.. i18n:   	* WebDav Interface
.. i18n:   	* User Authentication
.. i18n:   	* Document Indexation
..

::

  This is a complete document management system:
  	* WebDav Interface
  	* User Authentication
  	* Document Indexation

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/document_webdav_old.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/document_webdav_old.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/document_webdav_old.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/document_webdav_old.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
..

 * :mod:`base`

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
.. i18n:  * Document Management/Configuration/Directories
.. i18n:  * Document Management/Directorie's Structure
.. i18n:  * Document Management/Search a File
..

 * Document Management
 * Document Management/Configuration/Directories
 * Document Management/Directorie's Structure
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
..

 * document.directory (form)
 * document.directory (tree)
 * ir.attachment (form)
 * ir.attachment (tree)
 * \* INHERIT ir.attachment.view.inherit (form)

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

.. i18n: :group_ids: Groups, many2many
..

:group_ids: Groups, many2many

.. i18n: :create_date: Date Created, datetime, readonly
..

:create_date: Date Created, datetime, readonly

.. i18n: :ressource_type_id: Resource Model, many2one
..

:ressource_type_id: Resource Model, many2one

.. i18n: :ressource_tree: Tree Structure, boolean
..

:ressource_tree: Tree Structure, boolean

.. i18n: :file_type: Content Type, char
..

:file_type: Content Type, char

.. i18n: :content_ids: Virtual Files, one2many
..

:content_ids: Virtual Files, one2many

.. i18n: :child_ids: Childs, one2many
..

:child_ids: Childs, one2many

.. i18n: :file_ids: Files, one2many
..

:file_ids: Files, one2many

.. i18n: :write_uid: Last Modification User, many2one, readonly
..

:write_uid: Last Modification User, many2one, readonly

.. i18n: :parent_id: Parent Item, many2one
..

:parent_id: Parent Item, many2one

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

.. i18n: Object: Directory Content (document.directory.content)
.. i18n: ######################################################
..

Object: Directory Content (document.directory.content)
######################################################

.. i18n: :suffix: Suffix, char
..

:suffix: Suffix, char

.. i18n: :extension: Extension, selection, required
..

:extension: Extension, selection, required

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :name: Content Name, char, required
..

:name: Content Name, char, required

.. i18n: :directory_id: Directory, many2one
..

:directory_id: Directory, many2one

.. i18n: :versioning: Versioning, boolean
..

:versioning: Versioning, boolean

.. i18n: :report_id: Report, many2one, required
..

:report_id: Report, many2one, required
