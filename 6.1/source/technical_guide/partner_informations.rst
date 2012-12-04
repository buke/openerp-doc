
.. module:: partner_informations
    :synopsis: Partner informations 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/partner_informations"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Partner informations (*partner_informations*)
=============================================
:Module: partner_informations
:Name: Partner informations
:Version: 5.0.0.1
:Author: Sistheo
:Directory: partner_informations
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Add turnover and manpower information on partner definition.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/partner_informations.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/partner_informations.zip>`_


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

 * \* INHERIT res.partner.form.inherit (form)


Objects
-------

Object: Partner turnover (res.partner.turnover)
###############################################



:currency_id: Currency, many2one





:manpower: Manpower, float





:partner_id: Partner, many2one





:name: Period, char





:turnover: Turn over (Value), float


