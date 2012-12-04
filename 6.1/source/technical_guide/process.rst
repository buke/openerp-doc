
.. module:: process
    :synopsis: Enterprise Process (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/process"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Enterprise Process (*process*)
==============================
:Module: process
:Name: Enterprise Process
:Version: 5.0.1.0
:Author: Tiny
:Directory: process
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module allows you to manage your process for the end-users.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/process.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/process.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Administration/Customization/Enterprise Processes
 * Administration/Customization/Enterprise Processes/Process
 * Administration/Customization/Enterprise Processes/Process Nodes
 * Administration/Customization/Enterprise Processes/Process Transitions

Views
-----

 * process.process.form (form)
 * process.process.tree (tree)
 * process.node.tree (tree)
 * process.node.form (form)
 * process.transition.tree (tree)
 * process.transition.form (form)


Objects
-------

Object: Process (process.process)
#################################



:active: Active, boolean





:model_id: Object, many2one





:note: Notes, text





:name: Name, char, required





:node_ids: Nodes, one2many




Object: Process Nodes (process.node)
####################################



:menu_id: Related Menu, many2one





:model_id: Object, many2one





:kind: Kind of Node, selection, required





:name: Name, char, required





:subflow_id: Subflow, many2one





:condition_ids: Conditions, one2many





:note: Notes, text





:process_id: Process, many2one, required





:model_states: States Expression, char





:transition_out: Ending Transitions, one2many





:help_url: Help URL, char





:transition_in: Starting Transitions, one2many





:flow_start: Starting Flow, boolean




Object: Condition (process.condition)
#####################################



:model_id: Object, many2one





:node_id: Node, many2one, required





:model_states: Expression, char, required





:name: Name, char, required




Object: Process Transitions (process.transition)
################################################



:role_ids: Roles, many2many





:transition_ids: Workflow Transitions, many2many





:name: Name, char, required





:note: Description, text





:target_node_id: Target Node, many2one, required





:source_node_id: Source Node, many2one, required





:action_ids: Buttons, one2many




Object: Process Transitions Actions (process.transition.action)
###############################################################



:action: Action ID, char





:state: Type, selection, required





:name: Name, char, required





:transition_id: Transition, many2one, required


