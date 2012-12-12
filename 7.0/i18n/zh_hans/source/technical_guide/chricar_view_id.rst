
.. i18n: .. module:: chricar_view_id
.. i18n:     :synopsis: ChriCar unique View ID 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: chricar_view_id
    :synopsis: ChriCar unique View ID 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/chricar_view_id"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/chricar_view_id"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: ChriCar unique View ID (*chricar_view_id*)
.. i18n: ==========================================
.. i18n: :Module: chricar_view_id
.. i18n: :Name: ChriCar unique View ID
.. i18n: :Version: 5.0.0.2
.. i18n: :Author: Network Gulf IT - India
.. i18n: :Directory: chricar_view_id
.. i18n: :Web: http://www.chricar.at/ChriCar/index.html
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

ChriCar unique View ID (*chricar_view_id*)
==========================================
:Module: chricar_view_id
:Name: ChriCar unique View ID
:Version: 5.0.0.2
:Author: Network Gulf IT - India
:Directory: chricar_view_id
:Web: http://www.chricar.at/ChriCar/index.html
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module is funded by
.. i18n:   ChriCar Beteiligungs- und Beratungs- GmbH
.. i18n:   http://www.chricar.at/ChriCar/index.html
.. i18n:   
.. i18n:   Developed by
.. i18n:   Network Gulf IT - India
.. i18n:   http://www.networkgulf.com/
.. i18n:   
.. i18n:   usage: get_id('your_view_name',param1,param2,param3,param4)
.. i18n:   this function will always return the SAME unique id for a 
.. i18n:   certain combination of parameters for a view.
.. i18n:   
.. i18n:   Hint 1: You do not need this function if the unique ID can be easily 
.. i18n:   calculated during the grouping. Example
.. i18n:   - easy: group by product_id
.. i18n:   - more complex: group by account_id, period_id
.. i18n:   - very complex: group by account_id, period_id, currency_id
.. i18n:   
.. i18n:   Hint 2: for large tables (100000 rec)  
.. i18n:   performance gain of factor 10x and more
.. i18n:   split the grouping operation and the get_id into 2 views
.. i18n:   
.. i18n:   slow:
.. i18n:   select get_id(tablename,param1,param2,...), param1, param2, ... sum(field1), ...
.. i18n:   from
.. i18n:   group by get_id(tablename,param1,param2,...) ,param1,param2,...
.. i18n:   
.. i18n:   fast:
.. i18n:   1) view1: 
.. i18n:   select ....
.. i18n:   from
.. i18n:   group by param1,param2,...
.. i18n:   2) view 2
.. i18n:   select get_id('view1',param1,param2,...),* from view1;
.. i18n:   (no group by here)
..

::

  This module is funded by
  ChriCar Beteiligungs- und Beratungs- GmbH
  http://www.chricar.at/ChriCar/index.html
  
  Developed by
  Network Gulf IT - India
  http://www.networkgulf.com/
  
  usage: get_id('your_view_name',param1,param2,param3,param4)
  this function will always return the SAME unique id for a 
  certain combination of parameters for a view.
  
  Hint 1: You do not need this function if the unique ID can be easily 
  calculated during the grouping. Example
  - easy: group by product_id
  - more complex: group by account_id, period_id
  - very complex: group by account_id, period_id, currency_id
  
  Hint 2: for large tables (100000 rec)  
  performance gain of factor 10x and more
  split the grouping operation and the get_id into 2 views
  
  slow:
  select get_id(tablename,param1,param2,...), param1, param2, ... sum(field1), ...
  from
  group by get_id(tablename,param1,param2,...) ,param1,param2,...
  
  fast:
  1) view1: 
  select ....
  from
  group by param1,param2,...
  2) view 2
  select get_id('view1',param1,param2,...),* from view1;
  (no group by here)

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
..

 * :mod:`base`

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

.. i18n: None
..

None

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: chricar_view_id (chricar_view_id)
.. i18n: #########################################
..

Object: chricar_view_id (chricar_view_id)
#########################################

.. i18n: :name: Name, char
..

:name: Name, char
