
.. i18n: .. module:: users_ldap
.. i18n:     :synopsis: Authenticate users with ldap server 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: users_ldap
    :synopsis: Authenticate users with ldap server 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/users_ldap"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/users_ldap"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Authenticate users with ldap server (*users_ldap*)
.. i18n: ==================================================
.. i18n: :Module: users_ldap
.. i18n: :Name: Authenticate users with ldap server
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Tiny
.. i18n: :Directory: users_ldap
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Authenticate users with ldap server (*users_ldap*)
==================================================
:Module: users_ldap
:Name: Authenticate users with ldap server
:Version: 5.0.0.1
:Author: Tiny
:Directory: users_ldap
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
.. i18n:   Add support for authentication by ldap server
..

::

  Add support for authentication by ldap server

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/users_ldap.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/users_ldap.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/users_ldap.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/users_ldap.zip>`_

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

.. i18n:  * \* INHERIT res.company.form.inherit.users_ldap (form)
..

 * \* INHERIT res.company.form.inherit.users_ldap (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: res.company.ldap (res.company.ldap)
.. i18n: ###########################################
..

Object: res.company.ldap (res.company.ldap)
###########################################

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :ldap_password: LDAP password, char, required
..

:ldap_password: LDAP password, char, required

.. i18n: :ldap_server: LDAP Server address, char, required
..

:ldap_server: LDAP Server address, char, required

.. i18n: :company: Company, many2one, required
..

:company: Company, many2one, required

.. i18n: :ldap_base: LDAP base, char, required
..

:ldap_base: LDAP base, char, required

.. i18n: :create_user: Create user, boolean
..

:create_user: Create user, boolean

.. i18n:     *Create the user if not in database*
..

    *Create the user if not in database*

.. i18n: :ldap_server_port: LDAP Server port, integer, required
..

:ldap_server_port: LDAP Server port, integer, required

.. i18n: :user: Model user, many2one
..

:user: Model user, many2one

.. i18n:     *Model used for user creation*
..

    *Model used for user creation*

.. i18n: :ldap_binddn: LDAP binddn, char, required
..

:ldap_binddn: LDAP binddn, char, required

.. i18n: :ldap_filter: LDAP filter, char, required
..

:ldap_filter: LDAP filter, char, required
