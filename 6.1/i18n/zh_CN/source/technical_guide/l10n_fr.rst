
.. i18n: .. module:: l10n_fr
.. i18n:     :synopsis: France - Plan Comptable Général (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: l10n_fr
    :synopsis: France - Plan Comptable Général (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/l10n_fr"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/l10n_fr"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: France - Plan Comptable Général (*l10n_fr*)
.. i18n: ===========================================
.. i18n: :Module: l10n_fr
.. i18n: :Name: France - Plan Comptable Général
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: OpenERP
.. i18n: :Directory: l10n_fr
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This is the module to manage the accounting chart for France in OpenERP.
.. i18n:   
.. i18n:   Credits: Sistheo Zeekom CrysaLEAD
..

::

  This is the module to manage the accounting chart for France in OpenERP.
  
  Credits: Sistheo Zeekom CrysaLEAD

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/l10n_fr.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/l10n_fr.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/l10n_fr.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/l10n_fr.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/l10n_fr.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/l10n_fr.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`account_chart`
.. i18n:  * :mod:`account_report`
.. i18n:  * :mod:`base_vat`
..

 * :mod:`base`
 * :mod:`account`
 * :mod:`account_chart`
 * :mod:`account_report`
 * :mod:`base_vat`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Compte de resultat
.. i18n: 
.. i18n:  * Bilan
..

 * Compte de resultat

 * Bilan

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n: None
..

None

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n: None
..

None

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Report for l10n_fr (l10n.fr.report)
.. i18n: ###########################################
..

Object: Report for l10n_fr (l10n.fr.report)
###########################################

.. i18n: :line_ids: Lines, one2many
..

:line_ids: Lines, one2many

.. i18n: :code: Code, char
..

:code: Code, char

.. i18n: :name: Name, char
..

:name: Name, char

.. i18n: Object: Report Lines for l10n_fr (l10n.fr.line)
.. i18n: ###############################################
..

Object: Report Lines for l10n_fr (l10n.fr.line)
###############################################

.. i18n: :definition: Definition, char
..

:definition: Definition, char

.. i18n: :code: Variable Name, char
..

:code: Variable Name, char

.. i18n: :name: Name, char
..

:name: Name, char

.. i18n: :report_id: Report, many2one
..

:report_id: Report, many2one
