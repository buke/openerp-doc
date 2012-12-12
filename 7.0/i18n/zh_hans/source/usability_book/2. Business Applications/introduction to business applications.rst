
.. i18n: =====================================
.. i18n: Introduction to Business Applications
.. i18n: =====================================
..

=====================================
Introduction to Business Applications
=====================================

.. i18n: The complexity of an ERP is usually due to the high number of available features. Most of the users of the system use only a few features, according to their job position(s) in the company. In order to remain easy to use, the different features are split into business applications.
..

The complexity of an ERP is usually due to the high number of available features. Most of the users of the system use only a few features, according to their job position(s) in the company. In order to remain easy to use, the different features are split into business applications.

.. i18n: The main idea is that a user is often working in a particular context (working on a project, recording accounting entries). When he is in such a context, he should directly see all features related to this context (=business application). We try to create business applications according to user's position in the company: salesman, project user, purchasers, accountant, etc.
..

The main idea is that a user is often working in a particular context (working on a project, recording accounting entries). When he is in such a context, he should directly see all features related to this context (=business application). We try to create business applications according to user's position in the company: salesman, project user, purchasers, accountant, etc.

.. i18n: .. note:: 
.. i18n: 
.. i18n: 	OpenERP distinguishes between modules and applications. A module is a set of features packaged together for technical reasons. A business application includes all the features coming from different modules and creates a menu structure according to a specific role in the company. An application is usually composed of a set of modules.
..

.. note:: 

	OpenERP distinguishes between modules and applications. A module is a set of features packaged together for technical reasons. A business application includes all the features coming from different modules and creates a menu structure according to a specific role in the company. An application is usually composed of a set of modules.

.. i18n: These business applications define a context of work and all terminology used in an application must be relative to this context, so that it's easier to understand : a purchaser will see screens adapted to purchasing operations. An accountant may see the same data, but in an accounting context. (adapted terminology, adapted menus, adapted default values in each screen)
..

These business applications define a context of work and all terminology used in an application must be relative to this context, so that it's easier to understand : a purchaser will see screens adapted to purchasing operations. An accountant may see the same data, but in an accounting context. (adapted terminology, adapted menus, adapted default values in each screen)

.. i18n: As an example, a purchaser will see the following menu on the left:
..

As an example, a purchaser will see the following menu on the left:

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
