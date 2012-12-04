
.. module:: zarafa
    :synopsis: Zarafa Integration 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/zarafa"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Zarafa Integration (*zarafa*)
=============================
:Module: zarafa
:Name: Zarafa Integration
:Version: 5.0.1.0
:Author: Sednacom
:Directory: zarafa
:Web: http://www.sednacom.fr
:Official module: no
:Quality certified: no

Description
-----------

::

  New objects and views to improve use of OpenERP:
   * shortcuts view
   * module view
   * email object
   * Zarafa tools

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/zarafa.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/zarafa.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`crm`

Reports
-------

None


Menus
-------

 * Administration/Modules Management/Modules by Sednacom
 * Tools/Shortcuts
 * Tools/Import contact from Zarafa
 * Tools/Emails

Views
-----

 * \* INHERIT res.users.form.zarafa (form)
 * \* INHERIT res.partner.address.tree.email (tree)
 * sednacom.email.form (form)
 * sednacom.email.tree (tree)


Objects
-------

Object: sednacom.email (sednacom.email)
#######################################



:body: Message, text, readonly





:name: Title, char, required, readonly





:recipients: Contacts, many2many, readonly





:datetime: Date, datetime, readonly





:to: To, char, readonly





:state: State, selection, readonly





:exp: From, char, required, readonly





:crm_case: Case, many2one, readonly




Object: Contacts, with features to import from Zarafa server (zarafa.contact)
#############################################################################



:fax: Fax, char





:name: Name, char, required





:mobile: Mobile, char





:company: Company, char





:state: State, selection, readonly





:phone: Phone, char





:zid: Z-Id, char, required





:email: Email, char, required


