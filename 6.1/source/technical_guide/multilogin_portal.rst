
.. module:: multilogin_portal
    :synopsis: Multilogin portal 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/multilogin_portal"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Multilogin portal (*multilogin_portal*)
=======================================
:Module: multilogin_portal
:Name: Multilogin portal
:Version: 5.0.1.0
:Author: Ferme Urbaine
:Directory: multilogin_portal
:Web: http://www.lafermedusart.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Allows xmlrpc queries from partners email+password as:
  	- Customer standard user
  	- Provider standard user
  
  Allows xmlrpc queries from computers (IP automatically recognized) as:
  	- Computer standard user
  
  Standard users are set into res.company.
  For multi-company, please alter this code.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/multilogin_portal.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/multilogin_portal.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Administration/Configuration/Computers

Views
-----

 * \* INHERIT res.company.form (form)
 * res.computer.tree (tree)


Objects
-------

Object: Computers (res.computer)
################################



:active: Active, boolean





:state: State, selection, required





:ip_address: IP address, char, required





:name: Name, char, required


