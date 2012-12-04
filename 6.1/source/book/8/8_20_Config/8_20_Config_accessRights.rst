.. index::
   single: access rights
   single: access; user

User Login
==========

.. tip:: Managing Passwords

   If you let users change their passwords for themselves, you will have no direct control over the
   password they choose.
   You should have a written policy about password strength to try to maintain a level of security in
   your system.

.. index::
   single: module; users_ldap

.. tip:: Managing Users through LDAP

	With the :mod:`users_ldap` module, user accounts can be managed through an LDAP directory that can be
	made common to various different company resources.

	Connection parameters for the LDAP directory are then registered with the company definition.
	You can provide a user profile template there from which new users are automatically created during
	their first connection to OpenERP.

.. index::
   single: LDAP

.. note:: LDAP

	The LDAP protocol (Lightweight Directory Access Protocol) enables you to manage common directories
	for various different resources through your standard TCP/IP network.

	This enables users in the company to have the same username and password to access all
	their applications (such as email and intranet).

Managing Access Rights
======================

One of the most important areas in configuring OpenERP is how to manage access rights to the
information in it.

You are planning to put everything significant to your business into the system, but most of your
staff need see only part of it, and may need to change even less of it. Who should have rights to
what, and how do you manage that?

OpenERP's approach to rights management is highly flexible. Each user can belong to one or more
groups, and the group(s) you belong to determine(s):

* the visibility of each menu item and

* the accessibility of each table in the database.

For example, the group \ ``Warehouse / User`` \ may only be given access to some of the menus in
:menuselection:`Warehouse`, and may have no access to any of the accounting information. Each system user who works in
stores is given membership of the ``Warehouse / User`` group. If some users also work elsewhere, they would also be
given membership of other groups.

.. index::
   pair: user; group

Groups and Users
================

To configure access rights, you would start by defining the groups. It is important for the groups to
be representative of your company's job functions rather than of its individual employees.

So if your finance director is also your sales director, you should create both a Finance Director
group and a Sales Director group, even though they are both the same person, and would both be
assigned to this user in practice. This gives you flexibility for the future.

You should also create groups within departmental areas that have different levels of access
rights. For example, if you create a \ ``Sales Director`` \ group and a \ ``Sales`` \ group avoid
assigning exactly the same rights to each group. The first could see all the of reports, while the
second could be restricted to seeing quotations. You could either make the Sales Director a
member of both groups, and give the \ ``Sales Director`` \ group a limited set of extra rights, or give the
\ ``Sales Director`` \ group all the rights it needs for a Sales Director to belong only to this one
group. You should choose the scheme that gives you most flexibility and then stick with it to
maintain consistency.

.. index::
   pair:  system; administrator

.. tip:: Flexibility in Managing Access

	To give yourself flexibility, you can ensure that a trusted staff member
	(perhaps a director or someone in accounts, or even the system administrator) is given wide rights
	to use the system,
	and is authorized by the management to carry out specific tasks for people.

.. index::
   single: access; menu

Access Rights for Menus
-----------------------

To get a feel for rights management in OpenERP, you will create a new \ ``Stock1`` \  group, with
access to the *Warehouse* menu items. You will then create a stores person user who is a member
of the \ ``Stock1`` \  group.

To create a new group, use the menu :menuselection:`Administration --> Users --> Groups`. Enter the
group name ``Stock1``.

Then to create a new user linked to this, use :menuselection:`Administration --> Users --> Users` to
enter the following:

*  :guilabel:`User Name` : \ ``Stores Person`` \ ,

*  :guilabel:`Login` : \ ``stores`` \ ,

*  :guilabel:`Password` : \ ``stores`` \ ,

*  :guilabel:`Menu Action` : \ ``Menu`` \ .

In the :guilabel:`Groups` section of the user form, add the \ ``Stock1`` \ group that you
just created.

.. figure::  images/menu_access.png
   :scale: 75
   :align: center

   *Groups that have access to the Warehouse menu*

Save the user, then go into the menu :menuselection:`Administration --> Customization --> User
Interface --> Menu Items` to get a list of menus. Filter this list using the search field :guilabel:`Menu` to
get the :menuselection:`Warehouse` menu item. In the form describing the menu, add \ ``Stock1`` \ into the :guilabel:`Groups` field. From now on, only members of
the \ ``Warehouse / Manager`` \, \ ``Warehouse / User`` \ and \ ``Stock1`` \ group will be able to see
this menu item in their main menu list.

.. tip:: Menu Hierarchy

	Since menus are hierarchical, there is no need to hide access to lower menus:
	once you have configured :menuselection:`Warehouse` this way, all lower-level menus become invisible to
	members of other groups.

.. tip:: Security

	This method of managing access to menus does not guarantee that users are prevented from reaching
	hidden business objects in the system in other ways.
	For example, hiding the :guilabel:`Invoices` menu will not prevent people reaching invoices through purchase and
	sales orders, or by guessing the URL.

	For effective security management, you must use the methods for managing access rights to objects
	presented in the following section.

