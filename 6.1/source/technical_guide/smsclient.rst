
.. i18n: .. module:: smsclient
.. i18n:     :synopsis: SMS Client 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: smsclient
    :synopsis: SMS Client 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/smsclient"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/smsclient"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: SMS Client (*smsclient*)
.. i18n: ========================
.. i18n: :Module: smsclient
.. i18n: :Name: SMS Client
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: smsclient
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   SMS Client module that provides:
.. i18n:       Sending SMS
.. i18n:       Use Multiple Gateways
..

::

  SMS Client module that provides:
      Sending SMS
      Use Multiple Gateways

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/smsclient.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/smsclient.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/smsclient.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/smsclient.zip>`_

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

.. i18n:  * Administration/Configuration/SMS Gateway
.. i18n:  * Administration/Configuration/SMS Gateway/Gateway List
.. i18n:  * Administration/Configuration/SMS Gateway/SMS Gateway History
.. i18n:  * Administration/Configuration/SMS Gateway/Message Queue
..

 * Administration/Configuration/SMS Gateway
 * Administration/Configuration/SMS Gateway/Gateway List
 * Administration/Configuration/SMS Gateway/SMS Gateway History
 * Administration/Configuration/SMS Gateway/Message Queue

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * sms.smsclient.form (form)
.. i18n:  * sms.smsclient.history.tree (tree)
.. i18n:  * sms.smsclient.history.form (form)
.. i18n:  * sms.smsclient.queue.tree (tree)
.. i18n:  * sms.smsclient.history.form (form)
.. i18n:  * \* INHERIT ir.actions.server.form.inherit (form)
..

 * sms.smsclient.form (form)
 * sms.smsclient.history.tree (tree)
 * sms.smsclient.history.form (form)
 * sms.smsclient.queue.tree (tree)
 * sms.smsclient.history.form (form)
 * \* INHERIT ir.actions.server.form.inherit (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: SMS Client (sms.smsclient)
.. i18n: ##################################
..

Object: SMS Client (sms.smsclient)
##################################

.. i18n: :property_ids: Parameters, one2many
..

:property_ids: Parameters, one2many

.. i18n: :history_line: History, one2many
..

:history_line: History, one2many

.. i18n: :code: Verification Code, char
..

:code: Verification Code, char

.. i18n: :name: Gateway Name, char, required
..

:name: Gateway Name, char, required

.. i18n: :url: Gateway URL, char, required
..

:url: Gateway URL, char, required

.. i18n: :body: Message, text
..

:body: Message, text

.. i18n:     *The message text that will be send along with the email which is send through this server*
..

    *The message text that will be send along with the email which is send through this server*

.. i18n: :users_id: Users Allowed, many2many
..

:users_id: Users Allowed, many2many

.. i18n: :state: Gateway Status, selection, readonly
..

:state: Gateway Status, selection, readonly

.. i18n: :method: API Method, selection
..

:method: API Method, selection

.. i18n: Object: SMS Queue (sms.smsclient.queue)
.. i18n: #######################################
..

Object: SMS Queue (sms.smsclient.queue)
#######################################

.. i18n: :gateway_id: SMS Gateway, many2one, readonly
..

:gateway_id: SMS Gateway, many2one, readonly

.. i18n: :name: SMS Request, text, required, readonly
..

:name: SMS Request, text, required, readonly

.. i18n: :mobile: Mobile No, char, required, readonly
..

:mobile: Mobile No, char, required, readonly

.. i18n: :date_create: Date, datetime, readonly
..

:date_create: Date, datetime, readonly

.. i18n: :state: Message Status, selection, readonly
..

:state: Message Status, selection, readonly

.. i18n: :error: Last Error, text, readonly
..

:error: Last Error, text, readonly

.. i18n: :msg: SMS Text, text, required, readonly
..

:msg: SMS Text, text, required, readonly

.. i18n: Object: SMS Client Properties (sms.smsclient.parms)
.. i18n: ###################################################
..

Object: SMS Client Properties (sms.smsclient.parms)
###################################################

.. i18n: :gateway_id: SMS Gateway, many2one
..

:gateway_id: SMS Gateway, many2one

.. i18n: :type: API Method, selection
..

:type: API Method, selection

.. i18n: :name: Property name, char, required
..

:name: Property name, char, required

.. i18n: :value: Property value, char, required
..

:value: Property value, char, required

.. i18n: Object: SMS Client History (sms.smsclient.history)
.. i18n: ##################################################
..

Object: SMS Client History (sms.smsclient.history)
##################################################

.. i18n: :gateway_id: SMS Gateway, many2one, required
..

:gateway_id: SMS Gateway, many2one, required

.. i18n: :user_id: Username, many2one, readonly
..

:user_id: Username, many2one, readonly

.. i18n: :name: Description, char, required, readonly
..

:name: Description, char, required, readonly

.. i18n: :sms: SMS, text, readonly
..

:sms: SMS, text, readonly

.. i18n: :date_create: Date, datetime, readonly
..

:date_create: Date, datetime, readonly

.. i18n: :to: Mobile No, char, readonly
..

:to: Mobile No, char, readonly
