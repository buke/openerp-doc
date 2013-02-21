.. i18n: Project Management
.. i18n: ==================
..

项目管理
========

.. i18n: In the previous chapter you learned more about the financial management of projects, based on
.. i18n: OpenERP's analytic accounts, structured into cases. This way of working enables you to analyze
.. i18n: time plans and budgets, to control invoicing and to manage your different contracts.
..

在前面的章节中，您基于OpenERP的辅助核算、实例结构了解了项目的财务管理。这种工作方式使您能够分析时间计划和预算，
和管理不同合同的发票。

.. i18n: Here we will explain operational project management to organize tasks and plan the work you
.. i18n: need to get the tasks completed. All the necessary operations are carried out from the
.. i18n: :menuselection:`Project` menu.
..

在这里，我们将解释使用项目管理模块来组织任务和计划您需要完成的工作。所有必要的操作均出自于 :menuselection:`Project` 
菜单中。

.. i18n: .. tip:: Remember that you will have less options in Simplified view than in Extended view.
..

.. tip:: 记得您在简化界面中比在扩展界面中选项更少.

.. i18n: .. index::
.. i18n:    single: project
..

.. index::
   single: project

.. i18n: .. note:: Project
.. i18n: 
.. i18n: 	In OpenERP, a project is represented by a set of tasks to be completed.
.. i18n: 	Projects have a tree structure that can be divided into phases and sub-phases.
.. i18n: 	This structure is very useful to organise your work.
.. i18n: 
.. i18n: 	Whereas analytic accounts look at the past activities of the company, Project Management's role is
.. i18n: 	to plan the future.
.. i18n: 	Even though there is a close link between the two (such as where a project has been planned and then
.. i18n: 	completed through OpenERP) they are still two different concepts, each making its own contribution to a flexible workflow.
..

.. note:: 项目

	在OpenERP中，项目代表了一系列需完成的任务。项目有一个树状结构，可以划分阶段和子阶段。这种结构非常有益于组织您
	的工作。

	相对于辅助核算是审视公司过去的活动，工程管理的作用是规划未来。虽然在两者之间存在密切的联系（如项目已通过OpenERP
	计划和完成），他们仍然是两个不同的概念，各自形成自己的工作流程。

.. i18n: Most customer projects are represented by:
..

大多数自定义项目由以下构成:

.. i18n: * one or several analytic accounts in the Accounting System, to keep track of the contract and its
.. i18n:   different phases,
.. i18n: 
.. i18n: * one or several projects in Project Management, to track the project and the different tasks to
.. i18n:   be completed.
..

* 总账系统中一个或多个辅助核算以跟踪合同及其不同阶段,

* 项目管理系统中一个或多个项目以跟踪需完成的不同任务.

.. i18n: There is a direct link between the project and the analytic account, because for each new project created, OpenERP will automatically create the corresponding analytic account in the `Projects` analytic chart of accounts. Note that you have no access to the analytic account directly from a project.
..

这里项目和辅助核算可以直接关联，这是因为每创建一新的项目，OpenERP会在 `项目` 辅助核算表中自动创建对应的辅助核算项。
注意您不能从项目中直接存取辅助核算。

.. i18n: Creating Projects and Related Tasks
.. i18n: -----------------------------------
..

创建项目和相关项目任务
-----------------------------------

.. i18n: To define a new project, go to the menu :menuselection:`Project --> Project --> Projects`.
.. i18n: Click :guilabel:`New` and give your new project a :guilabel:`Project Name`.
..

定义一个新项目，到菜单 :menuselection:`Project --> Project --> Projects` ，点击 :guilabel:`New` 并给项目一个 :guilabel:`Project Name` .

.. i18n: You can put this project into a hierarchy, as a child of a :guilabel:`Parent Project`, and
.. i18n: assign a :guilabel:`Project Manager`.
.. i18n: Enter the general duration by completing :guilabel:`Start Date` and :guilabel:`End Date`.
..

