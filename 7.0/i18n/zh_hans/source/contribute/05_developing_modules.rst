
.. i18n: Developing modules
.. i18n: -------------------
..

Developing modules
-------------------

.. i18n: .. index::
.. i18n:    single: modules development
.. i18n: ..
..

.. index::
   single: modules development
..

.. i18n: Introduction
.. i18n: ++++++++++++
..

Introduction
++++++++++++

.. i18n: Here you will find information about the organisation of the community in
.. i18n: OpenERP project. It includes a description of the different tools used, the role
.. i18n: of the different actors, and the different process for improvement management.
..

Here you will find information about the organisation of the community in
OpenERP project. It includes a description of the different tools used, the role
of the different actors, and the different process for improvement management.

.. i18n: The whole organisation is managed through our launchpad projects: http://launchpad.net
.. i18n: Our projects on launchpad are currently organised like this:
..

The whole organisation is managed through our launchpad projects: http://launchpad.net
Our projects on launchpad are currently organised like this:

.. i18n: +----------------------------+----------------------------------------------+--------------------------------------------+
.. i18n: | **Project name**           | **URL**                                      | **Description**                            |
.. i18n: +============================+==============================================+============================================+
.. i18n: |                            |                                              |                                            |
.. i18n: | **openobject**             | https://launchpad.net/openobject             | the main super-project (group) where all   |
.. i18n: |                            |                                              | bugs, features and faq are managed         |
.. i18n: |                            |                                              |                                            |
.. i18n: +----------------------------+----------------------------------------------+--------------------------------------------+
.. i18n: |                            |                                              |                                            |
.. i18n: | **openobject-bi**          | https://launchpad.net/openobject-bin         | business intelligence project              |
.. i18n: |                            |                                              |                                            |
.. i18n: +----------------------------+----------------------------------------------+--------------------------------------------+
.. i18n: |                            |                                              |                                            |
.. i18n: | **openobject-server**      | https://launchpad.net/openobject-server      |  the openobject server                     |
.. i18n: |                            |                                              |                                            |
.. i18n: +----------------------------+----------------------------------------------+--------------------------------------------+
.. i18n: |                            |                                              |                                            |
.. i18n: | **openobject-client**      | https://launchpad.net/openobject-client      | the openobject application client (gtk)    |
.. i18n: |                            |                                              |                                            |
.. i18n: +----------------------------+----------------------------------------------+--------------------------------------------+
.. i18n: |                            |                                              |                                            |
.. i18n: | **openobject-client-web**  | https://launchpad.net/openobject-client-web  | the openobject web client (previously      |
.. i18n: |                            |                                              | called eTiny)                              |
.. i18n: |                            |                                              |                                            |
.. i18n: +----------------------------+----------------------------------------------+--------------------------------------------+
.. i18n: |                            |                                              |                                            |
.. i18n: | **openobject-addons**      | https://launchpad.net/openobject-addons      | the project for all modules about          |
.. i18n: |                            |                                              | openobject                                 |
.. i18n: |                            |                                              |                                            |
.. i18n: +----------------------------+----------------------------------------------+--------------------------------------------+
.. i18n: |                            |                                              |                                            |
.. i18n: | **openerp**                | https://launchpad.net/openerp                | packaging around openobject (a selection   |
.. i18n: |                            |                                              | of modules to build applications)          |
.. i18n: |                            |                                              |                                            |
.. i18n: +----------------------------+----------------------------------------------+--------------------------------------------+
..

+----------------------------+----------------------------------------------+--------------------------------------------+
| **Project name**           | **URL**                                      | **Description**                            |
+============================+==============================================+============================================+
|                            |                                              |                                            |
| **openobject**             | https://launchpad.net/openobject             | the main super-project (group) where all   |
|                            |                                              | bugs, features and faq are managed         |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openobject-bi**          | https://launchpad.net/openobject-bin         | business intelligence project              |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openobject-server**      | https://launchpad.net/openobject-server      |  the openobject server                     |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openobject-client**      | https://launchpad.net/openobject-client      | the openobject application client (gtk)    |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openobject-client-web**  | https://launchpad.net/openobject-client-web  | the openobject web client (previously      |
|                            |                                              | called eTiny)                              |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openobject-addons**      | https://launchpad.net/openobject-addons      | the project for all modules about          |
|                            |                                              | openobject                                 |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openerp**                | https://launchpad.net/openerp                | packaging around openobject (a selection   |
|                            |                                              | of modules to build applications)          |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+

