
.. module:: wiki_extension
    :synopsis: Document Management - Wiki Extension 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/wiki_extension"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Document Management - Wiki Extension (*wiki_extension*)
=======================================================
:Module: wiki_extension
:Name: Document Management - Wiki Extension
:Version: 5.0.1.0
:Author: SYLEAM Info Services
:Directory: wiki_extension
:Web: http://Syleam.fr
:Official module: no
:Quality certified: no

Description
-----------

::

  The base module to manage documents(wiki) 
  
      Add new features :
      - members in wiki groups
      - state in page wiki (Running, Raed Only, Obsolete)
      - improvement view

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`base`
 * :mod:`wiki`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT wiki.groups.form.extension (form)
 * \* INHERIT wiki.wiki.form.extension text_area (form)
 * \* INHERIT wiki.wiki.form.extension state (form)


Objects
-------

None
