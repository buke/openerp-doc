
.. module:: webmail
    :synopsis: Webmail 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/webmail"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Webmail (*webmail*)
===================
:Module: webmail
:Name: Webmail
:Version: 5.0.1.0
:Author: Tiny
:Directory: webmail
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Webmail module covers:
          - Mail server configuration.
          - Sending and Receiving mail

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/webmail.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/webmail.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Webmail
 * Webmail/Configuration
 * Webmail/Configuration/Server
 * Webmail/Compose Mail

Views
-----

 * webmail.server.tree (tree)
 * webmail.server.form (form)
 * webmail.tiny.user.form (form)
 * webmail.mailbox.tree (tree)
 * webmail.email.compose.form (form)
 * webmail.email.read.form (form)


Objects
-------

Object: User Configuration (webmail.tiny.user)
##############################################



:server_conf_id: Configuration, one2many





:user_id: User, many2one




Object: Mail Server Configuration (webmail.server)
##################################################



:iconn_port: Port, integer





:server_id: Mail Client, many2one





:iserver_type: Server Type, selection





:name: Name, char, required





:oconn_type: SSL, boolean





:oconn_port: Port, integer





:iserver_name: Server Name, char, required





:oserver_name: Server Name, char, required





:iconn_type: SSL, boolean





:password: Password, char, required





:user_name: User Name, char, required




Object: User Mailbox (webmail.mailbox)
######################################



:parent_id: Parent Folder, many2one





:child_id: Child Folder, one2many





:user_id: User, many2one





:name: Name, char, required





:account_id: Server, many2one




Object: Email Tag (webmail.tags)
################################



:user_id: User, many2one





:name: Tag Name, char





:account_id: Server, many2one




Object: User Email (webmail.email)
##################################



:body: Body, text





:user_id: User, many2one





:account_id: Server, many2one





:cc: Cc, char





:tag_id: Tags, many2one





:bcc: Bcc, char





:to: To, char





:folder_id: Folder, many2one





:from_user: From, char





:date: Date, datetime





:active: Active, boolean





:message_id: Message Id, char





:subject: Subject, char