.. i18n: Getting Sources
.. i18n: +++++++++++++++
..

Getting Sources
+++++++++++++++

.. i18n: Please refer to :ref:`how-to-get-the-latest-trunk-source-code-link` in the Bazaar section
..

Please refer to :ref:`how-to-get-the-latest-trunk-source-code-link` in the Bazaar section

.. i18n: If you don't know the Bazaar version control system, please read the :ref:`documentation on Bazaar <bazaar-link>`
..

If you don't know the Bazaar version control system, please read the :ref:`documentation on Bazaar <bazaar-link>`

.. i18n: Coding Guidelines
.. i18n: +++++++++++++++++
..

Coding Guidelines
+++++++++++++++++

.. i18n: Development Guidelines
.. i18n: """"""""""""""""""""""
..

Development Guidelines
""""""""""""""""""""""

.. i18n: Modules
.. i18n: ^^^^^^^
..

Modules
^^^^^^^

.. i18n: Organisation of files in modules
.. i18n: ################################
..

Organisation of files in modules
################################

.. i18n: .. === Organisation of files in modules ===
..

.. === Organisation of files in modules ===

.. i18n: The structure of a module should be::
.. i18n: 
.. i18n:  /module_name/
.. i18n:  /module_name/__init__.py
.. i18n:  /module_name/__openerp__.py
.. i18n:  /module_name/module.py
.. i18n:  /module_name/module_view.xml
.. i18n:  /module_name/module_wizard.xml
.. i18n:  /module_name/module_report.xml
.. i18n:  /module_name/module_data.xml
.. i18n:  /module_name/module_demo.xml
.. i18n:  /module_name/module_security.xml
.. i18n:  /module_name/wizard/
.. i18n:  /module_name/wizard/__init__.py
.. i18n:  /module_name/wizard/wizard_name.py
.. i18n:  /module_name/wizard/wizard_name_view.xml
.. i18n:  /module_name/wizard/wizard_name_workflow.xml
.. i18n:  /module_name/report/
.. i18n:  /module_name/report/__init__.py
.. i18n:  /module_name/report/report_name.sxw
.. i18n:  /module_name/report/report_name.rml
.. i18n:  /module_name/report/report_name.py
..

The structure of a module should be::

 /module_name/
 /module_name/__init__.py
 /module_name/__openerp__.py
 /module_name/module.py
 /module_name/module_view.xml
 /module_name/module_wizard.xml
 /module_name/module_report.xml
 /module_name/module_data.xml
 /module_name/module_demo.xml
 /module_name/module_security.xml
 /module_name/wizard/
 /module_name/wizard/__init__.py
 /module_name/wizard/wizard_name.py
 /module_name/wizard/wizard_name_view.xml
 /module_name/wizard/wizard_name_workflow.xml
 /module_name/report/
 /module_name/report/__init__.py
 /module_name/report/report_name.sxw
 /module_name/report/report_name.rml
 /module_name/report/report_name.py

.. i18n: Naming Objects and fields
.. i18n: #########################
..

Naming Objects and fields
#########################

.. i18n: Security
.. i18n: ########
..

Security
########

.. i18n: Each object defined in your module must have at least one security rule
.. i18n: defined on it to make it accessible.
..

Each object defined in your module must have at least one security rule
defined on it to make it accessible.

.. i18n: Development
.. i18n: ^^^^^^^^^^^
..

Development
^^^^^^^^^^^

.. i18n: Coding Guidelines
.. i18n: #################
..

Coding Guidelines
#################

.. i18n: Follow Python PEP 8: http://www.python.org/dev/peps/pep-0008/
..

Follow Python PEP 8: http://www.python.org/dev/peps/pep-0008/

.. i18n: Reporting
.. i18n: ^^^^^^^^^
..

Reporting
^^^^^^^^^

.. i18n: General Style
.. i18n: #############
..

General Style
#############

