.. i18n: .. index::
.. i18n:    single: access rights
.. i18n:    single: access; user
..

.. index::
   single: access rights
   single: access; user

.. i18n: User Login
.. i18n: ==========
..

用户登陆
==========

.. i18n: .. tip:: Managing Passwords
.. i18n: 
.. i18n:    If you let users change their passwords for themselves, you will have no direct control over the
.. i18n:    password they choose.
.. i18n:    You should have a written policy about password strength to try to maintain a level of security in
.. i18n:    your system.
..

.. tip:: Managing Passwords

   如果你让用户有权更改自己的密码，你将无法直接控制他们的密码。
   你应该有一个书面的关于密码强度的政策，以保证系统的安全。

.. i18n: .. index::
.. i18n:    single: module; users_ldap
..

.. index::
   single: module; users_ldap

.. i18n: .. tip:: Managing Users through LDAP
.. i18n: 
.. i18n: 	With the :mod:`users_ldap` module, user accounts can be managed through an LDAP directory that can be
.. i18n: 	made common to various different company resources.
.. i18n: 
.. i18n: 	Connection parameters for the LDAP directory are then registered with the company definition.
.. i18n: 	You can provide a user profile template there from which new users are automatically created during
.. i18n: 	their first connection to OpenERP.
..

.. tip:: 通过LDAP管理用户


        使用:mod:`users_ldap`模块，用户帐户可通过LDAP目录，共同管理各种不同的公司资源。
        LDAP目录中的连接参数，根据公司定义进行注册。你可以提供一个用户设置文件的模板，
        新用户在第一次连接到OpenERP自动创建。




.. i18n: .. index::
.. i18n:    single: LDAP
..

.. index::
   single: LDAP

.. i18n: .. note:: LDAP
.. i18n: 
.. i18n: 	The LDAP protocol (Lightweight Directory Access Protocol) enables you to manage common directories
.. i18n: 	for various different resources through your standard TCP/IP network.
.. i18n: 
.. i18n: 	This enables users in the company to have the same username and password to access all
.. i18n: 	their applications (such as email and intranet).
..

.. note:: LDAP

	LDAP协议（Lightweight Directory Access Protocol），使您通过标准的TCP/IP网络
        为各种不同的资源管理公共目录这使得该公司的用户有相同的用户名和密码来访问所有
        的应用程序（如Email和Intranet）。


.. i18n: Managing Access Rights
.. i18n: ======================
..

Managing Access Rights
======================

.. i18n: One of the most important areas in configuring OpenERP is how to manage access rights to the
.. i18n: information in it.
..

One of the most important areas in configuring OpenERP is how to manage access rights to the
information in it.

.. i18n: You are planning to put everything significant to your business into the system, but most of your
.. i18n: staff need see only part of it, and may need to change even less of it. Who should have rights to
.. i18n: what, and how do you manage that?
..

You are planning to put everything significant to your business into the system, but most of your
staff need see only part of it, and may need to change even less of it. Who should have rights to
what, and how do you manage that?

.. i18n: OpenERP's approach to rights management is highly flexible. Each user can belong to one or more
.. i18n: groups, and the group(s) you belong to determine(s):
..

OpenERP's approach to rights management is highly flexible. Each user can belong to one or more
groups, and the group(s) you belong to determine(s):

.. i18n: * the visibility of each menu item and
.. i18n: 
.. i18n: * the accessibility of each table in the database.
..

* the visibility of each menu item and

* the accessibility of each table in the database.

.. i18n: For example, the group \ ``Warehouse / User`` \ may only be given access to some of the menus in
.. i18n: :menuselection:`Warehouse`, and may have no access to any of the accounting information. Each system user who works in
.. i18n: stores is given membership of the ``Warehouse / User`` group. If some users also work elsewhere, they would also be
.. i18n: given membership of other groups.
..

For example, the group \ ``Warehouse / User`` \ may only be given access to some of the menus in
:menuselection:`Warehouse`, and may have no access to any of the accounting information. Each system user who works in
stores is given membership of the ``Warehouse / User`` group. If some users also work elsewhere, they would also be
given membership of other groups.

