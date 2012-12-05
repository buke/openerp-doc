
.. i18n: .. module:: chricar_partner_parent_companies
.. i18n:     :synopsis: Partner Parent Companies 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: chricar_partner_parent_companies
    :synopsis: Partner Parent Companies 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/chricar_partner_parent_companies"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/chricar_partner_parent_companies"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Partner Parent Companies (*chricar_partner_parent_companies*)
.. i18n: =============================================================
.. i18n: :Module: chricar_partner_parent_companies
.. i18n: :Name: Partner Parent Companies
.. i18n: :Version: 5.0.0.2
.. i18n: :Author: ChriCar Beteiligungs- und Beratungs- GmbH
.. i18n: :Directory: chricar_partner_parent_companies
.. i18n: :Web: http://www.chricar.at/ChriCar
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Partner Parent Companies (*chricar_partner_parent_companies*)
=============================================================
:Module: chricar_partner_parent_companies
:Name: Partner Parent Companies
:Version: 5.0.0.2
:Author: ChriCar Beteiligungs- und Beratungs- GmbH
:Directory: chricar_partner_parent_companies
:Web: http://www.chricar.at/ChriCar
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows to define owners of a partner.
.. i18n:       The owner has to be defined in OpenERP as partner.
.. i18n:       Currently no check is made if max 100% of the capital is defined here
.. i18n:       Contract date+number
.. i18n:       legal and fiscal relevant periods
.. i18n:       Added Participation tab to partners to show Parent and Participations
..

::

  This module allows to define owners of a partner.
      The owner has to be defined in OpenERP as partner.
      Currently no check is made if max 100% of the capital is defined here
      Contract date+number
      legal and fiscal relevant periods
      Added Participation tab to partners to show Parent and Participations

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/chricar_partner_parent_companies.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/chricar_partner_parent_companies.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/chricar_partner_parent_companies.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/chricar_partner_parent_companies.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
..

 * :mod:`base`

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

.. i18n: None
..

None

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT res.partner.form.parent_company (form)
.. i18n:  * res.partner.parent_company.form (form)
.. i18n:  * res.partner.parent_company.tree (tree)
..

 * \* INHERIT res.partner.form.parent_company (form)
 * res.partner.parent_company.form (form)
 * res.partner.parent_company.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: res.partner.parent_company (res.partner.parent_company)
.. i18n: ###############################################################
..

Object: res.partner.parent_company (res.partner.parent_company)
###############################################################

.. i18n: :valid_until: Valid Until, date
..

:valid_until: Valid Until, date

.. i18n: :comment: Notes, text
..

:comment: Notes, text

.. i18n: :valid_from: Valid From, date
..

:valid_from: Valid From, date

.. i18n: :name: Share, float, required
..

:name: Share, float, required

.. i18n: :contract_date: Contract Date, date
..

:contract_date: Contract Date, date

.. i18n: :consolidation: Consolidation, boolean
..

:consolidation: Consolidation, boolean

.. i18n: :partner_parent_id: Parent, many2one, required
..

:partner_parent_id: Parent, many2one, required

.. i18n: :state: State, char
..

:state: State, char

.. i18n: :valid_fiscal_until: Fiscal Valid Until, date
..

:valid_fiscal_until: Fiscal Valid Until, date

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :percentage: Percentage, float
..

:percentage: Percentage, float

.. i18n: :valid_fiscal_from: Fiscal Valid From, date
..

:valid_fiscal_from: Fiscal Valid From, date

.. i18n: :partner_id: Partner, many2one, required
..

:partner_id: Partner, many2one, required

.. i18n: :contract_number: Contract Number, char
..

:contract_number: Contract Number, char
