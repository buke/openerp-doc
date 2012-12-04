

Developing modules
-------------------

.. index::
   single: modules development
..

Introduction
++++++++++++

Here you will find information about the organisation of the community in
OpenERP project. It includes a description of the different tools used, the role
of the different actors, and the different process for improvement management.

The whole organisation is managed through our launchpad projects: http://launchpad.net
Our projects on launchpad are currently organised like this:


+----------------------------+----------------------------------------------+--------------------------------------------+
| **Project name**           | **URL**                                      | **Description**                            |
+============================+==============================================+============================================+
|                            |                                              |                                            |
| **openobject**             | https://launchpad.net/openobject             | the main super-project (group) where all   |
|                            |                                              | bugs, features and faq are managed         |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openobject-addons**      | https://launchpad.net/openobject-addons      | the project for core OpenERP modules       |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openobject-server**      | https://launchpad.net/openobject-server      | the OpenERP server                         |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openerp-web**            | https://launchpad.net/openerp-web            | the web client for OpenERP 6.1 and newer   |
|                            |                                              | versions                                   |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openobject-client**      | https://launchpad.net/openobject-client      | the native client (gtk) for OpenERP 6.1    |
|                            |                                              | and earlier                                |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+
|                            |                                              |                                            |
| **openobject-client-web**  | https://launchpad.net/openobject-client-web  | the web client for OpenERP 6.0 and earlier |
|                            |                                              | versions                                   |
|                            |                                              |                                            |
+----------------------------+----------------------------------------------+--------------------------------------------+

Getting Sources
+++++++++++++++

Please refer to :ref:`how-to-get-the-latest-trunk-source-code-link` in the Bazaar section

If you don't know the Bazaar version control system, please read the :ref:`documentation on Bazaar <bazaar-link>`

Community Addons
++++++++++++++++

OpenERP modules developed by the community were historically published in a shared source
code branch on Launchpad, nicknamed ``extra-addons``: https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-extra-addons

As of 2012 and the release of OpenERP 6.1, this shared branch is being phased out, due to several downsides to this
organization, such as:

 * difficult to enforce access control on the modules (commit right is all or nothing)
 * difficult to enforce quality (therefore impossible to rely on it for customer projects)
 * commit history mixes all modules
 * download/checkout of the branch requires to fetch all modules at once

A better organization was discussed on the OpenERP `mailing-lists <https://lists.launchpad.net/openerp-expert-framework/msg00948.html>`_,
with the `following goals <https://lists.launchpad.net/openerp-expert-framework/msg00997.html>`_:

 * To get rid of the big extra-addons branch
 * To join efforts on the same topic in order to avoid too many modules for a same feature
 * To become more aware of the developments that have been done by others
 * To start working with merge proposal between us
 * To improve the quality of our code

The community modules have therefore been split into separate Launchpad project and
their respective branches. When possible, existing ones were reused. All listed projects
provide a short description of the kind of modules you can find/merge into.

The community welcomes everyone on board to join efforts! In order to add your own modules in the appropriate project,
you should use merge proposals. Depending on the volume, some time might be needed at the beginning to review everything.
So thank you all in advance for your patience during this transition period.

For all of these projects, the rules we expect you to adhere to and respect are:

 * No company-related prefix or suffix in the module names (like ``c2c-account-something``);
 * Always make merge proposal for any bugfix or improvement so that everyone can take note of it and eventually ask for a different approach;
 * Nobody merge his/her own work into the branch. Another member of the team must do it. Exceptions may be accepted if the merge proposal has been strongly approved by the rest of the team;
 * If your module doesn’t fit into any of the available projects, or you found no related team, please post a request on the `framework expert mailing list <https://launchpad.net/~openerp-expert-framework>`_ so that we can create a specific one for you;
 * When at least one of your modules has been approved in the branch, you may ask to be part of the team. If you are not part of the team, you can still contribute to the project through merge proposals;
 * Use the available teams (see :ref:`community_contrib_teams` section) according to their topics (it means that you always need to attribute a new project to these teams, so as to avoid having hundreds of them).

