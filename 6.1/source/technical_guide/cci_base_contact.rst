
.. i18n: .. module:: cci_base_contact
.. i18n:     :synopsis: CCI Base Contact 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: cci_base_contact
    :synopsis: CCI Base Contact 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_base_contact"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_base_contact"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: CCI Base Contact (*cci_base_contact*)
.. i18n: =====================================
.. i18n: :Module: cci_base_contact
.. i18n: :Name: CCI Base Contact
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: cci_base_contact
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   specific module for cci project which will inherit
.. i18n:           base_contact module..
..

::

  specific module for cci project which will inherit
          base_contact module..

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/cci_base_contact.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/cci_base_contact.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/cci_base_contact.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/cci_base_contact.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`base_contact`
.. i18n:  * :mod:`project`
..

 * :mod:`base`
 * :mod:`base_contact`
 * :mod:`project`

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

.. i18n:  * Partners/Configuration/Link Type
.. i18n:  * Partners/Configuration/Link Type/Contact Link Type
..

 * Partners/Configuration/Link Type
 * Partners/Configuration/Link Type/Contact Link Type

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * res.partner.country.relation.tree (tree)
.. i18n:  * res.partner.country.relation.form (form)
.. i18n:  * \* INHERIT res.partner.contact.tree2 (tree)
.. i18n:  * \* INHERIT res.partner.contact.form (form)
.. i18n:  * \* INHERIT res.partner.contact.form (form)
.. i18n:  * \* INHERIT res.partner.contact.form (form)
.. i18n:  * \* INHERIT res.partner.contact.form (form)
.. i18n:  * res.partner.contact.link.type.tree (tree)
.. i18n:  * res.partner.contact.link.type.form (form)
.. i18n:  * \* INHERIT project.project.form.inherit (form)
.. i18n:  * \* INHERIT res.partner.job.form.inherit (form)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: res.partner.contact.link.type (res.partner.contact.link.type)
.. i18n: #####################################################################
..

Object: res.partner.contact.link.type (res.partner.contact.link.type)
#####################################################################

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: res.partner.contact.link (res.partner.contact.link)
.. i18n: ###########################################################
..

Object: res.partner.contact.link (res.partner.contact.link)
###########################################################

.. i18n: :current_contact_id: Current contact, many2one, required
..

:current_contact_id: Current contact, many2one, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :contact_id: Contact, many2one, required
..

:contact_id: Contact, many2one, required

.. i18n: :type_id: Type, many2one, required
..

:type_id: Type, many2one, required
