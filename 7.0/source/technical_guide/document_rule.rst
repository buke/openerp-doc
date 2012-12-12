
.. module:: document_rule
    :synopsis: Extension Module of Document Management System 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/document_rule"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Extension Module of Document Management System (*document_rule*)
================================================================
:Module: document_rule
:Name: Extension Module of Document Management System
:Version: 5.0.1.0
:Author: Tiny
:Directory: document_rule
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  This is  module of document management system with
       Implementation of document rule

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/document_rule.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/document_rule.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`process`
 * :mod:`document`

Reports
-------

None


Menus
-------

 * Document Management/Document Configuration/Document Rules

Views
-----

 * document.rule (form)
 * document.rule (tree)


Objects
-------

Object: Document Rule (document.rule)
#####################################



:act_assign_user_id: Assign to User, many2one





:resource_object: Resource Name, char





:author: Author, many2one





:act_assign_partner_id: Assign to Partner, many2one





:date_type: Trigger Date, selection





:sequence: Sequence, integer





:directory_id: Directory, many2one





:server_act: Action, many2one





:act_move_directory_id: Move to, many2one





:active: Active, boolean





:filename: File, many2one





:partner_id: Partner, many2one





:act_copy_directory_id: Copy to, many2one





:name: Name, char, required