.. note:: Initial Access Configuration

	In the initial configuration, OpenERP's \ ``admin`` \ user, a member of the \ ``Administration / Configuration`` \
	group, is given access to the Configuration menu
	in each section of the main menu. This is a general convention.
	For example, :menuselection:`Sales --> Configuration` is visible in the administrator's menu
	amongst the other Sales menu items.
	But only the menu items other than :menuselection:`Sales --> Configuration` are visible to other users.
	Similarly, the main menu item :menuselection:`Administration` is, by convention, visible only to
	users who are members of the \ ``Administration / Configuration`` \ group.

.. index::
   single: access; objects

Access Rights to Objects
------------------------

The menu access rights determine who can access which menu, but does not define what you can do once
you are in the menu.

Access controls on the objects give you the possibility of defining what your users have the right
to do with your data when they get access to it. Access control of objects is structured the same
way as access to menus.

.. note:: Object

   An object represents a document in the system.
   Objects are linked to database tables, and also have additional concepts,
   such as the functions of fields, inheritance from other objects, and class methods that give them
   behavior.

If no group is assigned to an object, all users can access it without any restriction of any sort.
Conversely, when an access control is defined for an object, a user must be a member of a group
owning appropriate access rights to have any sort of access to that object.

You must always ensure that you do not lock the \ ``Administration / Access Rights`` \ group out of any object
that controls administration and configuration options, such as the \ ``ir.model.access`` \ model.

You can manage four access modes on objects independently:

*  :guilabel:`Read access` : members of the group can read the data in the object,

*  :guilabel:`Create access` : members of the group can create a new record in the object,

*  :guilabel:`Write access` : members of the group can modify the contents of records in the object,

*  :guilabel:`Delete access` : members of the group can delete records from the object.

.. figure::  images/access_control.png
   :scale: 75
   :align: center

   *Access control to invoices for the Accounting / Invoice group*

To configure access rights on an OpenERP object, use the menu :menuselection:`Administration -->
Security --> Access Controls List` and click :guilabel:`New` or choose an existing one
and click :guilabel:`Edit`.
You give a :guilabel:`Name` to the access control, select a :guilabel:`Group`, and
the :guilabel:`Object`, then check the checkbox corresponding to each of the four :guilabel:`Access` modes.

If you do not specify any group in the access rules, the rule is applied to all groups. So to remove
access to an object for all users you could create a rule:

* which is defined for a specific object,

* which is linked to no group,

* for which none of the four access options is checked.

You can then create additional rules on the same object to give specific rights to certain groups.

.. index::
   single: record

Record Rules For Objects
------------------------

Record rules determine who can access the objects, depending on the rules set for the particular object. A record rule has some tests to be performed on objects.

You can manage four access modes on objects independently, depending on the test:

    * :guilabel:`Read access` : can read the data in the object,

    * :guilabel:`Create access` : can create a new record in the object,

    * :guilabel:`Write access` : can modify the contents of records in the object,

    * :guilabel:`Delete access` : can delete records from the object.

To configure a rule on an object, use the menu :menuselection:`Administration -->
Security --> Record Rules`. The fields in the ``ir.rule`` object describe:

    * :guilabel:`Object` : Object on which to have the rule

    * :guilabel:`Name` : Name of the rule

    * :guilabel:`Global` : If global is checked, then that rule would be applied for all the groups; and if it is unchecked, then that rule would be applied only for the groups selected for it

    * :guilabel:`Domain` : A list of all the tests for the object. It is specified through a Python expression as a list of tuples.

            * If there are multiple tests on same object, then all of them are joined using ``AND`` operator, and depending on the result the rule would be satisfied

            * If there are multiple rules on same object, then all of them are joined using ``OR`` operator

    * :guilabel:`Access Modes` : Read, Write, Create, Delete as described earlier

            * If only one access mode is checked, then only that mode would be applied

            * If all of them are checked, then all the access modes would be applied

        But at least one access mode has to be checked, all of them cannot be unchecked. If all of them are unchecked, it would raise an exception.

.. .. figure:: images/security_rule.png
..    :scale: 75
..    :align: center

*For example :* We can have a rule defined on ``res.partner`` object, which tests if the user is the dedicated salesman of the partner ``[('user_id', '=', user.id)]``. We check only the create and write access modes and keep other access modes unchecked.

This would mean that a user in the group for which the rule is applied can only create/write records where he himself serves as the dedicated salesman, and cannot create/write records where he is not the dedicated salesman. As other access modes are unchecked, the user can read/delete the records of partners where he is not the dedicated salesman.

.. index::
   single: modification history

Modification History
--------------------

.. _fig-log:

.. figure::  images/view_log.png
   :scale: 75
   :align: center

   *Partner Record History*

Each record in an OpenERP database carries a note of its history. You can find out who it was
created by and when that occurred, and who last modified it and when that occurred. Click the
:guilabel:`View Log` link at the right of any form in the web client
to display a dialog box showing this information, as shown in the
figure :ref:`fig-log`. It can help you identify who to contact if there are any problems with the
data in the records.

.. index::
   single: module; audittrail

.. tip:: Audit Trail

   OpenERP has an Audit Trail module :mod:`audittrail`, which can be used to track any or
   all of the changes to one or more objects. It should be used with care, because it
   can generate huge amounts of data in the live database, but can be an invaluable
   tool.

.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium

