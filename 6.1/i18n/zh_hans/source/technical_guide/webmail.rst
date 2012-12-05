
.. i18n: .. module:: webmail
.. i18n:     :synopsis: Webmail 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: webmail
    :synopsis: Webmail 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/webmail"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/webmail"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Webmail (*webmail*)
.. i18n: ===================
.. i18n: :Module: webmail
.. i18n: :Name: Webmail
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: webmail
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Webmail module covers:
.. i18n:           - Mail server configuration.
.. i18n:           - Sending and Receiving mail
..

::

  Webmail module covers:
          - Mail server configuration.
          - Sending and Receiving mail

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/webmail.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/webmail.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/webmail.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/webmail.zip>`_

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

.. i18n:  * Webmail
.. i18n:  * Webmail/Configuration
.. i18n:  * Webmail/Configuration/Server
.. i18n:  * Webmail/Compose Mail
..

 * Webmail
 * Webmail/Configuration
 * Webmail/Configuration/Server
 * Webmail/Compose Mail

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * webmail.server.tree (tree)
.. i18n:  * webmail.server.form (form)
.. i18n:  * webmail.tiny.user.form (form)
.. i18n:  * webmail.mailbox.tree (tree)
.. i18n:  * webmail.email.compose.form (form)
.. i18n:  * webmail.email.read.form (form)
..

 * webmail.server.tree (tree)
 * webmail.server.form (form)
 * webmail.tiny.user.form (form)
 * webmail.mailbox.tree (tree)
 * webmail.email.compose.form (form)
 * webmail.email.read.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: User Configuration (webmail.tiny.user)
.. i18n: ##############################################
..

Object: User Configuration (webmail.tiny.user)
##############################################

.. i18n: :server_conf_id: Configuration, one2many
..

:server_conf_id: Configuration, one2many

.. i18n: :user_id: User, many2one
..

:user_id: User, many2one

.. i18n: Object: Mail Server Configuration (webmail.server)
.. i18n: ##################################################
..

Object: Mail Server Configuration (webmail.server)
##################################################

.. i18n: :iconn_port: Port, integer
..

:iconn_port: Port, integer

.. i18n: :server_id: Mail Client, many2one
..

:server_id: Mail Client, many2one

.. i18n: :iserver_type: Server Type, selection
..

:iserver_type: Server Type, selection

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :oconn_type: SSL, boolean
..

:oconn_type: SSL, boolean

.. i18n: :oconn_port: Port, integer
..

:oconn_port: Port, integer

.. i18n: :iserver_name: Server Name, char, required
..

:iserver_name: Server Name, char, required

.. i18n: :oserver_name: Server Name, char, required
..

:oserver_name: Server Name, char, required

.. i18n: :iconn_type: SSL, boolean
..

:iconn_type: SSL, boolean

.. i18n: :password: Password, char, required
..

:password: Password, char, required

.. i18n: :user_name: User Name, char, required
..

:user_name: User Name, char, required

.. i18n: Object: User Mailbox (webmail.mailbox)
.. i18n: ######################################
..

Object: User Mailbox (webmail.mailbox)
######################################

.. i18n: :parent_id: Parent Folder, many2one
..

:parent_id: Parent Folder, many2one

.. i18n: :child_id: Child Folder, one2many
..

:child_id: Child Folder, one2many

.. i18n: :user_id: User, many2one
..

:user_id: User, many2one

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :account_id: Server, many2one
..

:account_id: Server, many2one

.. i18n: Object: Email Tag (webmail.tags)
.. i18n: ################################
..

Object: Email Tag (webmail.tags)
################################

.. i18n: :user_id: User, many2one
..

:user_id: User, many2one

.. i18n: :name: Tag Name, char
..

:name: Tag Name, char

.. i18n: :account_id: Server, many2one
..

:account_id: Server, many2one

.. i18n: Object: User Email (webmail.email)
.. i18n: ##################################
..

Object: User Email (webmail.email)
##################################

.. i18n: :body: Body, text
..

:body: Body, text

.. i18n: :user_id: User, many2one
..

:user_id: User, many2one

.. i18n: :account_id: Server, many2one
..

:account_id: Server, many2one

.. i18n: :cc: Cc, char
..

:cc: Cc, char

.. i18n: :tag_id: Tags, many2one
..

:tag_id: Tags, many2one

.. i18n: :bcc: Bcc, char
..

:bcc: Bcc, char

.. i18n: :to: To, char
..

:to: To, char

.. i18n: :folder_id: Folder, many2one
..

:folder_id: Folder, many2one

.. i18n: :from_user: From, char
..

:from_user: From, char

.. i18n: :date: Date, datetime
..

:date: Date, datetime

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :message_id: Message Id, char
..

:message_id: Message Id, char

.. i18n: :subject: Subject, char
..

:subject: Subject, char
