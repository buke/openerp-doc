
.. module:: l10n_fr
    :synopsis: France - Plan Comptable Général (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/l10n_fr"></div>
    <script src="http://js-kit.com/ratings.js"></script>

France - Plan Comptable Général (*l10n_fr*)
===========================================
:Module: l10n_fr
:Name: France - Plan Comptable Général
:Version: 5.0.1.0
:Author: OpenERP
:Directory: l10n_fr
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This is the module to manage the accounting chart for France in OpenERP.
  
  Credits: Sistheo Zeekom CrysaLEAD

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/l10n_fr.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/l10n_fr.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/l10n_fr.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`account_chart`
 * :mod:`account_report`
 * :mod:`base_vat`

Reports
-------

 * Compte de resultat

 * Bilan

Menus
-------


None


Views
-----


None



Objects
-------

Object: Report for l10n_fr (l10n.fr.report)
###########################################



:line_ids: Lines, one2many





:code: Code, char





:name: Name, char




Object: Report Lines for l10n_fr (l10n.fr.line)
###############################################



:definition: Definition, char





:code: Variable Name, char





:name: Name, char





:report_id: Report, many2one


