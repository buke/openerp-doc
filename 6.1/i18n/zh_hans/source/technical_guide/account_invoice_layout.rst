
.. i18n: .. module:: account_invoice_layout
.. i18n:     :synopsis: account_invoice_layout (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_invoice_layout
    :synopsis: account_invoice_layout (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_invoice_layout"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_invoice_layout"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: account_invoice_layout (*account_invoice_layout*)
.. i18n: =================================================
.. i18n: :Module: account_invoice_layout
.. i18n: :Name: account_invoice_layout
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: account_invoice_layout
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module provides some features to improve the layout of the invoices.
.. i18n:   
.. i18n:       It gives you the possibility to
.. i18n:           * order all the lines of an invoice
.. i18n:           * add titles, comment lines, sub total lines
.. i18n:           * draw horizontal lines and put page breaks
.. i18n:   
.. i18n:       Moreover, there is one option which allow you to print all the selected invoices with a given special message at the bottom of it. This feature can be very useful for printing your invoices with end-of-year wishes, special punctual conditions...
..

::

  This module provides some features to improve the layout of the invoices.
  
      It gives you the possibility to
          * order all the lines of an invoice
          * add titles, comment lines, sub total lines
          * draw horizontal lines and put page breaks
  
      Moreover, there is one option which allow you to print all the selected invoices with a given special message at the bottom of it. This feature can be very useful for printing your invoices with end-of-year wishes, special punctual conditions...

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/account_invoice_layout.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/account_invoice_layout.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_invoice_layout.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_invoice_layout.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
..

 * :mod:`base`
 * :mod:`account`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Invoices with Layout
..

 * Invoices with Layout

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Financial Management/Configuration/Notification Message
.. i18n:  * Financial Management/Configuration/Notification Message/All Notification Messages
..

 * Financial Management/Configuration/Notification Message
 * Financial Management/Configuration/Notification Message/All Notification Messages

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT account.invoice.line.form.inherit_1 (form)
.. i18n:  * \* INHERIT account.invoice.line.tree.inherit_1 (tree)
.. i18n:  * \* INHERIT account.invoice.line.tree.inherit_2 (tree)
.. i18n:  * \* INHERIT account.invoice.form.inherit_1 (form)
.. i18n:  * notify.message.tree (tree)
.. i18n:  * notify.message.form (form)
..

 * \* INHERIT account.invoice.line.form.inherit_1 (form)
 * \* INHERIT account.invoice.line.tree.inherit_1 (tree)
 * \* INHERIT account.invoice.line.tree.inherit_2 (tree)
 * \* INHERIT account.invoice.form.inherit_1 (form)
 * notify.message.tree (tree)
 * notify.message.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Notify By Messages (notify.message)
.. i18n: ###########################################
..

Object: Notify By Messages (notify.message)
###########################################

.. i18n: :msg: Special Message, text, required
..

:msg: Special Message, text, required

.. i18n:     *This notification will appear at the bottom of the Invoices when printed.*
..

    *This notification will appear at the bottom of the Invoices when printed.*

.. i18n: :name: Title, char, required
..

:name: Title, char, required
