.. i18n: .. module:: wiki
.. i18n:     :synopsis: Document Management - Wiki (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: wiki
    :synopsis: Document Management - Wiki (Official, Quality Certified)
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

.. tip:: 本模块是业界领先的开源企业管理系统OpenERP的一部分。如果你想探索OpenERP，请查看我们的 
  `截屏 <http://openerp.tv>`_ 或直接下载 
  `OpenERP <http://openerp.com>`_ .

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/wiki"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/wiki"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Document Management - Wiki (*wiki*)
.. i18n: ===================================
.. i18n: :Module: wiki
.. i18n: :Name: Document Management - Wiki
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny & Axelor
.. i18n: :Directory: wiki
.. i18n: :Web: http://openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Document Management - Wiki (*wiki*)
===================================
:Module: wiki
:Name: Document Management - Wiki
:Version: 5.0.1.0
:Author: Tiny & Axelor
:Directory: wiki
:Web: http://openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   The base module to manage documents(wiki) 
.. i18n:       
.. i18n:       keep track for the wiki groups, pages, and history
..

::

  The base module to manage documents(wiki) 
      
      keep track for the wiki groups, pages, and history

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/wiki.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/wiki.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/wiki.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/wiki.zip>`_

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
.. i18n:  * Document Management/Wiki Configuration
.. i18n:  * Document Management/Wiki
.. i18n:  * Document Management/Wiki Configuration/Wiki Groups
.. i18n:  * Document Management/Wiki/Wiki Groups
.. i18n:  * Document Management/Wiki/Wiki Pages
.. i18n:  * Document Management/Wiki Configuration/All Page Histories
..

 * Document Management
 * Document Management/Wiki Configuration
 * Document Management/Wiki
 * Document Management/Wiki Configuration/Wiki Groups
 * Document Management/Wiki/Wiki Groups
 * Document Management/Wiki/Wiki Pages
 * Document Management/Wiki Configuration/All Page Histories

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * wiki.groups.tree (tree)
.. i18n:  * wiki.groups.form (form)
.. i18n:  * wiki.wiki.tree (tree)
.. i18n:  * wiki.wiki.form (form)
.. i18n:  * wiki.wiki.history.tree (tree)
.. i18n:  * wiki.wiki.history.form (form)
.. i18n:  * Differences (form)
..

 * wiki.groups.tree (tree)
 * wiki.groups.form (form)
 * wiki.wiki.tree (tree)
 * wiki.wiki.form (form)
 * wiki.wiki.history.tree (tree)
 * wiki.wiki.history.form (form)
 * Differences (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: wiki.wiki (wiki.wiki)
.. i18n: #############################
..

Object: wiki.wiki (wiki.wiki)
#############################

.. i18n: :create_uid: Author, many2one
..

:create_uid: Author, many2one

.. i18n: :group_id: Wiki Group, many2one
..

:group_id: Wiki Group, many2one

.. i18n: :create_date: Created on, datetime
..

:create_date: Created on, datetime

.. i18n: :name: Title, char, required
..

:name: Title, char, required

.. i18n: :tags: Tags, char
..

:tags: Tags, char

.. i18n: :minor_edit: Minor edit, boolean
..

:minor_edit: Minor edit, boolean

.. i18n: :history_id: History Lines, one2many
..

:history_id: History Lines, one2many

.. i18n: :summary: Summary, char
..

:summary: Summary, char

.. i18n: :text_area: Content, text
..

:text_area: Content, text

.. i18n: :write_date: Modification Date, datetime
..

:write_date: Modification Date, datetime

.. i18n: :review: Need Review, boolean
..

:review: Need Review, boolean

.. i18n: :toc: Table of Contents, boolean
..

:toc: Table of Contents, boolean

.. i18n: :write_uid: Last Author, many2one
..

:write_uid: Last Author, many2one

.. i18n: :section: Section, char
..

:section: Section, char

.. i18n:     *Use page section code like 1.2.1*
..

    *Use page section code like 1.2.1*

.. i18n: Object: Wiki Groups (wiki.groups)
.. i18n: #################################
..

Object: Wiki Groups (wiki.groups)
#################################

.. i18n: :create_date: Created Date, datetime
..

:create_date: Created Date, datetime

.. i18n: :name: Wiki Group, char, required
..

:name: Wiki Group, char, required

.. i18n: :notes: Description, text
..

:notes: Description, text

.. i18n: :child_ids: Child Groups, one2many
..

:child_ids: Child Groups, one2many

.. i18n: :parent_id: Parent Group, many2one
..

:parent_id: Parent Group, many2one

.. i18n: :page_ids: Pages, one2many
..

:page_ids: Pages, one2many

.. i18n: :template: Wiki Template, text
..

:template: Wiki Template, text

.. i18n: :home: Pages, many2one
..

:home: Pages, many2one

.. i18n: :section: Make Section ?, boolean
..

:section: Make Section ?, boolean

.. i18n: Object: Wiki Groups Links (wiki.groups.link)
.. i18n: ############################################
..

Object: Wiki Groups Links (wiki.groups.link)
############################################

.. i18n: :group_id: Parent Group, many2one
..

:group_id: Parent Group, many2one

.. i18n: :action_id: Menu, many2one
..

:action_id: Menu, many2one

.. i18n: Object: Wiki History (wiki.wiki.history)
.. i18n: ########################################
..

Object: Wiki History (wiki.wiki.history)
########################################

.. i18n: :create_date: Date, datetime
..

:create_date: Date, datetime

.. i18n: :minor_edit: This is a major edit ?, boolean
..

:minor_edit: This is a major edit ?, boolean

.. i18n: :write_uid: Modify By, many2one
..

:write_uid: Modify By, many2one

.. i18n: :text_area: Text area, text
..

:text_area: Text area, text

.. i18n: :wiki_id: Wiki Id, many2one
..

:wiki_id: Wiki Id, many2one

.. i18n: :summary: Summary, char
..

:summary: Summary, char

.. i18n: Object: wizard.wiki.history.show_diff (wizard.wiki.history.show_diff)
.. i18n: #####################################################################
..

Object: wizard.wiki.history.show_diff (wizard.wiki.history.show_diff)
#####################################################################

.. i18n: :diff: Diff, text
..

:diff: Diff, text
