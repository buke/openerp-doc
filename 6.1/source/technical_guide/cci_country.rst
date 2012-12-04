
.. module:: cci_country
    :synopsis: CCI Country 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_country"></div>
    <script src="http://js-kit.com/ratings.js"></script>

CCI Country (*cci_country*)
===========================
:Module: cci_country
:Name: CCI Country
:Version: 5.0.1.0
:Author: CCILV
:Directory: cci_country
:Web: http://www.ccilv.be
:Official module: no
:Quality certified: no

Description
-----------

::

  For some applications in the OpenERP software used by some Belgian Chamber of Commerce,
          we need a table regrouping countries and areas (group of countries). The table used by
          default in OpenERP doesn't answer to this need, because it's used in other and we need to
          specify if this code can be used in some cases or others
          This table is by evidence very specific to the Chamber of Commerce dedicated modules.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/cci_country.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/cci_country.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Partners/Configuration/Country and Area

Views
-----

 * cci_country.form (form)
 * cci_country.tree (tree)


Objects
-------

Object: Country or Area for CCI (cci.country)
#############################################



:cci_country_ids: Linked Countries-Areas, many2many





:phoneprefix: Phone Prefix, integer





:description: Description, text





:valid4embassy: Embassy, boolean

    *Indicates if this code can be used for Embassies*



:valid4certificate: Certificates, boolean

    *Indicates if this code can be used for certificates*



:iscountry: Country, boolean

    *Indicates if this code designates a country; if False, designates an area*



:postalabbrev: Postal Abbreviation, char





:code: Code, char, required





:official_name: Official Name, char





:active: Active, boolean

    *Indicates if we can still use this country-area code*



:valid4ata: ATA, boolean

    *Indicates if this code can be used for carnets ATA*



:name: Name, char, required


