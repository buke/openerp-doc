****************************
Getting Started with OpenERP
****************************

You will now explore the database \ ``openerp_ch02``\   with these profile modules installed to give
you an insight into the coverage of the core OpenERP software.

.. tip:: Translating New Modules

	When you have installed a new module and are using additional languages to English, you have to reload
	the translation file. New terms introduced in these modules are not translated by default. To do
	this use :menuselection:`Administration --> Translations --> Load an Official Translation`.

Depending on the user you are connected as, the page appears differently.
Using the installation sequence above, certain dashboards may be assigned as various
users' home pages. They show a summary of the information required to start the day effectively. A
project dashboard might contain:

* a list of the tasks to carry out,

* a list of the tasks which is assigned to current user,

* a list of sprints,

* a list of issues assigned to current user,

* a graph of Planned vs Total hours,

* a graph of Remaining hours by Project,

* a graph of Open Issues by Creation Date.

Each of the lists can be reordered simply by clicking the heading of a column – first in ascending, then in descending order as you click repeatedly. To get more information about any particular entry, click on the name in the first column, or if you want to show a particular panel, click :guilabel:`Zoom` above it.

.. figure:: images/admin_project_dashboard.png
   :align: center
   :scale: 65

   *Project Dashboard*

A user's home page is automatically reassigned during the creation or upgrading of a database. It is
customary to assign a dashboard to someone's home page, but any OpenERP screen can be assigned to the
home page of any user.

.. index::
   single: shortcut

.. tip:: Creating Shortcuts

	Each user has access to many menu items from the menu. But in
	general, an employee uses only a small part of the system's functions.

	So you can define shortcuts for the most-used menus. These shortcuts are personal for each user. To
	create a new shortcut, just click the '*' of the header of the view in web client.

	To remove a shortcut just click the link and again click '*' of the header of the view.

The following sections present an overview of the main functions of OpenERP. Some areas are
covered in more detail in the following chapters of this book and you will find many other functions
available in the optional modules. Functions are presented in the order that they appear on the main
menu.

Basic Concepts
==============

.. index::
   single: Partners

Partners & Contacts
^^^^^^^^^^^^^^^^^^^

To get familiar with the OpenERP user interface, you will start working with information about
partners. Clicking :menuselection:`Sales --> Address Book --> Customers` brings up a list of partners that were
automatically loaded when you created the database with :guilabel:`Load Demonstration Data` checked.

.. index::
   single: partner; search

Search for a Partner
^^^^^^^^^^^^^^^^^^^^

Above the partner list you will see a search form that enables you to quickly filter the partners.

The \ ``Customers`` \ filter is enabled by default showing partners who are customers. If you have applied no filter, the list shows every partner in the system. For space reasons, this list shows only the first few partners. If you want to display other records, you can search for them or navigate through the whole list using the :guilabel:`First`, :guilabel:`Previous`, :guilabel:`Next`, :guilabel:`Last` arrows.

.. figure:: images/partner_search_tab.png
   :scale: 75
   :align: center

   *Standard partner search*

.. note:: List Limits

	By default, the list in the GTK client shows only the first 80 records, to avoid overloading the
	network and the server.

	But you can change that limit by clicking the selection widget (showing 80 by default) to the
	right of the search criteria.

	Similarly, the list in the web client shows only the first 20, 50, 100, 500 or unlimited records.

	The actual number can be switched by clicking the link between the PREVIOUS and NEXT buttons
	and selecting one of the other limits.

In the web version, if you click the name of a partner, the form view corresponding to that partner opens in Read-Only
mode. In the list you could alternatively click the pencil icon to open the same form in Edit mode.
Once you have a form, you can toggle between the two modes by clicking :guilabel:`Save` or :guilabel:`Cancel` when in
Edit mode and :guilabel:`Edit` when in Read-Only mode.

.. index::
   single: partner; view form

Partner Form
^^^^^^^^^^^^

