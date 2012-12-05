.. i18n: Developing modules
.. i18n: -------------------
..

开发模块
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

序
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
.. i18n: | **openobject-addons**      | https://launchpad.net/openobject-addons      | the project for core OpenERP modules       |
.. i18n: |                            |                                              |                                            |
.. i18n: +----------------------------+----------------------------------------------+--------------------------------------------+
.. i18n: |                            |                                              |                                            |
.. i18n: | **openobject-server**      | https://launchpad.net/openobject-server      | the OpenERP server                         |
.. i18n: |                            |                                              |                                            |
.. i18n: +----------------------------+----------------------------------------------+--------------------------------------------+
.. i18n: |                            |                                              |                                            |
.. i18n: | **openerp-web**            | https://launchpad.net/openerp-web            | the web client for OpenERP 6.1 and newer   |
.. i18n: |                            |                                              | versions                                   |
.. i18n: |                            |                                              |                                            |
.. i18n: +----------------------------+----------------------------------------------+--------------------------------------------+
.. i18n: |                            |                                              |                                            |
.. i18n: | **openobject-client**      | https://launchpad.net/openobject-client      | the native client (gtk) for OpenERP 6.1    |
.. i18n: |                            |                                              | and earlier                                |
.. i18n: |                            |                                              |                                            |
.. i18n: +----------------------------+----------------------------------------------+--------------------------------------------+
.. i18n: |                            |                                              |                                            |
.. i18n: | **openobject-client-web**  | https://launchpad.net/openobject-client-web  | the web client for OpenERP 6.0 and earlier |
.. i18n: |                            |                                              | versions                                   |
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

.. i18n: Getting Sources
.. i18n: +++++++++++++++
..

获取源码
+++++++++++++++

.. i18n: Please refer to :ref:`how-to-get-the-latest-trunk-source-code-link` in the Bazaar section
..

Please refer to :ref:`how-to-get-the-latest-trunk-source-code-link` in the Bazaar section

.. i18n: If you don't know the Bazaar version control system, please read the :ref:`documentation on Bazaar <bazaar-link>`
..

If you don't know the Bazaar version control system, please read the :ref:`documentation on Bazaar <bazaar-link>`

.. i18n: Community Addons
.. i18n: ++++++++++++++++
..

社区模块
++++++++++++++++

.. i18n: OpenERP modules developed by the community were historically published in a shared source
.. i18n: code branch on Launchpad, nicknamed ``extra-addons``: https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-extra-addons
..

OpenERP modules developed by the community were historically published in a shared source
code branch on Launchpad, nicknamed ``extra-addons``: https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-extra-addons

.. i18n: As of 2012 and the release of OpenERP 6.1, this shared branch is being phased out, due to several downsides to this
.. i18n: organization, such as:
..

As of 2012 and the release of OpenERP 6.1, this shared branch is being phased out, due to several downsides to this
organization, such as:

.. i18n:  * difficult to enforce access control on the modules (commit right is all or nothing)
.. i18n:  * difficult to enforce quality (therefore impossible to rely on it for customer projects)
.. i18n:  * commit history mixes all modules
.. i18n:  * download/checkout of the branch requires to fetch all modules at once
..

 * difficult to enforce access control on the modules (commit right is all or nothing)
 * difficult to enforce quality (therefore impossible to rely on it for customer projects)
 * commit history mixes all modules
 * download/checkout of the branch requires to fetch all modules at once

.. i18n: A better organization was discussed on the OpenERP `mailing-lists <https://lists.launchpad.net/openerp-expert-framework/msg00948.html>`_,
.. i18n: with the `following goals <https://lists.launchpad.net/openerp-expert-framework/msg00997.html>`_:
..

A better organization was discussed on the OpenERP `mailing-lists <https://lists.launchpad.net/openerp-expert-framework/msg00948.html>`_,
with the `following goals <https://lists.launchpad.net/openerp-expert-framework/msg00997.html>`_:

.. i18n:  * To get rid of the big extra-addons branch
.. i18n:  * To join efforts on the same topic in order to avoid too many modules for a same feature
.. i18n:  * To become more aware of the developments that have been done by others
.. i18n:  * To start working with merge proposal between us
.. i18n:  * To improve the quality of our code
..

 * To get rid of the big extra-addons branch
 * To join efforts on the same topic in order to avoid too many modules for a same feature
 * To become more aware of the developments that have been done by others
 * To start working with merge proposal between us
 * To improve the quality of our code