.. i18n:   * use the Helvetica font everywhere
.. i18n:   * margins (in millimeters):
.. i18n: 
.. i18n:     - top: 14
.. i18n:     - bottom: 16
.. i18n:     - left: between 12 and 13 to allow punching holes without punching in the text area
.. i18n:     - right: between 12 and 13
..

  * use the Helvetica font everywhere
  * margins (in millimeters):

    - top: 14
    - bottom: 16
    - left: between 12 and 13 to allow punching holes without punching in the text area
    - right: between 12 and 13

.. i18n:     .. note:: the line separator between the header and the body can overlap slightly in the left and right margins: up to 9 millimeters on the left and up to 12 millimeters on the right
.. i18n: 
.. i18n:   * for Titles use font *Helvetica-Bold* with size *14.5*
.. i18n: 
.. i18n:   * put the context on each report: example, for the report account_balance: the context is the fiscal year and periods
.. i18n: 
.. i18n:   * for the name of cells: use Capital Letter if the name contains more than one word (ex: Date Ordered)
.. i18n:   * content and name of cells should have the same indentation
.. i18n: 
.. i18n:   * for report, we can define two kinds of arrays:
.. i18n: 
.. i18n:     - array with general information, like reference, date..., use:
.. i18n: 
.. i18n:       + *Bold-Helvetica* and size=8 for cells name
.. i18n:       + *Helvetica* size="8" for content
.. i18n:       
.. i18n:     - array with detailed information, use:
.. i18n: 
.. i18n:       + *Helvetica-Bold* size *9* for cells names
.. i18n:       + *Helvetica* size *8* for content
..

    .. note:: the line separator between the header and the body can overlap slightly in the left and right margins: up to 9 millimeters on the left and up to 12 millimeters on the right

  * for Titles use font *Helvetica-Bold* with size *14.5*

  * put the context on each report: example, for the report account_balance: the context is the fiscal year and periods

  * for the name of cells: use Capital Letter if the name contains more than one word (ex: Date Ordered)
  * content and name of cells should have the same indentation

  * for report, we can define two kinds of arrays:

    - array with general information, like reference, date..., use:

      + *Bold-Helvetica* and size=8 for cells name
      + *Helvetica* size="8" for content
      
    - array with detailed information, use:

      + *Helvetica-Bold* size *9* for cells names
      + *Helvetica* size *8* for content