The partner form contains several tabs, all referring to the current record:

*  :guilabel:`General`,

*  :guilabel:`Sales & Purchases`,

*  :guilabel:`Accounting`,

*  :guilabel:`History`,

*  :guilabel:`Notes`.

The fields in a tab are not all of the same type – some (such as :guilabel:`Name`) contain free
text, some (such as the :guilabel:`Language`) enable you to select a value from a list of options,
others give you a view of another object (such as :guilabel:`Partner Contacts` – because a partner
can have several contacts) or a list of links to another object (such as :guilabel:`Partner Categories`).
There are checkboxes (such as the :guilabel:`Active` field in the :guilabel:`Sales & Purchases` tab),
numeric fields (such as :guilabel:`Credit Limit` in the :guilabel:`Accounting` tab) and date fields (such as :guilabel:`Date`).

The :guilabel:`History` tab gives a quick overview of partner activities – an overview of useful information such as Leads and Opportunities, Meetings, Phone Calls, Emails and Tasks. Events are generated automatically by OpenERP from changes in other documents that refer to this partner.

It is possible to add events manually which directly relate to the corresponding form, such as a note recording a phone call. To add a new event click :guilabel:`New` in the :guilabel:`Phone Calls` section. That opens a new :guilabel:`Phone Call` pop-up form enabling a phone-call event to be created and added to the current partner.

Possible Partner Actions
^^^^^^^^^^^^^^^^^^^^^^^^

To the right of the partner form is a toolbar containing a list of possible :guilabel:`Reports` ,
:guilabel:`Actions` and quick :guilabel:`Links` about the partner displayed in the form.

You can generate PDF documents for the selected object (or, in list view, about one or more
selected objects) using certain buttons in the :guilabel:`Reports` section of the toolbar:

*  :guilabel:`Labels` : print address labels for the selected partners,

*  :guilabel:`Overdue Payments` : print a letter to notify the selected partners of overdue payments,

Certain actions can be started by the following buttons in the :guilabel:`Actions` section of the
toolbar:

*  :guilabel:`SMS Send`: enables you to send an SMS to selected partners. This system uses the bulk
   SMS facilities of the Clickatell® company http://clickatell.com,

*  :guilabel:`Mass Mailing`: enables you to send an email to a selection of partners,

*  :guilabel:`Create Opportunity`: opens a window to create an opportunity for the partner.

.. index::
   single: buttons; reports, actions, links

.. tip:: Reports, Actions and Links in the GTK Client

	When you are viewing a form in the GTK client, the buttons to the right of the form are shortcuts to
	the same Reports, Actions and Links as described in the text. When you are viewing a list (such as
	the partner list), those buttons are not available to you. Instead, you can reach Reports and Actions
	through two of the buttons in the toolbar at the top of the list – Print and Action.

Partners are used throughout the OpenERP system in other documents. For example, the menu
:menuselection:`Sales --> Sales Orders` brings up all the Sales Orders in list view. Open an order in form view and click the name of a partner, even when the form is read-only. The Partner form will open.

.. tip:: Right-clicks and Shortcuts

	In the GTK client you do not get hyperlinks to other document types. Instead, you can right-click in
	a list view to show the linked fields (that is fields having a link to other forms) on that line.

	In the web client you will see hyperlink shortcuts on several of the fields on a form in Read-
	Only mode, allowing you to be taken directly to the corresponding form. When the web form is in Edit mode,
	you can instead right-click the mouse button
	in the field, to get all of the linked fields in a pop-up menu just as you would with the GTK
	client.

	You can quickly give this a try by going to any one of the sales orders in :menuselection:`Sales
	--> Sales Orders`. See where you can go from the
	:guilabel:`Customer` field using either the web client with the form in
	both read-only and in edit mode, or with the GTK client.

.. figure:: images/familiarization_sale_partner.png
   :scale: 85
   :align: center

   *Links for a partner appear in an order form*

