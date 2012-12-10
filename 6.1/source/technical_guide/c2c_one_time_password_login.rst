
.. i18n: .. module:: c2c_one_time_password_login
.. i18n:     :synopsis: c2c_one_time_password_login 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: c2c_one_time_password_login
    :synopsis: c2c_one_time_password_login 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_one_time_password_login"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_one_time_password_login"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: c2c_one_time_password_login (*c2c_one_time_password_login*)
.. i18n: ===========================================================
.. i18n: :Module: c2c_one_time_password_login
.. i18n: :Name: c2c_one_time_password_login
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Camptocamp SA
.. i18n: :Directory: c2c_one_time_password_login
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

c2c_one_time_password_login (*c2c_one_time_password_login*)
===========================================================
:Module: c2c_one_time_password_login
:Name: c2c_one_time_password_login
:Version: 5.0.1.0
:Author: Camptocamp SA
:Directory: c2c_one_time_password_login
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
.. i18n:   Generic OTP login module that provides basic 
.. i18n:       session and mechanism for OTP.
.. i18n:       
.. i18n:       We do not intend to provide a generic authentication framework, just one for OTP.   
.. i18n:       Actually it is not designed to support CAS, Kerberos etc.
.. i18n:   
.. i18n:       The c2c_one_time_password_login provides the base mechanism for OTP 
.. i18n:       like authentication function overriding, user session, login management, timeout management, multi connection, etc.
.. i18n:       You have one function (check_otp) to override in a provider module.
.. i18n:       A provider module lets you write a provider for a specific OTP system 
.. i18n:       You have a sample in the c2c_one_time_password_login_yubikey_provider module.
.. i18n:       The OTP configuration is done on the company view. Please see the help in the form.
..

::

  Generic OTP login module that provides basic 
      session and mechanism for OTP.
      
      We do not intend to provide a generic authentication framework, just one for OTP.   
      Actually it is not designed to support CAS, Kerberos etc.
  
      The c2c_one_time_password_login provides the base mechanism for OTP 
      like authentication function overriding, user session, login management, timeout management, multi connection, etc.
      You have one function (check_otp) to override in a provider module.
      A provider module lets you write a provider for a specific OTP system 
      You have a sample in the c2c_one_time_password_login_yubikey_provider module.
      The OTP configuration is done on the company view. Please see the help in the form.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n: (No download links available)
..

(No download links available)

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

.. i18n:  * \* INHERIT res.company.form.inherit (form)
.. i18n:  * \* INHERIT res.company.form.otp_setting (form)
..

 * \* INHERIT res.company.form.inherit (form)
 * \* INHERIT res.company.form.otp_setting (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
