.. i18n: =============
.. i18n: Server Action
.. i18n: =============
..

==========
服务端动作
==========

.. i18n: Introduction
.. i18n: ------------
..

简介
----

.. i18n: Server action is an new feature available since the OpenERP
.. i18n: version 5.0 beta. This is an useful feature to fulfill customer
.. i18n: requirements. It provides a quick and easy configuration for day to
.. i18n: day requirements such as sending emails on confirmation of sale
.. i18n: orders or invoice, logging operations on invoices (confirm, cancel,
.. i18n: etc.), or running wizard/report on confirmation of sales, purchases,
.. i18n: or invoices.
..

Server action is an new feature available since the OpenERP
version 5.0 beta. This is an useful feature to fulfill customer
requirements. It provides a quick and easy configuration for day to
day requirements such as sending emails on confirmation of sale
orders or invoice, logging operations on invoices (confirm, cancel,
etc.), or running wizard/report on confirmation of sales, purchases,
or invoices.

.. i18n: Step 1: Definition of Server Action 
.. i18n: -----------------------------------
..

第一步：定义服务端动作
-----------------------------------

.. i18n: Here is the list of the different action types supplied under the Server Action.
..

下面列举了支持的服务端动作类型:

.. i18n:        * Client Action
.. i18n:        * Dummy
.. i18n:        * Iteration
.. i18n:        * Python Code
.. i18n:        * Trigger
.. i18n:        * Email
.. i18n:        * SMS
.. i18n:        * Create Object
.. i18n:        * Write Object
.. i18n:        * Multi Action
..

       * Client Action
       * Dummy
       * Iteration
       * Python Code
       * Trigger
       * Email
       * SMS
       * Create Object
       * Write Object
       * Multi Action

.. i18n: Each type of action has special features and different configuration
.. i18n: parameters. The following sections review each action type and
.. i18n: describe how to configure them, together with a list of parameters affecting the system.
..

Each type of action has special features and different configuration
parameters. The following sections review each action type and
describe how to configure them, together with a list of parameters affecting the system.

.. i18n: .. _client-action:
.. i18n: 
.. i18n: Client Action
.. i18n: ~~~~~~~~~~~~~
..

.. _client-action:

客户端动作
~~~~~~~~~~

.. i18n: This action executes on the client side. It can be used to run a
.. i18n: wizard or report on the client side. For example, a Client Action can
.. i18n: print an invoice after it has been confirmed and run the payment wizard. Technically we
.. i18n: can run any client action executed on client side. This includes ir.actions.report.custom,
.. i18n: ir.actions.report.xml, ir.actions.act_window, ir.actions.wizard, and
.. i18n: ir.actions.url. In the following example, we can configure a
.. i18n: Client Action to print the invoice after it has been confirmed.
..

This action executes on the client side. It can be used to run a
wizard or report on the client side. For example, a Client Action can
print an invoice after it has been confirmed and run the payment wizard. Technically we
can run any client action executed on client side. This includes ir.actions.report.custom,
ir.actions.report.xml, ir.actions.act_window, ir.actions.wizard, and
ir.actions.url. In the following example, we can configure a
Client Action to print the invoice after it has been confirmed.

.. i18n: .. image:: images/client_action.png
..

.. image:: images/client_action.png

.. i18n: Important fields are:
..

重点字段:

.. i18n: :Object: the object affected by the workflow on for which we want to
.. i18n:          run the action
.. i18n: :Client Action: the client action, which will be executed on the
.. i18n:                 client side. It must have one of the following types:
..

:Object: the object affected by the workflow on for which we want to
         run the action
:Client Action: the client action, which will be executed on the
                client side. It must have one of the following types:

.. i18n: * ir.actions.report.custom
.. i18n: * ir.actions.report.xml
.. i18n: * ir.actions.act_window
.. i18n: * ir.actions.wizard
.. i18n: * ir.actions.url
..

* ir.actions.report.custom
* ir.actions.report.xml
* ir.actions.act_window
* ir.actions.wizard
* ir.actions.url

.. i18n: Iteration
.. i18n: ~~~~~~~~~
..

Iteration
~~~~~~~~~

.. i18n: Using a Python loop expression, it is possible to iterate over a
.. i18n: server action.  For example, when confirming a inward stock move, each
.. i18n: line item must be historized. You can loop on expression object.move_lines and create another server action which is referred to do the historizing job.
..

