
.. module:: chricar_view_id
    :synopsis: ChriCar unique View ID 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/chricar_view_id"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

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

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------


None


Views
-----


None



Objects
-------

Object: chricar_view_id (chricar_view_id)
#########################################



:name: Name, char


