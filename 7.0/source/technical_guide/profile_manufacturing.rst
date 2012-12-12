
.. module:: profile_manufacturing
    :synopsis: Manufacturing industry profile (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/profile_manufacturing"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Manufacturing industry profile (*profile_manufacturing*)
========================================================
:Module: profile_manufacturing
:Name: Manufacturing industry profile
:Version: 5.0.1.0
:Author: Tiny
:Directory: profile_manufacturing
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Profile for manufacturing industries

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/profile_manufacturing.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/profile_manufacturing.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/profile_manufacturing.zip>`_


Dependencies
------------

 * :mod:`mrp`
 * :mod:`sale`
 * :mod:`delivery`
 * :mod:`board_manufacturing`
 * :mod:`product_margin`
 * :mod:`sale_delivery_report`

Reports
-------

None


Menus
-------


None


Views
-----

 * Manufacturing Profile: Install Extra Modules (form)


Objects
-------

Object: profile.manufacturing.config.install_modules_wizard (profile.manufacturing.config.install_modules_wizard)
#################################################################################################################



:mrp_repair: Repair, boolean

    *Allow to manage product repairs. Handle the guarantee limit date and the invoicing of products and services.*



:mrp_jit: Just in Time Scheduling, boolean

    *The JIT module allows you to not run the scheduler periodically. It's easier and faster for real time stock computation but, in counter-part, it manages less efficiently priorities in procurements.*



:sale_journal: Manage by Journals, boolean

    *This module  allows you to manage your sales, invoicing and picking by journals. You can define journals for trucks, salesman, departments, invoicing date delivery period, etc.*



:mrp_subproduct: Mrp Sub Product, boolean

    *This module allows you to add sub-products in mrp bom.*



:sale_margin: Margins on Sales Order, boolean

    *Display margins on the sale order form.*



:stock_location: Advanced Locations, boolean

    *Allows you to manage an advanced logistic with different locations. You can define, by product: default locations, path of locations for different operations, etc. This module is often used for: localisation of products, managing a manufacturing chain, a quality control location, product that you rent, etc.*



:warning: Warning, boolean

    *Able you to set warnings on products and partners.*



:portal: Portal, boolean

    *This module allows you to manage a Portal system.*



:point_of_sale: Point of Sale, boolean

    *This module allows you to manage a point of sale system. It offers a basic form for pos operations. You must also check our frontend point of sale for a perfect interface with touchscreen materials and payment processing hardware.*



:sale_crm: CRM and Calendars, boolean

    *This installs the customer relationship features like: leads and opportunities tracking, shared calendar, jobs tracking, bug tracker, and so on.*



:mrp_operation: Manufacturing Operations, boolean

    *This module allows you to not only manage by production order but also by work order/operation. You will be able to plan, analyse the cost, check times, ... on all operations of each manufacturing order*



:board_document: Document Management, boolean

    *The Document Management System of OpenERP allows you to store, browse, automatically index, search and preview all kind of documents (internal documents, printed reports, calendar system). It opens an FTP access for the users to easily browse association's document.*