Using a Python loop expression, it is possible to iterate over a
server action.  For example, when confirming a inward stock move, each
line item must be historized. You can loop on expression object.move_lines and create another server action which is referred to do the historizing job.

.. i18n: Python Code
.. i18n: ~~~~~~~~~~~
..

Python 代码
~~~~~~~~~~~

.. i18n: This action type is used to execute multiline python code. The
.. i18n: returned value is the value of the variable ``action``, defaulting to
.. i18n: ``{}``. This makes sense only if you want to pop a specific
.. i18n: window(form) specific to the context, but a return value is generally
.. i18n: not needed.
..

This action type is used to execute multiline python code. The
returned value is the value of the variable ``action``, defaulting to
``{}``. This makes sense only if you want to pop a specific
window(form) specific to the context, but a return value is generally
not needed.

.. i18n: Note: The code is executed using Python's ``exec`` built-in
.. i18n: function. This function is run in a dedicated namespace containing the
.. i18n: following identifiers: ``object``, ``time``, ``cr``, ``uid``, ``ids``.
..

Note: The code is executed using Python's ``exec`` built-in
function. This function is run in a dedicated namespace containing the
following identifiers: ``object``, ``time``, ``cr``, ``uid``, ``ids``.

.. i18n: Trigger
.. i18n: ~~~~~~~~
..

触发器
~~~~~~

.. i18n: Any transition of the workflow can be triggered using this action. The
.. i18n: options you need to set are:
..

Any transition of the workflow can be triggered using this action. The
options you need to set are:

.. i18n: :Object: the object affected by the workflow on for which we want to
.. i18n:          run the action
.. i18n: :Workflow on: The target object on which you want to trigger the
.. i18n:                  workflow.
.. i18n: :Trigger on: the ID of the target model record, e.g. Invoice if you want to trigger a change on an invoice. 
.. i18n: :Trigger Name: the signal you have to use to initiate the
.. i18n:                transition. The drop down lists all possible
.. i18n:                triggers. Note: the list contains all possible
.. i18n:                transitions from other models also, so ensure you
.. i18n:                select the right trigger. Models are shown in brackets. 
..

:Object: the object affected by the workflow on for which we want to
         run the action
:Workflow on: The target object on which you want to trigger the
                 workflow.
:Trigger on: the ID of the target model record, e.g. Invoice if you want to trigger a change on an invoice. 
:Trigger Name: the signal you have to use to initiate the
               transition. The drop down lists all possible
               triggers. Note: the list contains all possible
               transitions from other models also, so ensure you
               select the right trigger. Models are shown in brackets. 

.. i18n: The following example shows the configuration of a trigger used to
.. i18n: automatically confirm invoices:
..

The following example shows the configuration of a trigger used to
automatically confirm invoices:

.. i18n: .. image:: images/trigger_action.png
..

.. image:: images/trigger_action.png

.. i18n: Email Action
.. i18n: ~~~~~~~~~~~~~
..

Email 动作
~~~~~~~~~~

.. i18n: This action fulfills a  common requirement for all business process, sending a confirmation by email
.. i18n: whenever sales order, purchase order, invoice, payment or shipping of
.. i18n: goods takes place. 
..

This action fulfills a  common requirement for all business process, sending a confirmation by email
whenever sales order, purchase order, invoice, payment or shipping of
goods takes place. 

.. i18n: Using this action does not require a dedicated email
.. i18n: server: any existing SMTP email server and account can be used,
.. i18n: including free email account (Gmail, Yahoo !, etc...)
..

Using this action does not require a dedicated email
server: any existing SMTP email server and account can be used,
including free email account (Gmail, Yahoo !, etc...)

.. i18n: *Server Configuration*
..

*服务器配置*

.. i18n: The OpenERP server must know how to connect to the SMTP server. This
.. i18n: can be done from the command line when starting the server or by
.. i18n: editing the configuration file. Here are the command line options:
..

The OpenERP server must know how to connect to the SMTP server. This
can be done from the command line when starting the server or by
editing the configuration file. Here are the command line options:

.. i18n: ::
.. i18n: 
.. i18n:   --email-from=<sender_email@address>
.. i18n:   --smtp=<smtp server name or IP address>
.. i18n:   --smtp-port=<smtp server port>
.. i18n:   --smtp-user=<smtp user name, if required>
.. i18n:   --smtp-password=<smtp user password, if required>
.. i18n:   --smtp-ssl=<true if the server requires SSL for sending email, else false>
..

::

  --email-from=<sender_email@address>
  --smtp=<smtp server name or IP address>
  --smtp-port=<smtp server port>
  --smtp-user=<smtp user name, if required>
  --smtp-password=<smtp user password, if required>
  --smtp-ssl=<true if the server requires SSL for sending email, else false>

.. i18n: .. **
..

.. **

.. i18n: Here is an example configuration an action which sends an email when
.. i18n: an invoice is confirmed
..

Here is an example configuration an action which sends an email when
an invoice is confirmed

.. i18n: .. image:: images/email_action.png
..

.. image:: images/email_action.png

.. i18n: Important Fields are:
..

重点字段:

.. i18n: :Object: the object affected by the workflow on for which we want to
.. i18n:          run the action
.. i18n: :Contact: the field from which action will find the email address of
.. i18n:           the recipient of the email. The system will displays all the
.. i18n:           fields related to the object selected in the Object field. 
.. i18n: :Message: the message template with the fields that will filled using
.. i18n:           the current object. The notation is the same as the one used
.. i18n:           RML to design reports: you can use the [[ ]] + HTML tags to
.. i18n:           design in the HTML format. For example to get the partner
.. i18n:           name we can use [[ object.partner_id.name ]], object refers
.. i18n:           to the current object and we can access any fields which
.. i18n:           exist in the model.
..

:Object: the object affected by the workflow on for which we want to
         run the action
:Contact: the field from which action will find the email address of
          the recipient of the email. The system will displays all the
          fields related to the object selected in the Object field. 
:Message: the message template with the fields that will filled using
          the current object. The notation is the same as the one used
          RML to design reports: you can use the [[ ]] + HTML tags to
          design in the HTML format. For example to get the partner
          name we can use [[ object.partner_id.name ]], object refers
          to the current object and we can access any fields which
          exist in the model.

.. i18n: After configuring this action, whenever an invoice is confirmed, an
.. i18n: email such as the following is sent:
..

After configuring this action, whenever an invoice is confirmed, an
email such as the following is sent:

.. i18n: .. image:: images/email_confirm.png
..

.. image:: images/email_confirm.png

.. i18n: Create Object
.. i18n: ~~~~~~~~~~~~~
..

创建对象
~~~~~~~~

.. i18n: This type of action can be used to emulate the Event history feature currently
.. i18n: available on Partners, which logs sales orders issued by a partner, on
.. i18n: other objects which do not natively support this feature, such as
.. i18n: invoices:
..

This type of action can be used to emulate the Event history feature currently
available on Partners, which logs sales orders issued by a partner, on
other objects which do not natively support this feature, such as
invoices:

.. i18n: .. image:: images/create_object.png
..

.. image:: images/create_object.png

.. i18n: Create Object action configuration can be tricky, since it is
.. i18n: currently necessary to remember the field names (or to check them out
.. i18n: from the source code itself). There are plans to provide an
.. i18n: expression builder inside OpenERP in the future, which will be useful
.. i18n: to build complex expressions.
..

Create Object action configuration can be tricky, since it is
currently necessary to remember the field names (or to check them out
from the source code itself). There are plans to provide an
expression builder inside OpenERP in the future, which will be useful
to build complex expressions.

.. i18n: Important fields are:
..

重点字段:

.. i18n: :Object: the object affected by the workflow on for which we want to
.. i18n:          run the action
.. i18n: :Model: the target model for the object to be created. If empty, it
.. i18n:         refers to the current object and allows to select the fields
.. i18n:         from it. It is recommended to provide a model in all cases. 
.. i18n: :Fields Mapping: Need to provide 3 values:
..

:Object: the object affected by the workflow on for which we want to
         run the action
:Model: the target model for the object to be created. If empty, it
        refers to the current object and allows to select the fields
        from it. It is recommended to provide a model in all cases. 
:Fields Mapping: Need to provide 3 values:

.. i18n: 1. *Destination*: any of the fields from the target model
.. i18n: 2. *Type*: the type of the mapping. Allowed values are ``value`` or ``formula``
.. i18n: 3. *Value*: provide the value or expression the expression. The
.. i18n:    ``object`` refers to the current object.
..

1. *Destination*: any of the fields from the target model
2. *Type*: the type of the mapping. Allowed values are ``value`` or ``formula``
3. *Value*: provide the value or expression the expression. The
   ``object`` refers to the current object.

.. i18n: *You must select the all required fields from the target model*
..

*You must select the all required fields from the target model*

.. i18n: :Record Id: the field in which the  id of the new record is
.. i18n:             stored. This is used to refer to the same object in future
.. i18n:             operations (see below)
..

:Record Id: the field in which the  id of the new record is
            stored. This is used to refer to the same object in future
            operations (see below)

.. i18n: Write Object
.. i18n: ~~~~~~~~~~~~~
..

编辑对象
~~~~~~~~

.. i18n: The configuration is very similar to the Create Object actions. The
.. i18n: following example writes 'Additional Information' on the same object
..

The configuration is very similar to the Create Object actions. The
following example writes 'Additional Information' on the same object

.. i18n: .. image:: images/write_object.png
..

.. image:: images/write_object.png

.. i18n: Important Fields are
..

重点字段:

.. i18n:   **same as the Create Object**
..

  **same as the Create Object**

.. i18n: Multi Action
.. i18n: ~~~~~~~~~~~~~
..

多重组合动作
~~~~~~~~~~~~

.. i18n: This action allows to execute  multiple server actions on the same
.. i18n: business operation. For instance, it can be used to print *and* send
.. i18n: an email on confirmation of an invoice. This requires creating 3 server actions:
..

This action allows to execute  multiple server actions on the same
business operation. For instance, it can be used to print *and* send
an email on confirmation of an invoice. This requires creating 3 server actions:

.. i18n:   * Print Invoice
.. i18n:   * Invoice Confirmation Email !!
.. i18n:   * Multi Action
..

  * Print Invoice
  * Invoice Confirmation Email !!
  * Multi Action

.. i18n: There is a fundamental restriction on this action: it can execute many actions at the server side, but only
.. i18n: one single client action. It is therefore not possible to print a
.. i18n: report and execute a wizard at the same time. 
..

There is a fundamental restriction on this action: it can execute many actions at the server side, but only
one single client action. It is therefore not possible to print a
report and execute a wizard at the same time. 

.. i18n: .. image:: images/multi_action.png
..

.. image:: images/multi_action.png

.. i18n: Important Fields are:
..

重点字段:

.. i18n: :Object: the object affected by the workflow on for which we want to
.. i18n:          run the action
.. i18n: :Other Actions: the list of server action. Any number of actions can
.. i18n:                 be selected, but beware of the restriction mentioned
.. i18n:                 above: if you select more than one Client action, only
.. i18n:                 the first will be executed. 
..

:Object: the object affected by the workflow on for which we want to
         run the action
:Other Actions: the list of server action. Any number of actions can
                be selected, but beware of the restriction mentioned
                above: if you select more than one Client action, only
                the first will be executed. 

.. i18n: Step 2: Mapping Server actions to workflows
.. i18n: -------------------------------------------
..

第二步：给工作流定义服务端动作
------------------------------

.. i18n: Server actions by themselves are useless, until a workflow stage is
.. i18n: set up to trigger them.
..

Server actions by themselves are useless, until a workflow stage is
set up to trigger them.

.. i18n: Workflows can be accessed at: Administration >> Customization >>
.. i18n: Workflow Definitions >> Workflows. Open the corresponding workflow,
.. i18n: edit the stage at which the server action needs to be triggered. Then 
.. i18n: Select the server action in the box.
..

Workflows can be accessed at: Administration >> Customization >>
Workflow Definitions >> Workflows. Open the corresponding workflow,
edit the stage at which the server action needs to be triggered. Then 
Select the server action in the box.

.. i18n: The following example shows how to associate the Print invoice action
.. i18n: to the Open state of the Invoice workflow:
..

The following example shows how to associate the Print invoice action
to the Open state of the Invoice workflow:

.. i18n: .. image:: images/link_workflow.png
..

.. image:: images/link_workflow.png