.. i18n: .. index::
.. i18n:    pair: user; group
..

.. index::
   pair: user; group

.. i18n: Groups and Users
.. i18n: ================
..

Groups and Users
================

.. i18n: To configure access rights, you would start by defining the groups. It is important for the groups to
.. i18n: be representative of your company's job functions rather than of its individual employees.
..

To configure access rights, you would start by defining the groups. It is important for the groups to
be representative of your company's job functions rather than of its individual employees.

.. i18n: So if your finance director is also your sales director, you should create both a Finance Director
.. i18n: group and a Sales Director group, even though they are both the same person, and would both be
.. i18n: assigned to this user in practice. This gives you flexibility for the future.
..

So if your finance director is also your sales director, you should create both a Finance Director
group and a Sales Director group, even though they are both the same person, and would both be
assigned to this user in practice. This gives you flexibility for the future.

.. i18n: You should also create groups within departmental areas that have different levels of access
.. i18n: rights. For example, if you create a \ ``Sales Director`` \ group and a \ ``Sales`` \ group avoid
.. i18n: assigning exactly the same rights to each group. The first could see all the of reports, while the
.. i18n: second could be restricted to seeing quotations. You could either make the Sales Director a
.. i18n: member of both groups, and give the \ ``Sales Director`` \ group a limited set of extra rights, or give the
.. i18n: \ ``Sales Director`` \ group all the rights it needs for a Sales Director to belong only to this one
.. i18n: group. You should choose the scheme that gives you most flexibility and then stick with it to
.. i18n: maintain consistency.
..

You should also create groups within departmental areas that have different levels of access
rights. For example, if you create a \ ``Sales Director`` \ group and a \ ``Sales`` \ group avoid
assigning exactly the same rights to each group. The first could see all the of reports, while the
second could be restricted to seeing quotations. You could either make the Sales Director a
member of both groups, and give the \ ``Sales Director`` \ group a limited set of extra rights, or give the
\ ``Sales Director`` \ group all the rights it needs for a Sales Director to belong only to this one
group. You should choose the scheme that gives you most flexibility and then stick with it to
maintain consistency.

.. i18n: .. index::
.. i18n:    pair:  system; administrator
..

.. index::
   pair:  system; administrator

.. i18n: .. tip:: Flexibility in Managing Access
.. i18n: 
.. i18n: 	To give yourself flexibility, you can ensure that a trusted staff member
.. i18n: 	(perhaps a director or someone in accounts, or even the system administrator) is given wide rights
.. i18n: 	to use the system,
.. i18n: 	and is authorized by the management to carry out specific tasks for people.
..

.. tip:: Flexibility in Managing Access

	To give yourself flexibility, you can ensure that a trusted staff member
	(perhaps a director or someone in accounts, or even the system administrator) is given wide rights
	to use the system,
	and is authorized by the management to carry out specific tasks for people.

.. i18n: .. index::
.. i18n:    single: access; menu
..

.. index::
   single: access; menu

.. i18n: Access Rights for Menus
.. i18n: -----------------------
..

Access Rights for Menus
-----------------------

.. i18n: To get a feel for rights management in OpenERP, you will create a new \ ``Stock1`` \  group, with
.. i18n: access to the *Warehouse* menu items. You will then create a stores person user who is a member
.. i18n: of the \ ``Stock1`` \  group.
..

To get a feel for rights management in OpenERP, you will create a new \ ``Stock1`` \  group, with
access to the *Warehouse* menu items. You will then create a stores person user who is a member
of the \ ``Stock1`` \  group.

.. i18n: To create a new group, use the menu :menuselection:`Administration --> Users --> Groups`. Enter the
.. i18n: group name ``Stock1``.
..

To create a new group, use the menu :menuselection:`Administration --> Users --> Groups`. Enter the
group name ``Stock1``.

.. i18n: Then to create a new user linked to this, use :menuselection:`Administration --> Users --> Users` to
.. i18n: enter the following:
..

Then to create a new user linked to this, use :menuselection:`Administration --> Users --> Users` to
enter the following:

.. i18n: *  :guilabel:`User Name` : \ ``Stores Person`` \ ,
.. i18n: 
.. i18n: *  :guilabel:`Login` : \ ``stores`` \ ,
.. i18n: 
.. i18n: *  :guilabel:`Password` : \ ``stores`` \ ,
.. i18n: 
.. i18n: *  :guilabel:`Menu Action` : \ ``Menu`` \ .
..

*  :guilabel:`User Name` : \ ``Stores Person`` \ ,

*  :guilabel:`Login` : \ ``stores`` \ ,

*  :guilabel:`Password` : \ ``stores`` \ ,

*  :guilabel:`Menu Action` : \ ``Menu`` \ .

.. i18n: In the :guilabel:`Groups` section of the user form, add the \ ``Stock1`` \ group that you
.. i18n: just created.
..

In the :guilabel:`Groups` section of the user form, add the \ ``Stock1`` \ group that you
just created.

.. i18n: .. figure::  images/menu_access.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Groups that have access to the Warehouse menu*
..

.. figure::  images/menu_access.png
   :scale: 75
   :align: center

   *Groups that have access to the Warehouse menu*

.. i18n: Save the user, then go into the menu :menuselection:`Administration --> Customization --> User
.. i18n: Interface --> Menu Items` to get a list of menus. Filter this list using the search field :guilabel:`Menu` to
.. i18n: get the :menuselection:`Warehouse` menu item. In the form describing the menu, add \ ``Stock1`` \ into the :guilabel:`Groups` field. From now on, only members of
.. i18n: the \ ``Warehouse / Manager`` \, \ ``Warehouse / User`` \ and \ ``Stock1`` \ group will be able to see
.. i18n: this menu item in their main menu list.
..

Save the user, then go into the menu :menuselection:`Administration --> Customization --> User
Interface --> Menu Items` to get a list of menus. Filter this list using the search field :guilabel:`Menu` to
get the :menuselection:`Warehouse` menu item. In the form describing the menu, add \ ``Stock1`` \ into the :guilabel:`Groups` field. From now on, only members of
the \ ``Warehouse / Manager`` \, \ ``Warehouse / User`` \ and \ ``Stock1`` \ group will be able to see
this menu item in their main menu list.

.. i18n: .. tip:: Menu Hierarchy
.. i18n: 
.. i18n: 	Since menus are hierarchical, there is no need to hide access to lower menus:
.. i18n: 	once you have configured :menuselection:`Warehouse` this way, all lower-level menus become invisible to
.. i18n: 	members of other groups.
..

.. tip:: Menu Hierarchy

	Since menus are hierarchical, there is no need to hide access to lower menus:
	once you have configured :menuselection:`Warehouse` this way, all lower-level menus become invisible to
	members of other groups.

.. i18n: .. tip:: Security
.. i18n: 
.. i18n: 	This method of managing access to menus does not guarantee that users are prevented from reaching
.. i18n: 	hidden business objects in the system in other ways.
.. i18n: 	For example, hiding the :guilabel:`Invoices` menu will not prevent people reaching invoices through purchase and
.. i18n: 	sales orders, or by guessing the URL.
.. i18n: 
.. i18n: 	For effective security management, you must use the methods for managing access rights to objects
.. i18n: 	presented in the following section.
..

.. tip:: Security

	This method of managing access to menus does not guarantee that users are prevented from reaching
	hidden business objects in the system in other ways.
	For example, hiding the :guilabel:`Invoices` menu will not prevent people reaching invoices through purchase and
	sales orders, or by guessing the URL.

	For effective security management, you must use the methods for managing access rights to objects
	presented in the following section.

.. i18n: .. note:: Initial Access Configuration
.. i18n: 
.. i18n: 	In the initial configuration, OpenERP's \ ``admin`` \ user, a member of the \ ``Administration / Configuration`` \
.. i18n: 	group, is given access to the Configuration menu
.. i18n: 	in each section of the main menu. This is a general convention.
.. i18n: 	For example, :menuselection:`Sales --> Configuration` is visible in the administrator's menu
.. i18n: 	amongst the other Sales menu items.
.. i18n: 	But only the menu items other than :menuselection:`Sales --> Configuration` are visible to other users.
.. i18n: 	Similarly, the main menu item :menuselection:`Administration` is, by convention, visible only to
.. i18n: 	users who are members of the \ ``Administration / Configuration`` \ group.
..

