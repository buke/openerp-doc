
.. i18n: .. module:: l10n_fr_account_generation
.. i18n:     :synopsis: France - Generation de compte comptable tiers 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: l10n_fr_account_generation
    :synopsis: France - Generation de compte comptable tiers 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/l10n_fr_account_generation"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/l10n_fr_account_generation"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: France - Generation de compte comptable tiers (*l10n_fr_account_generation*)
.. i18n: ============================================================================
.. i18n: :Module: l10n_fr_account_generation
.. i18n: :Name: France - Generation de compte comptable tiers
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: SISTHEO
.. i18n: :Directory: l10n_fr_account_generation
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

France - Generation de compte comptable tiers (*l10n_fr_account_generation*)
============================================================================
:Module: l10n_fr_account_generation
:Name: France - Generation de compte comptable tiers
:Version: 5.0.1.0
:Author: SISTHEO
:Directory: l10n_fr_account_generation
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Add a button in partners form for creating the payable and receive accounts in general account.
.. i18n:   
.. i18n:   Credits: Sistheo Zeekom
..

::

  Add a button in partners form for creating the payable and receive accounts in general account.
  
  Credits: Sistheo Zeekom

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/l10n_fr_account_generation.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/l10n_fr_account_generation.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/l10n_fr_account_generation.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/l10n_fr_account_generation.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`account_chart`
..

 * :mod:`base`
 * :mod:`account`
 * :mod:`account_chart`

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

.. i18n:  * Financial Management/Configuration/Account generation config
..

 * Financial Management/Configuration/Account generation config

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT res.partner.form (form)
.. i18n:  * account.generation.config.form (form)
..

 * \* INHERIT res.partner.form (form)
 * account.generation.config.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Account Generation Configuration (account.generation.config)
.. i18n: ####################################################################
..

Object: Account Generation Configuration (account.generation.config)
####################################################################

.. i18n: :customer: Global Customer, many2one
..

:customer: Global Customer, many2one

.. i18n: :supplier: Global Supplier, many2one
..

:supplier: Global Supplier, many2one

.. i18n: :name: Configuration Name, char, required
..

:name: Configuration Name, char, required

.. i18n: :nbcar: Char size, integer
..

:nbcar: Char size, integer

.. i18n:     *Number of character for the creation of accounts*
..

    *Number of character for the creation of accounts*