Should you have any suggestions related to the above rules, please feel free to post them on the framework expert mailing list.


Community Projects
^^^^^^^^^^^^^^^^^^
The list of the official community projects/topics can be found under this project group: https://launchpad.net/openobject,
and is summarized below.

 * Stock and Logistic Barcode: https://launchpad.net/stock-logistic-barcode
 * Stock and Logistic Warehouse: https://launchpad.net/stock-logistic-warehouse
 * Stock and Logistic Tracking: https://launchpad.net/stock-logistic-tracking
 * Stock and Logistic Flows: https://launchpad.net/stock-logistic-flows
 * Stock and Logistic - Reports: https://launchpad.net/stock-logistic-report
 * Carriers And Deliveries Management: https://launchpad.net/carriers-deliveries
 * Banking Addons: https://launchpad.net/banking-addons
 * Contact and Partner Management: https://launchpad.net/partner-contact-management
 * Purchase - Workflow and Organization: https://launchpad.net/purchase-wkfl
 * Purchase - Financial Controlling: https://launchpad.net/purchase-financial
 * Purchase - Reports: https://launchpad.net/purchase-report
 * Sales - Financial Controlling: https://launchpad.net/sale-financial
 * Sales - Workflow and Organization: https://launchpad.net/sale-wkfl
 * Sales - Reports: https://launchpad.net/sale-reports
 * Product - Kitting Management: https://launchpad.net/product-kitting
 * OpenERP Product Attributes : https://launchpad.net/openerp-product-attributes
 * Account - Financial Report: https://launchpad.net/account-financial-report
 * Account - Analytic Accounting: https://launchpad.net/account-analytic
 * Account - Budgeting: https://launchpad.net/account-budgeting
 * Account - Invoicing Reports: https://launchpad.net/account-invoice-report
 * Account Payment Addons: https://launchpad.net/account-payment
 * Account - Closing: https://launchpad.net/account-closing
 * Account - Consolidation: https://launchpad.net/account-consolidation
 * Account - Financial Tools: https://launchpad.net/account-financial-tools
 * Account - Invoicing: https://launchpad.net/account-invoicing
 * Contract management: https://launchpad.net/contract-management
 * OpenERP Fiscal Rule: https://launchpad.net/openerp-fiscal-rules
 * Margin Analysis: https://launchpad.net/margin-analysis
 * Medical in OpenERP : https://launchpad.net/oemedical
 * Construction : https://launchpad.net/openerp-construction
 * Project Management - Invoicing and Reporting: https://launchpad.net/project-reporting
 * Project Management - Services: https://launchpad.net/project-service
 * HR - Timesheet Management: https://launchpad.net/hr-timesheet
 * Hotel Management System on OpenERP : https://launchpad.net/hotel-management-system
 * Department Management: https://launchpad.net/department-mgmt
 * Server Environment And Tools: https://launchpad.net/server-env-tools
 * Webkit Utils: https://launchpad.net/webkit-utils
 * E-Commerce addons: https://launchpad.net/e-commerce-addons
 * Report - Printing and Sending: https://launchpad.net/report-print-send
 * Management Systems : https://launchpad.net/openerp-mgmtsystem
 * Web-Addons for OpenERP : https://launchpad.net/web-addons
 * Geospatial Addons for OpenERP : https://launchpad.net/geospatial-addons

Some of them are waiting on their owner to bring some modifications so they can fit into other projects (changing team, series,...).
Should you be one of these owners, please inform the others on the mailing-list when ready.
If some refuse to open the projects to the community, it is always possibel to create another project.


Misc Guidelines
+++++++++++++++

Modules
^^^^^^^

Organisation of files in modules
################################