.. note:: Initial Access Configuration

	In the initial configuration, OpenERP's \ ``admin`` \ user, a member of the \ ``Administration / Configuration`` \
	group, is given access to the Configuration menu
	in each section of the main menu. This is a general convention.
	For example, :menuselection:`Sales --> Configuration` is visible in the administrator's menu
	amongst the other Sales menu items.
	But only the menu items other than :menuselection:`Sales --> Configuration` are visible to other users.
	Similarly, the main menu item :menuselection:`Administration` is, by convention, visible only to
	users who are members of the \ ``Administration / Configuration`` \ group.

.. i18n: .. index::
.. i18n:    single: access; objects
..

.. index::
   single: access; objects

.. i18n: Access Rights to Objects
.. i18n: ------------------------
..

Access Rights to Objects
------------------------

.. i18n: The menu access rights determine who can access which menu, but does not define what you can do once
.. i18n: you are in the menu.
..

The menu access rights determine who can access which menu, but does not define what you can do once
you are in the menu.

.. i18n: Access controls on the objects give you the possibility of defining what your users have the right
.. i18n: to do with your data when they get access to it. Access control of objects is structured the same
.. i18n: way as access to menus.
..

Access controls on the objects give you the possibility of defining what your users have the right
to do with your data when they get access to it. Access control of objects is structured the same
way as access to menus.

.. i18n: .. note:: Object
.. i18n: 
.. i18n:    An object represents a document in the system.
.. i18n:    Objects are linked to database tables, and also have additional concepts,
.. i18n:    such as the functions of fields, inheritance from other objects, and class methods that give them
.. i18n:    behavior.
..

.. note:: Object

   An object represents a document in the system.
   Objects are linked to database tables, and also have additional concepts,
   such as the functions of fields, inheritance from other objects, and class methods that give them
   behavior.

.. i18n: If no group is assigned to an object, all users can access it without any restriction of any sort.
.. i18n: Conversely, when an access control is defined for an object, a user must be a member of a group
.. i18n: owning appropriate access rights to have any sort of access to that object.
..

If no group is assigned to an object, all users can access it without any restriction of any sort.
Conversely, when an access control is defined for an object, a user must be a member of a group
owning appropriate access rights to have any sort of access to that object.

.. i18n: You must always ensure that you do not lock the \ ``Administration / Access Rights`` \ group out of any object
.. i18n: that controls administration and configuration options, such as the \ ``ir.model.access`` \ model.
..

You must always ensure that you do not lock the \ ``Administration / Access Rights`` \ group out of any object
that controls administration and configuration options, such as the \ ``ir.model.access`` \ model.

.. i18n: You can manage four access modes on objects independently:
..

You can manage four access modes on objects independently:

.. i18n: *  :guilabel:`Read access` : members of the group can read the data in the object,
.. i18n: 
.. i18n: *  :guilabel:`Create access` : members of the group can create a new record in the object,
.. i18n: 
.. i18n: *  :guilabel:`Write access` : members of the group can modify the contents of records in the object,
.. i18n: 
.. i18n: *  :guilabel:`Delete access` : members of the group can delete records from the object.
..

*  :guilabel:`Read access` : members of the group can read the data in the object,

*  :guilabel:`Create access` : members of the group can create a new record in the object,

*  :guilabel:`Write access` : members of the group can modify the contents of records in the object,

*  :guilabel:`Delete access` : members of the group can delete records from the object.

.. i18n: .. figure::  images/access_control.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Access control to invoices for the Accounting / Invoice group*
..

.. figure::  images/access_control.png
   :scale: 75
   :align: center

   *Access control to invoices for the Accounting / Invoice group*