您可以将这个项目作为一个 :guilabel:`Parent Project` 的子项放入一个层次结构中，并指派一个 :guilabel:`Project Manager` 。
通过输入 :guilabel:`Start Date` 和 :guilabel:`End Date` 确定总持续时间。

.. i18n: The `Administration` tab displays information about Planned Time and the Time Spent on the project according to the task work completed.
.. i18n: By checking the box :guilabel:`Warn Manager`, you configure the system to automatically send the project manager
.. i18n: an OpenERP `Request` every time a task is closed.
..

`Administration` 选项卡显示关于计划时间的信息，并根据已完成任务计算项目花费的时间。如果选中了 :guilabel:`Warn Manager` 选择框，
您可设置系统在每一任务完成时向项目经理发一条 `Request` 。万一项目运行时间过长，它可升级成另一项目。在 `提升` 处选择需提升成项目的已进行任务。

.. i18n: In case a project takes too long, it can also be escalated to another project. This feature is available if you have installed the module :mod:`project_issue`, which can be done by selecting :guilabel:`Issues Tracker` in the :guilabel:`Reconfigure` wizard. In :guilabel:`Project Escalation`, enter the project that will be used for escalated tasks.
.. i18n: Define a generic :guilabel:`Reply-To Email Address` linked to all automated mails; this allows you to receive replies directly in OpenERP.
.. i18n: You can also link to a :guilabel:`Working Time` category, which will be used to calculate the Project's time line, i.e. through a Gantt chart.
..

In case a project takes too long, it can also be escalated to another project. This feature is available if you have installed the module :mod:`project_issue`, which can be done by selecting :guilabel:`Issues Tracker` in the :guilabel:`Reconfigure` wizard. In :guilabel:`Project Escalation`, enter the project that will be used for escalated tasks.
为自动电子邮件定义一个一般的 :guilabel:`Reply-To Email Address` ；这允许您直接从OpenERP中接收回复。您可定义一个 :guilabel:`Working Time` 类型，这可用于计算项目时间，特别是通过甘特图。

.. i18n: The status of a project can take the following values:
..

项目有如下状态:

.. i18n: * \ ``Open``\: the project is being carried out,
.. i18n: 
.. i18n: * \ ``Pending``\: the project is paused,
.. i18n: 
.. i18n: * \ ``Cancelled``\: the project has been cancelled and therefore aborted,
.. i18n: 
.. i18n: * \ ``Closed``\: the project has been successfully completed,
.. i18n: 
.. i18n: * \ ``Template``\: the project can be used as a template to make projects based on this.
..

* \ ``打开``\: 项目开出来了,

* \ ``中止``\: 项目暂停,

* \ ``取消``\: 项目因为取消而中断,

* \ ``关闭``\: 项目成功结束,

* \ ``Template``\: the project can be used as a template to make projects based on this.

.. i18n: On the `Members` tab, add :guilabel:`Members` to the project; this is related to access rights too.
..

在 `Members` 选项卡，将 :guilabel:`Members` 添加到该项目，这与访问权限有关。

.. i18n: On the `Billing` tab, you find information to invoice your customer.
.. i18n: Select the `Customer`; the Invoice address will automatically be filled from the customer form.
.. i18n: To generate invoices based on time spent on tasks, if activated on a project, you may install :mod:`project_timesheet` by selecting :guilabel:`Bill Time on Tasks` in the :guilabel:`Reconfigure` wizard.
.. i18n: Then you can complete the invoicing data, such as `Sale Pricelist` and `Invoice Task Work` to directly invoice from task work done.
.. i18n: OpenERP allows you to set a `Max. Invoice Price` for the project (or sub-project). The `Invoiced Amount` shows the total amount that has already been invoiced for the project concerned. 
..