.. i18n: .. describe:: Headers and footers for internal reports:
.. i18n: 
.. i18n:   * Internal report = all accounting reports and other that have only internal use (not sent to customers)
.. i18n:   * height of headers should be shorter
.. i18n:   * take off corporate header and footer for internal report (Use a simplified header for internal reports: Company's name, report title, printing date and page number)
.. i18n: 
.. i18n:   * header:
.. i18n: 
.. i18n:     - company's name: in the middle of each page
.. i18n:     - report's name: is printed centered after the header
.. i18n:     - printing date: not in the middle of the report, but on the left in the header
.. i18n:     - page number: on each page, is printed on the right. This page number should contain the current page number and the total of pages. Ex: page 3/15
.. i18n:   * footer:
.. i18n: 
.. i18n:     - to avoid wasting paper, we have taken off the footer
..

.. describe:: Headers and footers for internal reports:

  * Internal report = all accounting reports and other that have only internal use (not sent to customers)
  * height of headers should be shorter
  * take off corporate header and footer for internal report (Use a simplified header for internal reports: Company's name, report title, printing date and page number)

  * header:

    - company's name: in the middle of each page
    - report's name: is printed centered after the header
    - printing date: not in the middle of the report, but on the left in the header
    - page number: on each page, is printed on the right. This page number should contain the current page number and the total of pages. Ex: page 3/15
  * footer:

    - to avoid wasting paper, we have taken off the footer

.. i18n: .. describe:: table line separator:
..

.. describe:: table line separator:

.. i18n: * it's prettier if each line in a table has a light grey line as separator
.. i18n: * use a grey column separator only for array containing general information
..

* it's prettier if each line in a table has a light grey line as separator
* use a grey column separator only for array containing general information

.. i18n: .. describe:: table breaking
.. i18n: 
.. i18n:   * a table header should at least have two data rows (no table header alone at the bottom of the page)
.. i18n:   * when a big table is broken, the table header is repeated on every page
..

.. describe:: table breaking

  * a table header should at least have two data rows (no table header alone at the bottom of the page)
  * when a big table is broken, the table header is repeated on every page

.. i18n: .. describe:: how to differentiate parents and children ?
.. i18n: 
.. i18n:   * When you have more than one level, use these styles:
.. i18n: 
.. i18n:   - for the levels 1 and 2:fontSize="8.0" fontName="Helvetica-Bold"
.. i18n:   - from the third level, use:fontName="Helvetica" fontSize="8.0" and increase the indentation with  13 (pixels) for each level
.. i18n:   - underline sums when the element is a parent
..

.. describe:: how to differentiate parents and children ?

  * When you have more than one level, use these styles:

  - for the levels 1 and 2:fontSize="8.0" fontName="Helvetica-Bold"
  - from the third level, use:fontName="Helvetica" fontSize="8.0" and increase the indentation with  13 (pixels) for each level
  - underline sums when the element is a parent

.. i18n: Modules
.. i18n: """""""
..

Modules
"""""""

.. i18n: Naming Convention
.. i18n: ^^^^^^^^^^^^^^^^^
..

Naming Convention
^^^^^^^^^^^^^^^^^

.. i18n: The name of the module are all lowercase, each word separated by underscores.
.. i18n: Always start with the most relevant words, which are preferably names of other
.. i18n: modules on which it depends.
..

The name of the module are all lowercase, each word separated by underscores.
Always start with the most relevant words, which are preferably names of other
modules on which it depends.

.. i18n: Example:
..

Example:

.. i18n:   * account_invoice_layout
..

  * account_invoice_layout

.. i18n: Information Required
.. i18n: ^^^^^^^^^^^^^^^^^^^^
..

Information Required
^^^^^^^^^^^^^^^^^^^^

.. i18n: Each module must contain at least:
..

Each module must contain at least:

.. i18n:   * name
.. i18n:   * description
..

  * name
  * description

.. i18n: Modules Description
.. i18n: ^^^^^^^^^^^^^^^^^^^
..

Modules Description
^^^^^^^^^^^^^^^^^^^

.. i18n: Dependencies
.. i18n: ^^^^^^^^^^^^
..

Dependencies
^^^^^^^^^^^^

.. i18n: Each module must contain:
..

Each module must contain:

.. i18n:   * A list of dependencies amongst others modules: ['account','sale']
.. i18n: 
.. i18n:     - Provide only highest requirement level, not need to set ['account','base','product','sale']
.. i18n:   * A version requirement string where base is the OpenERP version as a Python expression
.. i18n: 
.. i18n:     - account>=1.0 && base=4.4
..

  * A list of dependencies amongst others modules: ['account','sale']

    - Provide only highest requirement level, not need to set ['account','base','product','sale']
  * A version requirement string where base is the OpenERP version as a Python expression

    - account>=1.0 && base=4.4

.. i18n: Module Content
.. i18n: ^^^^^^^^^^^^^^
..

Module Content
^^^^^^^^^^^^^^

.. i18n: Each module must contain demo data for every object defined in the module.
..

Each module must contain demo data for every object defined in the module.

.. i18n: If you implemented workflows in the module, create demo data that passes
.. i18n: most branches of your workflow. You can use the module recorder to help you
.. i18n: build such demo data.
..

If you implemented workflows in the module, create demo data that passes
most branches of your workflow. You can use the module recorder to help you
build such demo data.

.. i18n: User Interface Guidelines
.. i18n: """""""""""""""""""""""""
..

User Interface Guidelines
"""""""""""""""""""""""""

.. i18n: Menus
.. i18n: ^^^^^
..

Menus
^^^^^

.. i18n: Organising menus
.. i18n: ################
..

Organising menus
################

.. i18n: Here is a good example:
..

Here is a good example:

.. i18n:   * Invoices (list)
.. i18n: 
.. i18n:     - Customer Invoices (list)
..

  * Invoices (list)

    - Customer Invoices (list)

.. i18n:       + Draft Customer Invoices (list)
.. i18n:       + Open Customer Invoices (list)
.. i18n:       + New Customer Invoice (form)
.. i18n:     - Supplier Invoices
..

      + Draft Customer Invoices (list)
      + Open Customer Invoices (list)
      + New Customer Invoice (form)
    - Supplier Invoices

.. i18n:       + ...
..

      + ...

.. i18n: Add a *New ...* menu only if the user requires it, otherwise, open all
.. i18n: menus as lists. The *New ...* menu open as a form instead of a list. For example,
.. i18n: don't put *New ...* in a menu in the configuration part.
..

Add a *New ...* menu only if the user requires it, otherwise, open all
menus as lists. The *New ...* menu open as a form instead of a list. For example,
don't put *New ...* in a menu in the configuration part.

.. i18n: If you use folders that are clickable, their child must be of the
.. i18n: same object type. (we suppose that inheritances are the same objects)
..

If you use folders that are clickable, their child must be of the
same object type. (we suppose that inheritances are the same objects)

.. i18n: List are plurals:
..

List are plurals:

.. i18n:   * *Customer Invoice*, should be *Customer Invoices*
..

  * *Customer Invoice*, should be *Customer Invoices*

.. i18n: If you want to create menu that filters on the user (*All* and *My*) put them at the same level:
..

If you want to create menu that filters on the user (*All* and *My*) put them at the same level:

.. i18n:   * Tasks
.. i18n:   * My Tasks
..

  * Tasks
  * My Tasks

.. i18n: And not:
..

And not:

.. i18n:   * Tasks
.. i18n: 
.. i18n:     - My Tasks
..

  * Tasks

    - My Tasks

.. i18n: Avoid Abbreviations in menus if possible. Example:
..

Avoid Abbreviations in menus if possible. Example:

.. i18n:   * BoM Lines -> Bill of Materials Lines
..

  * BoM Lines -> Bill of Materials Lines

.. i18n: Reporting Menu
.. i18n: ##############
..

Reporting Menu
##############

.. i18n: The dashboard menu must be under the report section of each main menu
..

The dashboard menu must be under the report section of each main menu

.. i18n:   * Good: Sales Management / Reporting / Dashboards / Sales Manager
.. i18n:   * Bad: Dashboard / Sales / Sales Manager
..

  * Good: Sales Management / Reporting / Dashboards / Sales Manager
  * Bad: Dashboard / Sales / Sales Manager

.. i18n: If you want to manage the *This Month/ALL months* menu, put them at the lowest level:
..

If you want to manage the *This Month/ALL months* menu, put them at the lowest level:

.. i18n:   * Reporting/Timesheet by User/All Month
.. i18n:   * Reporting/Timesheet by User/This Month
..

  * Reporting/Timesheet by User/All Month
  * Reporting/Timesheet by User/This Month

.. i18n: Icons in the menu
.. i18n: #################
..

Icons in the menu
#################

.. i18n:   * The icon of the menu, must be set according to the final action of the wizard, example:
.. i18n: 
.. i18n:     - wizard that prints a report, should use a report icon and not a wizard
.. i18n:     - wizard that opens a list at the end, should use a list icon and not a wizard
..

  * The icon of the menu, must be set according to the final action of the wizard, example:

    - wizard that prints a report, should use a report icon and not a wizard
    - wizard that opens a list at the end, should use a list icon and not a wizard

.. i18n: Order of the menus
.. i18n: ##################
..

Order of the menus
##################

.. i18n: The configuration menu must be at the top of the list, use a sequence=0
..

The configuration menu must be at the top of the list, use a sequence=0

.. i18n: The *Reporting* menu is at the bottom of the list, use a sequence=50.
..

The *Reporting* menu is at the bottom of the list, use a sequence=50.

.. i18n: Common Mistakes
.. i18n: ###############
..

Common Mistakes
###############

.. i18n:   * Edit Categories -> Categories
.. i18n:   * List of Categories -> Categories
..

  * Edit Categories -> Categories
  * List of Categories -> Categories

.. i18n: Views
.. i18n: ^^^^^
..

Views
^^^^^

.. i18n: Objects with States
.. i18n: ###################
..

Objects with States
###################

.. i18n:   * The state field, if any, must be at the bottom left corner of the view
.. i18n:   * Buttons to make the state change at the right of this state field
..

  * The state field, if any, must be at the bottom left corner of the view
  * Buttons to make the state change at the right of this state field

.. i18n: Search Criteria
.. i18n: #################
..

Search Criteria
#################

.. i18n: Search criteria: search available on all columns of the list view
..

Search criteria: search available on all columns of the list view

.. i18n: Action Names
.. i18n: ^^^^^^^^^^^^
..

Action Names
^^^^^^^^^^^^

.. i18n: .. todo:: write 'Action Names' section
..

.. todo:: write 'Action Names' section

.. i18n: Wizards
.. i18n: ^^^^^^^
..

Wizards
^^^^^^^

.. i18n: Terminology
.. i18n: """""""""""
..

Terminology
"""""""""""

.. i18n: Default Language
.. i18n: ^^^^^^^^^^^^^^^^
..

Default Language
^^^^^^^^^^^^^^^^

.. i18n: The default language for every development must be U.S. English.
..

The default language for every development must be U.S. English.

.. i18n: For menus and fields, use uppercase for all first letters, excluding conjections:
..

For menus and fields, use uppercase for all first letters, excluding conjections:

.. i18n:   * Chart of Accounts
..

  * Chart of Accounts

.. i18n: Field Naming Conventions
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^
..

Field Naming Conventions
^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n:   * Avoid generic terms in fields and use if possible explicit terms, some example:
.. i18n: 
.. i18n:     - Name -> Sale Order Name
.. i18n:     - Parent -> Bill of Material Parent
.. i18n:     - Rate -> Currency Rate Conversion
.. i18n:     - Amount -> Quantity Sold
..

  * Avoid generic terms in fields and use if possible explicit terms, some example:

    - Name -> Sale Order Name
    - Parent -> Bill of Material Parent
    - Rate -> Currency Rate Conversion
    - Amount -> Quantity Sold

.. i18n: Here are some rules to respect:
..

Here are some rules to respect:

.. i18n: * many2one fields should respect this regex: '.*_id'
.. i18n: * one2many fields should respect this regex: '.*_ids'
.. i18n: * one2many relation table should respect this regex: '.*_rel'
.. i18n: * many2many fields should respect this regex: '.*_ids'
.. i18n: * use underscore to separate words
.. i18n: * avoid using uppercase
.. i18n: * if a field is composed of several words, start with the most important words
.. i18n: 
.. i18n:    * This is good: sale_price, partner_address_id
.. i18n:    * This is bad: is_sellable
..

* many2one fields should respect this regex: '.*_id'
* one2many fields should respect this regex: '.*_ids'
* one2many relation table should respect this regex: '.*_rel'
* many2many fields should respect this regex: '.*_ids'
* use underscore to separate words
* avoid using uppercase
* if a field is composed of several words, start with the most important words

   * This is good: sale_price, partner_address_id
   * This is bad: is_sellable

.. i18n: Object Naming Conventions
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^
..

Object Naming Conventions
^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: * All objects must start by the name of the module they are defined in.
.. i18n: * If an object is composed of several words, use points to separate words
..

* All objects must start by the name of the module they are defined in.
* If an object is composed of several words, use points to separate words

.. i18n: Some terms
.. i18n: ^^^^^^^^^^
..

Some terms
^^^^^^^^^^

.. i18n:   * All Tree of resources are called *XXX's Structure*, unless a dedicated term exist for the concept
.. i18n: 
.. i18n:     - Good: Location' Structure, Chart of Accounts, Categories' Structure
.. i18n:     - Bad: Tree of Category, Tree of Bill of Materials
..

  * All Tree of resources are called *XXX's Structure*, unless a dedicated term exist for the concept

    - Good: Location' Structure, Chart of Accounts, Categories' Structure
    - Bad: Tree of Category, Tree of Bill of Materials

.. i18n: Module Recorder
.. i18n: +++++++++++++++
..

Module Recorder
+++++++++++++++

.. i18n: .. todo:: write 'Module Recorder' section
..

.. todo:: write 'Module Recorder' section

.. i18n: Review quality
.. i18n: ++++++++++++++
..

Review quality
++++++++++++++

.. i18n: 	- You can check your module quality using "base_module_quality" module available on stable addons
..

	- You can check your module quality using "base_module_quality" module available on stable addons
