
.. i18n: =========================
.. i18n: Workflow-Business Process
.. i18n: =========================
..

=========================
Workflow-Business Process
=========================

.. i18n: Introduction
.. i18n: ============
..

Introduction
============

.. i18n: The workflow system in OpenERP is a very powerful mechanism that can describe the evolution of documents (model) in time.
..

The workflow system in OpenERP is a very powerful mechanism that can describe the evolution of documents (model) in time.

.. i18n: Workflows are entirely customizable, they can be adapted to the flows and trade logic of almost any company. The workflow system makes OpenERP very flexible and allows it to easily support changing needs without having to program new functionality.
..

Workflows are entirely customizable, they can be adapted to the flows and trade logic of almost any company. The workflow system makes OpenERP very flexible and allows it to easily support changing needs without having to program new functionality.

.. i18n: **Goals**
..

**Goals**

.. i18n:     * description of document evolution in time
.. i18n:     * automatic trigger of actions if some conditions are met
.. i18n:     * management of company roles and validation steps
.. i18n:     * management of interactions between the different objects/modules
.. i18n:     * graphical tool for visualization of document flows
..

    * description of document evolution in time
    * automatic trigger of actions if some conditions are met
    * management of company roles and validation steps
    * management of interactions between the different objects/modules
    * graphical tool for visualization of document flows

.. i18n: **To understand their utility, see the following three:**
..

**To understand their utility, see the following three:**

.. i18n: Example 1: Discount On Orders
.. i18n: -----------------------------
..

Example 1: Discount On Orders
-----------------------------

.. i18n: The first diagram represent a very basic workflow of an order:
..

The first diagram represent a very basic workflow of an order:

.. i18n: .. image:: images/Workflow_bc1.png
..

.. image:: images/Workflow_bc1.png

.. i18n: The order starts in the 'draft' state, when it is being written and
.. i18n: has not been approved yet. When the user presses on the 'Confirm' button, the invoice is created and the order transitions to the 'CONFIRMED' state.
..

The order starts in the 'draft' state, when it is being written and
has not been approved yet. When the user presses on the 'Confirm' button, the invoice is created and the order transitions to the 'CONFIRMED' state.

.. i18n: Then, two operations are possible:
..

Then, two operations are possible:

.. i18n: #. the order is done (shipped)
.. i18n: 
.. i18n: #. the order is canceled
..

#. the order is done (shipped)

#. the order is canceled

.. i18n: Let's suppose a company has a need not implemented in OpenERP. For example, their sales staff can only offer discounts of 15% or less. Every order having a discount above 15% must be approved by the sales manager.
..

Let's suppose a company has a need not implemented in OpenERP. For example, their sales staff can only offer discounts of 15% or less. Every order having a discount above 15% must be approved by the sales manager.

.. i18n: This modification in the sales logic doesn't need any lines of Python code! A simple modification of the workflow allows us to take this new need into account and add the extra validation step.
..

This modification in the sales logic doesn't need any lines of Python code! A simple modification of the workflow allows us to take this new need into account and add the extra validation step.

.. i18n: .. image:: images/Workflow_bc2.png
..

.. image:: images/Workflow_bc2.png

.. i18n: The workflow is modified as above and the orders will react as requested. We then only need to modify the order form view and add a validation button at the desired location.
..

The workflow is modified as above and the orders will react as requested. We then only need to modify the order form view and add a validation button at the desired location.

.. i18n: We could then further improve this workflow by sending a request to the sales manager when an order enters the 'Validation' state. Workflow nodes can execute object methods; only two lines of Python are needed to send a request asking the sales manager to validate or reject the order.
..

We could then further improve this workflow by sending a request to the sales manager when an order enters the 'Validation' state. Workflow nodes can execute object methods; only two lines of Python are needed to send a request asking the sales manager to validate or reject the order.

.. i18n: Example 2: A sale order that generates an invoice and a shipping order
.. i18n: ----------------------------------------------------------------------
..

Example 2: A sale order that generates an invoice and a shipping order
----------------------------------------------------------------------

.. i18n: .. image:: images/Workflow_sale.png
..

.. image:: images/Workflow_sale.png

.. i18n: Example 3: Account invoice basic workflow
.. i18n: -----------------------------------------
..

Example 3: Account invoice basic workflow
-----------------------------------------

.. i18n: .. image:: images/Acount_inv_wkf.jpg
..

.. image:: images/Acount_inv_wkf.jpg

.. i18n: Defining Workflow
.. i18n: =================
..

Defining Workflow
=================

