
.. module:: c2c_partner_address
    :synopsis: C2C partner address 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_partner_address"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  Add fields on address and categories 
      to be more compatible with 
      LDAP and Active Directory.
      Add commodities for addresses input.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_partner_address.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Partners/Configuration/Address categories/Address category's Structure
 * Partners/Contact by address category
 * Partners/Configuration/Address categories/Edit adresses categories

Views
-----

 * \* INHERIT res.partner.address.form1.c2c_partner_adress (form)
 * \* INHERIT res.partner.address.form1.c2c_partner_adress (form)
 * \* INHERIT res.partner.address.form2_c2c_partner_address (form)
 * \* INHERIT res.partner.address.form2_c2c_partner_address (form)
 * res.partner.address.category.form (form)
 * res.partner.address.category.list (tree)
 * res.partner.address.category.tree (tree)


Objects
-------

Object: Partner address Categories (res.partner.address.category)
#################################################################



:active: Active, boolean





:parent_id: Parent Category, many2one





:child_ids: Childs Category, one2many





:complete_name: Name, char, readonly





:name: Category Name, char, required


