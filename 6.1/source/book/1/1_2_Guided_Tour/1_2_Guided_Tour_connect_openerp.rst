To Connect to OpenERP
=====================

Since this is the first time you have connected to OpenERP, you will be given the opportunity
to configure the system. You may choose to either :guilabel:`Skip Configuration Wizards`
or :guilabel:`Start Configuration`. We shall proceed with system configuration by clicking
:guilabel:`Start Configuration`.

Configuration consists of a set of wizards that help you through options for the installed modules.
Hardly anything is installed, so this is a very simple process at the moment.
   
    #.  :guilabel:`Configure Your Interface` : select ``Simplified`` and click :guilabel:`Next`.

    #.  At the :guilabel:`Company Configuration` step, you should select your own :guilabel:`Company Name` and 
	:guilabel:`Currency`. You may add your company address, contact and other details and a logo,
	if you have one, that appears on reports. Then, click :guilabel:`Next`.

    #.  The :guilabel:`Install Applications` section would enable you to add applications to
	your system. For now, click :guilabel:`Skip` to proceed without installing any applications.
	You are now connected to OpenERP and can start using the system as an Administrator.


.. index::
   single:  administrator

Once you are displaying the main menu, you are able to see the following screen items, 
as shown in screenshot :ref:`fig-oech2-main`:

* the name of the database you are logged into and, just below it, the current user name,

* the :guilabel:`ONLINE SUPPORT` button, which gives you an overview of the support services provided by OpenERP
  which is available for subscription,

* the :guilabel:`Preferences` toolbar to the top right, showing the links to the :guilabel:`HOME` page,
  :guilabel:`EDIT PREFERENCES` page, :guilabel:`ABOUT`, :guilabel:`HELP`
  and :guilabel:`LOGOUT` button,

* just below, you will find shortcuts (which the user can customize) and links to the menu items of installed applications,

* a collection of interesting and useful widgets are available on the right of the home page beside the main menu.

.. _fig-oech2-main:

.. figure:: images/main_window_openerp_ch02.png
   :scale: 65
   :align: center

   *The Main Menu of the openerp_ch02 database*

Two menus are available at the moment:

* :menuselection:`Sales`

* :menuselection:`Administration`

.. index::
   single: Preferences

Preferences Toolbar
-------------------

When you are connected to OpenERP, the topmost toolbar indicates which user you are connected as.
So it should currently be showing :guilabel:`Administrator` (unless you logged in as another
user and it is reflecting the name of that user instead).

You will find the Preferences toolbar to its right containing a set of useful links.
First, you will find a link to the :guilabel:`HOME` page. This takes you to either the
Home page containing links to the available menus or to another window or dashboard, depending on the
user configuration. In the case of the \ ``openerp_ch02`` \ database, so far the Home page
is the Main Menu. But in general each user of the
system is presented with a dashboard that is designed to show performance indicators and urgent
documents that are most useful to someone of the user's position in the company. You will see how to
assign dashboards to different users in a later chapter, :ref:`ch-config`.

.. index::
   single: timezone

.. tip::  Multi-nationals and Time Zones

	If you have users in different countries, they can configure their own timezone. Timestamp displays
	are then adjusted by reference to the user's own localization setting.

	So if you have a team in India and a team in England, the times will automatically be converted. If
	an Indian employee sets her working hours from 9 to 6, that will be converted and saved in the
	server's timezone. When the English users want to set up a meeting with an Indian user, the Indian
	user's available time will be converted to English time.

The next element in the toolbar is a link to :guilabel:`EDIT PREFERENCES`. By clicking that link, you
get a dialog box where the current user can set his interface in the :guilabel:`Current Activity` tab;
and in the :guilabel:`Preferences` tab, set his password, a timezone, a working language,
e-mail and a signature:

* The :guilabel:`Interface` field in the :guilabel:`Current Activity` tab allows the user to switch
  between the \ ``Simplified`` \ and \ ``Extended`` \ interfaces.

* The :guilabel:`Language` field enables the user's working language to be changed. But first, the
  system must be loaded with other languages for the user to be able to choose an alternative, which
  is described in the next subsection of this chapter. This is a mandatory field.

* The :guilabel:`Timezone` setting indicates the user's location to OpenERP. This can be different
  from that of the server. All of the dates in the system are converted to the user's timezone
  automatically.

* The :guilabel:`Menu Tips` checkbox gives the user the choice to have tips displayed on each menu action.

* The :guilabel:`Change Password` button gives users the opportunity to change their own password.
  It opens a new dialog box where users may change the password and must logout and login again after the change.
  You should take steps (perhaps written policies) to prevent users making these too trivial.

* The :guilabel:`Email` field is for storing the current user's default e-mail address.

* The :guilabel:`Signature` field gives the user a place for the signature attached to messages sent
  from within OpenERP. 

The :guilabel:`ABOUT` link gives information about the development of the OpenERP software and 
various links to other information.

The :guilabel:`HELP` link directs the user to the online documentation of OpenERP, where extensive help is available on a host of topics.

The :guilabel:`LOGOUT` link enables you to logout and return to the original login page. You can
then login to another database, or to the same database as another user. This page also gives you
access to the super-administrator functions for managing databases on this server.

.. index::
   single: installation; language

Installing a New Language
^^^^^^^^^^^^^^^^^^^^^^^^^

Each user of the system can work in his or her own language. More than twenty languages are
currently available besides English. Users select their working language using the Preferences link.
You can also assign a language to a partner (customer or supplier), in which case all the documents
sent to that partner will be automatically translated into that language.

.. attention:: More about Languages

	The base version of OpenERP is translated into the following languages: English, German, Chinese,
	Spanish, Italian, Hungarian, Dutch, Portuguese, Romanian, Swedish and Czech.

	But other languages are also available: Arabic, Afghan,
	Austrian, Bulgarian, Indonesian, Finnish, Thai, Turkish and Vietnamese..

As administrator, you can install a new main working language into the system.

	#. Select :menuselection:`Administration` in the Menu Toolbar and click
	   :menuselection:`Translations --> Load an Official Translation` in the main menu window,

	#. Select the language to install, \ ``French``\  for example, and click :guilabel:`Load`,

	#. The system will intimate you when the selected language has been successfully installed.
	   Click :guilabel:`Close` to return to the menu.

To see the effects of this installation, change the preferences of your user to change the working
language (you may first need to ensure that you have explicitly selected English as your language,
rather than keep the default, before you are given the French option). 
You may have to reload the page to see the effects. The main menu is immediately translated in
the selected language. If you are using the GTK
client, you will first have to close the menu then open a new main menu to start seeing things in the
new language.

.. note:: Navigating the Menu

   From this point in the book navigation from the main menu is written as a series of menu entries
   connected by the :menuselection:`-->` character. Instead of seeing “Select Administration in
   the Menu toolbar then click Translations > Load an Official Translation” you will just get “use menu
   :menuselection:`Administration --> Translations --> Load an Official Translation`”.

.. index:: requests

Requests
^^^^^^^^

Requests have been removed in OpenERP 6.1 - a new internal communication system will be added in 7.0.

.. index::
   single: user; configuration

Configuring Users
-----------------

The database you created contains minimal functionality but can be extended to include all of the
potential functionality available to OpenERP. About the only functions actually available in this
minimal database are Customers and Currencies – and these only because the definition of your main
company required this. And because you chose to include demonstration data, both Customers and
Currencies were installed with some samples.

.. index::
   single: administrator

Because you logged in as Administrator, you have all the access you need to configure users. Click
:menuselection:`Administration --> Users --> Users` to display the list of users defined in the
system. A second user, \ ``Demo User`` \, is also present in the system as part of the
demonstration data. Click the \ ``Demo User`` \ name to open a non-editable form on that user.

Click the :guilabel:`Groups`  tab to see that the demo user is a member of only the ``Employee`` group,
and is subject to no specialized rules.
The user \ ``Administrator`` \ is different, as you can see if you
follow the same sequence to review its definition. It is a member of the \ ``Administration / Configuration`` \
and the \ ``Administration / Access Rights`` \ groups,
which gives it more advanced rights to configure new users.

.. index:: 
   single: user; access
   single: user; role
   single: user; group

.. tip::  Groups and Users

	Users and groups provide the structure for specifying access rights to different documents. Their
	setup answers the question “Who has access to what?”

Click :menuselection:`Administration --> Users --> Groups` to open the list of
groups defined in the system. If you open the form view of the \ ``Administration / Configuration`` \
group by clicking its name in the list, the first tab :guilabel:`Users` gives you the list of
all the users who belong to this group.

You can also see in the :guilabel:`Menus` tab, the list of menus reserved for this group. By convention,
the \ ``Administration / Configuration`` \ in OpenERP has rights of access to
the :menuselection:`Configuration` menu in each section. So \ ``Sales / Configuration`` \ is
found in the list of access rights but \ ``Sales`` \ is not found there because it is accessible
to all users. Click the :guilabel:`Access Rights` tab and it gives you details of the access rights
for that group. These are detailed later in :ref:`ch-config`. 

You can create some new users to integrate them into the system. Assign them to predefined groups to
grant them certain access rights. Then try their access rights when you login as these users.
Management defines these access rights as described in :ref:`ch-config`.

.. note::  Changes to Default Access Rights

	New versions of OpenERP differ from earlier versions of OpenERP and Tiny ERP in this area:
	many groups have been predefined and access to many of the menus and objects are keyed to these
	groups by default.
	This is quite a contrast to the rather liberal approach in 4.2.2 and before, where access rights
	could be defined but were not activated by default.

.. index::
   single: partner; managing

Managing Partners
-----------------

In OpenERP, a partner represents an entity that you do business with. That can be a prospect, a
customer, a supplier, or even an employee of your company.

List of Partners
^^^^^^^^^^^^^^^^

Click :menuselection:`Sales --> Address Book --> Customers` in the main menu to open the list of partners who are customers. Then click the name of the first partner to get hold of the details – a form appears with 
information about the company, such as its corporate name, its primary language, its reference and whether it is a
\ ``Customer`` \ and/or a \ ``Supplier`` \. You will also find several other tabs on it:

* the :guilabel:`General` tab contains information about different contacts at that partner, postal information,
  communication information and the categories it belongs to.

* the :guilabel:`Sales & Purchases` tab contains information that is slightly less immediate.

* the :menuselection:`History` tab (visible if you install other modules like :mod:`crm`)
  contains the history of all the events that the partner has
  been involved in. These events are created automatically by different system documents: invoices,
  orders, support requests and so on, from a list that can be configured in the system. 
  These give you a rapid view of the partner's history on a single
  screen.

* the :menuselection:`Notes` tab is an area for free text notes.

To the right of the form is a list of Reports, Actions, Links and Attachments related to a partner. Click some of 
them to get a feel for their use.

.. figure:: images/partner.png
   :align: center
   :scale: 80

   *Partner form*

.. index::
   single: partner; category

.. tip::  Partner Categories

	Partner Categories enable you to segment different partners according to their relation with you
	(client, prospect, supplier, and so on). A partner can belong to several categories – for example
	it may be both a customer and supplier at the same time.
	
	But there are also Customer and Supplier checkboxes on the partner form, which are different.
	These checkboxes are designed to enable OpenERP to quickly select what should appear on some of the
	system drop-down selection boxes. They, too, need to be set correctly.

Partner Categories
^^^^^^^^^^^^^^^^^^

You can list your partners by category using the menu :menuselection:`Sales --> Configuration -->
Address Book --> Partners Categories`. Click a category to obtain a list of partners in that category.

.. figure:: images/main_window_partner_menu_config.png
   :scale: 75
   :align: center

   *Categories of partner*

The administrator can define new categories. So you will create a new category and link it to a
partner:

	#. Use :menuselection:`Sales --> Configuration --> Address Book --> Partners Categories`
	   to reach the list of categories in a list view.

	#. Click :guilabel:`New` to open an empty form for creating a new category

	#. Enter \ ``My Prospects``\  in the field :guilabel:`Category Name`. Then click on the
	   :guilabel:`Search` icon to the right of the :guilabel:`Parent Category` field and select 
	   \ ``Prospect``\  in the list that appears.

	#. Then save your new category using the :guilabel:`Save` button.

You may add exiting partners to this new category using the :guilabel:`Add` button in the
:guilabel:`Partners` section.

.. tip:: Required Fields

	Fields colored blue are required. If you try to save the form while any of these fields are empty,
	the field turns red to indicate that there is a problem. It is impossible to save the form until
	you have completed every required field.

You can review your new category structure using the list view. 
You should see the new structure of \ ``Prospects / My Prospects``\   there.

.. figure:: images/main_window_partner_tab.png
   :scale: 75
   :align: center

   *Creating a new partner category*

To create a new partner and link it to this new category, open a new partner form to modify it.

	#. Type \ ``New Partner``\  into the :guilabel:`Name` field.

	#. In the :guilabel:`General` tab, click the :guilabel:`Add` button under the
	   :guilabel:`Categories` section and select your
	   new category from the list that appears: \ ``Prospect / My Prospects`` \.

	#. Then save your partner by clicking :guilabel:`Save`. The partner now belongs in the category 
	   \ ``Prospect / My Prospects`` \.

	#. Monitor your modification in the menu :menuselection:`Sales --> Configuration --> Address Book -->
	   Partners Categories`. Select the category :guilabel:`Prospect / My Prospects`. The list of partners opens
	   and you will find your new partner there in that list.

.. tip:: Searching for Documents

	If you need to search through a long list of partners, it is best to use the available search
	criteria rather than scroll through the whole partner list. It is a habit that will save you a lot of
	time in the long run as you search for all kinds of documents.

.. note::  Example Categories of Partners

	A partner can be assigned to several categories. These enable you to create alternative
	classifications as necessary, usually in a hierarchical form.

	Here are some structures that are often used:

	* geographical locations,

	* interest in certain product lines,

	* subscriptions to newsletters,

	* type of industry.


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