.. i18n: Workflows are defined in the file ``server/addons/base/ir/workflow/workflow.py``. The first three classes defined in this file are ``workflow``, ``wkf_activity`` and ``wkf_transition``. They correspond to the three types of resources necessary to describe a workflow:
..

Workflows are defined in the file ``server/addons/base/ir/workflow/workflow.py``. The first three classes defined in this file are ``workflow``, ``wkf_activity`` and ``wkf_transition``. They correspond to the three types of resources necessary to describe a workflow:

.. i18n:     * `workflow <http://openobject.com/wiki/index.php/WkfDefXML>`_ : the workflow,
.. i18n:     * `wkf_activity <http://openobject.com/wiki/index.php/WorkflowActivity>`_ : the activities (nodes),
.. i18n:     * `wkf_transition <http://openobject.com/wiki/index.php/WorkflowTransition>`_ : the transitions between the activities.
..

    * `workflow <http://openobject.com/wiki/index.php/WkfDefXML>`_ : the workflow,
    * `wkf_activity <http://openobject.com/wiki/index.php/WorkflowActivity>`_ : the activities (nodes),
    * `wkf_transition <http://openobject.com/wiki/index.php/WorkflowTransition>`_ : the transitions between the activities.

.. i18n: General structure of a workflow XML file
.. i18n: ========================================
..

General structure of a workflow XML file
========================================

.. i18n: The general structure of a workflow XML file is as follows:
..

The general structure of a workflow XML file is as follows:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <?xml version="1.0"?>
.. i18n:     <openerp>
.. i18n:     <data>
.. i18n:     <record model="workflow" id=workflow_id>
.. i18n: 
.. i18n:         <field name="name">workflow.name</field>
.. i18n:         <field name="osv">resource.model</field>
.. i18n:         <field name="on_create" eval='True|False' />
.. i18n: 
.. i18n:     </record>
.. i18n: 
.. i18n:     </data>
.. i18n:     </openerp>
..

.. code-block:: xml

    <?xml version="1.0"?>
    <openerp>
    <data>
    <record model="workflow" id=workflow_id>

        <field name="name">workflow.name</field>
        <field name="osv">resource.model</field>
        <field name="on_create" eval='True|False' />

    </record>

    </data>
    </openerp>

.. i18n: **Where**
..

**Where**

.. i18n:     * **id** (here "workflow_id") is a workflow identifier. Each workflow must have an unique identifier.
.. i18n:     * **name** (here "workflow.name") is the name of the workflow. The name of the workflow must respect the OpenERP syntax of "dotted names".
.. i18n:     * **osv** (here "resource.model") is the name of the object we use as a model [-(Remember an OpenERP object inherits from osv.osv, hence the '<field name="osv">')-].
.. i18n:     * **on_create** is True if workflow.name must be instantiated automatically when resource.model is created, and False otherwise.
..

    * **id** (here "workflow_id") is a workflow identifier. Each workflow must have an unique identifier.
    * **name** (here "workflow.name") is the name of the workflow. The name of the workflow must respect the OpenERP syntax of "dotted names".
    * **osv** (here "resource.model") is the name of the object we use as a model [-(Remember an OpenERP object inherits from osv.osv, hence the '<field name="osv">')-].
    * **on_create** is True if workflow.name must be instantiated automatically when resource.model is created, and False otherwise.

.. i18n: **Example**
..

**Example**

.. i18n: The workflow ``sale.order.basic`` defined in ``addons/sale/sale_workflow.xml`` follows exactly this model, the code of its workflow tag is:
..

The workflow ``sale.order.basic`` defined in ``addons/sale/sale_workflow.xml`` follows exactly this model, the code of its workflow tag is:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="workflow" id="wkf_sale">
.. i18n: 
.. i18n:         <field name="name">sale.order.basic</field>
.. i18n:         <field name="osv">sale.order</field>
.. i18n:         <field name="on_create" eval='True' />
.. i18n: 
.. i18n:     </record>
..

.. code-block:: xml

    <record model="workflow" id="wkf_sale">

        <field name="name">sale.order.basic</field>
        <field name="osv">sale.order</field>
        <field name="on_create" eval='True' />

    </record>

.. i18n: Activity
.. i18n: ==========
..

Activity
==========

.. i18n: Introduction
.. i18n: ------------
..

Introduction
------------

.. i18n: The ``wkf_activity`` class represents the nodes of workflows. These nodes are the actions to be executed.
..

The ``wkf_activity`` class represents the nodes of workflows. These nodes are the actions to be executed.

.. i18n: The fields
.. i18n: ----------
..

The fields
----------

