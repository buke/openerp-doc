
.. module:: portal_training
    :synopsis: Training Portal 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/portal_training"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Training Portal (*portal_training*)
===================================
:Module: portal_training
:Name: Training Portal
:Version: 5.0.0.0.1
:Author: Tiny SPRL
:Directory: portal_training
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Training Portals

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/portal_training.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/portal_training.zip>`_


Dependencies
------------

 * :mod:`portal`
 * :mod:`board`
 * :mod:`training`

Reports
-------

None


Menus
-------

 * Portal/Training Portals
 * Portal/Training Portals/Supplier Portal
 * Portal/Training Portals/Supplier Portal/Purchase Management
 * Portal/Training Portals/Supplier Portal/Purchase Management/Your Purchase Order Lines
 * Portal/Training Portals/Supplier Portal/Training Management
 * Portal/Training Portals/Supplier Portal/Training Management/Seances
 * Portal/Training Portals/Partner Portal
 * Portal/Training Portals/Partner Portal/Training Management
 * Portal/Training Portals/Partner Portal/Training Management/Subscriptions
 * Portal/Training Portals/Partner Portal/Training Management/Subscriptions/New Subscription
 * Portal/Training Portals/Partner Portal/Survey
 * Portal/Training Portals/Partner Portal/Survey/Old Subscriptions
 * Portal/Training Portals/Partner Portal/Financial Management
 * Portal/Training Portals/Partner Portal/Financial Management/Customer Invoices
 * Portal/Training Portals/SkateHolder Portal
 * Portal/Training Portals/SkateHolder Portal/Training Management
 * Portal/Training Portals/SkateHolder Portal/Training Management/Participations of the Participants
 * Portal/Training Portals/SkateHolder Portal/Training Management/Evaluation Form

Views
-----

 * purchase.order.line.form.portal (form)
 * view.portal.supplier.training.seance.list (tree)
 * view.portal.partner.subscription.tree (tree)
 * board.portal.training.supplier (form)


Objects
-------

Object: portal.training.subscription (portal.training.subscription)
###################################################################



:session_id: Session, many2one, readonly





:note: Note, text, readonly





:course_id: Course, many2one, readonly





:contact_id: Contact, many2one, readonly





:seance_id: Seance, many2one, readonly





:date: Date, date, readonly





:examen: Is Examen, boolean, readonly





:partner_id: Partner, many2one, readonly


