.. i18n: =============
.. i18n: Server Action
.. i18n: =============
..

==========
服务行为
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

服务行为(Server Action)是OpenErp 5.0以来推出的一项新的功能。对于客户来说，
这是一个有趣的功能，可以充分满足他们的要求。它可以为客户日常的一些业务要求提供简单而又快速的配置。
比如发送销售订单的电子确认邮件、货物的确认，货物的操作记录（确认、取消等）、
或者需要一个可以进行销售购买和发票确认的向导报告操作的系统.

.. i18n: Step 1: Definition of Server Action 
.. i18n: -----------------------------------
..

第一步：服务器操作的定义
-----------------------------------

.. i18n: Here is the list of the different action types supplied under the Server Action.
..

下面列举了服务器操作的行为类型:

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

       * 客户端行为Client Action
       * 虚拟行为Dummy
       * 迭代器Iteration
       * Python 代码
       * 触发器Trigger
       * Email
       * 消息服务SMS
       * 创建对象Create Object
       * 操作对象Write Object
       * 多重行为Multi Action

.. i18n: Each type of action has special features and different configuration
.. i18n: parameters. The following sections review each action type and
.. i18n: describe how to configure them, together with a list of parameters affecting the system.
..

每一种行为类型具有特殊的功能和不同的配置参数。我们接下来将看到每一种行为类型的不同的参数配置是如何影响系统的.

.. i18n: .. _client-action:
.. i18n: 
.. i18n: Client Action
.. i18n: ~~~~~~~~~~~~~
..

.. _client-action:

客户端行为（Client Action）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. i18n: This action executes on the client side. It can be used to run a
.. i18n: wizard or report on the client side. For example, a Client Action can
.. i18n: print an invoice after it has been confirmed and run the payment wizard. Technically we
.. i18n: can run any client action executed on client side. This includes ir.actions.report.custom,
.. i18n: ir.actions.report.xml, ir.actions.act_window, ir.actions.wizard, and
.. i18n: ir.actions.url. In the following example, we can configure a
.. i18n: Client Action to print the invoice after it has been confirmed.
..

这一行为在客户端执行，而且在客户端运行向导报告是一个好的主意。使用这种类型的行为可以使我们的系统像ERP一样在对发票进行确认后再打印。
它也会在发票确认后进入付款向导。从技术上来讲我们能够运行所有客户执行的行为。我们能够执行 ir.actions.report.custom,
ir.actions.report.xml, ir.actions.act_window, ir.actions.wizard, 和
ir.actions.url. 下面这个例子向我们演示了如何配置客户端行为来打印确认后的发票.

.. i18n: .. image:: images/client_action.png
..

.. image:: images/client_action.png

.. i18n: Important fields are:
..

重要字段:

.. i18n: :Object: the object affected by the workflow on for which we want to
.. i18n:          run the action
.. i18n: :Client Action: the client action, which will be executed on the
.. i18n:                 client side. It must have one of the following types:
..

:Object: 选择实现工作流服务器行为将要执行的对象
:Client Action: 选择客户端边执行的行为，这些行为可以是如下种类种的一个:

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

迭代器Iteration
~~~~~~~~~~~~~~~

.. i18n: Using a Python loop expression, it is possible to iterate over a
.. i18n: server action.  For example, when confirming a inward stock move, each
.. i18n: line item must be historized. You can loop on expression object.move_lines and create another server action which is referred to do the historizing job.
..

在Python的循环表达式基础上，你可以遍历服务器的行为。比如：当你确认一只股票出现向内移动时，
你希望每一个行子项显示出它的历史变化，你能循环遍历这个对象。这种移动行子项并且创造另一个服务行为的动作被称为historising job.

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

这个行为类型是执行一个多行的Python代码. 返回的值返回的值是变量 ``action``, 缺省值是
``{}``. 如果你想弹出一个带有特定内容的特定的窗体的话, 这是很有用的.恕我直言，你不会需要的一个返回值.

.. i18n: Note: The code is executed using Python's ``exec`` built-in
.. i18n: function. This function is run in a dedicated namespace containing the
.. i18n: following identifiers: ``object``, ``time``, ``cr``, ``uid``, ``ids``.
..

记住: 被执行的代码使用了Python的 ``exec`` 函数. 这个函数在字典的命名空间定义，
具有如下变量: ``object``, ``time``, ``cr``, ``uid``, ``ids``.

.. i18n: Trigger
.. i18n: ~~~~~~~~
..

触发器Trigger
~~~~~~~~~~~~~

.. i18n: Any transition of the workflow can be triggered using this action. The
.. i18n: options you need to set are:
..

任何工作流的转换都可以使用触发。你需要设定的选型是:

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

:Object: 我们想执行行为的受工作流影响的对象.
:Workflow on: 触发工作流的目标对象.
:Trigger on: 字段应该填入目标模式记录的 ID, 比如. 如果你想触发一个发票的改变，你应该填入这个发票的 ID. 
:Trigger Name: 是用来初始化转换的信号。下拉列表框列出了所有可能的触发.
               记住: 列出了多有可能的转换，所欲确认你选择了正确的转换。括号内给出的是模型. 

.. i18n: The following example shows the configuration of a trigger used to
.. i18n: automatically confirm invoices:
..

下面的示例演示了一个触发器用来配置自动确认发票:

.. i18n: .. image:: images/trigger_action.png
..

.. image:: images/trigger_action.png

.. i18n: Email Action
.. i18n: ~~~~~~~~~~~~~
..

邮件行为Email Action
~~~~~~~~~~~~~~~~~~~~

.. i18n: This action fulfills a  common requirement for all business process, sending a confirmation by email
.. i18n: whenever sales order, purchase order, invoice, payment or shipping of
.. i18n: goods takes place. 
..

邮件行为是所有业务过程的共同要求，比如通过邮件确认销售订单、购买订单、发票、付款、货物运输等. 

.. i18n: Using this action does not require a dedicated email
.. i18n: server: any existing SMTP email server and account can be used,
.. i18n: including free email account (Gmail, Yahoo !, etc...)
..

为了达到这个目的，我们只需要进行简单的配置就可以使邮件很容易的快速发送了。尽管不需要设置你自己的邮件服务器，你可以使用你想用的邮件服务和账号。尽管你没有自己的邮件服务，你可以使用免费的邮件服务账号，比如Gmail、Yahoo等等。
(Gmail, Yahoo !, etc...)

.. i18n: *Server Configuration*
..

*邮件服务配置*

.. i18n: The OpenERP server must know how to connect to the SMTP server. This
.. i18n: can be done from the command line when starting the server or by
.. i18n: editing the configuration file. Here are the command line options:
..

启用OpenErp服务时，我们提供下列参数:

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

重要字段:

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

:Object: 选择实现工作流服务器行为将要执行的对象
:Contact: 这个字段表示我们想发送的目标邮件地址，并且在这个字段中系统会显示出相近的地址对象. 
:Message: 在这个字段中你可以提供与当前对象相近的邮件信息模板。在发送时它会自动合并。用的格式语言与我们用来设计报表rmi的语言一致，
          这里我们可以使用HTML规范中的标签来规范字段中的任何对象。比如上图中我们选择了[[]]发票对象.

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
