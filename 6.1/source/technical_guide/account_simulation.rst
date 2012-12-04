
.. module:: account_simulation
    :synopsis: Accounting simulation journal 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_simulation"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Accounting simulation journal (*account_simulation*)
====================================================
:Module: account_simulation
:Name: Accounting simulation journal
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_simulation
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Accounting simulation plan.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_simulation.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_simulation.zip>`_


Dependencies
------------

 * :mod:`account`

Reports
-------

None


Menus
-------

 * Financial Management/Configuration/Financial Accounting/Financial Journals/Journal Simulations
 * Financial Management/Configuration/Financial Accounting/Financial Journals/Account Journal

Views
-----

 * account.journal.simulation.tree (tree)
 * account.journal.simulation.form (form)
 * \* INHERIT account.journal.simulation.form.inherit (form)
 * account.journal.tree (tree)


Objects
-------

Object: Simulation level (account.journal.simulation)
#####################################################



:code: Simulation code, char, required





:name: Simulation name, char, required