Before moving on to the next topic, take a quick look at the :menuselection:`Sales -->
Configuration --> Address Book`  menu, particularly :menuselection:`Partner Categories`  and  :menuselection:`Localisation` menus.
They contain some of the demonstration data that you installed when you created the database.

Products
--------

In OpenERP, `product` is used to define a raw material, a stockable product, a consumable or a service. You can
work with whole products or with templates that separate the definition of products and variants (*extra module*).

For example, if you sell t-shirts in different sizes and colors:

* the product template is the “T-shirt” which contains information common to all sizes and all
  colors,

* the variants are “Size:S” and “Color:Red”, which define the parameters for that size and
  color,

* the final product is thus the combination of the two – T-shirt in size S and color Red.

The value of this approach, for some sectors, is that you can just define a template in detail and all
of its available variants briefly, rather than every item as an entire product.

	.. note::  *Example Product Templates and Variants*

			A product can be defined as a whole or as a product template and several variants. The variants
			can be in one or several dimensions, depending on the installed modules.

			For example, if you work in textiles, the variants on the product template for “T-shirt” are:

			* Size (S, M, L, XL, XXL),

			* Colour (white, grey, black, red),

			* Quality of Cloth (125g/m2, 150g/m2, 160g/m2, 180g/m2),

			* Collar (V, Round).

			.. index::
			   single: module; product_variant_multi

			This separation of variant types requires the optional module :mod:`product_variant_multi`.
			Using it
			means that you can avoid an explosion in the number of products to manage in the database. If you
			take the example above, it is easier to manage a template with 15 variants in four different types
			than 160 completely different products. This module is available in ``extra-addons``.

The :menuselection:`Sales --> Products` menu gives you access to the definition of products and their templates and variants.

.. index::
   single: Product; Consumable

.. tip::  Consumables

	In OpenERP, a consumable is a physical product which is treated like a stockable product, with the exception
	that stock management is not taken into account by the system. You could buy it, deliver it or
	produce it but OpenERP will always assume that there is enough of it in stock. It never triggers a
	procurement exception.

Open a product form to see the information that describes it. The demonstration data show several types of products, which gives quite a good overview of the options.

Price lists (:menuselection:`Sales --> Configuration --> Pricelists`) determine the purchase and selling prices and
adjustments derived from the use of different currencies. The :menuselection:`Default Purchase
Pricelist` uses the product's :guilabel:`Cost Price` field for the Purchase price to be calculated. The
:menuselection:`Public Pricelist` uses the product's :guilabel:`Sale Price` field to calculate the Sales price in quotations.

Price lists are extremely flexible and enable you to put a complete price management policy in place.
They are composed of simple rules that enable you to build up a rule set for most complex situations:
multiple discounts, selling prices based on purchase prices, price reductions, promotions on product ranges and so on.

You can find many optional modules to extend product functionality, such as:

.. index::
   single: module; membership

* :mod:`membership` : for managing the subscriptions of members of a company,

  .. index::
     single: module; product_electronic

* :mod:`product_electronic` : for managing electronic products,

  .. index::
     single: module; product_extended

* :mod:`product_extended` : for managing production costs,

  .. index::
     single: module; product_expiry

* :mod:`product_expiry` : for agro-food products where items must be retired after a certain
  period,

  .. index::
     single: module; product_lot_foundry

* :mod:`product_lot_foundry` : for managing forged metal products.

All of the above modules are found in ``extra-addons``, except for the :mod:`membership` and the :mod:`product_expiry` module.

.. index::
   single: CRM
   single: Customer Relationship Management
   single: SRM
   single: Supplier Relationship Management
..

Boost your Sales
================

OpenERP provides many tools for managing relationships with partners. These are available through
the :menuselection:`Sales` menu.

.. tip::  :guilabel:`CRM & SRM`

	``CRM`` stands for Customer Relationship Management, a standard term for systems that manage client and
	customer relations. ``SRM`` stands for Supplier Relationship Management, and is commonly used for
	functions that manage your communications with your suppliers.

