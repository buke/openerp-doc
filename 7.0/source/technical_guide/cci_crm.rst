
.. module:: cci_crm
    :synopsis: CCI CRM 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_crm"></div>
    <script src="http://js-kit.com/ratings.js"></script>

CCI CRM (*cci_crm*)
===================
:Module: cci_crm
:Name: CCI CRM
:Version: 5.0.1.0
:Author: Tiny
:Directory: cci_crm
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  - define some groups with access rules
          - so using above rules , new object which will be confidential (can only be accessed by some users of group)

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/cci_crm.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/cci_crm.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`crm_configuration`
 * :mod:`event`
 * :mod:`cci_partner`

Reports
-------

None


Menus
-------

 * CRM & SRM/Meeting Confidential Info

Views
-----

 * \* INHERIT crm.case.form.confidential (form)
 * \* INHERIT crm.case.form.inherit (form)
 * \* INHERIT event.event.form.inherit (form)
 * meeting.confidential.info.form (form)
 * meeting.confidential.info.tree (tree)
 * meeting.confidential.info.form (form)
 * meeting.confidential.info.tree (tree)


Objects
-------

Object: Meeting Confidential Info (meeting.confidential.info)
#############################################################



:group: Group, selection, required





:name: Table, char





:description: Description, text, required