.. i18n: The community modules have therefore been split into separate Launchpad project and
.. i18n: their respective branches. When possible, existing ones were reused. All listed projects
.. i18n: provide a short description of the kind of modules you can find/merge into.
..

The community modules have therefore been split into separate Launchpad project and
their respective branches. When possible, existing ones were reused. All listed projects
provide a short description of the kind of modules you can find/merge into.

.. i18n: The community welcomes everyone on board to join efforts! In order to add your own modules in the appropriate project,
.. i18n: you should use merge proposals. Depending on the volume, some time might be needed at the beginning to review everything.
.. i18n: So thank you all in advance for your patience during this transition period.
..

The community welcomes everyone on board to join efforts! In order to add your own modules in the appropriate project,
you should use merge proposals. Depending on the volume, some time might be needed at the beginning to review everything.
So thank you all in advance for your patience during this transition period.

.. i18n: For all of these projects, the rules we expect you to adhere to and respect are:
..

For all of these projects, the rules we expect you to adhere to and respect are:

.. i18n:  * No company-related prefix or suffix in the module names (like ``c2c-account-something``);
.. i18n:  * Always make merge proposal for any bugfix or improvement so that everyone can take note of it and eventually ask for a different approach;
.. i18n:  * Nobody merge his/her own work into the branch. Another member of the team must do it. Exceptions may be accepted if the merge proposal has been strongly approved by the rest of the team;
.. i18n:  * If your module doesn’t fit into any of the available projects, or you found no related team, please post a request on the `framework expert mailing list <https://launchpad.net/~openerp-expert-framework>`_ so that we can create a specific one for you;
.. i18n:  * When at least one of your modules has been approved in the branch, you may ask to be part of the team. If you are not part of the team, you can still contribute to the project through merge proposals;
.. i18n:  * Use the available teams (see :ref:`community_contrib_teams` section) according to their topics (it means that you always need to attribute a new project to these teams, so as to avoid having hundreds of them).
..

 * No company-related prefix or suffix in the module names (like ``c2c-account-something``);
 * Always make merge proposal for any bugfix or improvement so that everyone can take note of it and eventually ask for a different approach;
 * Nobody merge his/her own work into the branch. Another member of the team must do it. Exceptions may be accepted if the merge proposal has been strongly approved by the rest of the team;
 * If your module doesn’t fit into any of the available projects, or you found no related team, please post a request on the `framework expert mailing list <https://launchpad.net/~openerp-expert-framework>`_ so that we can create a specific one for you;
 * When at least one of your modules has been approved in the branch, you may ask to be part of the team. If you are not part of the team, you can still contribute to the project through merge proposals;
 * Use the available teams (see :ref:`community_contrib_teams` section) according to their topics (it means that you always need to attribute a new project to these teams, so as to avoid having hundreds of them).

.. i18n: Should you have any suggestions related to the above rules, please feel free to post them on the framework expert mailing list.
..

Should you have any suggestions related to the above rules, please feel free to post them on the framework expert mailing list.

.. i18n: Community Projects
.. i18n: ^^^^^^^^^^^^^^^^^^
.. i18n: The list of the official community projects/topics can be found under this project group: https://launchpad.net/openobject,
.. i18n: and is summarized below.
..

Community Projects
^^^^^^^^^^^^^^^^^^
The list of the official community projects/topics can be found under this project group: https://launchpad.net/openobject,
and is summarized below.

