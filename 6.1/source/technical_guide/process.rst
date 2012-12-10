
.. i18n: .. module:: process
.. i18n:     :synopsis: Enterprise Process (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: process
    :synopsis: Enterprise Process (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/process"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/process"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Enterprise Process (*process*)
.. i18n: ==============================
.. i18n: :Module: process
.. i18n: :Name: Enterprise Process
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: process
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows you to manage your process for the end-users.
..

::

  This module allows you to manage your process for the end-users.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/process.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/process.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/process.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/process.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
..

 * :mod:`base`

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

.. i18n:  * Administration/Customization/Enterprise Processes
.. i18n:  * Administration/Customization/Enterprise Processes/Process
.. i18n:  * Administration/Customization/Enterprise Processes/Process Nodes
.. i18n:  * Administration/Customization/Enterprise Processes/Process Transitions
..

 * Administration/Customization/Enterprise Processes
 * Administration/Customization/Enterprise Processes/Process
 * Administration/Customization/Enterprise Processes/Process Nodes
 * Administration/Customization/Enterprise Processes/Process Transitions

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * process.process.form (form)
.. i18n:  * process.process.tree (tree)
.. i18n:  * process.node.tree (tree)
.. i18n:  * process.node.form (form)
.. i18n:  * process.transition.tree (tree)
.. i18n:  * process.transition.form (form)
..

 * process.process.form (form)
 * process.process.tree (tree)
 * process.node.tree (tree)
 * process.node.form (form)
 * process.transition.tree (tree)
 * process.transition.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Process (process.process)
.. i18n: #################################
..

Object: Process (process.process)
#################################

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :model_id: Object, many2one
..

:model_id: Object, many2one

.. i18n: :note: Notes, text
..

:note: Notes, text

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :node_ids: Nodes, one2many
..

:node_ids: Nodes, one2many

.. i18n: Object: Process Nodes (process.node)
.. i18n: ####################################
..

Object: Process Nodes (process.node)
####################################

.. i18n: :menu_id: Related Menu, many2one
..

:menu_id: Related Menu, many2one

.. i18n: :model_id: Object, many2one
..

:model_id: Object, many2one

.. i18n: :kind: Kind of Node, selection, required
..

:kind: Kind of Node, selection, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :subflow_id: Subflow, many2one
..

:subflow_id: Subflow, many2one

.. i18n: :condition_ids: Conditions, one2many
..

:condition_ids: Conditions, one2many

.. i18n: :note: Notes, text
..

:note: Notes, text

.. i18n: :process_id: Process, many2one, required
..

:process_id: Process, many2one, required

.. i18n: :model_states: States Expression, char
..

:model_states: States Expression, char

.. i18n: :transition_out: Ending Transitions, one2many
..

:transition_out: Ending Transitions, one2many

.. i18n: :help_url: Help URL, char
..

:help_url: Help URL, char

.. i18n: :transition_in: Starting Transitions, one2many
..

:transition_in: Starting Transitions, one2many

.. i18n: :flow_start: Starting Flow, boolean
..

:flow_start: Starting Flow, boolean

.. i18n: Object: Condition (process.condition)
.. i18n: #####################################
..

Object: Condition (process.condition)
#####################################

.. i18n: :model_id: Object, many2one
..

:model_id: Object, many2one

.. i18n: :node_id: Node, many2one, required
..

:node_id: Node, many2one, required

.. i18n: :model_states: Expression, char, required
..

:model_states: Expression, char, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: Process Transitions (process.transition)
.. i18n: ################################################
..

Object: Process Transitions (process.transition)
################################################

.. i18n: :role_ids: Roles, many2many
..

:role_ids: Roles, many2many

.. i18n: :transition_ids: Workflow Transitions, many2many
..

:transition_ids: Workflow Transitions, many2many

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :note: Description, text
..

:note: Description, text

.. i18n: :target_node_id: Target Node, many2one, required
..

:target_node_id: Target Node, many2one, required

.. i18n: :source_node_id: Source Node, many2one, required
..

:source_node_id: Source Node, many2one, required

.. i18n: :action_ids: Buttons, one2many
..

:action_ids: Buttons, one2many

.. i18n: Object: Process Transitions Actions (process.transition.action)
.. i18n: ###############################################################
..

Object: Process Transitions Actions (process.transition.action)
###############################################################

.. i18n: :action: Action ID, char
..

:action: Action ID, char

.. i18n: :state: Type, selection, required
..

:state: Type, selection, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :transition_id: Transition, many2one, required
..

:transition_id: Transition, many2one, required