Through Customer Relationship Management, OpenERP allows you to keep track of:

* Leads
* Opportunities
* Meetings
* Phone Calls
* Claims
* Helpdesk and Support
* Fund Raising

OpenERP ensures that each case is handled effectively by the system's users, customers and
suppliers. It can automatically reassign a case, track it for the new owner, send reminders by email
and raise other OpenERP documentation and processes.

All operations are archived, and an email gateway lets you update a case automatically from emails
sent and received. A system of rules enables you to set up actions that can automatically improve
your process quality by ensuring that open cases never escape attention.

As well as those functions, you have got tools to improve the productivity of all staff in their daily
work:

* an email client plugin for Outlook and Thunderbird enabling you to automatically store your emails and their attachments in the
  Knowledge Management (previously Document Management System) integrated with OpenERP,

* interfaces to synchronize your Contacts and Calendars with OpenERP,

* sync your meetings on your mobile phone,

* build a 360° view on your Customer,

* integration with Google applications.

You can implement a continuous improvement policy for all of your services, by using some of the
statistical tools in OpenERP to analyze the different communications with your partners. With
these, you can execute a real improvement policy to manage your service quality.

The management of customer relationships is detailed in the second section of this book (see
:ref:`part2-crm`).

.. index::
   single: Sales Management


.. index::
   single: Accounting and Finance
   single: Financial Management

Manage your Books
=================

The chapters in :ref:`part-genacct` in this book are dedicated to general and analytic accounting.
Following is a  brief overview of the functions to introduce you to this Business Application.

Accounting is totally integrated into all of the company's functions, whether it is general,
analytic, budgetary or auxiliary accounting. OpenERP's accounting function is double-entry and
supports multiple company divisions and multiple companies, as well as multiple currencies and
languages.

Accounting that is integrated throughout all of the company's processes greatly simplifies the work
of entering accounting data, because most of the entries are generated automatically while other
documents are being processed. You can avoid entering data twice in OpenERP, which is commonly a
source of errors and delays.

So OpenERP's accounting is not just for financial reporting – it is also the anchor-point for many
of the company's management processes. For example, if one of your accountants puts a customer on
credit hold, then that will immediately block any other action related to that company's credit (such
as sales or delivery).

OpenERP also provides integrated analytical accounting, which enables management by business
activity or project and provides very detailed levels of analysis. You can control your operations
based on business management needs, rather than on the charts of accounts that generally meet only
statutory requirements.

OpenERP has added a flexible, easy **Invoicing** module allowing you to keep track of your documents and payments, even when you are not an accountant. This will allow smaller businesses to keep track of their payments without having to implement a complete accounting system.

Keep track of your Cash Moves by using the new OpenERP Cash Box.

.. index::
     single: Human Resources
     single: HR

Lead & Inspire your People
==========================

OpenERP's Human Resources Management Business Application provides functionality such as:

* Manage your Employees, Contracts & Staff Performance,

* Talent Acquisition,

* Keep track of Holidays and Sickness Leaves,

* Manage the Evaluation Process,

* Keep track of Attendances & Timesheets,

* Track Expenses.

.. index::
   single: modules; hr_
   single: module; hr

Most of these functions are provided from optional modules whose name starts with \ ``hr_`` \
rather than the core :mod:`hr` module, but they are all loaded into the main :menuselection:`Human
Resources` menu.

The different issues are handled in detail in the fourth part of this book :ref:`part-ops`, dedicated to internal
organization and to the management of a services business.

.. index::
   single: project management
   single: project

Drive your Projects
===================

OpenERP's project management tools enable you to define tasks and specify requirements for those tasks, efficient allocation of resources to the requirements, project planning, scheduling and automatic communication with partners.

All projects are hierarchically structured. You can review all of the projects from the menu :menuselection:`Project --> Projects`. Then select :guilabel:`Gantt view` to obtain a graphical representation of the project.