.. i18n: To configure access rights on an OpenERP object, use the menu :menuselection:`Administration -->
.. i18n: Security --> Access Controls List` and click :guilabel:`New` or choose an existing one
.. i18n: and click :guilabel:`Edit`.
.. i18n: You give a :guilabel:`Name` to the access control, select a :guilabel:`Group`, and
.. i18n: the :guilabel:`Object`, then check the checkbox corresponding to each of the four :guilabel:`Access` modes.
..

To configure access rights on an OpenERP object, use the menu :menuselection:`Administration -->
Security --> Access Controls List` and click :guilabel:`New` or choose an existing one
and click :guilabel:`Edit`.
You give a :guilabel:`Name` to the access control, select a :guilabel:`Group`, and
the :guilabel:`Object`, then check the checkbox corresponding to each of the four :guilabel:`Access` modes.

.. i18n: If you do not specify any group in the access rules, the rule is applied to all groups. So to remove
.. i18n: access to an object for all users you could create a rule:
..

If you do not specify any group in the access rules, the rule is applied to all groups. So to remove
access to an object for all users you could create a rule:

.. i18n: * which is defined for a specific object,
.. i18n: 
.. i18n: * which is linked to no group,
.. i18n: 
.. i18n: * for which none of the four access options is checked.
..

* which is defined for a specific object,

* which is linked to no group,

* for which none of the four access options is checked.

.. i18n: You can then create additional rules on the same object to give specific rights to certain groups.
..

You can then create additional rules on the same object to give specific rights to certain groups.

.. i18n: .. index::
.. i18n:    single: record
..

.. index::
   single: record

.. i18n: Record Rules For Objects
.. i18n: ------------------------
..

Record Rules For Objects
------------------------

.. i18n: Record rules determine who can access the objects, depending on the rules set for the particular object. A record rule has some tests to be performed on objects.
..

Record rules determine who can access the objects, depending on the rules set for the particular object. A record rule has some tests to be performed on objects.

.. i18n: You can manage four access modes on objects independently, depending on the test:
..

You can manage four access modes on objects independently, depending on the test:

.. i18n:     * :guilabel:`Read access` : can read the data in the object,
.. i18n: 
.. i18n:     * :guilabel:`Create access` : can create a new record in the object,
.. i18n: 
.. i18n:     * :guilabel:`Write access` : can modify the contents of records in the object,
.. i18n: 
.. i18n:     * :guilabel:`Delete access` : can delete records from the object.
..

    * :guilabel:`Read access` : can read the data in the object,

    * :guilabel:`Create access` : can create a new record in the object,

    * :guilabel:`Write access` : can modify the contents of records in the object,

    * :guilabel:`Delete access` : can delete records from the object.

.. i18n: To configure a rule on an object, use the menu :menuselection:`Administration -->
.. i18n: Security --> Record Rules`. The fields in the ``ir.rule`` object describe:
..

To configure a rule on an object, use the menu :menuselection:`Administration -->
Security --> Record Rules`. The fields in the ``ir.rule`` object describe:

.. i18n:     * :guilabel:`Object` : Object on which to have the rule
.. i18n: 
.. i18n:     * :guilabel:`Name` : Name of the rule
.. i18n: 
.. i18n:     * :guilabel:`Global` : If global is checked, then that rule would be applied for all the groups; and if it is unchecked, then that rule would be applied only for the groups selected for it
.. i18n: 
.. i18n:     * :guilabel:`Domain` : A list of all the tests for the object. It is specified through a Python expression as a list of tuples.
.. i18n: 
.. i18n:             * If there are multiple tests on same object, then all of them are joined using ``AND`` operator, and depending on the result the rule would be satisfied
.. i18n: 
.. i18n:             * If there are multiple rules on same object, then all of them are joined using ``OR`` operator
.. i18n: 
.. i18n:     * :guilabel:`Access Modes` : Read, Write, Create, Delete as described earlier
.. i18n: 
.. i18n:             * If only one access mode is checked, then only that mode would be applied
.. i18n: 
.. i18n:             * If all of them are checked, then all the access modes would be applied
..

    * :guilabel:`Object` : Object on which to have the rule

    * :guilabel:`Name` : Name of the rule

    * :guilabel:`Global` : If global is checked, then that rule would be applied for all the groups; and if it is unchecked, then that rule would be applied only for the groups selected for it

    * :guilabel:`Domain` : A list of all the tests for the object. It is specified through a Python expression as a list of tuples.

            * If there are multiple tests on same object, then all of them are joined using ``AND`` operator, and depending on the result the rule would be satisfied

            * If there are multiple rules on same object, then all of them are joined using ``OR`` operator

    * :guilabel:`Access Modes` : Read, Write, Create, Delete as described earlier

            * If only one access mode is checked, then only that mode would be applied

            * If all of them are checked, then all the access modes would be applied