.. i18n: ::
.. i18n: 
.. i18n:     split_mode
..

::

    split_mode

.. i18n: .. image::  images/Wkf_split.png
..

.. image::  images/Wkf_split.png

.. i18n: Possible values:
..

Possible values:

.. i18n: * XOR: One necessary transition, takes the first one found (default).
.. i18n: * OR: Take only valid transitions (0 or more) in sequential order.
.. i18n: * AND: All valid transitions are launched at the same time (fork).
..

* XOR: One necessary transition, takes the first one found (default).
* OR: Take only valid transitions (0 or more) in sequential order.
* AND: All valid transitions are launched at the same time (fork).

.. i18n: In the OR and AND separation mode, certain workitems can be generated.
..

In the OR and AND separation mode, certain workitems can be generated.

.. i18n: In the AND mode, the activity waits for all transitions to be valid, even if some of them are already valid. They are all triggered at the same time.
..

In the AND mode, the activity waits for all transitions to be valid, even if some of them are already valid. They are all triggered at the same time.

.. i18n: ::
.. i18n: 
.. i18n:     join_mode
..

::

    join_mode

.. i18n: .. image:: images/Wkf_join.png
..

.. image:: images/Wkf_join.png

.. i18n: Possible values:
..

Possible values:

.. i18n: * **XOR**: One transition necessary to continue to the destination activity (default).
.. i18n: * **AND**: Waits for all transition conditions to be valid to execute the destination activity.
..

* **XOR**: One transition necessary to continue to the destination activity (default).
* **AND**: Waits for all transition conditions to be valid to execute the destination activity.

.. i18n: ::
.. i18n: 
.. i18n:     kind
..

::

    kind

.. i18n: Possible values:
..

Possible values:

.. i18n:     * **dummy**: Do nothing (default).
.. i18n:     * **function**: Execute the function selected by an action.
.. i18n:     * **subflow**: Execute a sub-workflow SUBFLOW_ID. The action method must return the ID of the concerned resource by the subflow. If the action returns False, the workitem disappears.
.. i18n:     * **stopall**:
..

    * **dummy**: Do nothing (default).
    * **function**: Execute the function selected by an action.
    * **subflow**: Execute a sub-workflow SUBFLOW_ID. The action method must return the ID of the concerned resource by the subflow. If the action returns False, the workitem disappears.
    * **stopall**:

.. i18n: A sub-workflow is executed when an activity is of the type SUBFLOW. This activity ends when the sub-workflow has finished. While the sub-workflow is active, the workitem of this activity is frozen.
..

A sub-workflow is executed when an activity is of the type SUBFLOW. This activity ends when the sub-workflow has finished. While the sub-workflow is active, the workitem of this activity is frozen.

.. i18n: ::
.. i18n: 
.. i18n:     action
..

::

    action

.. i18n: The action indicates the method to execute when a workitem comes into this activity. The method must be defined in an object which belongs to this workflow and have the following signature:
..

The action indicates the method to execute when a workitem comes into this activity. The method must be defined in an object which belongs to this workflow and have the following signature:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     def object_method(self, cr, uid, ids):
..

.. code-block:: python

    def object_method(self, cr, uid, ids):

.. i18n: In the action though, they will be called by a statement like:
..

In the action though, they will be called by a statement like:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     object_method()
..

.. code-block:: python

    object_method()

.. i18n: ::
.. i18n: 
.. i18n:     signal_send
..

::

    signal_send

.. i18n: This field is used to specify a signal that will be sent to the parent
.. i18n: workflow when the activity becomes active. To do this, set the value
.. i18n: to the name of the signal (without the ``signal.`` prefix). 
..

This field is used to specify a signal that will be sent to the parent
workflow when the activity becomes active. To do this, set the value
to the name of the signal (without the ``signal.`` prefix). 

.. i18n: ::
.. i18n: 
.. i18n:     flow_start
..

::

    flow_start

.. i18n: Indicates if the node is a start node. When a new instance of a workflow is created, a workitem is activated for each activity marked as a ``flow_start``.
..

Indicates if the node is a start node. When a new instance of a workflow is created, a workitem is activated for each activity marked as a ``flow_start``.

.. i18n: .. warning::
.. i18n: 
.. i18n:     As for all Boolean fields, when writing the ``<field>`` tag in
.. i18n:     your XML data, be sure to use the ``eval`` attribute and not a
.. i18n:     text node for this attribute. Read the section about the
.. i18n:     :ref:`eval attribute <eval-attribute-link>` for an explanation.
..

