
.. i18n: .. module:: lunch
.. i18n:     :synopsis: Lunch Module 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: lunch
    :synopsis: Lunch Module 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/lunch"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/lunch"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Lunch Module (*lunch*)
.. i18n: ======================
.. i18n: :Module: lunch
.. i18n: :Name: Lunch Module
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Tiny
.. i18n: :Directory: lunch
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Lunch Module (*lunch*)
======================
:Module: lunch
:Name: Lunch Module
:Version: 5.0.0.1
:Author: Tiny
:Directory: lunch
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

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/lunch.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/lunch.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/lunch.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/lunch.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
..

 * :mod:`base`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Print Order
..

 * Print Order

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Tools
.. i18n:  * Tools/Lunch
.. i18n:  * Tools/Lunch/Configuration
.. i18n:  * Tools/Lunch/Make order
.. i18n:  * Tools/Lunch/Make order/Order of the day
.. i18n:  * Tools/Lunch/Configuration/CashBox
.. i18n:  * Tools/Lunch/Cash Moves
.. i18n:  * Tools/Lunch/Configuration/Products
.. i18n:  * Tools/Lunch/Configuration/Products/Category of product
.. i18n:  * Tools/Lunch/Box Amount by User
..

 * Tools
 * Tools/Lunch
 * Tools/Lunch/Configuration
 * Tools/Lunch/Make order
 * Tools/Lunch/Make order/Order of the day
 * Tools/Lunch/Configuration/CashBox
 * Tools/Lunch/Cash Moves
 * Tools/Lunch/Configuration/Products
 * Tools/Lunch/Configuration/Products/Category of product
 * Tools/Lunch/Box Amount by User

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * Order (form)
.. i18n:  * Order (tree)
.. i18n:  * CashBox (form)
.. i18n:  * CashBox (tree)
.. i18n:  * CashMove (form)
.. i18n:  * CashMove (tree)
.. i18n:  *  Category of product  (form)
.. i18n:  * Category (tree)
.. i18n:  * Products (form)
.. i18n:  * Products (tree)
.. i18n:  * Lunch amount (tree)
.. i18n:  * Lunch amount (form)
..

 * Order (form)
 * Order (tree)
 * CashBox (form)
 * CashBox (tree)
 * CashMove (form)
 * CashMove (tree)
 *  Category of product  (form)
 * Category (tree)
 * Products (form)
 * Products (tree)
 * Lunch amount (tree)
 * Lunch amount (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Category (lunch.category)
.. i18n: #################################
..

Object: Category (lunch.category)
#################################

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: lunch.product (lunch.product)
.. i18n: #####################################
..

Object: lunch.product (lunch.product)
#####################################

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :price: Price, float
..

:price: Price, float

.. i18n: :category_id: Category, selection
..

:category_id: Category, selection

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :description: Description, char
..

:description: Description, char

.. i18n: Object: lunch.cashbox (lunch.cashbox)
.. i18n: #####################################
..

Object: lunch.cashbox (lunch.cashbox)
#####################################

.. i18n: :manager: Manager, many2one
..

:manager: Manager, many2one

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :sum_remain: Remained Total, float, readonly
..

:sum_remain: Remained Total, float, readonly

.. i18n: Object: lunch.cashmove (lunch.cashmove)
.. i18n: #######################################
..

Object: lunch.cashmove (lunch.cashmove)
#######################################

.. i18n: :box: Box Name, many2one, required
..

:box: Box Name, many2one, required

.. i18n: :create_date: Created date, datetime, readonly
..

:create_date: Created date, datetime, readonly

.. i18n: :name: Name, char
..

:name: Name, char

.. i18n: :user_cashmove: User Name, many2one, required
..

:user_cashmove: User Name, many2one, required

.. i18n: :amount: Amount, float
..

:amount: Amount, float

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: Object: lunch.order (lunch.order)
.. i18n: #################################
..

Object: lunch.order (lunch.order)
#################################

.. i18n: :product: Product, many2one, required, readonly
..

:product: Product, many2one, required, readonly

.. i18n: :user_id: User Name, many2one, required, readonly
..

:user_id: User Name, many2one, required, readonly

.. i18n: :price: Price, float, readonly
..

:price: Price, float, readonly

.. i18n: :descript: Description Order, char, readonly
..

:descript: Description Order, char, readonly

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :date: Date, date, readonly
..

:date: Date, date, readonly

.. i18n: :cashmove: CashMove, many2one, readonly
..

:cashmove: CashMove, many2one, readonly

.. i18n: Object: Amount available by user and box (report.lunch.amount)
.. i18n: ##############################################################
..

Object: Amount available by user and box (report.lunch.amount)
##############################################################

.. i18n: :box: Box Name, many2one, readonly
..

:box: Box Name, many2one, readonly

.. i18n: :amount: Amount, float, readonly
..

:amount: Amount, float, readonly

.. i18n: :user_id: User Name, many2one, readonly
..

:user_id: User Name, many2one, readonly