.. figure:: images/project_gantt.png
   :scale: 65
   :align: center

   *Project Planning*

You can run projects related to Services or Support, Production or Development – it is a universal
module for all enterprise needs.

Project management is described in :ref:`ch-projects`.

.. index::
   single: sales

Driving your Sales
==================

The :menuselection:`Sales` menu gives you roughly the same functionality as the
:menuselection:`Purchases` menu – the ability to create new orders and to review the
existing orders in their various states – but there are important differences in the workflows.

Confirmation of an order triggers the delivery of goods, and invoicing timing is defined by a
setting in each individual order.

Delivery charges can be managed using a grid of tariffs for different carriers.

.. index::
   single: purchase
   single: purchase management

Driving your Purchases
======================

:menuselection:`Purchases` enables you to track your suppliers' price quotations and convert them into
Purchase Orders as you require. OpenERP has several methods of monitoring invoices and tracking
the receipt of ordered goods.

You can handle partial deliveries in OpenERP, so you can keep track of items that are still to be
delivered on your orders, and you can issue reminders automatically.

OpenERP's replenishment management rules enable the system to generate draft purchase orders
automatically, or you can configure it to run a lean process, driven entirely by current production
needs.

You can also manage purchase requisitions to keep track of quotations sent to a multitude of suppliers.

.. index::
   single: stock
   single: warehouse management

Organise your Warehouse
=======================

The various sub-menus under :menuselection:`Warehouse` together provide operations you need to manage stock.
You can:

* define your warehouses and structure them around locations you choose,

* manage inventory rotation and stock levels,

* execute packing orders generated by the system,

* execute deliveries with delivery notes and calculate delivery charges,

* manage lots and serial numbers for traceability,

* calculate theoretical stock levels and automate stock valuation,

* create rules for automatic stock replenishment.

Packing orders and deliveries are usually defined automatically by calculating requirements based on
sales. Stores staff use picking lists generated by OpenERP, produced automatically in order of
priority.

Stock management is, like accounting, double-entry. So stocks do not appear and vanish magically
within a warehouse, they just get moved from place to place. And, just like accounting, such a
double-entry system gives you big advantages when you come to audit stock because each missing item
has a counterpart somewhere.

Most stock management software is limited to generating lists of products in warehouses. Because of
its double-entry system, OpenERP automatically manages customer and suppliers stocks as well, which
has many advantages: complete traceability from supplier to customer, management of consigned stock,
and analysis of counterpart stock moves.

Furthermore, just like accounts, stock locations are hierarchical, so you can carry out analyses at
various levels of detail.


.. index::
   single: Production Management
   single: Manufacturing

Get Manufacturing Done
======================

OpenERP's production management capabilities enable companies to plan, automate and track manufacturing and product assembly. OpenERP supports multi-level bills of materials and lets you substitute sub-assemblies dynamically, at the time of sales ordering. You can create virtual sub-assemblies for re-use on several products with phantom bills of materials.

.. index::
   single: bill of materials
   single: BOM

.. note:: BOMs, Routing, Workcenters

	These documents describe the materials that make up a larger assembly. They are commonly called
	Bills of Materials or BOMs.

	They are linked to routings which list the operations needed to carry out the manufacturing or
	assembly of the product.

	Each operation is carried out at a workcenter, which can be a machine or a person.

Production orders based on your company's requirements are scheduled automatically by the system,
but you can also run the schedulers manually whenever you want. Orders are worked out by calculating
the requirements from sales, through bills of materials, taking current inventory into account. The
production schedule is also generated from the various lead times defined throughout the system, using the same
route.

The demonstration data contain a list of products and raw materials with various classifications
and ranges. You can test the system using this data.

.. index::
   single: knowledge
   single: document
   single: FTP
   single: Document Management
   single: calendar
   single: CalDAV

