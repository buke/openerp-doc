
.. module:: smtpclient
    :synopsis: Email Client 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/smtpclient"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Email Client (*smtpclient*)
===========================
:Module: smtpclient
:Name: Email Client
:Version: 5.0.1.0
:Author: Tiny
:Directory: smtpclient
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Email Client module that provides:
      Sending Email
      Use Multiple Server
      Multi Threading
      Multi Attachment

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/smtpclient.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/smtpclient.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Administration/Configuration/Email Servers
 * Administration/Configuration/Email Servers/SMTP Server
 * Administration/Configuration/Email Servers/Email Server History
 * Administration/Configuration/Email Servers/Message Queue

Views
-----

 * \* INHERIT ir.actions.server.form.inherit (form)
 * report.smtp.server.tree (tree)
 * report.smtp.server.form (form)
 * \* INHERIT smtp.company.form (form)
 * email.smtpclient.form (form)
 * email.smtpclient.form (tree)
 * email.smtpclient.history.tree (tree)
 * email.smtpclient.history.form (form)
 * email.smtpclient.queue.tree (tree)
 * email.smtpclient.queue.form (form)


Objects
-------

Object: Email Client (email.smtpclient)
#######################################



:body: Message, text

    *The message text that will be send along with the email which is send through this server*



:history_line: History, one2many





:code: Verification Code, char





:name: Server Name, char, required





:use_debug: Show debugging information, boolean





:test_email: Test Message, text





:server: SMTP Server, char, required, readonly





:from_email: Email From, char, required, readonly





:date_create: Date Create, date, required, readonly





:ssl: Use SSL?, boolean, readonly





:state: Server Status, selection, readonly





:email: Email Address, char, required, readonly





:server_statistics: Statistics, one2many





:user: User Name, char, readonly





:active: Active, boolean





:verify_email: Verify Message, text, readonly





:password: Password, char, readonly





:type: Server Type, selection, required





:port: SMTP Port, char, required, readonly





:use_auth: Use Authentication, boolean, readonly





:users_id: Users Allowed, many2many




Object: Email Client History (email.smtpclient.history)
#######################################################



:server_id: Smtp Server, many2one, required, readonly





:user_id: Username, many2one, readonly





:name: Description, text, required, readonly





:resource_id: Resource ID, integer, readonly





:date_create: Date, datetime, readonly





:model: Model, many2one, readonly





:email: Email, char, readonly




Object: Email Queue (email.smtpclient.queue)
############################################



:body: Email Text, text, readonly





:server_id: SMTP Server, many2one, readonly





:serialized_message: Message, text, readonly





:name: Subject, char, readonly





:cc: CC to, char, readonly





:bcc: BCC to, char, readonly





:date_create: Date, datetime, readonly





:to: Mail to, char, readonly





:state: Message Status, selection, readonly





:error: Last Error, text, readonly




Object: Server Statistics (report.smtp.server)
##############################################



:server_id: Server ID, many2one, readonly





:no: Total No., integer, readonly





:name: Server, char, readonly





:history: History, char, readonly




Object: res.company.address (res.company.address)
#################################################



:email: Email Address, many2one, required





:name: Address Type, selection, required





:company_id: Company, many2one, required


