
.. module:: audittrail
    :synopsis: Audit Trail (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/audittrail"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  Allows the administrator to track every user operation on all objects of the system.
      Subscribe Rules for read, write, create and delete on objects and check logs

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/audittrail.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/audittrail.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`purchase`
 * :mod:`mrp`

Reports
-------

None


Menus
-------

 * Administration/Audittrails
 * Administration/Audittrails/Rules
 * Administration/Audittrails/Rules/Subscribed Rules
 * Administration/Audittrails/Logs
 * Administration/Audittrails/View Logs

Views
-----

 * audittrail.rule.form (form)
 * audittrail.rule.tree (tree)
 * audittrail.log.form (form)
 * audittrail.log.tree (tree)


Objects
-------

Object: audittrail.rule (audittrail.rule)
#########################################



:log_read: Log reads, boolean





:log_unlink: Log deletes, boolean





:user_id: Users, many2many





:name: Rule Name, char, required





:log_write: Log writes, boolean





:object_id: Object, many2one, required





:log_create: Log creates, boolean





:state: State, selection, required





:action_id: Action ID, many2one




Object: audittrail.log (audittrail.log)
#######################################



:user_id: User, many2one





:name: Name, char





:timestamp: Date, datetime





:object_id: Object, many2one





:line_ids: Log lines, one2many





:res_id: Resource Id, integer





:method: Method, selection




Object: audittrail.log.line (audittrail.log.line)
#################################################



:log: Log ID, integer





:log_id: Log, many2one





:old_value: Old Value, text





:field_id: Fields, many2one, required





:old_value_text: Old value Text, text





:field_description: Field Description, char





:new_value: New Value, text





:new_value_text: New value Text, text


