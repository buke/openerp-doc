
.. i18n: .. module:: product_index
.. i18n:     :synopsis: Manage indexes on products prices 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: product_index
    :synopsis: Manage indexes on products prices 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_index"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_index"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Manage indexes on products prices (*product_index*)
.. i18n: ===================================================
.. i18n: :Module: product_index
.. i18n: :Name: Manage indexes on products prices
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: product_index
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Manage indexes on products prices (*product_index*)
===================================================
:Module: product_index
:Name: Manage indexes on products prices
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_index
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   None
..

::

  None

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/product_index.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/product_index.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_index.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_index.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`product`
..

 * :mod:`product`

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

.. i18n:  * Products/Configuration/Indexes
.. i18n:  * Products/Configuration/Indexes/New index
..

 * Products/Configuration/Indexes
 * Products/Configuration/Indexes/New index

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * product.index.tree (tree)
.. i18n:  * product.index.form (form)
.. i18n:  * \* INHERIT product.normal.form (form)
..

 * product.index.tree (tree)
 * product.index.form (form)
 * \* INHERIT product.normal.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Index (product.index)
.. i18n: #############################
..

Object: Index (product.index)
#############################

.. i18n: :rate_ids: Rates, one2many
..

:rate_ids: Rates, one2many

.. i18n: :code: Index code, char
..

:code: Index code, char

.. i18n: :name: Index name, char, required
..

:name: Index name, char, required

.. i18n: :rounding: Rounding factor, float
..

:rounding: Rounding factor, float

.. i18n: :rate: Current rate, float, readonly
..

:rate: Current rate, float, readonly

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: Object: Index Rate (product.index.rate)
.. i18n: #######################################
..

Object: Index Rate (product.index.rate)
#######################################

.. i18n: :rate: Rate, float, required
..

:rate: Rate, float, required

.. i18n: :index_id: index, many2one, readonly
..

:index_id: index, many2one, readonly

.. i18n: :name: Date, date, required
..

:name: Date, date, required
