
.. module:: sale_intercompany_auto
    :synopsis: Sale Inter-Company - Fully Automatic 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_intercompany_auto"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Sale Inter-Company - Fully Automatic (*sale_intercompany_auto*)
===============================================================
:Module: sale_intercompany_auto
:Name: Sale Inter-Company - Fully Automatic
:Version: 5.0.1.0
:Author: Tiny
:Directory: sale_intercompany_auto
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This module automatically generates inter-company documents, without
      confirmations or validation steps. When a purchase order is confirmed,
      if the partner exist in one of the company <> from the current one, it
      generates a SO.
  
      Company C1: Sale order -> Purchase Order (MTO)
      Inter-Co : Confirm Purchase Order (C1)
      Inter-Co : Purchase Order (C1) -> Sale Order (C2)
      Inter-Co : Confirm Sale Order (C2)
      Company C2: Continue... picking/production/C3
  
      It also works in cascade if you installed the mrp_jit module.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/sale_intercompany_auto.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/sale_intercompany_auto.zip>`_


Dependencies
------------

 * :mod:`sale`
 * :mod:`purchase`

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

None