.. warning::

    As for all Boolean fields, when writing the ``<field>`` tag in
    your XML data, be sure to use the ``eval`` attribute and not a
    text node for this attribute. Read the section about the
    :ref:`eval attribute <eval-attribute-link>` for an explanation.

.. i18n: ::
.. i18n: 
.. i18n:     flow_stop
..

::

    flow_stop

.. i18n: Indicates if the node is an ending node. When all the active workitems for a given instance come in the node marked by flow_stop, the workflow is finished.
..

Indicates if the node is an ending node. When all the active workitems for a given instance come in the node marked by flow_stop, the workflow is finished.

.. i18n: .. warning::
.. i18n: 
.. i18n:     See above in the description of the ``flow_start`` field.
..

.. warning::

    See above in the description of the ``flow_start`` field.

.. i18n: ::
.. i18n:     wkf_id
..

::
    wkf_id

.. i18n: The workflow this activity belongs to.
..

The workflow this activity belongs to.

.. i18n: Defining activities using XML files
.. i18n: -----------------------------------
..

Defining activities using XML files
-----------------------------------

.. i18n: The general structure of an activity record is as follows
..

The general structure of an activity record is as follows

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="workflow.activity" id="''activity_id''">
.. i18n:           <field name="wkf_id" ref="''workflow_id''"/>
.. i18n:           <field name="name">''activity.name''</field>::
.. i18n: 
.. i18n:           <field name="split_mode">XOR | OR | AND</field>
.. i18n:           <field name="join_mode">XOR | AND</field>
.. i18n:           <field name="kind">dummy | function | subflow | stopall</field>
.. i18n: 
.. i18n:           <field name="action">''(...)''</field>
.. i18n:           <field name="signal_send">''(...)''</field>
.. i18n:           <field name="flow_start" eval='True | False' />
.. i18n:           <field name="flow_stop" eval='True | False' />
.. i18n:       </record>
..

.. code-block:: xml

    <record model="workflow.activity" id="''activity_id''">
          <field name="wkf_id" ref="''workflow_id''"/>
          <field name="name">''activity.name''</field>::

          <field name="split_mode">XOR | OR | AND</field>
          <field name="join_mode">XOR | AND</field>
          <field name="kind">dummy | function | subflow | stopall</field>

          <field name="action">''(...)''</field>
          <field name="signal_send">''(...)''</field>
          <field name="flow_start" eval='True | False' />
          <field name="flow_stop" eval='True | False' />
      </record>

.. i18n: The first two arguments **wkf_id** and name are mandatory.
..

The first two arguments **wkf_id** and name are mandatory.

.. i18n: Examples
.. i18n: --------
..

Examples
--------

.. i18n: There are too many possibilities of activity definition to choose from using this definition. We recommend you to have a look at the file ``server/addons/sale/sale_workflow.xml`` for several examples of activity definitions.
..

There are too many possibilities of activity definition to choose from using this definition. We recommend you to have a look at the file ``server/addons/sale/sale_workflow.xml`` for several examples of activity definitions.

.. i18n: Transition
.. i18n: ===========
..

Transition
===========

.. i18n: Introduction
.. i18n: ------------
..

Introduction
------------

.. i18n: Workflow transitions are the conditions which need to be satisfied to
.. i18n: move from one activity to the next. They are represented by one-way arrows joining two activities.
..

Workflow transitions are the conditions which need to be satisfied to
move from one activity to the next. They are represented by one-way arrows joining two activities.

.. i18n: The conditions are of different types:
..

The conditions are of different types:

.. i18n:     * role that the user must satisfy
.. i18n:     * button pressed in the interface
.. i18n:     * end of a subflow through a selected activity of subflow
..

    * role that the user must satisfy
    * button pressed in the interface
    * end of a subflow through a selected activity of subflow

.. i18n: The roles and signals are evaluated before the expression. If a role or a signal is false, the expression will not be evaluated.
..

The roles and signals are evaluated before the expression. If a role or a signal is false, the expression will not be evaluated.

.. i18n: Transition tests may not write values in objects.
..

Transition tests may not write values in objects.

.. i18n: The fields
.. i18n: ----------
..

The fields
----------

.. i18n: ::
.. i18n: 
.. i18n:     act_from
..

::

    act_from

.. i18n: Source activity. When this activity is over, the condition is tested to determine if we can start the ACT_TO activity.
..

Source activity. When this activity is over, the condition is tested to determine if we can start the ACT_TO activity.

.. i18n: ::
.. i18n: 
.. i18n:     act_to
..

::

    act_to

.. i18n: The destination activity.
..

The destination activity.

