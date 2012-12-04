
.. module:: analytic_partners
    :synopsis: Analytic accounts with multiple partners 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/analytic_partners"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Analytic accounts with multiple partners (*analytic_partners*)
==============================================================
:Module: analytic_partners
:Name: Analytic accounts with multiple partners
:Version: 5.0.1.0
:Author: Tiny
:Directory: analytic_partners
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  This module adds the possibility to assign multiple partners on
      the same analytic account. It's usefull when you do a management
      by affairs, where you can attach all suppliers and customers to
      a project.
  
      A report for the project manager is added to print the analytic
      account and all associated partners with their contacts.
  
      It's usefull to give to all members of a project, so that they
      get the contacts of all suppliers in this project.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/analytic_partners.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/analytic_partners.zip>`_


Dependencies
------------

 * :mod:`account`

Reports
-------

 * Analytic Account with Partners

Menus
-------


None


Views
-----

 * \* INHERIT analytic_partners.analytic.account.form (form)


Objects
-------

None
