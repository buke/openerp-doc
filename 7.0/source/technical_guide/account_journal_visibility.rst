
.. module:: account_journal_visibility
    :synopsis: Accounting journal visibility 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_journal_visibility"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Accounting journal visibility (*account_journal_visibility*)
============================================================
:Module: account_journal_visibility
:Name: Accounting journal visibility
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_journal_visibility
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Using this module :
      when we open the journals list, people will only see journal for which they are allowed
      (means their group is specified on the journal definition). and also
      Only people in the group defined on the journal will be able to see the invoices of this journal.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_journal_visibility.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_journal_visibility.zip>`_


Dependencies
------------

 * :mod:`account`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT account.journal.form.inherit (form)


Objects
-------

None