在 `Billing` 选项卡，您能看到客户的发票信息。选择 `Customer` ，客户表单的“客户地址”会自动填入。您必须完成其他信息，
比如 :mod:`销售价格表` 和在任务完成后直接 :guilabel:`按任务进展开票` 。OpenERP允许您设置项目（或自项目）的 `最大开票价` 。
`已开票金额` 显示的是相关项目的已开发票的总金额。

.. i18n: If you want to automatically keep your customer informed about the progress of the project, check `Warn Partner`. 
..

如果您想自动使您的客户了解项目的进展情况，选中 `通知业务伙伴`。（通知合作伙伴）

.. i18n: .. note:: Warn Partner Setup
.. i18n: 
.. i18n:    If you check :guilabel:`Warn Partner`, you should define a generic Mail Header and Mail Footer in the
.. i18n:    :guilabel:`Billing` tab that will be used in the automated email (*Extended view* only).
.. i18n:    OpenERP prepares an email the user can send to the customer
.. i18n:    each time that a task is completed. The contents of this email are based on details of the project
.. i18n:    task, and can be modified by the user before the email is sent.
.. i18n:    OpenERP displays a number of variables at the bottom of this tab.
..

.. note:: 通知业务伙伴

   如果您选中 :guilabel:`通知业务伙伴` ，在 :guilabel:`发票` 页签中需要您定义一个常用的 `邮件头` 和 `邮件页脚` 用于
   自动生成的电子邮件（仅扩展用户界面）。OpenERP会准备好电子邮件，用户可以在每个任务结束后发给客户。这封电子邮件的
   内容是基于项目任务的详细信息，并且在发送电子邮件之前，可以由用户修改。在这个页签下面，OpenERP显示了多个可用于电
   子邮件的变量。

.. i18n: .. note:: Study of Customer Satisfaction
.. i18n: 
.. i18n: 	Some companies run a system where emails are automatically sent at the end of a task requesting the
.. i18n: 	customer to complete an online survey.
.. i18n: 	This survey enables a company to ask several questions about the work carried out, to gauge customer
.. i18n: 	satisfaction as the project progresses.
.. i18n: 
.. i18n: 	This function can also be used by ISO 9001-certified companies, to measure customer satisfaction.
.. i18n: 	OpenERP also allows you to create your own surveys. 
..

.. note:: 客户满意度的研究

	一些企业运行的电子邮件系统自动发送请求客户的任务，以完成一项网上调查结束。这项调查使公司询问有关工作开展的
	一些问题，来衡量顾客对项目进展的满意程度。

	此功能也可用于通过ISO 9001认证的公司，来衡量顾客的满意度。 OpenERP还允许您创建自己的调查。

.. i18n: The `Task Stages` tab allows you to define stages that help you divide your tasks. You can add a sequence number to set the stage order, allowing you to prioritize your task work, i.e. first you will have the Specification stage and then Development.
..

`Task Stages` 选项卡允许您定义阶段帮助你分割您的任务。您可以添加一个序列号来设置各阶段顺序，使您考虑优先的工作任务，
即：首先，您将先有 `详细说明书` 阶段然后才是 `开发` 。

.. i18n: Managing Tasks
.. i18n: --------------
..

任务管理
--------------

.. i18n: Once a project has been defined, you can enter the tasks to be executed. You have two possibilities for this:
..

一旦一个项目已被定义，你可以输入要执行的任务。这有两种方法：

.. i18n: * click the :guilabel:`ACTION` button :guilabel:`Tasks` to the right of the project form, then click :guilabel:`New`,
.. i18n: 
.. i18n: * from the menu :menuselection:`Project --> Project --> Tasks`, create a new task and assign it
.. i18n:   to an existing project.
..

* 点在项目表单右边的 :guilabel:`ACTION` :guilabel:`Tasks` ，然后点 :guilabel:`New` 按钮,

* 从菜单 :menuselection:`Project --> Project --> Tasks` ，创建一个新任务并将其分配到现有项目.

