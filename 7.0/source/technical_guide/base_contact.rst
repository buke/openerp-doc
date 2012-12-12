
.. module:: base_contact
    :synopsis: Base Contact (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_contact"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Base Contact (*base_contact*)
=============================
:Module: base_contact
:Name: Base Contact
:Version: 5.0.1.0
:Author: Tiny
:Directory: base_contact
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module allows you to manage entirely your contacts.
  
      It lets you define
          *contacts unrelated to a partner,
          *contacts working at several addresses (possibly for different partners),
          *contacts with possibly different functions for each of its job's addresses
  
      It also add new menu items located in
          Partners \ Contacts
          Partners \ Functions
  
      Pay attention that this module converts the existing addresses into "addresses + contacts". It means that some fields of the addresses will be missing (like the contact name), since these are supposed to be defined in an other object.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/base_contact.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/base_contact.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`process`

Reports
-------

None


Menus
-------

 * Partners/Contacts
 * Partners/Contact's Jobs

Views
-----

 * res.partner.contact.tree (tree)
 * res.partner.contact.form (form)
 * \* INHERIT Partner form inherited (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT Partner addresses inherited (tree)
 * \* INHERIT res.partner.address.form.inherited0 (form)
 * \* INHERIT res.partner.address.form.inherited1 (form)
 * \* INHERIT res.partner.address.form.inherited2 (form)
 * \* INHERIT res.partner.address.form.inherited3 (form)
 * \* INHERIT res.partner.address.form.inherited4 (form)
 * \* INHERIT res.partner.address.form.inherited6 (form)
 * \* INHERIT res.partner.address.form.inherited5 (form)
 * res.partner.job.tree (tree)
 * res.partner.job.form (form)


Objects
-------

Object: res.partner.contact (res.partner.contact)
#################################################



:website: Website, char





:first_name: First Name, char





:job_id: Main Job, many2one, readonly





:title: Title, selection





:mobile: Mobile, char





:country_id: Nationality, many2one





:birthdate: Birth Date, date





:job_ids: Functions and Addresses, one2many





:lang_id: Language, many2one





:active: Active, boolean





:function_id: Main Function, many2one





:partner_id: Main Employer, many2one





:email: E-Mail, char





:name: Last Name, char, required




Object: Contact Partner Function (res.partner.job)
##################################################



:sequence_partner: Partner Seq., integer

    *Order of importance of this job title in the list of job title of the linked partner*



:sequence_contact: Contact Seq., integer

    *Order of importance of this address in the list of addresses of the linked contact*



:fax: Fax, char





:name: Partner, many2one





:extension: Extension, char

    *Internal/External extension phone number*



:date_start: Date Start, date





:address_id: Address, many2one





:contact_id: Contact, many2one, required





:email: E-Mail, char





:phone: Phone, char





:state: State, selection, required





:date_stop: Date Stop, date





:function_id: Partner Function, many2one





:other: Other, char

    *Additional phone field*
