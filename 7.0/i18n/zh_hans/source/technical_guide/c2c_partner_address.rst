
.. i18n: .. module:: c2c_partner_address
.. i18n:     :synopsis: C2C partner address 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: c2c_partner_address
    :synopsis: C2C partner address 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_partner_address"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_partner_address"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: C2C partner address (*c2c_partner_address*)
.. i18n: ===========================================
.. i18n: :Module: c2c_partner_address
.. i18n: :Name: C2C partner address
.. i18n: :Version: 5.0.1.2
.. i18n: :Author: Camptocamp
.. i18n: :Directory: c2c_partner_address
.. i18n: :Web: http://www.camptocamp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

C2C partner address (*c2c_partner_address*)
===========================================
:Module: c2c_partner_address
:Name: C2C partner address
:Version: 5.0.1.2
:Author: Camptocamp
:Directory: c2c_partner_address
:Web: http://www.camptocamp.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Add fields on address and categories 
.. i18n:       to be more compatible with 
.. i18n:       LDAP and Active Directory.
.. i18n:       Add commodities for addresses input.
..

::

  Add fields on address and categories 
      to be more compatible with 
      LDAP and Active Directory.
      Add commodities for addresses input.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_partner_address.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_partner_address.zip>`_

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

.. i18n:  * Partners/Configuration/Address categories/Address category's Structure
.. i18n:  * Partners/Contact by address category
.. i18n:  * Partners/Configuration/Address categories/Edit adresses categories
..

 * Partners/Configuration/Address categories/Address category's Structure
 * Partners/Contact by address category
 * Partners/Configuration/Address categories/Edit adresses categories

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT res.partner.address.form1.c2c_partner_adress (form)
.. i18n:  * \* INHERIT res.partner.address.form1.c2c_partner_adress (form)
.. i18n:  * \* INHERIT res.partner.address.form2_c2c_partner_address (form)
.. i18n:  * \* INHERIT res.partner.address.form2_c2c_partner_address (form)
.. i18n:  * res.partner.address.category.form (form)
.. i18n:  * res.partner.address.category.list (tree)
.. i18n:  * res.partner.address.category.tree (tree)
..

 * \* INHERIT res.partner.address.form1.c2c_partner_adress (form)
 * \* INHERIT res.partner.address.form1.c2c_partner_adress (form)
 * \* INHERIT res.partner.address.form2_c2c_partner_address (form)
 * \* INHERIT res.partner.address.form2_c2c_partner_address (form)
 * res.partner.address.category.form (form)
 * res.partner.address.category.list (tree)
 * res.partner.address.category.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Partner address Categories (res.partner.address.category)
.. i18n: #################################################################
..

Object: Partner address Categories (res.partner.address.category)
#################################################################

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :parent_id: Parent Category, many2one
..

:parent_id: Parent Category, many2one

.. i18n: :child_ids: Childs Category, one2many
..

:child_ids: Childs Category, one2many

.. i18n: :complete_name: Name, char, readonly
..

:complete_name: Name, char, readonly

.. i18n: :name: Category Name, char, required
..

:name: Category Name, char, required
