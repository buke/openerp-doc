
.. module:: chricar_partner_parent_companies
    :synopsis: Partner Parent Companies 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/chricar_partner_parent_companies"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  This module allows to define owners of a partner.
      The owner has to be defined in OpenERP as partner.
      Currently no check is made if max 100% of the capital is defined here
      Contract date+number
      legal and fiscal relevant periods
      Added Participation tab to partners to show Parent and Participations

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/chricar_partner_parent_companies.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/chricar_partner_parent_companies.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT res.partner.form.parent_company (form)
 * res.partner.parent_company.form (form)
 * res.partner.parent_company.tree (tree)


Objects
-------

Object: res.partner.parent_company (res.partner.parent_company)
###############################################################



:valid_until: Valid Until, date





:comment: Notes, text





:valid_from: Valid From, date





:name: Share, float, required





:contract_date: Contract Date, date





:consolidation: Consolidation, boolean





:partner_parent_id: Parent, many2one, required





:state: State, char





:valid_fiscal_until: Fiscal Valid Until, date





:active: Active, boolean





:percentage: Percentage, float





:valid_fiscal_from: Fiscal Valid From, date





:partner_id: Partner, many2one, required





:contract_number: Contract Number, char


