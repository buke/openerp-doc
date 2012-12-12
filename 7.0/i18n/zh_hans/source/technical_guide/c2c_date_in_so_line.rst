
.. i18n: .. module:: c2c_date_in_so_line
.. i18n:     :synopsis: Date in SO lines 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: c2c_date_in_so_line
    :synopsis: Date in SO lines 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_date_in_so_line"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_date_in_so_line"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Date in SO lines (*c2c_date_in_so_line*)
.. i18n: ========================================
.. i18n: :Module: c2c_date_in_so_line
.. i18n: :Name: Date in SO lines
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Camptocamp SA
.. i18n: :Directory: c2c_date_in_so_line
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Date in SO lines (*c2c_date_in_so_line*)
========================================
:Module: c2c_date_in_so_line
:Name: Date in SO lines
:Version: 5.0.1.0
:Author: Camptocamp SA
:Directory: c2c_date_in_so_line
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows to set planned execution date in Sale order
.. i18n:       When the SO is confirmed the delay is automatically computed, you do not have to use 
.. i18n:       day for computing Delivery date of generated picking. If a date is set on the SO, it will automatically be taken in SO line, if not it will recompute a date based on the product customer lead time !!!Warning this module overwrites the SO line product_id_change function and add a parameters in signature. If another module does the same they will conflict
..

::

  This module allows to set planned execution date in Sale order
      When the SO is confirmed the delay is automatically computed, you do not have to use 
      day for computing Delivery date of generated picking. If a date is set on the SO, it will automatically be taken in SO line, if not it will recompute a date based on the product customer lead time !!!Warning this module overwrites the SO line product_id_change function and add a parameters in signature. If another module does the same they will conflict

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n: (No download links available)
..

(No download links available)

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`sale`
..

 * :mod:`base`
 * :mod:`sale`

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

.. i18n:  * \* INHERIT sale.order.form (form)
.. i18n:  * \* INHERIT sale.order.form (form)
.. i18n:  * \* INHERIT sale.order.form (form)
..

 * \* INHERIT sale.order.form (form)
 * \* INHERIT sale.order.form (form)
 * \* INHERIT sale.order.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
