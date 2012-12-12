.. i18n: =====================================
.. i18n: Introduction to Business Applications
.. i18n: =====================================
..

=====================================
业务应用介绍
=====================================

.. i18n: The complexity of an ERP is usually due to the high number of available features. Most of the users of the system use only a few features, according to their job position(s) in the company. In order to remain easy to use, the different features are split into business applications.
..

一个完整复杂的 ERP 系统通常包含了大量的功能。而根据他们在公司的工作岗位的不同，大多数用户往往只能用到少量一些功能。为了保持简单易用，这些功能分成不同的模块应用。

.. i18n: The main idea is that a user is often working in a particular context (working on a project, recording accounting entries). When he is in such a context, he should directly see all features related to this context (=business application). We try to create business applications according to user's position in the company: salesman, project user, purchasers, accountant, etc.
..

其主要思想是用户往往在一个特定岗位工作（如为某个项目工作，会计分录等）。当这个用户处于这样的情况下，他应该直接看到有关这方面的全部功能。我们试图创建各个不同的模块，按照用户的工作职位划分：业务员，项目用户，采购商，会计师等。

.. i18n: .. note:: 
.. i18n: 
.. i18n: 	OpenERP distinguishes between modules and applications. A module is a set of features packaged together for technical reasons. A business application includes all the features coming from different modules and creates a menu structure according to a specific role in the company. An application is usually composed of a set of modules.
..

.. note:: 

        注意OpenERP的模块和应用套件之间的区别。模块是从技术上将一组功能打包在一起。应用套件则包括了所有的功能，根据该公司在一个特定的角色创建一系列的菜单。一个应用程序通常是由数个模块组成。

.. i18n: These business applications define a context of work and all terminology used in an application must be relative to this context, so that it's easier to understand : a purchaser will see screens adapted to purchasing operations. An accountant may see the same data, but in an accounting context. (adapted terminology, adapted menus, adapted default values in each screen)
..

这些业务应用定义了工作场景和相关的全部术语，因此就很容易理解：采购员可以看到订购相关的屏幕，而一个会计也许可以在财务会计屏幕中看到相同的数据（相应的术语、相应的菜单、在每个屏幕相应的默认值）

.. i18n: As an example, a purchaser will see the following menu on the left:
..

例如，采购员可以看到以下菜单：

.. i18n: * Purchases
.. i18n:    * Request for Quotations
.. i18n:    * Purchase Orders
.. i18n: * Address Book
.. i18n:    * Suppliers
.. i18n: * Invoice Control
.. i18n:    * Supplier Invoices to Receive
.. i18n: * Inventory Control
.. i18n:    * Incoming Shipments
..

* Purchases
   * Request for Quotations
   * Purchase Orders
* Address Book
   * Suppliers
* Invoice Control
   * Supplier Invoices to Receive
* Inventory Control
   * Incoming Shipments

.. i18n: The menu related to the application is always visible on the left of the screen and the applications are displayed in the red top menubar.
..

The menu related to the application is always visible on the left of the screen and the applications are displayed in the red top menubar.

.. i18n: .. figure:: Pictures/1.1menu_application.png
.. i18n:    :align: center
..

.. figure:: Pictures/1.1menu_application.png
   :align: center

.. i18n: Business Application means that one responsible user could stay in only one menu to achieve his work.
..

Business Application means that one responsible user could stay in only one menu to achieve his work.

.. i18n: Several menus may refer to the same view (with adapted default values) because they are used by several applications. As an example, a warehouse manager should see the following menus:
..

Several menus may refer to the same view (with adapted default values) because they are used by several applications. As an example, a warehouse manager should see the following menus:

.. i18n: * Warehouse Management
.. i18n:    * Incoming Shipments
.. i18n:    * Internal Moves
.. i18n:    * Delivery Orders
..

* Warehouse Management
   * Incoming Shipments
   * Internal Moves
   * Delivery Orders

.. i18n: In that example, Incoming Shipments is available in the “warehouse management” application and in the “purchase management” application. The menu Suppliers is also referred to as Partners in the “Accounting” application, but partners includes Suppliers & Customers. So, the terminology is adapted to each application.
..

In that example, Incoming Shipments is available in the “warehouse management” application and in the “purchase management” application. The menu Suppliers is also referred to as Partners in the “Accounting” application, but partners includes Suppliers & Customers. So, the terminology is adapted to each application.
