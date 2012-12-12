
.. module:: smsclient
    :synopsis: SMS Client 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/smsclient"></div>
    <script src="http://js-kit.com/ratings.js"></script>

SMS Client (*smsclient*)
========================
:Module: smsclient
:Name: SMS Client
:Version: 5.0.1.0
:Author: Tiny
:Directory: smsclient
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  SMS Client module that provides:
      Sending SMS
      Use Multiple Gateways

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/smsclient.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/smsclient.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Administration/Configuration/SMS Gateway
 * Administration/Configuration/SMS Gateway/Gateway List
 * Administration/Configuration/SMS Gateway/SMS Gateway History
 * Administration/Configuration/SMS Gateway/Message Queue

Views
-----

 * sms.smsclient.form (form)
 * sms.smsclient.history.tree (tree)
 * sms.smsclient.history.form (form)
 * sms.smsclient.queue.tree (tree)
 * sms.smsclient.history.form (form)
 * \* INHERIT ir.actions.server.form.inherit (form)


Objects
-------

Object: SMS Client (sms.smsclient)
##################################



:property_ids: Parameters, one2many





:history_line: History, one2many





:code: Verification Code, char





:name: Gateway Name, char, required





:url: Gateway URL, char, required





:body: Message, text

    *The message text that will be send along with the email which is send through this server*



:users_id: Users Allowed, many2many





:state: Gateway Status, selection, readonly





:method: API Method, selection




Object: SMS Queue (sms.smsclient.queue)
#######################################



:gateway_id: SMS Gateway, many2one, readonly





:name: SMS Request, text, required, readonly





:mobile: Mobile No, char, required, readonly





:date_create: Date, datetime, readonly





:state: Message Status, selection, readonly





:error: Last Error, text, readonly





:msg: SMS Text, text, required, readonly




Object: SMS Client Properties (sms.smsclient.parms)
###################################################



:gateway_id: SMS Gateway, many2one





:type: API Method, selection





:name: Property name, char, required





:value: Property value, char, required




Object: SMS Client History (sms.smsclient.history)
##################################################



:gateway_id: SMS Gateway, many2one, required





:user_id: Username, many2one, readonly





:name: Description, char, required, readonly





:sms: SMS, text, readonly





:date_create: Date, datetime, readonly





:to: Mobile No, char, readonly