.. i18n: ::
.. i18n: 
.. i18n:     condition
..

::

    condition

.. i18n: **Expression** to be satisfied if we want the transition done.
..

**Expression** to be satisfied if we want the transition done.

.. i18n: ::
.. i18n: 
.. i18n:     signal
..

::

    signal

.. i18n: When the operation of transition comes from a button pressed in the client form, signal tests the name of the pressed button.
..

When the operation of transition comes from a button pressed in the client form, signal tests the name of the pressed button.

.. i18n: If signal is NULL, no button is necessary to validate this transition.
..

If signal is NULL, no button is necessary to validate this transition.

.. i18n: ::
.. i18n: 
.. i18n:     role_id
..

::

    role_id

.. i18n: The **role** that a user must have to validate this transition.
..

The **role** that a user must have to validate this transition.

.. i18n: Defining Transitions Using XML Files
.. i18n: ------------------------------------
..

Defining Transitions Using XML Files
------------------------------------

.. i18n: The general structure of a transition record is as follows
..

The general structure of a transition record is as follows

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="workflow.transition" id="transition_id">
.. i18n: 
.. i18n:         <field name="act_from" ref="activity_id'_1_'"/>
.. i18n:         <field name="act_to" ref="activity_id'_2_'"/>
.. i18n: 
.. i18n:         <field name="signal">(...)</field>
.. i18n:         <field name="role_id" ref="role_id'_1_'"/>
.. i18n:         <field name="condition">(...)</field>
.. i18n: 
.. i18n:         <field name="trigger_model">(...)</field>
.. i18n:         <field name="trigger_expr_id">(...)</field>
.. i18n: 
.. i18n:     </record>
..

.. code-block:: xml

    <record model="workflow.transition" id="transition_id">

        <field name="act_from" ref="activity_id'_1_'"/>
        <field name="act_to" ref="activity_id'_2_'"/>

        <field name="signal">(...)</field>
        <field name="role_id" ref="role_id'_1_'"/>
        <field name="condition">(...)</field>

        <field name="trigger_model">(...)</field>
        <field name="trigger_expr_id">(...)</field>

    </record>

.. i18n: Only the fields **act_from** and **act_to** are mandatory.
..

Only the fields **act_from** and **act_to** are mandatory.

.. i18n: Expressions
.. i18n: ===========
..

Expressions
===========

.. i18n: Expressions are written as in Python:
..

Expressions are written as in Python:

.. i18n:     * True
.. i18n:     * 1==1
.. i18n:     * 'hello' in ['hello','bye']
..

    * True
    * 1==1
    * 'hello' in ['hello','bye']

.. i18n: Any field from the resource the workflow refers to can be used in these expressions. For example, if you were creating a workflow for partner addresses, you could use expressions like:
..

Any field from the resource the workflow refers to can be used in these expressions. For example, if you were creating a workflow for partner addresses, you could use expressions like:

.. i18n:     * zip==1400
.. i18n:     * phone==mobile
..

    * zip==1400
    * phone==mobile

.. i18n: User Role
.. i18n: =========
.. i18n: Roles can be attached to transitions. If a role is given for a transition, that transition can only be executed if the user who triggered it has the required role.
..

User Role
=========
Roles can be attached to transitions. If a role is given for a transition, that transition can only be executed if the user who triggered it has the required role.

.. i18n: Each user can have one or several roles. Roles are defined in a tree of roles, parent roles having the rights of all their children.
..

Each user can have one or several roles. Roles are defined in a tree of roles, parent roles having the rights of all their children.

.. i18n: Example:
..

Example:

.. i18n: CEO
..

CEO

.. i18n:   * Technical manager
.. i18n: 
.. i18n:     - Lead developer
..

  * Technical manager

    - Lead developer

.. i18n:       + Developers
.. i18n:       + Testers
..

      + Developers
      + Testers

.. i18n:   * Sales manager
.. i18n: 
.. i18n:     - Commercials
.. i18n:     - ...
..

  * Sales manager

    - Commercials
    - ...

.. i18n: Let's suppose we handle our own bug database and that the action of marking a bug as valid needs the Testers role. In the example tree above, marking a bug as valid could be done by all the users having the following roles: Testers, Lead developer, Technical manager, CEO.
..

Let's suppose we handle our own bug database and that the action of marking a bug as valid needs the Testers role. In the example tree above, marking a bug as valid could be done by all the users having the following roles: Testers, Lead developer, Technical manager, CEO.

.. i18n: Error handling
.. i18n: ==============
..

Error handling
==============

