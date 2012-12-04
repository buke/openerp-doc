
.. module:: gnucash
    :synopsis: Module for Import from file 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/gnucash"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Module for Import from file (*gnucash*)
=======================================
:Module: gnucash
:Name: Module for Import from file
:Version: 5.0.0.1
:Author: P. Christeas
:Directory: gnucash
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Gnucash Import from file

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/gnucash.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/gnucash.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`

Reports
-------

None


Menus
-------

 * Administration/GnuCash
 * Administration/GnuCash/Gnucash Mappings
 * Administration/GnuCash/Import GnuCash File

Views
-----

 * gnucash.index.form (form)
 * gnucash.index.tree (tree)


Objects
-------

Object: gnucash.index (gnucash.index)
#####################################



:noupdate: Non Updatable, boolean





:parent_book: Parent book, many2one





:date_init: Init Date, datetime





:date_update: Update Date, datetime





:module: Module, char, required





:to_delete: Should be deleted, boolean, required





:model: Object, char, required





:guid: Gnucash UID, char, required





:res_id: Resource ID, integer


