
.. module:: base_translation
    :synopsis: Translation 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_translation"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Translation (*base_translation*)
================================
:Module: base_translation
:Name: Translation
:Version: 5.0.1.0
:Author: Tiny
:Directory: base_translation
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  For better translation process

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/base_translation.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/base_translation.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Administration/Translations/Translations Management
 * Administration/Translations/Translations Management/All Contribution
 * Administration/Translations/Translations Management/Maintainer
 * Administration/Translations/Translations Management/Maintainer/Review Proposed Contribution
 * Administration/Translations/Translations Management/Contributors
 * Administration/Translations/Translations Management/Contributors/Download New Version
 * Administration/Translations/Translations Management/Maintainer/Download Contributor's Proposition
 * Administration/Translations/Translations Management/Contributors/Review Proposed Contributions
 * Administration/Translations/Translations Management/Contributors/Upload Contributions
 * Administration/Translations/Translations Management/Maintainer/Publish New Version

Views
-----

 * Translations Contrib (form)
 * Translations Contrib (tree)


Objects
-------

Object: Translation Contribution (ir.translation.contribution)
##############################################################



:lang: Language, selection





:src: Source, text





:name: Field Name, char, required





:res_id: Resource ID, integer





:upload: upload, boolean





:value: Translation Value, text





:state: Translation State, selection, readonly





:contributor_email: Email Id of Contributor, char





:type: Type, selection


