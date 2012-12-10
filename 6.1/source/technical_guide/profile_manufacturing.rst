
.. i18n: .. module:: profile_manufacturing
.. i18n:     :synopsis: Manufacturing industry profile (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: profile_manufacturing
    :synopsis: Manufacturing industry profile (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:       <br />
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />
..

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: .. tip:: This module is part of the OpenERP software, the leading Open Source 
.. i18n:   enterprise management system. If you want to discover OpenERP, check our 
.. i18n:   `screencasts <http://openerp.tv>`_ or download 
.. i18n:   `OpenERP <http://openerp.com>`_ directly.
..

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/profile_manufacturing"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/profile_manufacturing"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Manufacturing industry profile (*profile_manufacturing*)
.. i18n: ========================================================
.. i18n: :Module: profile_manufacturing
.. i18n: :Name: Manufacturing industry profile
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: profile_manufacturing
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Profile for manufacturing industries
..

::

  Profile for manufacturing industries

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/profile_manufacturing.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/profile_manufacturing.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/profile_manufacturing.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/profile_manufacturing.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/profile_manufacturing.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/profile_manufacturing.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`mrp`
.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`delivery`
.. i18n:  * :mod:`board_manufacturing`
.. i18n:  * :mod:`product_margin`
.. i18n:  * :mod:`sale_delivery_report`
..

 * :mod:`mrp`
 * :mod:`sale`
 * :mod:`delivery`
 * :mod:`board_manufacturing`
 * :mod:`product_margin`
 * :mod:`sale_delivery_report`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n: None
..

None

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n: None
..

None

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * Manufacturing Profile: Install Extra Modules (form)
..

 * Manufacturing Profile: Install Extra Modules (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: profile.manufacturing.config.install_modules_wizard (profile.manufacturing.config.install_modules_wizard)
.. i18n: #################################################################################################################
..

Object: profile.manufacturing.config.install_modules_wizard (profile.manufacturing.config.install_modules_wizard)
#################################################################################################################

.. i18n: :mrp_repair: Repair, boolean
..

:mrp_repair: Repair, boolean

.. i18n:     *Allow to manage product repairs. Handle the guarantee limit date and the invoicing of products and services.*
..

    *Allow to manage product repairs. Handle the guarantee limit date and the invoicing of products and services.*

.. i18n: :mrp_jit: Just in Time Scheduling, boolean
..

:mrp_jit: Just in Time Scheduling, boolean

.. i18n:     *The JIT module allows you to not run the scheduler periodically. It's easier and faster for real time stock computation but, in counter-part, it manages less efficiently priorities in procurements.*
..

    *The JIT module allows you to not run the scheduler periodically. It's easier and faster for real time stock computation but, in counter-part, it manages less efficiently priorities in procurements.*

.. i18n: :sale_journal: Manage by Journals, boolean
..

:sale_journal: Manage by Journals, boolean

.. i18n:     *This module  allows you to manage your sales, invoicing and picking by journals. You can define journals for trucks, salesman, departments, invoicing date delivery period, etc.*
..

    *This module  allows you to manage your sales, invoicing and picking by journals. You can define journals for trucks, salesman, departments, invoicing date delivery period, etc.*

.. i18n: :mrp_subproduct: Mrp Sub Product, boolean
..

:mrp_subproduct: Mrp Sub Product, boolean

.. i18n:     *This module allows you to add sub-products in mrp bom.*
..

    *This module allows you to add sub-products in mrp bom.*

.. i18n: :sale_margin: Margins on Sales Order, boolean
..

:sale_margin: Margins on Sales Order, boolean

.. i18n:     *Display margins on the sale order form.*
..

    *Display margins on the sale order form.*

.. i18n: :stock_location: Advanced Locations, boolean
..

:stock_location: Advanced Locations, boolean

.. i18n:     *Allows you to manage an advanced logistic with different locations. You can define, by product: default locations, path of locations for different operations, etc. This module is often used for: localisation of products, managing a manufacturing chain, a quality control location, product that you rent, etc.*
..

    *Allows you to manage an advanced logistic with different locations. You can define, by product: default locations, path of locations for different operations, etc. This module is often used for: localisation of products, managing a manufacturing chain, a quality control location, product that you rent, etc.*

.. i18n: :warning: Warning, boolean
..

:warning: Warning, boolean

.. i18n:     *Able you to set warnings on products and partners.*
..

    *Able you to set warnings on products and partners.*

.. i18n: :portal: Portal, boolean
..

:portal: Portal, boolean

.. i18n:     *This module allows you to manage a Portal system.*
..

    *This module allows you to manage a Portal system.*

.. i18n: :point_of_sale: Point of Sale, boolean
..

:point_of_sale: Point of Sale, boolean

.. i18n:     *This module allows you to manage a point of sale system. It offers a basic form for pos operations. You must also check our frontend point of sale for a perfect interface with touchscreen materials and payment processing hardware.*
..

    *This module allows you to manage a point of sale system. It offers a basic form for pos operations. You must also check our frontend point of sale for a perfect interface with touchscreen materials and payment processing hardware.*

.. i18n: :sale_crm: CRM and Calendars, boolean
..

:sale_crm: CRM and Calendars, boolean

.. i18n:     *This installs the customer relationship features like: leads and opportunities tracking, shared calendar, jobs tracking, bug tracker, and so on.*
..

    *This installs the customer relationship features like: leads and opportunities tracking, shared calendar, jobs tracking, bug tracker, and so on.*

.. i18n: :mrp_operation: Manufacturing Operations, boolean
..

:mrp_operation: Manufacturing Operations, boolean

.. i18n:     *This module allows you to not only manage by production order but also by work order/operation. You will be able to plan, analyse the cost, check times, ... on all operations of each manufacturing order*
..

    *This module allows you to not only manage by production order but also by work order/operation. You will be able to plan, analyse the cost, check times, ... on all operations of each manufacturing order*

.. i18n: :board_document: Document Management, boolean
..

:board_document: Document Management, boolean

.. i18n:     *The Document Management System of OpenERP allows you to store, browse, automatically index, search and preview all kind of documents (internal documents, printed reports, calendar system). It opens an FTP access for the users to easily browse association's document.*
..

    *The Document Management System of OpenERP allows you to store, browse, automatically index, search and preview all kind of documents (internal documents, printed reports, calendar system). It opens an FTP access for the users to easily browse association's document.*
