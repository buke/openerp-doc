
.. module:: account_invoice_layout
    :synopsis: account_invoice_layout (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_invoice_layout"></div>
    <script src="http://js-kit.com/ratings.js"></script>

account_invoice_layout (*account_invoice_layout*)
=================================================
:Module: account_invoice_layout
:Name: account_invoice_layout
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_invoice_layout
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module provides some features to improve the layout of the invoices.
  
      It gives you the possibility to
          * order all the lines of an invoice
          * add titles, comment lines, sub total lines
          * draw horizontal lines and put page breaks
  
      Moreover, there is one option which allow you to print all the selected invoices with a given special message at the bottom of it. This feature can be very useful for printing your invoices with end-of-year wishes, special punctual conditions...

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_invoice_layout.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_invoice_layout.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`

Reports
-------

 * Invoices with Layout

Menus
-------

 * Financial Management/Configuration/Notification Message
 * Financial Management/Configuration/Notification Message/All Notification Messages

Views
-----

 * \* INHERIT account.invoice.line.form.inherit_1 (form)
 * \* INHERIT account.invoice.line.tree.inherit_1 (tree)
 * \* INHERIT account.invoice.line.tree.inherit_2 (tree)
 * \* INHERIT account.invoice.form.inherit_1 (form)
 * notify.message.tree (tree)
 * notify.message.form (form)


Objects
-------

Object: Notify By Messages (notify.message)
###########################################



:msg: Special Message, text, required

    *This notification will appear at the bottom of the Invoices when printed.*



:name: Title, char, required