Share your Knowledge through Efficient Document Management and Being Mobile
===========================================================================

OpenERP integrates a complete document management system that not only
carries out the functions of a standard DMS, but also integrates with all
of its system-generated documents such as Invoices and Quotations. Moreover, it
it keeps all of this synchronized. You can define your own directory structure and tell OpenERP to automatically store documents such as Invoices in the DMS.

OpenERP provides an FTP Interface for the Document Management System. You will not only be able to access documents from OpenERP, but you can also use a regular file system with the FTP client.
FTP is just a way of getting access to files without needing to use an OpenERP client, to allow you to access files from anywhere.
You can also add documents to be stored in OpenERP directly through the FTP system in the corresponding OpenERP directory. These documents will automatically be accessible from the form concerned in OpenERP.

The Knowledge system is also well-integrated with e-mail clients such as Thunderbird and Outlook. It also allows you to sync your calendars (CalDAV).

.. index::
   single: Dashboards

Measure your Business Performance
=================================

To measure your business performance OpenERP, provides two interesting features:

* Dashboards
* Statistical Reports

On a single page, Dashboards give you an overview of all the information that is important to you.
In OpenERP, each application has its own dashboard which opens by default when you select the specific application.
For example, `Administration Dashboard` will open when you click the :menuselection:`Administration` menu.

.. note:: Dashboards

	Unlike most other ERP systems and classic statistic-based systems,
	OpenERP can provide dashboards for all system users, and not just managers and accountants.

	Each user can have his own dashboard, adapted to his needs,
	enabling him to manage his own work effectively.
	For example, a developer using the :guilabel:`Project Dashboard` can see information such
	as a list of open tasks, tasks delegated to him and an analysis of the progress of
	the relevant projects.

Dashboards are dynamic, letting you navigate easily around the entire information base.
Using the icons above a graph, for example, you can filter the data or zoom into the graph. You can
click any element of the list to get detailed statistics on the selected element.

Dashboards can be customized to fit the needs of each user and each company.

.. note:: Creating or Customizing Dashboards

	OpenERP contains a Dashboard Editor. Create your own dashboard to fit your
	specific needs in only a few clicks. Go to the :menuselection:`Administration --> Customization --> Reporting --> Dashboard Definition` menu to define your own dashboard.

The `Statistical Analysis` is one of the crucial thing for decision making process in any business. OpenERP provides
Statistical Reports for each application. For example, you can access the statistical analysis of Sales-related information
from the menu :menuselection:`Sales --> Reporting --> Sales Analysis`. You can search and group the data using this
`Statistical Report`.

Track your Process Flows
========================

Many documents have a workflow of their own, and also take part in cross-functional processes.
Take a document that could be expected to have a workflow, such as a Sales Order, and
then click the :guilabel:`?` button above its form to see the full process.

.. figure:: images/guided_tour_process.png
   :scale: 55
   :align: center

   *Process for a Sales Order*

You can see where a particular document is in its process, if you have selected
a single document, by the solid bar on one of the process nodes. You also link
to documents and menus for each of the stages.

