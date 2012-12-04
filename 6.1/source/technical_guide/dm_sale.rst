
.. module:: dm_sale
    :synopsis: dm_sale 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/dm_sale"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Sales Management for DM (*dm_sale*)
===================================

:Module: dm_sale
:Name: Sales Management for DM
:Version: 0.1
:Author: Tiny
:Directory: dm_sale
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

             This module adds sales management for Direct Marketing.             

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk <http://www.openerp.com/download/modules/trunk/dm_sale.zip>`_ 


Dependencies
------------

  * :mod:`dm`


Reports
-------
None

Menus
-------

None

Views
-----

  * \* INHERIT sale.order.form.inherit (form)
  * \* INHERIT dm.workitem.form.inherit (form)
  * \* INHERIT dm.offer.step.form.inherit (form)
  * dm.event.sale.tree (tree)
  * dm.event.sale.form (form)
  * \* INHERIT dm.campaign.proposition.form.inherit (form)


Objects
-------

  * dm.event.sale



