
.. i18n: .. module:: zarafa
.. i18n:     :synopsis: Zarafa Integration 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: zarafa
    :synopsis: Zarafa Integration 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/zarafa"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/zarafa"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Zarafa Integration (*zarafa*)
.. i18n: =============================
.. i18n: :Module: zarafa
.. i18n: :Name: Zarafa Integration
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Sednacom
.. i18n: :Directory: zarafa
.. i18n: :Web: http://www.sednacom.fr
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Zarafa Integration (*zarafa*)
=============================
:Module: zarafa
:Name: Zarafa Integration
:Version: 5.0.1.0
:Author: Sednacom
:Directory: zarafa
:Web: http://www.sednacom.fr
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   New objects and views to improve use of OpenERP:
.. i18n:    * shortcuts view
.. i18n:    * module view
.. i18n:    * email object
.. i18n:    * Zarafa tools
..

::

  New objects and views to improve use of OpenERP:
   * shortcuts view
   * module view
   * email object
   * Zarafa tools

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/zarafa.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/zarafa.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/zarafa.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/zarafa.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`crm`
..

 * :mod:`base`
 * :mod:`crm`

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

.. i18n:  * Administration/Modules Management/Modules by Sednacom
.. i18n:  * Tools/Shortcuts
.. i18n:  * Tools/Import contact from Zarafa
.. i18n:  * Tools/Emails
..

 * Administration/Modules Management/Modules by Sednacom
 * Tools/Shortcuts
 * Tools/Import contact from Zarafa
 * Tools/Emails

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT res.users.form.zarafa (form)
.. i18n:  * \* INHERIT res.partner.address.tree.email (tree)
.. i18n:  * sednacom.email.form (form)
.. i18n:  * sednacom.email.tree (tree)
..

 * \* INHERIT res.users.form.zarafa (form)
 * \* INHERIT res.partner.address.tree.email (tree)
 * sednacom.email.form (form)
 * sednacom.email.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: sednacom.email (sednacom.email)
.. i18n: #######################################
..

Object: sednacom.email (sednacom.email)
#######################################

.. i18n: :body: Message, text, readonly
..

:body: Message, text, readonly

.. i18n: :name: Title, char, required, readonly
..

:name: Title, char, required, readonly

.. i18n: :recipients: Contacts, many2many, readonly
..

:recipients: Contacts, many2many, readonly

.. i18n: :datetime: Date, datetime, readonly
..

:datetime: Date, datetime, readonly

.. i18n: :to: To, char, readonly
..

:to: To, char, readonly

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :exp: From, char, required, readonly
..

:exp: From, char, required, readonly

.. i18n: :crm_case: Case, many2one, readonly
..

:crm_case: Case, many2one, readonly

.. i18n: Object: Contacts, with features to import from Zarafa server (zarafa.contact)
.. i18n: #############################################################################
..

Object: Contacts, with features to import from Zarafa server (zarafa.contact)
#############################################################################

.. i18n: :fax: Fax, char
..

:fax: Fax, char

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :mobile: Mobile, char
..

:mobile: Mobile, char

.. i18n: :company: Company, char
..

:company: Company, char

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :phone: Phone, char
..

:phone: Phone, char

.. i18n: :zid: Z-Id, char, required
..

:zid: Z-Id, char, required

.. i18n: :email: Email, char, required
..

:email: Email, char, required