.. i18n: Each task has one of the following states:
..

每个任务包含以下状态:

.. i18n: * \ ``Draft``\: the task has been entered but has not yet been validated by the person who will
.. i18n:   have to do it,
.. i18n: 
.. i18n: * \ ``In Progress``\: you can start working on the task, hence the task is in progress,
.. i18n: 
.. i18n: * \ ``Done``\: task is completed,
.. i18n: 
.. i18n: * \ ``Cancelled``\: task work is no longer required,
.. i18n: 
.. i18n: * \ ``Pending``\: task is waiting for response of someone else (e.g. customer information).
..

* \ ``草稿``\: 任务已经录入但尚未得到有权限的人的审核,

* \ ``打开``\: 您可以开始工作或该任务已在运作,

* \ ``关闭``\: 任务已经结束,

* \ ``中止``\: 已不需要该任务,

* \ ``待决``\: 任务在等待其他人的响应（如客户信息）.

.. i18n: A task can be assigned to a user, who then becomes responsible for closing it. But you could also
.. i18n: leave it unassigned so that nobody specific will be responsible: various team members instead are
.. i18n: made jointly responsible for working on tasks they have the skills for.
..

一个任务可以被分配给一个用户，他将负责关闭该任务。但你也可以不分配特定人员：取而代之的是各团队成员共同负责他们的
各自擅长的任务。

.. i18n: .. figure::  images/service_task.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Tasks in Project Management*
..

.. figure::  images/service_task.png
   :scale: 75
   :align: center

   *项目管理中的任务*

.. i18n: Each user manages his or her own task using the various menus available. To open the list of
.. i18n: unclosed tasks that have been specifically assigned to you, go to the menu :menuselection:`Project --> Project --> Tasks`. Or to open the unassigned tasks, go to :menuselection:`Project --> Project --> Tasks` and then click \ ``Clear``\ button
.. i18n: and then \ ``Unassigned``\   button.
..

每个用户利用现有的各种菜单管理自己的任务。要打开已专门指派给您未关闭的任务列表，到菜单 :menuselection:`Project --> Project --> Tasks` 。
或是打开未指派的任务，到 :menuselection:`Project --> Project --> Tasks` 然后点 \ ``Clear``\ 按钮再点  \ ``Unassigned``\ 按钮。.

.. i18n: .. tip:: Shortcuts
.. i18n: 
.. i18n: 	Every user should create a link in their own shortcuts to the :menuselection:`Tasks` menu, because they will
.. i18n: 	have to consult this menu several times a day.
..

.. tip:: 快捷方式

	每个用户最好在自己的快捷方式里建立到 :menuselection:`Tasks` 菜单的链接，因为他们将不得不每日多次访问该菜单。

.. i18n: The `Delegations` tab allows you to define links between your tasks. From `Parent Tasks` set the tasks that are related to this task. Use this feature to define the order in which tasks need to be accomplished, i.e. task 2 may not be executed before task 1.
..

`委派` 标签允许你定义你的任务之间的联系。从 `Parent Tasks` 设置和本任务相关联的任务。通过这个方式可以定义需完成任务
的顺序，举例说，任务2不能先于任务1运行。

.. i18n: .. index::
.. i18n:    single: invoicing; tasks
..

.. index::
   single: invoicing; tasks

.. i18n: Invoicing Tasks
.. i18n: ---------------
..

开票任务
---------------

.. i18n: Several methods of invoicing have already been described:
..

开票的几种方法:

.. i18n: * invoicing from a sales order,
.. i18n: 
.. i18n: * invoicing on the basis of analytic costs (service times, expenses),
.. i18n: 
.. i18n: * invoicing on the basis of deliveries,
.. i18n: 
.. i18n: * manual invoicing.
..

* 根据销售订单开票,

* 基于成本（服务时间、费用）开票,

* 基于发货单开票,

* 手工开票.

