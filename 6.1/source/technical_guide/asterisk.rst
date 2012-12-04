
.. module:: asterisk
    :synopsis: Asterisk - Manage Asterisk servers and IP phones. 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/asterisk"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Asterisk - Manage Asterisk servers and IP phones. (*asterisk*)
==============================================================
:Module: asterisk
:Name: Asterisk - Manage Asterisk servers and IP phones.
:Version: 5.0.0.1proto2
:Author: Tiny
:Directory: asterisk
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Manages a list of asterisk servers and IP phones.
  This module implements a system to popup the partner form based on phone calls.
  This is still a proof of concept, that have been made during Tiny ERP's
  technical training session.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/asterisk.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/asterisk.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Sys Admin
 * Sys Admin/Configuration
 * Sys Admin/Configuration/Asterisk Server
 * Sys Admin/Configuration/IP Phones
 * Sys Admin/Get Partner From Call

Views
-----

 * Asterisk Server (tree)
 * Asterisk Server (form)
 * IP Phone (tree)
 * IP Phone (form)


Objects
-------

Object: asterisk.server (asterisk.server)
#########################################



:host: Server Host, char, required





:login: Login, char





:password: Password, char





:port: Server Port, integer, required





:name: Asterisk Server, char, required




Object: IP Phone (asterisk.phone)
#################################



:current_callerid: Current Caller, char





:user_id: User, many2one, required





:name: Phone Name, char, required





:ip: Phone IP, char





:state: State, selection





:phoneid: Phone ID, char





:asterisk_id: Asterisk Server, many2one, required