There is a clear distinction between a cross-functional process (that is currently only
shown in the web client) and the detailed document workflow (that is shown in both the
web client from a process node, and the GTK client from the
:menuselection:`Plugins > Execute a Plugin...` menu and clicking either
the :guilabel:`Print Workflow` or the :guilabel:`Print Workflow (Complex)` option.

.. figure:: images/purchase_workflow.png
   :scale: 65
   :align: center

   *Workflow for a Purchase Order*

Alongside the document management system, the process visualization features make OpenERP
far better for documentation than similar systems.

Need More?
==========

You have been guided through a brisk, brief overview of many of the main functional areas of OpenERP.
Some of these – a large proportion of the core modules – are treated in more detail
in the following chapters.

You can use the menu :menuselection:`Administration --> Modules --> Modules`
to find the remaining modules that have been loaded into your installation but
not yet installed in your database. Some modules have only minor side-effects to OpenERP (such as
:mod:`google_maps`), some have quite extensive effects (such as the various charts of accounts), and
some make fundamental additions.

But there are now more than hundred modules available. You can install them according to your needs.

A brief description is available for each module, but the most thorough way of understanding their
functionality is to install one and try it. So, pausing only to prepare another test database to try
it out on, just download and install the modules that appear interesting.

Tips & Tricks
=============

Overview of Shortcut Keys
^^^^^^^^^^^^^^^^^^^^^^^^^

* Shortcuts for OpenERP

.. table::

   ============  ===============================
   Shortcut Key  What does it do?
   ============  ===============================
   Ctrl+H        Contextual Help
   Ctrl+O        Connect
   Ctrl+Q        Quit
   ============  ===============================

* Shortcuts for OpenERP Form

.. table::

   ==============  ===============================
   Shortcut Key    What does it do?
   ==============  ===============================
   Ctrl+D          Delete
   Ctrl+F          Find
   Ctrl+G          Go To Resource ID
   Ctrl+L          Switch to List/Form
   Ctrl+N          New
   Ctrl+P          Preview in PDF
   Ctrl+Page Down  Next Tab
   Ctrl+Page Up    Previous Tab
   Ctrl+R          Reload/Undo
   Ctrl+S          Save
   Ctrl+T          Menu
   Ctrl+W          Close Tab
   Page Down       Next
   Page Up         Previous
   Shift+Ctrl+D    Duplicate
   Shift+Ctrl+H    New Home Tab
   Shift+Ctrl+Y    Repeat latest action
   ==============  ===============================

* Shortcuts for OpenERP when editing a resource in a popup window

.. table::

   ============  ===============================
   Shortcut Key  What does it do?
   ============  ===============================
   Ctrl+Enter    Save and Close window
   Ctrl+Esc      Close window without Saving
   ============  ===============================

* Shortcuts in a relation field

.. table::

   ============  ===============================
   Shortcut Key  What does it do?
   ============  ===============================
   F1            Add new Field/Line on the fly
   F2            Look up information
   F3            Zoom on current field
   ============  ===============================

* Shortcuts in text entries

.. table::

   ============  ===============================
   Shortcut Key  What does it do?
   ============  ===============================
   Ctrl+C        Copy selected text
   Ctrl+V        Paste selected text
   Ctrl+X        Cut selected text
   Enter         Auto-complete text field
   Shift+Tab     Previous editable widget
   Tab           Next editable widget
   ============  ===============================

Filters
^^^^^^^

The `Advanced Search View` is a new feature of OpenERP v6 which provides a very user-friendly filtering mechanism
for the end user to easily look up desired records from the list.

The perfect example of an advanced search view is the `Statistical Report` of OpenERP.
Such a report shows the statistical summary with filtered results to the end user.

Usually an Advanced Search is composed of three elements, the Filter buttons at the top, the Extended Filters, and the Group by option.
These filters are dynamic, so according to filters you apply, extra columns may be added to the view.

You can also easily combine filters; an arrow will be displayed and you will get a structure according to the order in which you clicked the Filter buttons.

Let's show an example.
The statistical report for project tasks is `Task Analysis` which can be displayed using the
menu :menuselection:`Project --> Reporting --> Tasks Analysis` when you have installed the `Project Management` module.

.. figure:: images/filter_task_analysis.png
   :scale: 75
   :align: center

   *Task Analysis*

You can see the `Advanced Search View` in the light green shaded area.

You can filter the information of a task according to the Group by features.

Click, for instance, the `Stage` button in Group by, and then click `Task` to analyse your tasks by stage and then by task.

This `Advanced Search View` can also be attached to any `List View` of an object and hence increase the
search facility when a user looks up the record in list view.

.. figure:: images/filter_task_list_view.png
   :scale: 75
   :align: center

   *Search the Tasks which are `In Progress` with Group by Project and State*



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