.. i18n:         But at least one access mode has to be checked, all of them cannot be unchecked. If all of them are unchecked, it would raise an exception.
..

        But at least one access mode has to be checked, all of them cannot be unchecked. If all of them are unchecked, it would raise an exception.

.. i18n: .. .. figure:: images/security_rule.png
.. i18n: ..    :scale: 75
.. i18n: ..    :align: center
..

.. .. figure:: images/security_rule.png
..    :scale: 75
..    :align: center

.. i18n: *For example :* We can have a rule defined on ``res.partner`` object, which tests if the user is the dedicated salesman of the partner ``[('user_id', '=', user.id)]``. We check only the create and write access modes and keep other access modes unchecked.
..

*For example :* We can have a rule defined on ``res.partner`` object, which tests if the user is the dedicated salesman of the partner ``[('user_id', '=', user.id)]``. We check only the create and write access modes and keep other access modes unchecked.

.. i18n: This would mean that a user in the group for which the rule is applied can only create/write records where he himself serves as the dedicated salesman, and cannot create/write records where he is not the dedicated salesman. As other access modes are unchecked, the user can read/delete the records of partners where he is not the dedicated salesman.
..

This would mean that a user in the group for which the rule is applied can only create/write records where he himself serves as the dedicated salesman, and cannot create/write records where he is not the dedicated salesman. As other access modes are unchecked, the user can read/delete the records of partners where he is not the dedicated salesman.

.. i18n: .. index::
.. i18n:    single: modification history
..

.. index::
   single: modification history

.. i18n: Modification History
.. i18n: --------------------
..

Modification History
--------------------

.. i18n: .. _fig-log:
.. i18n: 
.. i18n: .. figure::  images/view_log.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Partner Record History*
..

.. _fig-log:

.. figure::  images/view_log.png
   :scale: 75
   :align: center

   *Partner Record History*

.. i18n: Each record in an OpenERP database carries a note of its history. You can find out who it was
.. i18n: created by and when that occurred, and who last modified it and when that occurred. Click the
.. i18n: :guilabel:`View Log` link at the right of any form in the web client
.. i18n: to display a dialog box showing this information, as shown in the
.. i18n: figure :ref:`fig-log`. It can help you identify who to contact if there are any problems with the
.. i18n: data in the records.
..

Each record in an OpenERP database carries a note of its history. You can find out who it was
created by and when that occurred, and who last modified it and when that occurred. Click the
:guilabel:`View Log` link at the right of any form in the web client
to display a dialog box showing this information, as shown in the
figure :ref:`fig-log`. It can help you identify who to contact if there are any problems with the
data in the records.

.. i18n: .. index::
.. i18n:    single: module; audittrail
..

.. index::
   single: module; audittrail

.. i18n: .. tip:: Audit Trail
.. i18n: 
.. i18n:    OpenERP has an Audit Trail module :mod:`audittrail`, which can be used to track any or
.. i18n:    all of the changes to one or more objects. It should be used with care, because it
.. i18n:    can generate huge amounts of data in the live database, but can be an invaluable
.. i18n:    tool.
..

.. tip:: Audit Trail

   OpenERP has an Audit Trail module :mod:`audittrail`, which can be used to track any or
   all of the changes to one or more objects. It should be used with care, because it
   can generate huge amounts of data in the live database, but can be an invaluable
   tool.

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
