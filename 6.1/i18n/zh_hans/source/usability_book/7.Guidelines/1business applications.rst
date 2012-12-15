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

Each application must create an entry in the main base_setup wizard that shows all the possible business applications defined in quality certified modules only.

.. i18n: .. figure:: Pictures/1.2.Installation_of_modules.png
.. i18n:    :align: center
..

.. figure:: Pictures/1.2.Installation_of_modules.png
   :align: center

.. i18n: You can also create one configuration wizard dedicated to your business application. For example, when you install project management, you get this wizard:
..

You can also create one configuration wizard dedicated to your business application. For example, when you install project management, you get this wizard:

.. i18n: .. figure:: Pictures/1.3.Project_management.png
.. i18n:    :align: center
..

.. figure:: Pictures/1.3.Project_management.png
   :align: center

.. i18n: Business Applications must be complete
.. i18n: ++++++++++++++++++++++++++++++++++++++
..

业务应用必须完整
++++++++++++++++++++++++++++++++++++++

.. i18n: Each user/role must be able to perform most of their tasks from one business application. For example, a salesman should see in his menu: Leads, Opportunities, Meetings, Sales Orders, Sales to Invoice, etc. He should not be forced to go to the accounting application to invoice the sales.
..

Each user/role must be able to perform most of their tasks from one business application. For example, a salesman should see in his menu: Leads, Opportunities, Meetings, Sales Orders, Sales to Invoice, etc. He should not be forced to go to the accounting application to invoice the sales.

.. i18n: Transversal features, used by all applications
.. i18n: ++++++++++++++++++++++++++++++++++++++++++++++
..

横向功能，能够被所有应用使用
++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: Some features should be accessible by all users, regardless of which application they usually work in. For example, most users should have access to: Partners, Agenda of Meetings, Products. In that case, you put the menu in the applications that needs these features more. (Example: the address book is in the sales, purchases and accounting application)
.. i18n: And, these features must be set as shortcuts for every user in the system by default, at the creation of the user.
..

Some features should be accessible by all users, regardless of which application they usually work in. For example, most users should have access to: Partners, Agenda of Meetings, Products. In that case, you put the menu in the applications that needs these features more. (Example: the address book is in the sales, purchases and accounting application)
And, these features must be set as shortcuts for every user in the system by default, at the creation of the user.

.. i18n: Access Rights must define groups per application.
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++++
..

每个应用必须为用户组定义权限
+++++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: The groups defined by each module must be directly related to business application. So, if you have an application which is “Accounting”.  All groups within this application must be like: “Accounting / Accountant”, “Accounting / Financial Manager”, etc.
..

The groups defined by each module must be directly related to business application. So, if you have an application which is “Accounting”.  All groups within this application must be like: “Accounting / Accountant”, “Accounting / Financial Manager”, etc.

.. i18n: One dashboard defined per application
.. i18n: +++++++++++++++++++++++++++++++++++++
..

每个应用定义一个面板
+++++++++++++++++++++++++++++++++++++

.. i18n: Each business application must have one dashboard attached to its root menu item. When a user enters a business application, they should see the dashboard related to this application.
..

Each business application must have one dashboard attached to its root menu item. When a user enters a business application, they should see the dashboard related to this application.
