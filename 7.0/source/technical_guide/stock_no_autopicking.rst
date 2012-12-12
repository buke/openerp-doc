
.. module:: stock_no_autopicking
    :synopsis: Stock No Auto-Picking (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/stock_no_autopicking"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Stock No Auto-Picking (*stock_no_autopicking*)
==============================================
:Module: stock_no_autopicking
:Name: Stock No Auto-Picking
:Version: 5.0.1.0
:Author: Tiny
:Directory: stock_no_autopicking
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module allows an intermediate picking process to provide raw materials
      to production orders.
  
      One example of usage of this module is to manage production made by your
      suppliers (sub-contracting). To achieve this, set the assembled product
      which is sub-contracted to "No Auto-Picking" and put the location of the
      supplier in the routing of the assembly operation.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/stock_no_autopicking.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/stock_no_autopicking.zip>`_


Dependencies
------------

 * :mod:`mrp`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT product.normal.auto_pick.form (form)


Objects
-------

None