.. i18n:  * Stock and Logistic Barcode: https://launchpad.net/stock-logistic-barcode
.. i18n:  * Stock and Logistic Warehouse: https://launchpad.net/stock-logistic-warehouse
.. i18n:  * Stock and Logistic Tracking: https://launchpad.net/stock-logistic-tracking
.. i18n:  * Stock and Logistic Flows: https://launchpad.net/stock-logistic-flows
.. i18n:  * Stock and Logistic - Reports: https://launchpad.net/stock-logistic-report
.. i18n:  * Carriers And Deliveries Management: https://launchpad.net/carriers-deliveries
.. i18n:  * Banking Addons: https://launchpad.net/banking-addons
.. i18n:  * Contact and Partner Management: https://launchpad.net/partner-contact-management
.. i18n:  * Purchase - Workflow and Organization: https://launchpad.net/purchase-wkfl
.. i18n:  * Purchase - Financial Controlling: https://launchpad.net/purchase-financial
.. i18n:  * Purchase - Reports: https://launchpad.net/purchase-report
.. i18n:  * Sales - Financial Controlling: https://launchpad.net/sale-financial
.. i18n:  * Sales - Workflow and Organization: https://launchpad.net/sale-wkfl
.. i18n:  * Sales - Reports: https://launchpad.net/sale-reports
.. i18n:  * Product - Kitting Management: https://launchpad.net/product-kitting
.. i18n:  * OpenERP Product Attributes : https://launchpad.net/openerp-product-attributes
.. i18n:  * Account - Financial Report: https://launchpad.net/account-financial-report
.. i18n:  * Account - Analytic Accounting: https://launchpad.net/account-analytic
.. i18n:  * Account - Budgeting: https://launchpad.net/account-budgeting
.. i18n:  * Account - Invoicing Reports: https://launchpad.net/account-invoice-report
.. i18n:  * Account Payment Addons: https://launchpad.net/account-payment
.. i18n:  * Account - Closing: https://launchpad.net/account-closing
.. i18n:  * Account - Consolidation: https://launchpad.net/account-consolidation
.. i18n:  * Account - Financial Tools: https://launchpad.net/account-financial-tools
.. i18n:  * Account - Invoicing: https://launchpad.net/account-invoicing
.. i18n:  * Contract management: https://launchpad.net/contract-management
.. i18n:  * OpenERP Fiscal Rule: https://launchpad.net/openerp-fiscal-rules
.. i18n:  * Margin Analysis: https://launchpad.net/margin-analysis
.. i18n:  * Medical in OpenERP : https://launchpad.net/oemedical
.. i18n:  * Construction : https://launchpad.net/openerp-construction
.. i18n:  * Project Management - Invoicing and Reporting: https://launchpad.net/project-reporting
.. i18n:  * Project Management - Services: https://launchpad.net/project-service
.. i18n:  * HR - Timesheet Management: https://launchpad.net/hr-timesheet
.. i18n:  * Hotel Management System on OpenERP : https://launchpad.net/hotel-management-system
.. i18n:  * Department Management: https://launchpad.net/department-mgmt
.. i18n:  * Server Environment And Tools: https://launchpad.net/server-env-tools
.. i18n:  * Webkit Utils: https://launchpad.net/webkit-utils
.. i18n:  * E-Commerce addons: https://launchpad.net/e-commerce-addons
.. i18n:  * Report - Printing and Sending: https://launchpad.net/report-print-send
.. i18n:  * Management Systems : https://launchpad.net/openerp-mgmtsystem
.. i18n:  * Web-Addons for OpenERP : https://launchpad.net/web-addons
.. i18n:  * Geospatial Addons for OpenERP : https://launchpad.net/geospatial-addons
..

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

.. i18n: Some of them are waiting on their owner to bring some modifications so they can fit into other projects (changing team, series,...).
.. i18n: Should you be one of these owners, please inform the others on the mailing-list when ready.
.. i18n: If some refuse to open the projects to the community, it is always possibel to create another project.
..

Some of them are waiting on their owner to bring some modifications so they can fit into other projects (changing team, series,...).
Should you be one of these owners, please inform the others on the mailing-list when ready.
If some refuse to open the projects to the community, it is always possibel to create another project.

.. i18n: Misc Guidelines
.. i18n: +++++++++++++++
..

其他规则
+++++++++++++++

.. i18n: Modules
.. i18n: ^^^^^^^
..

模块
^^^^^^^

.. i18n: Organisation of files in modules
.. i18n: ################################
..

模块中的文件组织
################################

.. i18n: .. === Organisation of files in modules ===
..

.. === Organisation of files in modules ===

.. i18n: The structure of a module should be::
.. i18n: 
.. i18n:  /module_name/
.. i18n:  /module_name/__init__.py
.. i18n:  /module_name/__openerp__.py
.. i18n:  /module_name/i18n
.. i18n:  /module_name/i18n/module_name.pot
.. i18n:  /module_name/images/
.. i18n:  /module_name/images/screenshot.png
.. i18n:  /module_name/migrations
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
.. i18n:  /module_name/security
.. i18n:  /module_name/security/ir.model.access.csv
.. i18n:  /module_name/static/src/img/icon.png
.. i18n:  /module_name/tests
..

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

