.. i18n: =====================
.. i18n: Business Applications
.. i18n: =====================
..

=====================
应用套件
=====================

.. i18n: Defining new applications or completing existing ones
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++++++++
..

定义新的应用或完成已存在的应用
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: We usually try to define new business applications related to job positions in the enterprise. These are good examples of applications: Purchase, Sales, Accounting and Project. Don't create business application by features. These are bad examples of business applications: lunch orders management, expenses sheets, etc.
..

一般来说我们是根据企业内部的职位来定义相关的业务套件。好的例子，如采购、销售、财务和项目管理等。
不好的例子就是按照功能来创建业务套件，如午餐订单管理，费用表，等等。


.. i18n: If you have specific features that don't belong in the existing business applications, you can put them in the “Miscelleanous Tools” application.
..

如果你的功能不属于已有的应用套件，你可以把它们放在“其他模块”应用中

.. i18n: Configuration wizards of business applications.
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++
..

业务应用的配置向导
+++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: Each application must create an entry in the main base_setup wizard that shows all the possible business applications defined in quality certified modules only.
..

每个应用都必须在主配置界面创建一个条目，上面显示了经过质量认证各种应用。

.. i18n: .. figure:: Pictures/1.2.Installation_of_modules.png
.. i18n:    :align: center
..

.. figure:: Pictures/1.2.Installation_of_modules.png
   :align: center

.. i18n: You can also create one configuration wizard dedicated to your business application. For example, when you install project management, you get this wizard:
..

你也可以为你的应用创建一个配置向导。例如，当你安装项目管理应用后，你可以看到以下的配置向导：

.. i18n: .. figure:: Pictures/1.3.Project_management.png
.. i18n:    :align: center
..

.. figure:: Pictures/1.3.Project_management.png
   :align: center

.. i18n: Business Applications must be complete
.. i18n: ++++++++++++++++++++++++++++++++++++++
..

应用模块功能完整
++++++++++++++++++++++++++++++++++++++

.. i18n: Each user/role must be able to perform most of their tasks from one business application. For example, a salesman should see in his menu: Leads, Opportunities, Meetings, Sales Orders, Sales to Invoice, etc. He should not be forced to go to the accounting application to invoice the sales.
..

每个用户/角色都应该在一个应用下完成自身的大部分工作。例如，一个销售人员应该可以看到线索、商机、会议、销售订单、销售发票等菜单。他不应该强制要去财务应用模块中才能看到销售发票。

.. i18n: Transversal features, used by all applications
.. i18n: ++++++++++++++++++++++++++++++++++++++++++++++
..

横向功能，能够被所有应用使用
++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: Some features should be accessible by all users, regardless of which application they usually work in. For example, most users should have access to: Partners, Agenda of Meetings, Products. In that case, you put the menu in the applications that needs these features more. (Example: the address book is in the sales, purchases and accounting application)
.. i18n: And, these features must be set as shortcuts for every user in the system by default, at the creation of the user.
..

有些功能应该可以被所有用户访问，无论他们是什么岗位。例如，大多数用户应该可以访问合作伙伴、会议日程、产品等。这种情况下，你可以把这些功能菜单放在各个应用下（如：联系人菜单在销售、采购、财务等模块都有）。而且在创建用户的时候，系统默认为这些用户创建菜单的快捷方式。

.. i18n: Access Rights must define groups per application.
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++++
..

每个应用必须为用户组定义权限
+++++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: The groups defined by each module must be directly related to business application. So, if you have an application which is “Accounting”.  All groups within this application must be like: “Accounting / Accountant”, “Accounting / Financial Manager”, etc.
..

每个应用组都必须按照相关的工作职责定义权限。因此，如果你有一个财务应用模块，这个应用的组应该是这样的：“财务/会计师”，“财务/财务经理”，等等。

.. i18n: One dashboard defined per application
.. i18n: +++++++++++++++++++++++++++++++++++++
..

每个应用定义一个面板
+++++++++++++++++++++++++++++++++++++

.. i18n: Each business application must have one dashboard attached to its root menu item. When a user enters a business application, they should see the dashboard related to this application.
..

每个应用应该在相应的根菜单下定义一个面板。当用户进入应用时，该用户应该可以看到相应的应用面板。