.. i18n: Although invoicing tasks might appear useful, in certain situations it is best to invoice from the
.. i18n: service or purchase orders instead. These methods of invoicing are more flexible, with various
.. i18n: pricing levels set out in the pricelist, and different products that can be invoiced. And it is
.. i18n: helpful to limit the number of invoicing methods in your company by extending the use of an
.. i18n: invoicing method that you already have.
..

虽然开票任务可能看起来很有用，但在特定情况下，最好从服务商开票或用采购订单代替。这种开票方式更灵活，可根据价目表开出
不同价位的发票，不同产品也可以进行发票开具。扩大你已有的开票方式对限制你公司的开票方式数量也有帮助。

.. i18n: If you want to connect your Sales Order with Project tasks you should create
.. i18n: products such as \ ``Consultant``\  and \ ``Senior Developer``\ . These products should be configured
.. i18n: with :guilabel:`Product Type` \ ``Service``\ , a :guilabel:`Procurement Method` of \ ``Make to Order``\  ,
.. i18n: and a :guilabel:`Supply Method` of \ ``Produce``\. Once you have set this up, OpenERP automatically creates a task in project management when the order is approved.
.. i18n: You can even take this further by adding a default project to your product. In the Product form, on the `Procurement & Locations` tab, enter the default project to which the automatically created task (from the sales order) should be linked.
..

如果你想连接你的销售订单与项目任务，你应该创建类似 \ ``咨询``\ 和 \ ``深度开发``\ 这样的产品。这些产品应如下配置：:guilabel:`产品类型` 是 \ ``服务``\ ，
:guilabel:`生产方法` 是 \ ``据订单生产``\ ， :guilabel:`供应方法` 是 \ ``生产``\ 。一旦你按此设置，当订单被批准时OpenERP会自动在项目管理中创建一个任务。你甚至
可以在产品中添加一个默认项目。在“产品”表单中，在 `需求与库位` 页签中，输入可以（从销售订单）自动创建任务的默认项目。

.. i18n: You can also change some of the order parameters, which affects the invoice:
..

您还可以改变某些参数的顺序，从而影响发票:

.. i18n: *  :guilabel:`Shipping Policy` : \ ``Invoice on Order After Delivery`` \ (when the task is closed),
.. i18n: 
.. i18n: *  :guilabel:`Invoice On` : \ ``Shipped Quantities`` \ (actual hours in the task).
..

*  :guilabel:`出运政策` : \ ``发票交付后``\ （任务关闭时） 

*  :guilabel:`发票当时情况` : \ ``实际发货量`` \ (任务的实际工时).

.. i18n: Create the `Sales Order` using the product :guilabel:`Consultant` with the above configuration and confirm it.
.. i18n: You can find the task created from this sale order using the menu :menuselection:`Project --> Project --> Tasks`.
.. i18n: Once you find that task, click on the :guilabel:`Start Task` button in order to start it.  You have to manually assign the
.. i18n: project for this task, unless you specified a default project in the Product form. When you complete the task, enter the information in the :guilabel:`Task Work` field. Then click the :guilabel:`Done` button in order to indicate to OpenERP that this task is finished.
.. i18n: As an example, the new task `SO008:Create SRS` generated from sales order `SO0008` is shown in following figure.
..

利用上述配置创建产品为 :guilabel:`咨询` 的 `销售订单` ，并确认它。您使用 :menuselection:`Project --> Project --> Tasks` 菜单
会发现根据销售订单创建的 :guilabel:`任务` 。一旦找到该任务，点击 `开始任务` 按钮以启用它。您必须手动指派这项任务所属的项目，
除非你在产品表单提供默认的项目。当你完成任务后，在 :guilabel:`工作任务` 字段中输入完成信息。单击 :guilabel:`完成` 按钮，以
通知OpenERP已完成这个任务。作为一个例子，新任务 `SO008：Create SRS` 如下图所示，据销售订单 `SO008` 生成的 `SO008：Create SRS` 。