.. i18n: As of this writing, there is no exception handling in workflows.
..

As of this writing, there is no exception handling in workflows.

.. i18n: Workflows being made of several actions executed in batch, they can't trigger exceptions. In order to improve the execution efficiency and to release a maximum of locks, workflows commit at the end of each activity. This approach is reasonable because an activity is only started if the conditions of the transactions are satisfied.
..

Workflows being made of several actions executed in batch, they can't trigger exceptions. In order to improve the execution efficiency and to release a maximum of locks, workflows commit at the end of each activity. This approach is reasonable because an activity is only started if the conditions of the transactions are satisfied.

.. i18n: The only problem comes from exceptions due to programming errors; in that case, only transactions belonging to the entirely completed activities are executed. Other transactions are "rolled back".
..

The only problem comes from exceptions due to programming errors; in that case, only transactions belonging to the entirely completed activities are executed. Other transactions are "rolled back".

.. i18n: Creating a Workflow
.. i18n: ===================
..

Creating a Workflow
===================

.. i18n: Steps for creating a simple state-changing workflow for a custom module called **mymod**
..

Steps for creating a simple state-changing workflow for a custom module called **mymod**

.. i18n: Define the States of your object
.. i18n: --------------------------------
..

Define the States of your object
--------------------------------

.. i18n: The first step is to define the States your object can be in. We do this by adding a 'state' field to our object, in the _columns collection
..

The first step is to define the States your object can be in. We do this by adding a 'state' field to our object, in the _columns collection

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     _columns = {
.. i18n:      ...
.. i18n:         'state': fields.selection([
.. i18n:         ('new','New'),
.. i18n:         ('assigned','Assigned'),
.. i18n:         ('negotiation','Negotiation'),
.. i18n:         ('won','Won'),
.. i18n:         ('lost','Lost')], 'Stage', readonly=True),
.. i18n:     }
..

.. code-block:: python

    _columns = {
     ...
        'state': fields.selection([
        ('new','New'),
        ('assigned','Assigned'),
        ('negotiation','Negotiation'),
        ('won','Won'),
        ('lost','Lost')], 'Stage', readonly=True),
    }

.. i18n: Define the State-change Handling Methods
.. i18n: ----------------------------------------
..

Define the State-change Handling Methods
----------------------------------------

.. i18n: Add the following additional methods to your object. These will be called by our workflow buttons.
..

Add the following additional methods to your object. These will be called by our workflow buttons.

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     def mymod_new(self, cr, uid, ids):
.. i18n:          self.write(cr, uid, ids, {'state': 'new'})
.. i18n:          return True
.. i18n: 
.. i18n:     def mymod_assigned(self, cr, uid, ids):
.. i18n:          self.write(cr, uid, ids, {'state': 'assigned'})
.. i18n:          return True
.. i18n: 
.. i18n:     def mymod_negotiation(self, cr, uid, ids):
.. i18n:          self.write(cr, uid, ids, {'state': 'negotiation'})
.. i18n:          return True
.. i18n: 
.. i18n:     def mymod_won(self, cr, uid, ids):
.. i18n:          self.write(cr, uid, ids, {'state': 'won'})
.. i18n:          return True
.. i18n: 
.. i18n:     def mymod_lost(self, cr, uid, ids):
.. i18n:          self.write(cr, uid, ids, {'state': 'lost'})
.. i18n:          return True
..

.. code-block:: python

    def mymod_new(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'new'})
         return True

    def mymod_assigned(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'assigned'})
         return True

    def mymod_negotiation(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'negotiation'})
         return True

    def mymod_won(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'won'})
         return True

    def mymod_lost(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'lost'})
         return True

.. i18n: Obviously you would extend these methods in the future to do something more useful!
..

Obviously you would extend these methods in the future to do something more useful!

.. i18n: Create your Workflow XML file
.. i18n: -----------------------------
..

Create your Workflow XML file
-----------------------------

.. i18n: There are three types of records we need to define in a file called ``mymod_workflow.xml``
..

There are three types of records we need to define in a file called ``mymod_workflow.xml``

.. i18n: #. Workflow header record (only one of these)
..

#. Workflow header record (only one of these)

.. i18n:     .. code-block:: xml
.. i18n: 
.. i18n:         <record model="workflow" id="wkf_mymod">
.. i18n:             <field name="name">mymod.wkf</field>
.. i18n:             <field name="osv">mymod.mymod</field>
.. i18n:             <field name="on_create" eval='True' />
.. i18n:         </record>
..

    .. code-block:: xml

        <record model="workflow" id="wkf_mymod">
            <field name="name">mymod.wkf</field>
            <field name="osv">mymod.mymod</field>
            <field name="on_create" eval='True' />
        </record>

