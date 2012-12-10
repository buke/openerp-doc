
.. i18n: .. module:: audittrail
.. i18n:     :synopsis: Audit Trail (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: audittrail
    :synopsis: Audit Trail (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/audittrail"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/audittrail"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Audit Trail (*audittrail*)
.. i18n: ==========================
.. i18n: :Module: audittrail
.. i18n: :Name: Audit Trail
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: audittrail
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Audit Trail (*audittrail*)
==========================
:Module: audittrail
:Name: Audit Trail
:Version: 5.0.1.0
:Author: Tiny
:Directory: audittrail
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Allows the administrator to track every user operation on all objects of the system.
.. i18n:       Subscribe Rules for read, write, create and delete on objects and check logs
..

::

  Allows the administrator to track every user operation on all objects of the system.
      Subscribe Rules for read, write, create and delete on objects and check logs

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/audittrail.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/audittrail.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/audittrail.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/audittrail.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`purchase`
.. i18n:  * :mod:`mrp`
..

 * :mod:`base`
 * :mod:`account`
 * :mod:`purchase`
 * :mod:`mrp`

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

.. i18n:  * Administration/Audittrails
.. i18n:  * Administration/Audittrails/Rules
.. i18n:  * Administration/Audittrails/Rules/Subscribed Rules
.. i18n:  * Administration/Audittrails/Logs
.. i18n:  * Administration/Audittrails/View Logs
..

 * Administration/Audittrails
 * Administration/Audittrails/Rules
 * Administration/Audittrails/Rules/Subscribed Rules
 * Administration/Audittrails/Logs
 * Administration/Audittrails/View Logs

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * audittrail.rule.form (form)
.. i18n:  * audittrail.rule.tree (tree)
.. i18n:  * audittrail.log.form (form)
.. i18n:  * audittrail.log.tree (tree)
..

 * audittrail.rule.form (form)
 * audittrail.rule.tree (tree)
 * audittrail.log.form (form)
 * audittrail.log.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: audittrail.rule (audittrail.rule)
.. i18n: #########################################
..

Object: audittrail.rule (audittrail.rule)
#########################################

.. i18n: :log_read: Log reads, boolean
..

:log_read: Log reads, boolean

.. i18n: :log_unlink: Log deletes, boolean
..

:log_unlink: Log deletes, boolean

.. i18n: :user_id: Users, many2many
..

:user_id: Users, many2many

.. i18n: :name: Rule Name, char, required
..

:name: Rule Name, char, required

.. i18n: :log_write: Log writes, boolean
..

:log_write: Log writes, boolean

.. i18n: :object_id: Object, many2one, required
..

:object_id: Object, many2one, required

.. i18n: :log_create: Log creates, boolean
..

:log_create: Log creates, boolean

.. i18n: :state: State, selection, required
..

:state: State, selection, required

.. i18n: :action_id: Action ID, many2one
..

:action_id: Action ID, many2one

.. i18n: Object: audittrail.log (audittrail.log)
.. i18n: #######################################
..

Object: audittrail.log (audittrail.log)
#######################################

.. i18n: :user_id: User, many2one
..

:user_id: User, many2one

.. i18n: :name: Name, char
..

:name: Name, char

.. i18n: :timestamp: Date, datetime
..

:timestamp: Date, datetime

.. i18n: :object_id: Object, many2one
..

:object_id: Object, many2one

.. i18n: :line_ids: Log lines, one2many
..

:line_ids: Log lines, one2many

.. i18n: :res_id: Resource Id, integer
..

:res_id: Resource Id, integer

.. i18n: :method: Method, selection
..

:method: Method, selection

.. i18n: Object: audittrail.log.line (audittrail.log.line)
.. i18n: #################################################
..

Object: audittrail.log.line (audittrail.log.line)
#################################################

.. i18n: :log: Log ID, integer
..

:log: Log ID, integer

.. i18n: :log_id: Log, many2one
..

:log_id: Log, many2one

.. i18n: :old_value: Old Value, text
..

:old_value: Old Value, text

.. i18n: :field_id: Fields, many2one, required
..

:field_id: Fields, many2one, required

.. i18n: :old_value_text: Old value Text, text
..

:old_value_text: Old value Text, text

.. i18n: :field_description: Field Description, char
..

:field_description: Field Description, char

.. i18n: :new_value: New Value, text
..

:new_value: New Value, text

.. i18n: :new_value_text: New value Text, text
..

:new_value_text: New value Text, text