.. i18n: .. figure::  images/project_task_from_sale_order.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Task created from Sales Order*
..

.. figure::  images/project_task_from_sale_order.png
   :scale: 75
   :align: center

   *创建自销售订单的任务*

.. i18n: .. tip:: You need to carefully configure the analytic account related to this project. If you use the Billing tab of the project to do this, the analytic account linked to the project will automatically get the related settings.
..

.. tip:: 你需要仔细配置有关这个项目的辅助核算，如果您使用项目的 `结算` 标签来做到这一点，与项目有关的成本帐户将自动获得相关的设置。

.. i18n: After finishing this task, go to the menu :menuselection:`Project --> Invoicing --> Invoice Tasks Work` in order to
.. i18n: find the list of uninvoiced task works.
.. i18n: Click the action :guilabel:`Invoice analytic lines` when you want to create an invoice for this task work.
..

任务结束后，到菜单 :menuselection:`项目 --> 开发票 --> 根据任务开票` 去找未开票任务。 当您想根据任务开发票时点击 :guilabel:`辅助核算记录` 行。

.. i18n: .. figure::  images/project_invoice_from_task_work.png
.. i18n:    :scale: 70
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Form to Create Invoice from Tasks Work*
..

.. figure::  images/project_invoice_from_task_work.png
   :scale: 70
   :align: center

   *Form to Create Invoice from Tasks Work*

.. i18n: Priority Management
.. i18n: -------------------
..

项目优先级管理
-------------------

.. i18n: Several methods can be used for ordering tasks by their respective priorities. OpenERP orders
.. i18n: tasks based on a function of the following fields: :guilabel:`Sequence`, :guilabel:`Priority`, and
.. i18n: :guilabel:`Deadline`.
..

有多种方法可以按各自重点确定任务的顺序。OpenERP按照以下方面的功能为任务排序： :guilabel:`序列` ， :guilabel:`优先次序` ， :guilabel:`最后期限` 。

.. i18n: Use the :guilabel:`Sequence` field on the second tab, :guilabel:`Extra Info`, to plan a
.. i18n: project made up of several tasks. In the case of an IT project, for example, where development tasks
.. i18n: are done in a given order, the first task to do will be sequence number 1, then numbers 2, 3, 4 and
.. i18n: so on. When you first open the list of project tasks, they are listed in their sequence order. You can simply drag and drop tasks to change their sequence.
..

使用第二张表单中的 :guilabel:`序列` 功能，:guilabel:`附加信息` 来为由多项任务组成的项目作规划。以软件项目举一个例子，所开发的
任务已给出序列，第一项任务为序号一号，以此类推2,3,4等。当你第一次打开项目任务的列表，任务已按序号排列好。你可简单地拖放
任务来改变顺序。

.. i18n: You can use one of these three ordering methods, or combine several of them, depending on the
.. i18n: project.
..

你可从这三种排序的方式中选一种，或者综合运用，这由项目决定。

.. i18n: .. index::
.. i18n:    single: module; scrum
.. i18n:    single: agile (method)
..

.. index::
   single: module; scrum
   single: agile (method)

.. i18n: .. note:: Agile Methods
.. i18n: 
.. i18n: 	OpenERP implements the agile methodology Scrum for IT development projects in the :mod:`project_scrum`
.. i18n: 	module.
.. i18n: 
.. i18n: 	Scrum supplements the task system with the following concepts:
.. i18n: 	long-term planning, sprints, iterative development, progress meetings, burndown chart, and product
.. i18n: 	backlog.
.. i18n: 
.. i18n: 	Look at the site: http://controlchaos.com for more information on the Scrum methodology.
..

.. note:: 灵活的方式

	OpenERP为软件开发项目项目组合模块补充了灵活的方法论 :mod:`project_scrum` ,

	`Srum` 为系统补充了以下概念：长期计划，冲刺，重复开发，进度报告会议，燃尽图，产品订单。

	查看以下网址: http://controlchaos.com 获取更多有关 `Srum` 的信息。