.. i18n: #. Workflow Activity records
..

#. Workflow Activity records

.. i18n:     These define the actions that must be executed when the workflow reaches a particular state
..

    These define the actions that must be executed when the workflow reaches a particular state

.. i18n:     .. code-block:: xml
.. i18n: 
.. i18n:         <record model="workflow.activity" id="act_new">
.. i18n:             <field name="wkf_id" ref="wkf_mymod" />
.. i18n:             <field name="flow_start" eval='True' />
.. i18n:             <field name="name">new</field>
.. i18n:             <field name="kind">function</field>
.. i18n:             <field name="action">mymod_new()</field>
.. i18n:         </record>
.. i18n: 
.. i18n:         <record model="workflow.activity" id="act_assigned">
.. i18n:             <field name="wkf_id" ref="wkf_mymod" />
.. i18n:             <field name="name">assigned</field>
.. i18n:             <field name="kind">function</field>
.. i18n:             <field name="action">mymod_assigned()</field>
.. i18n:         </record>
.. i18n: 
.. i18n:         <record model="workflow.activity" id="act_negotiation">
.. i18n:             <field name="wkf_id" ref="wkf_mymod" />
.. i18n:             <field name="name">negotiation</field>
.. i18n:             <field name="kind">function</field>
.. i18n:             <field name="action">mymod_negotiation()</field>
.. i18n:         </record>
.. i18n: 
.. i18n:         <record model="workflow.activity" id="act_won">
.. i18n:             <field name="wkf_id" ref="wkf_mymod" />
.. i18n:             <field name="name">won</field>
.. i18n:             <field name="kind">function</field>
.. i18n:             <field name="action">mymod_won()</field>
.. i18n:             <field name="flow_stop" eval='True' />
.. i18n:         </record>
.. i18n: 
.. i18n:         <record model="workflow.activity" id="act_lost">
.. i18n:             <field name="wkf_id" ref="wkf_mymod" />
.. i18n:             <field name="name">lost</field>
.. i18n:             <field name="kind">function</field>
.. i18n:             <field name="action">mymod_lost()</field>
.. i18n:             <field name="flow_stop" eval='True' />
.. i18n:         </record>
..

    .. code-block:: xml

        <record model="workflow.activity" id="act_new">
            <field name="wkf_id" ref="wkf_mymod" />
            <field name="flow_start" eval='True' />
            <field name="name">new</field>
            <field name="kind">function</field>
            <field name="action">mymod_new()</field>
        </record>

        <record model="workflow.activity" id="act_assigned">
            <field name="wkf_id" ref="wkf_mymod" />
            <field name="name">assigned</field>
            <field name="kind">function</field>
            <field name="action">mymod_assigned()</field>
        </record>

        <record model="workflow.activity" id="act_negotiation">
            <field name="wkf_id" ref="wkf_mymod" />
            <field name="name">negotiation</field>
            <field name="kind">function</field>
            <field name="action">mymod_negotiation()</field>
        </record>

        <record model="workflow.activity" id="act_won">
            <field name="wkf_id" ref="wkf_mymod" />
            <field name="name">won</field>
            <field name="kind">function</field>
            <field name="action">mymod_won()</field>
            <field name="flow_stop" eval='True' />
        </record>

        <record model="workflow.activity" id="act_lost">
            <field name="wkf_id" ref="wkf_mymod" />
            <field name="name">lost</field>
            <field name="kind">function</field>
            <field name="action">mymod_lost()</field>
            <field name="flow_stop" eval='True' />
        </record>

.. i18n: #. Workflow Transition records
..

#. Workflow Transition records

.. i18n:     These define the possible transitions between workflow states
..

    These define the possible transitions between workflow states

