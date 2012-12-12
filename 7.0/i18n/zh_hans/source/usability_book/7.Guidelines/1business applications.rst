
.. i18n: =====================
.. i18n: Business Applications
.. i18n: =====================
..

=====================
Business Applications
=====================

.. i18n: Defining new applications or completing existing ones
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++++++++
..

Defining new applications or completing existing ones
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: We usually try to define new business applications related to job positions in the enterprise. These are good examples of applications : Purchase, Sales, Accounting, Project, etc. Don't create business application by features. These are wrong examples of business applications : lunch orders management, expenses sheets, etc.
..

We usually try to define new business applications related to job positions in the enterprise. These are good examples of applications : Purchase, Sales, Accounting, Project, etc. Don't create business application by features. These are wrong examples of business applications : lunch orders management, expenses sheets, etc.

.. i18n: If you have specific features that do not belong the existing business applications, you can put them in the “Miscelleanous Tools” application.
..

If you have specific features that do not belong the existing business applications, you can put them in the “Miscelleanous Tools” application.

.. i18n: Configuration wizards of business applications.
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++
..

Configuration wizards of business applications.
+++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: Each application must create an entry in the main base_setup wizard that shows all the possible business applications defined in quality certified modules only.
..

Each application must create an entry in the main base_setup wizard that shows all the possible business applications defined in quality certified modules only.

.. i18n: .. figure:: Pictures/1.2.Installation_of_modules.png
.. i18n:    :align: center
..

.. figure:: Pictures/1.2.Installation_of_modules.png
   :align: center

.. i18n: You can also create one configuration wizard dedicated to your business application. Example, when you install the project management, you get this wizard:
..

You can also create one configuration wizard dedicated to your business application. Example, when you install the project management, you get this wizard:

.. i18n: .. figure:: Pictures/1.3.Project_management.png
.. i18n:    :align: center
..

.. figure:: Pictures/1.3.Project_management.png
   :align: center

.. i18n: Business Applications must be complete
.. i18n: ++++++++++++++++++++++++++++++++++++++
..

Business Applications must be complete
++++++++++++++++++++++++++++++++++++++

.. i18n: One user/role must be able to perform most of his tasks from one business application. He should not be forced to switch to another application to perform the tasks of the same role. Example, a salesman should see in his menu: Leads, Opportunities, Meetings, Sales Orders, Sales to Invoice, etc. He should not be forced to go to the accounting application to invoice the sales.
..

One user/role must be able to perform most of his tasks from one business application. He should not be forced to switch to another application to perform the tasks of the same role. Example, a salesman should see in his menu: Leads, Opportunities, Meetings, Sales Orders, Sales to Invoice, etc. He should not be forced to go to the accounting application to invoice the sales.

.. i18n: Transversal features, used by all applications
.. i18n: ++++++++++++++++++++++++++++++++++++++++++++++
..

Transversal features, used by all applications
++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: Some features should be accessible by all users, not depending on the application they usually works in. As an example, most of the users should have an access to: Partners, Agenda of Meetings, Products. In that case, you put the menu in the applications that needs these features more. (Example: the address book is in the sales, purchases and accounting application)
.. i18n: And, these features must be set as shortcuts for every user in the system by default, at the creation of the user.
..

Some features should be accessible by all users, not depending on the application they usually works in. As an example, most of the users should have an access to: Partners, Agenda of Meetings, Products. In that case, you put the menu in the applications that needs these features more. (Example: the address book is in the sales, purchases and accounting application)
And, these features must be set as shortcuts for every user in the system by default, at the creation of the user.

.. i18n: Access Rights must define groups per application.
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++++
..

Access Rights must define groups per application.
+++++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: The groups defined by each module must be directly related to business application. So, if you have an application which is “Accounting”.  All groups within this application must be like: “Accounting / Accountant”, “Accounting / Financial Manager”, etc.
..

The groups defined by each module must be directly related to business application. So, if you have an application which is “Accounting”.  All groups within this application must be like: “Accounting / Accountant”, “Accounting / Financial Manager”, etc.

.. i18n: One dashboard defined per application
.. i18n: +++++++++++++++++++++++++++++++++++++
..

One dashboard defined per application
+++++++++++++++++++++++++++++++++++++

.. i18n: Each business application must have one dashboard attached to his root menuitem. When a user enters in a business application, he should see the dashboard related to this application.
..

Each business application must have one dashboard attached to his root menuitem. When a user enters in a business application, he should see the dashboard related to this application.
