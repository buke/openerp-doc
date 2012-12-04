
.. module:: l10n_ch_chart_c2c_pcg
    :synopsis: Suisse - Plan comptable general pour PME STERCHI 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/l10n_ch_chart_c2c_pcg"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Suisse - Plan comptable general pour PME STERCHI (*l10n_ch_chart_c2c_pcg*)
==========================================================================
:Module: l10n_ch_chart_c2c_pcg
:Name: Suisse - Plan comptable general pour PME STERCHI
:Version: 5.0.1.0
:Author: Camptocamp
:Directory: l10n_ch_chart_c2c_pcg
:Web: camptocamp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Swiss account chart that add also tax template definition

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/l10n_ch_chart_c2c_pcg.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/l10n_ch_chart_c2c_pcg.zip>`_


Dependencies
------------

 * :mod:`account`
 * :mod:`account_chart`
 * :mod:`l10n_ch`

Reports
-------

None


Menus
-------


None


Views
-----

 * account.tax.template.todo (form)


Objects
-------

Object: account.tax.template.todo (account.tax.template.todo)
#############################################################



:account_paid_id: Refund Tax Account, many2one

    *You can set                                             here the refund tax account*



:name: Tax to set, many2one, readonly

    *The tax template you are currently editing*



:account_collected_id: Invoice Tax Account, many2one

    *You can set                                                 here the invoice tax account*