.. i18n:     .. code-block:: xml
.. i18n: 
.. i18n:         <record model="workflow.transition" id="t1">
.. i18n:             <field name="act_from" ref="act_new" />
.. i18n:             <field name="act_to" ref="act_assigned" />
.. i18n:             <field name="signal">mymod_assigned</field>
.. i18n:         </record>
.. i18n: 
.. i18n:         <record model="workflow.transition" id="t2">
.. i18n:             <field name="act_from" ref="act_assigned" />
.. i18n:             <field name="act_to" ref="act_negotiation" />
.. i18n:             <field name="signal">mymod_negotiation</field>
.. i18n:         </record>
.. i18n: 
.. i18n:         <record model="workflow.transition" id="t3">
.. i18n:             <field name="act_from" ref="act_negotiation" />
.. i18n:             <field name="act_to" ref="act_won" />
.. i18n:             <field name="signal">mymod_won</field>
.. i18n:         </record>
.. i18n: 
.. i18n:         <record model="workflow.transition" id="t4">
.. i18n:             <field name="act_from" ref="act_negotiation" />
.. i18n:             <field name="act_to" ref="act_lost" />
.. i18n:             <field name="signal">mymod_lost</field>
.. i18n:         </record>
..

    .. code-block:: xml

        <record model="workflow.transition" id="t1">
            <field name="act_from" ref="act_new" />
            <field name="act_to" ref="act_assigned" />
            <field name="signal">mymod_assigned</field>
        </record>

        <record model="workflow.transition" id="t2">
            <field name="act_from" ref="act_assigned" />
            <field name="act_to" ref="act_negotiation" />
            <field name="signal">mymod_negotiation</field>
        </record>

        <record model="workflow.transition" id="t3">
            <field name="act_from" ref="act_negotiation" />
            <field name="act_to" ref="act_won" />
            <field name="signal">mymod_won</field>
        </record>

        <record model="workflow.transition" id="t4">
            <field name="act_from" ref="act_negotiation" />
            <field name="act_to" ref="act_lost" />
            <field name="signal">mymod_lost</field>
        </record>

.. i18n: Add mymod_workflow.xml to __openerp__.py
.. i18n: ----------------------------------------
..

Add mymod_workflow.xml to __openerp__.py
----------------------------------------

.. i18n: Edit your module's ``__openerp__.py`` and add ``"mymod_workflow.xml"`` to the ``update_xml`` array, so that OpenERP picks it up next time your module is loaded.
..

Edit your module's ``__openerp__.py`` and add ``"mymod_workflow.xml"`` to the ``update_xml`` array, so that OpenERP picks it up next time your module is loaded.

.. i18n: Add Workflow Buttons to your View
.. i18n: ---------------------------------
..

Add Workflow Buttons to your View
---------------------------------

.. i18n: The final step is to add the required buttons to ``mymod_views.xml`` file.
..

The final step is to add the required buttons to ``mymod_views.xml`` file.

.. i18n: Add the following at the end of the ``<form>`` section of your object's view definition:
..

Add the following at the end of the ``<form>`` section of your object's view definition:

.. i18n:     .. code-block:: xml
.. i18n: 
.. i18n:         <separator string="Workflow Actions" colspan="4"/>
.. i18n:         <group colspan="4" col="3">
.. i18n:             <button name="mymod_assigned" string="Assigned" states="new" />
.. i18n:             <button name="mymod_negotiation" string="In Negotiation" states="assigned" />
.. i18n:             <button name="mymod_won" string="Won" states="negotiating" />
.. i18n:             <button name="mymod_lost" string="Lost" states="negotiating" />
.. i18n:         </group>
..

    .. code-block:: xml

        <separator string="Workflow Actions" colspan="4"/>
        <group colspan="4" col="3">
            <button name="mymod_assigned" string="Assigned" states="new" />
            <button name="mymod_negotiation" string="In Negotiation" states="assigned" />
            <button name="mymod_won" string="Won" states="negotiating" />
            <button name="mymod_lost" string="Lost" states="negotiating" />
        </group>

.. i18n: Testing
.. i18n: -------
.. i18n: Now use the Module Manager to install or update your module. If you have done everything correctly you shouldn't get any errors. You can check if your workflow is installed in the menu :menuselection:`Administration --> Customization --> Workflow Definitions`.
..

Testing
-------
Now use the Module Manager to install or update your module. If you have done everything correctly you shouldn't get any errors. You can check if your workflow is installed in the menu :menuselection:`Administration --> Customization --> Workflow Definitions`.

.. i18n: When you are testing, remember that the workflow will only apply to NEW records that you create.
..

When you are testing, remember that the workflow will only apply to NEW records that you create.

.. i18n: Troubleshooting
.. i18n: ---------------
.. i18n: If your buttons do not seem to be doing anything, one of the following two things are likely:
..

Troubleshooting
---------------
If your buttons do not seem to be doing anything, one of the following two things are likely:

.. i18n:    1. The record you are working on does not have a Workflow Instance record associated with it (it was probably created before you defined your workflow)
.. i18n:    2. You have not set the ``osv`` field correctly in your workflow XML file
..

   1. The record you are working on does not have a Workflow Instance record associated with it (it was probably created before you defined your workflow)
   2. You have not set the ``osv`` field correctly in your workflow XML file
