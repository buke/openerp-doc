
.. module:: user_ctg
    :synopsis: user_ctg 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/user_ctg"></div>
    <script src="http://js-kit.com/ratings.js"></script>

CTG points Management (*user_ctg*)
==================================

:Module: user_ctg
:Name: CTG points Management
:Version: 0.0.5
:Author: Tiny
:Directory: user_ctg
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

This Module is managed User CTG points (called CTG points as 'Contribution To Growth points') for * DMS: Added CTG points to Document's Author  when sent feedback by other people after downloading document through the DMS * Developments: Added CTG points to Developer  based on LP karma  * Marketing: Added CTG points to Marketing  base on number of incoming visitors on our website * Sales: Added CTG points to Saleman  that sold something and points accordingly to amount sold * Customer Satisfaction: Added CTG points to responsible person of project when customer send feedback for a service/an integration  

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk <http://www.openerp.com/download/modules/trunk/user_ctg.zip>`_ 


Dependencies
------------

  * :mod:`base`
  * :mod:`sale`
  * :mod:`document`
  * :mod:`account_invoice_salesman`
  * :mod:`project`


Reports
-------
None

Menus
-------

None

Views
-----

  * ctg.type.tree (tree)
  * ctg.type.form (form)
  * ctg.line.tree (tree)
  * ctg.line.form (form)
  * \* INHERIT users.inherit.form (form)
  * \* INHERIT users.inherit.form (form)
  * report.ctg.line.tree (tree)
  * report.ctg.line.form (form)
  * CTG Line -Graph (graph)
  * ctg.feedback.tree (tree)
  * ctg.feedback.form (form)
  * user.history.tree (tree)
  * user.history.form (form)


Objects
-------

  * ctg.line
  * report.ctg.line
  * ctg.feedback



