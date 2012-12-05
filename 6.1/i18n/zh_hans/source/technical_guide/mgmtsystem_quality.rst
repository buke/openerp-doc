
.. i18n: .. module:: mgmtsystem_quality
.. i18n:     :synopsis: Quality Management System
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: mgmtsystem_quality
    :synopsis: Quality Management System
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

.. i18n: Quality Management System (*mgmtsystem_quality*)
.. i18n: ================================================
.. i18n: :Module: mgmtsystem_quality
.. i18n: :Name: Quality Management System
.. i18n: :Version: 6.0.0.0.1
.. i18n: :Author: Savoir-faire Linux
.. i18n: :Directory: mgmtsystem_quality 
.. i18n: :Web: http://www.savoirfairelinux.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Quality Management System provides you with all the required applications to manage:
.. i18n:   
.. i18n:   * Manuals, procedures and work instructions
.. i18n:   * Audits with report and verification list
.. i18n:   * Non-conformities with causes and origins
.. i18n:   * Immediate, corrective and preventive actions
.. i18n:   * Improvement opportunities
..

::

  Quality Management System provides you with all the required applications to manage:
  
  * Manuals, procedures and work instructions
  * Audits with report and verification list
  * Non-conformities with causes and origins
  * Immediate, corrective and preventive actions
  * Improvement opportunities

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: This module is available in extra-trunk:
..

This module is available in extra-trunk:

.. i18n:   * `trunk <https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-extra-addons>`_
..

  * `trunk <https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-extra-addons>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`mgmtsystem`
.. i18n:  * :mod:`mgmtsystem_action`
.. i18n:  * :mod:`mgmtsystem_audit`
.. i18n:  * :mod:`mgmtsystem_nonconformity`
.. i18n:  * :mod:`wiki_quality_manual`
.. i18n:  * :mod:`wiki_procedure`
..

 * :mod:`mgmtsystem`
 * :mod:`mgmtsystem_action`
 * :mod:`mgmtsystem_audit`
 * :mod:`mgmtsystem_nonconformity`
 * :mod:`wiki_quality_manual`
 * :mod:`wiki_procedure`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Audit reports
.. i18n:  * Verification lists
..

 * Audit reports
 * Verification lists

.. i18n: Menus
.. i18n: -----
..

Menus
-----

.. i18n:  * Management System
.. i18n:  * Management System/Audits
.. i18n:  * Management System/Nonconformities
.. i18n:  * Management System/Actions
.. i18n:  * Management System/Configuration
.. i18n:  * Management System/Configuration/Causes
.. i18n:  * Management System/Configuration/Origins
..

 * Management System
 * Management System/Audits
 * Management System/Nonconformities
 * Management System/Actions
 * Management System/Configuration
 * Management System/Configuration/Causes
 * Management System/Configuration/Origins

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * mgmtsystem.action.form (form)
.. i18n:  * mgmtsystem.action.tree (tree)
.. i18n:  * mgmtsystem.audit.form (form)
.. i18n:  * mgmtsystem.audit.tree (tree)
..

 * mgmtsystem.action.form (form)
 * mgmtsystem.action.tree (tree)
 * mgmtsystem.audit.form (form)
 * mgmtsystem.audit.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: mgmtsystem.action
.. i18n: #########################
..

Object: mgmtsystem.action
#########################

.. i18n: :reference: Reference, char, required
.. i18n: :type_action: Type of Action, selection
.. i18n: :message_ids: Message Ids, one2many(mailgate.message)
..

:reference: Reference, char, required
:type_action: Type of Action, selection
:message_ids: Message Ids, one2many(mailgate.message)
