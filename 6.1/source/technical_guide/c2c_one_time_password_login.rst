
.. module:: c2c_one_time_password_login
    :synopsis: c2c_one_time_password_login 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_one_time_password_login"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

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

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT res.company.form.inherit (form)
 * \* INHERIT res.company.form.otp_setting (form)


Objects
-------

None