.. i18n: Security
.. i18n: ########
..

权限
########

.. i18n: Each object defined in your module must have at least one security rule
.. i18n: defined on it to make it accessible.
..

Each object defined in your module must have at least one security rule
defined on it to make it accessible.

.. i18n: Coding Guidelines
.. i18n: #################
..

编码指南
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

总体风格
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

模块
"""""""

.. i18n: Naming Convention
.. i18n: ^^^^^^^^^^^^^^^^^
..

命名惯例
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

必要信息
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

模块描述
^^^^^^^^^^^^^^^^^^^

.. i18n: Dependencies
.. i18n: ^^^^^^^^^^^^
..

描述
^^^^^^^^^^^^

.. i18n: Each module must contain:
..

Each module must contain:

.. i18n:   * A list of dependencies amongst others modules: ['account','sale']
.. i18n: 
.. i18n:   * Provide only highest requirement level, not need to set ['account','base','product','sale']
..

  * A list of dependencies amongst others modules: ['account','sale']

  * Provide only highest requirement level, not need to set ['account','base','product','sale']

.. i18n: Module Content
.. i18n: ^^^^^^^^^^^^^^
..

模块内容
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

.. i18n: Menus
.. i18n: ^^^^^
..

菜单
^^^^^

.. i18n: Naming Menus
.. i18n: ############
..

菜单命名
############

.. i18n:   * Use plural forms: *Customer Invoice*, should be *Customer Invoices*
.. i18n:   * Avoid abbreviations in menus if possible. Example: BoMs -> Bills of Materials
..

  * Use plural forms: *Customer Invoice*, should be *Customer Invoices*
  * Avoid abbreviations in menus if possible. Example: BoMs -> Bills of Materials

.. i18n: Order of the menus
.. i18n: ##################
..

菜单的顺序
##################

.. i18n: The *Reporting* menu is at the bottom of the list, use a sequence=50.
..

The *Reporting* menu is at the bottom of the list, use a sequence=50.

.. i18n: Common Mistakes
.. i18n: ###############
..

常见错误
###############

.. i18n:   * Edit Categories -> Categories
.. i18n:   * List of Categories -> Categories
..

  * Edit Categories -> Categories
  * List of Categories -> Categories

.. i18n: Search Criteria
.. i18n: #################
..

搜索条件
#################

.. i18n: Search criteria: search available on all columns of the list view
..

Search criteria: search available on all columns of the list view

.. i18n: Default Language
.. i18n: ^^^^^^^^^^^^^^^^
..

默认语言
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

字段命名惯例
^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n:   * many2one fields should respect this regex: '.*_id'
.. i18n:   * one2many fields should respect this regex: '.*_ids'
.. i18n:   * one2many relation table should respect this regex: '.*_rel'
.. i18n:   * many2many fields should respect this regex: '.*_ids'
.. i18n:   * use underscore to separate words
.. i18n:   * avoid using uppercase
.. i18n:   * if a field is composed of several words, start with the most important words
..

  * many2one fields should respect this regex: '.*_id'
  * one2many fields should respect this regex: '.*_ids'
  * one2many relation table should respect this regex: '.*_rel'
  * many2many fields should respect this regex: '.*_ids'
  * use underscore to separate words
  * avoid using uppercase
  * if a field is composed of several words, start with the most important words

.. i18n: Model Naming Conventions
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^
..

模型命名惯例
^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: * All objects must start with the name of the module they are defined in.
.. i18n: * If an object is composed of several words, use points to separate words
..

* All objects must start with the name of the module they are defined in.
* If an object is composed of several words, use points to separate words

.. i18n: Terminology
.. i18n: ^^^^^^^^^^^
..

术语
^^^^^^^^^^^

.. i18n:   * All Tree of resources are called *XXX's Structure*, unless a dedicated term exist for the concept
.. i18n: 
.. i18n:     - Good: Location' Structure, Chart of Accounts, Categories' Structure
.. i18n:     - Bad: Tree of Category, Tree of Bill of Materials
..

  * All Tree of resources are called *XXX's Structure*, unless a dedicated term exist for the concept

    - Good: Location' Structure, Chart of Accounts, Categories' Structure
    - Bad: Tree of Category, Tree of Bill of Materials
