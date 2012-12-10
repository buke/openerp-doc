
.. i18n: .. module:: account_analytic_default
.. i18n:     :synopsis: Account Analytic Default (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_analytic_default
    :synopsis: Account Analytic Default (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_analytic_default"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_analytic_default"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Account Analytic Default (*account_analytic_default*)
.. i18n: =====================================================
.. i18n: :Module: account_analytic_default
.. i18n: :Name: Account Analytic Default
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: account_analytic_default
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Account Analytic Default (*account_analytic_default*)
=====================================================
:Module: account_analytic_default
:Name: Account Analytic Default
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_analytic_default
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
.. i18n:   Allows to automatically select analytic accounts based on criterions:
.. i18n:   * Product
.. i18n:   * Partner
.. i18n:   * User
.. i18n:   * Company
.. i18n:   * Date
..

::

  Allows to automatically select analytic accounts based on criterions:
  * Product
  * Partner
  * User
  * Company
  * Date

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/account_analytic_default.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/account_analytic_default.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_analytic_default.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_analytic_default.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account`
.. i18n:  * :mod:`sale`
..

 * :mod:`account`
 * :mod:`sale`

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

.. i18n:  * Financial Management/Configuration/Analytic Accounting/Analytic Defaults
..

 * Financial Management/Configuration/Analytic Accounting/Analytic Defaults

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * account.analytic.default.tree (tree)
.. i18n:  * account.analytic.default.form (form)
..

 * account.analytic.default.tree (tree)
 * account.analytic.default.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Analytic Distributions (account.analytic.default)
.. i18n: #########################################################
..

Object: Analytic Distributions (account.analytic.default)
#########################################################

.. i18n: :date_stop: End Date, date
..

:date_stop: End Date, date

.. i18n: :user_id: User, many2one
..

:user_id: User, many2one

.. i18n: :product_id: Product, many2one
..

:product_id: Product, many2one

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :date_start: Start Date, date
..

:date_start: Start Date, date

.. i18n: :company_id: Company, many2one
..

:company_id: Company, many2one

.. i18n: :analytic_id: Analytic Account, many2one
..

:analytic_id: Analytic Account, many2one

.. i18n: :partner_id: Partner, many2one
..

:partner_id: Partner, many2one
