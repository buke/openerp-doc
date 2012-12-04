
.. module:: base_partner_relation
    :synopsis: Partners - relation extension 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_partner_relation"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Partners - relation extension (*base_partner_relation*)
=======================================================
:Module: base_partner_relation
:Name: Partners - relation extension
:Version: 5.0.1.0
:Author: Tiny
:Directory: base_partner_relation
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Add a tab in the partner form to encode relations between several partners.
      For eg, the partner 'Toubib and Co.' has different contacts.
      When 'Toubib and Co.' orders, you have to deliver to 'Toubib - Belgium'
      and invoice to 'Toubib - Geneva'.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/base_partner_relation.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/base_partner_relation.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/base_partner_relation.zip>`_


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

 * res.partner.relation.form (form)
 * res.partner.relation.tree (tree)
 * \* INHERIT res.partner.form.inherit (form)


Objects
-------

Object: Partner Relation (res.partner.relation)
###############################################



:partner_id: Main Partner, many2one, required





:name: Relation Type, selection, required





:relation_id: Relation Partner, many2one, required


