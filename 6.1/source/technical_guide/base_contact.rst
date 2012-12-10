
.. i18n: .. module:: base_contact
.. i18n:     :synopsis: Base Contact (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: base_contact
    :synopsis: Base Contact (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_contact"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_contact"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Base Contact (*base_contact*)
.. i18n: =============================
.. i18n: :Module: base_contact
.. i18n: :Name: Base Contact
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: base_contact
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows you to manage entirely your contacts.
.. i18n:   
.. i18n:       It lets you define
.. i18n:           *contacts unrelated to a partner,
.. i18n:           *contacts working at several addresses (possibly for different partners),
.. i18n:           *contacts with possibly different functions for each of its job's addresses
.. i18n:   
.. i18n:       It also add new menu items located in
.. i18n:           Partners \ Contacts
.. i18n:           Partners \ Functions
.. i18n:   
.. i18n:       Pay attention that this module converts the existing addresses into "addresses + contacts". It means that some fields of the addresses will be missing (like the contact name), since these are supposed to be defined in an other object.
..

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

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/base_contact.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/base_contact.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/base_contact.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/base_contact.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`process`
..

 * :mod:`base`
 * :mod:`process`

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

.. i18n:  * Partners/Contacts
.. i18n:  * Partners/Contact's Jobs
..

 * Partners/Contacts
 * Partners/Contact's Jobs

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * res.partner.contact.tree (tree)
.. i18n:  * res.partner.contact.form (form)
.. i18n:  * \* INHERIT Partner form inherited (form)
.. i18n:  * \* INHERIT res.partner.form (form)
.. i18n:  * \* INHERIT res.partner.form (form)
.. i18n:  * \* INHERIT res.partner.form (form)
.. i18n:  * \* INHERIT Partner addresses inherited (tree)
.. i18n:  * \* INHERIT res.partner.address.form.inherited0 (form)
.. i18n:  * \* INHERIT res.partner.address.form.inherited1 (form)
.. i18n:  * \* INHERIT res.partner.address.form.inherited2 (form)
.. i18n:  * \* INHERIT res.partner.address.form.inherited3 (form)
.. i18n:  * \* INHERIT res.partner.address.form.inherited4 (form)
.. i18n:  * \* INHERIT res.partner.address.form.inherited6 (form)
.. i18n:  * \* INHERIT res.partner.address.form.inherited5 (form)
.. i18n:  * res.partner.job.tree (tree)
.. i18n:  * res.partner.job.form (form)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: res.partner.contact (res.partner.contact)
.. i18n: #################################################
..

Object: res.partner.contact (res.partner.contact)
#################################################

.. i18n: :website: Website, char
..

:website: Website, char

.. i18n: :first_name: First Name, char
..

:first_name: First Name, char

.. i18n: :job_id: Main Job, many2one, readonly
..

:job_id: Main Job, many2one, readonly

.. i18n: :title: Title, selection
..

:title: Title, selection

.. i18n: :mobile: Mobile, char
..

:mobile: Mobile, char

.. i18n: :country_id: Nationality, many2one
..

:country_id: Nationality, many2one

.. i18n: :birthdate: Birth Date, date
..

:birthdate: Birth Date, date

.. i18n: :job_ids: Functions and Addresses, one2many
..

:job_ids: Functions and Addresses, one2many

.. i18n: :lang_id: Language, many2one
..

:lang_id: Language, many2one

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :function_id: Main Function, many2one
..

:function_id: Main Function, many2one

.. i18n: :partner_id: Main Employer, many2one
..

:partner_id: Main Employer, many2one

.. i18n: :email: E-Mail, char
..

:email: E-Mail, char

.. i18n: :name: Last Name, char, required
..

:name: Last Name, char, required

.. i18n: Object: Contact Partner Function (res.partner.job)
.. i18n: ##################################################
..

Object: Contact Partner Function (res.partner.job)
##################################################

.. i18n: :sequence_partner: Partner Seq., integer
..

:sequence_partner: Partner Seq., integer

.. i18n:     *Order of importance of this job title in the list of job title of the linked partner*
..

    *Order of importance of this job title in the list of job title of the linked partner*

.. i18n: :sequence_contact: Contact Seq., integer
..

:sequence_contact: Contact Seq., integer

.. i18n:     *Order of importance of this address in the list of addresses of the linked contact*
..

    *Order of importance of this address in the list of addresses of the linked contact*

.. i18n: :fax: Fax, char
..

:fax: Fax, char

.. i18n: :name: Partner, many2one
..

:name: Partner, many2one

.. i18n: :extension: Extension, char
..

:extension: Extension, char

.. i18n:     *Internal/External extension phone number*
..

    *Internal/External extension phone number*

.. i18n: :date_start: Date Start, date
..

:date_start: Date Start, date

.. i18n: :address_id: Address, many2one
..

:address_id: Address, many2one

.. i18n: :contact_id: Contact, many2one, required
..

:contact_id: Contact, many2one, required

.. i18n: :email: E-Mail, char
..

:email: E-Mail, char

.. i18n: :phone: Phone, char
..

:phone: Phone, char

.. i18n: :state: State, selection, required
..

:state: State, selection, required

.. i18n: :date_stop: Date Stop, date
..

:date_stop: Date Stop, date

.. i18n: :function_id: Partner Function, many2one
..

:function_id: Partner Function, many2one

.. i18n: :other: Other, char
..

:other: Other, char

.. i18n:     *Additional phone field*
..

    *Additional phone field*
