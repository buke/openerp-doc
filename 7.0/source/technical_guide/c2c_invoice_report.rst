
.. module:: c2c_invoice_report
    :synopsis: Invoice customisation 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_invoice_report"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Invoice customisation (*c2c_invoice_report*)
============================================
:Module: c2c_invoice_report
:Name: Invoice customisation
:Version: 5.0.1.0
:Author: Camptocamp
:Directory: c2c_invoice_report
:Web: http://www.camptocamp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  None

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/c2c_invoice_report.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/c2c_invoice_report.zip>`_


Dependencies
------------

 * :mod:`account`

Reports
-------

None


Menus
-------

 * Financial Management/Configuration/Invoice Condition/Conditions
 * Financial Management/Configuration/Invoice Condition/Edit Conditions

Views
-----

 * account.condition_text.form (form)
 * account.condition_text.list (tree)
 * \* INHERIT account.invoice.form.date_sent (form)
 * \* INHERIT account.invoice.form.date_sent (form)


Objects
-------

Object: Invoice condition text (account.condition_text)
#######################################################



:text: text, text, required





:type: type, selection, required





:name: Methode, char, required


