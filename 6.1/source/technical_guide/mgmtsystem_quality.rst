
.. module:: mgmtsystem_quality
    :synopsis: Quality Management System
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

Quality Management System (*mgmtsystem_quality*)
================================================
:Module: mgmtsystem_quality
:Name: Quality Management System
:Version: 6.0.0.0.1
:Author: Savoir-faire Linux
:Directory: mgmtsystem_quality 
:Web: http://www.savoirfairelinux.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Quality Management System provides you with all the required applications to manage:
  
  * Manuals, procedures and work instructions
  * Audits with report and verification list
  * Non-conformities with causes and origins
  * Immediate, corrective and preventive actions
  * Improvement opportunities

Download links
--------------

This module is available in extra-trunk:

  * `trunk <https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-extra-addons>`_


Dependencies
------------

 * :mod:`mgmtsystem`
 * :mod:`mgmtsystem_action`
 * :mod:`mgmtsystem_audit`
 * :mod:`mgmtsystem_nonconformity`
 * :mod:`wiki_quality_manual`
 * :mod:`wiki_procedure`

Reports
-------

 * Audit reports
 * Verification lists

Menus
-----

 * Management System
 * Management System/Audits
 * Management System/Nonconformities
 * Management System/Actions
 * Management System/Configuration
 * Management System/Configuration/Causes
 * Management System/Configuration/Origins

Views
-----

 * mgmtsystem.action.form (form)
 * mgmtsystem.action.tree (tree)
 * mgmtsystem.audit.form (form)
 * mgmtsystem.audit.tree (tree)


Objects
-------

Object: mgmtsystem.action
#########################

:reference: Reference, char, required
:type_action: Type of Action, selection
:message_ids: Message Ids, one2many(mailgate.message)