.. === Organisation of files in modules ===

The structure of a module should be::

 /module_name/
 /module_name/__init__.py
 /module_name/__openerp__.py
 /module_name/i18n
 /module_name/i18n/module_name.pot
 /module_name/images/
 /module_name/images/screenshot.png
 /module_name/migrations
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
 /module_name/security
 /module_name/security/ir.model.access.csv
 /module_name/static/src/img/icon.png
 /module_name/tests

Security
########

Each object defined in your module must have at least one security rule
defined on it to make it accessible.

Coding Guidelines
#################

Follow Python PEP 8: http://www.python.org/dev/peps/pep-0008/

Reporting
^^^^^^^^^

General Style
#############

  * use the Helvetica font everywhere
  * margins (in millimeters):

    - top: 14
    - bottom: 16
    - left: between 12 and 13 to allow punching holes without punching in the text area
    - right: between 12 and 13

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

.. describe:: table line separator:

* it's prettier if each line in a table has a light grey line as separator
* use a grey column separator only for array containing general information

.. describe:: table breaking

  * a table header should at least have two data rows (no table header alone at the bottom of the page)
  * when a big table is broken, the table header is repeated on every page

.. describe:: how to differentiate parents and children ?

  * When you have more than one level, use these styles:

  - for the levels 1 and 2:fontSize="8.0" fontName="Helvetica-Bold"
  - from the third level, use:fontName="Helvetica" fontSize="8.0" and increase the indentation with  13 (pixels) for each level
  - underline sums when the element is a parent

Modules
"""""""

Naming Convention
^^^^^^^^^^^^^^^^^

The name of the module are all lowercase, each word separated by underscores.
Always start with the most relevant words, which are preferably names of other
modules on which it depends.

Example:

  * account_invoice_layout

Information Required
^^^^^^^^^^^^^^^^^^^^

Each module must contain at least:

  * name
  * description

Modules Description
^^^^^^^^^^^^^^^^^^^

Dependencies
^^^^^^^^^^^^

Each module must contain:

  * A list of dependencies amongst others modules: ['account','sale']

  * Provide only highest requirement level, not need to set ['account','base','product','sale']

Module Content
^^^^^^^^^^^^^^

Each module must contain demo data for every object defined in the module.

If you implemented workflows in the module, create demo data that passes
most branches of your workflow. You can use the module recorder to help you
build such demo data.

Menus
^^^^^

Naming Menus
############

  * Use plural forms: *Customer Invoice*, should be *Customer Invoices*
  * Avoid abbreviations in menus if possible. Example: BoMs -> Bills of Materials


Order of the menus
##################

The *Reporting* menu is at the bottom of the list, use a sequence=50.

Common Mistakes
###############

  * Edit Categories -> Categories
  * List of Categories -> Categories

Search Criteria
#################

Search criteria: search available on all columns of the list view

Default Language
^^^^^^^^^^^^^^^^

The default language for every development must be U.S. English.

For menus and fields, use uppercase for all first letters, excluding conjections:

  * Chart of Accounts

Field Naming Conventions
^^^^^^^^^^^^^^^^^^^^^^^^

  * many2one fields should respect this regex: '.*_id'
  * one2many fields should respect this regex: '.*_ids'
  * one2many relation table should respect this regex: '.*_rel'
  * many2many fields should respect this regex: '.*_ids'
  * use underscore to separate words
  * avoid using uppercase
  * if a field is composed of several words, start with the most important words

Model Naming Conventions
^^^^^^^^^^^^^^^^^^^^^^^^

* All objects must start with the name of the module they are defined in.
* If an object is composed of several words, use points to separate words


Terminology
^^^^^^^^^^^

  * All Tree of resources are called *XXX's Structure*, unless a dedicated term exist for the concept

    - Good: Location' Structure, Chart of Accounts, Categories' Structure
    - Bad: Tree of Category, Tree of Bill of Materials
