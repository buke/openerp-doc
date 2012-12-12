
.. module:: cci_base_contact
    :synopsis: CCI Base Contact 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_base_contact"></div>
    <script src="http://js-kit.com/ratings.js"></script>

CCI Base Contact (*cci_base_contact*)
=====================================
:Module: cci_base_contact
:Name: CCI Base Contact
:Version: 5.0.1.0
:Author: Tiny
:Directory: cci_base_contact
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  specific module for cci project which will inherit
          base_contact module..

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/cci_base_contact.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/cci_base_contact.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`base_contact`
 * :mod:`project`

Reports
-------

None


Menus
-------

 * Partners/Configuration/Link Type
 * Partners/Configuration/Link Type/Contact Link Type

Views
-----

 * res.partner.country.relation.tree (tree)
 * res.partner.country.relation.form (form)
 * \* INHERIT res.partner.contact.tree2 (tree)
 * \* INHERIT res.partner.contact.form (form)
 * \* INHERIT res.partner.contact.form (form)
 * \* INHERIT res.partner.contact.form (form)
 * \* INHERIT res.partner.contact.form (form)
 * res.partner.contact.link.type.tree (tree)
 * res.partner.contact.link.type.form (form)
 * \* INHERIT project.project.form.inherit (form)
 * \* INHERIT res.partner.job.form.inherit (form)


Objects
-------

Object: res.partner.contact.link.type (res.partner.contact.link.type)
#####################################################################



:name: Name, char, required




Object: res.partner.contact.link (res.partner.contact.link)
###########################################################



:current_contact_id: Current contact, many2one, required





:name: Name, char, required





:contact_id: Contact, many2one, required





:type_id: Type, many2one, required


