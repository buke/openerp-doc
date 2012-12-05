
.. i18n: .. module:: base_partner_relation
.. i18n:     :synopsis: Partners - relation extension 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: base_partner_relation
    :synopsis: Partners - relation extension 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_partner_relation"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_partner_relation"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Partners - relation extension (*base_partner_relation*)
.. i18n: =======================================================
.. i18n: :Module: base_partner_relation
.. i18n: :Name: Partners - relation extension
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: base_partner_relation
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Add a tab in the partner form to encode relations between several partners.
.. i18n:       For eg, the partner 'Toubib and Co.' has different contacts.
.. i18n:       When 'Toubib and Co.' orders, you have to deliver to 'Toubib - Belgium'
.. i18n:       and invoice to 'Toubib - Geneva'.
..

::

  Add a tab in the partner form to encode relations between several partners.
      For eg, the partner 'Toubib and Co.' has different contacts.
      When 'Toubib and Co.' orders, you have to deliver to 'Toubib - Belgium'
      and invoice to 'Toubib - Geneva'.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/base_partner_relation.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/base_partner_relation.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/base_partner_relation.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/base_partner_relation.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/base_partner_relation.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/base_partner_relation.zip>`_

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

.. i18n:  * res.partner.relation.form (form)
.. i18n:  * res.partner.relation.tree (tree)
.. i18n:  * \* INHERIT res.partner.form.inherit (form)
..

 * res.partner.relation.form (form)
 * res.partner.relation.tree (tree)
 * \* INHERIT res.partner.form.inherit (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Partner Relation (res.partner.relation)
.. i18n: ###############################################
..

Object: Partner Relation (res.partner.relation)
###############################################

.. i18n: :partner_id: Main Partner, many2one, required
..

:partner_id: Main Partner, many2one, required

.. i18n: :name: Relation Type, selection, required
..

:name: Relation Type, selection, required

.. i18n: :relation_id: Relation Partner, many2one, required
..

:relation_id: Relation Partner, many2one, required