.. i18n: .. figure::  images/service_project_gantt.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Gantt chart, calculated for earliest delivery*
..

.. figure::  images/service_project_gantt.png
   :scale: 75
   :align: center

   *甘特图，计算最早发运日期*

.. i18n: You can set the Working Time in the project file. If you do not specify
.. i18n: anything, OpenERP assumes by default that you work 8 hours a day from Monday to Sunday. Once the
.. i18n: time is specified you can call up a project Gantt chart from Tasks. The system then
.. i18n: calculates a project plan for earliest delivery using task ordering and the working time.
..

你可在项目文件中设定工作时间。如果不设定，OpenERP会默认为周一到周日每天工作八小时。时间确定后，你可从任务中得到甘特图。
系统之后根据任务顺序和工作时间制定最快完成任务的项目计划。

.. i18n: .. tip:: Calendar View
.. i18n: 
.. i18n: 	OpenERP can give you a calendar view of the different tasks in both the web client and the GTK client.
.. i18n: 	This is all based on the deadline data and displays only tasks that have a deadline.
.. i18n: 	You can then delete, create or modify tasks using drag and drop (only in web).
.. i18n: 
.. i18n: 	.. figure::  images/service_task_calendar.png
.. i18n: 	   :scale: 65
.. i18n: 	   :align: center
.. i18n: 
.. i18n: 	*Calendar View of the System Tasks*
..

.. tip:: 日历视图

	OpenERP在web客户端和Gtk客户端下都提供不同任务的日历视图。您可以通过拖放删除、创建、修改任务（仅限于web客户端）。

	.. figure::  images/service_task_calendar.png
	   :scale: 65
	   :align: center

	*Calendar View of the System Tasks*

.. i18n: .. index:: delegation (task)
..

.. index:: delegation (task)

.. i18n: Delegate your Tasks
.. i18n: -------------------
..

任务委派
-------------------

.. i18n: To delegate a task to another user, you can just change the person responsible for that task. However,
.. i18n: the system does not help you track tasks that you have delegated, such as monitoring of work done, if
.. i18n: you do it this way.
..

通过委派任务给另外一个用户，您可以变更任务负责人。但是，通过这种方法系统无法帮助您跟踪您委派出去的任务，比方监控工作是否完成。

.. i18n: .. figure::  images/service_task_delegate.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Form for Delegating a Task to Another User*
..

.. figure::  images/service_task_delegate.png
   :scale: 75
   :align: center

   *委派任务给其他人表单*

.. i18n: Instead, you can use the :guilabel:`Delegate` button on a task.
..

作为替代，您可以在任务上使用 :guilabel:`委派` 按钮。

.. i18n: .. *Delegate* \ ``Pending``\
..

.. *Delegate* \ ``Pending``\

.. i18n: .. \ ``Pending``\  \ ``Open``\
..

.. \ ``Pending``\  \ ``Open``\

.. i18n: The system enables you to modify tasks at all levels in the chain of delegation, to add additional
.. i18n: information. A task can therefore start as a global objective and become more detailed as it is
.. i18n: delegated down in the hierarchy.
..

您可用该系统调整任务链中不同级别的任务，添加补充信息。任务由一项整体的目标开始，按照等级委托下来变得具体化。

.. i18n: The second tab on the task form gives you a complete history of the chain of delegation for each
.. i18n: task. You can find a link to the parent task there, and the different tasks that have been
.. i18n: delegated.
..

任务表单第二页签，给您一委派任务的完整的历史。您可以找到一个父任务的链接，以及已委派的不同任务。

.. i18n: .. Copyright © Open Object Press. All rights reserved.
..

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.
..

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the OpenERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.
..

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.
..

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.
..

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.
..

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium
..

.. Published by Open Object Press, Grand Rosière, Belgium
