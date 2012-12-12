
.. i18n: .. module:: c2c_invoice_report
.. i18n:     :synopsis: Invoice customisation 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: c2c_invoice_report
    :synopsis: Invoice customisation 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_invoice_report"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_invoice_report"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Invoice customisation (*c2c_invoice_report*)
.. i18n: ============================================
.. i18n: :Module: c2c_invoice_report
.. i18n: :Name: Invoice customisation
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Camptocamp
.. i18n: :Directory: c2c_invoice_report
.. i18n: :Web: http://www.camptocamp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   None
..

::

  None

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/c2c_invoice_report.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/c2c_invoice_report.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/c2c_invoice_report.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/c2c_invoice_report.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account`
..

 * :mod:`account`

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

.. i18n:  * Financial Management/Configuration/Invoice Condition/Conditions
.. i18n:  * Financial Management/Configuration/Invoice Condition/Edit Conditions
..

 * Financial Management/Configuration/Invoice Condition/Conditions
 * Financial Management/Configuration/Invoice Condition/Edit Conditions

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * account.condition_text.form (form)
.. i18n:  * account.condition_text.list (tree)
.. i18n:  * \* INHERIT account.invoice.form.date_sent (form)
.. i18n:  * \* INHERIT account.invoice.form.date_sent (form)
..

 * account.condition_text.form (form)
 * account.condition_text.list (tree)
 * \* INHERIT account.invoice.form.date_sent (form)
 * \* INHERIT account.invoice.form.date_sent (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Invoice condition text (account.condition_text)
.. i18n: #######################################################
..

Object: Invoice condition text (account.condition_text)
#######################################################

.. i18n: :text: text, text, required
..

:text: text, text, required

.. i18n: :type: type, selection, required
..

:type: type, selection, required

.. i18n: :name: Methode, char, required
..

:name: Methode, char, required
