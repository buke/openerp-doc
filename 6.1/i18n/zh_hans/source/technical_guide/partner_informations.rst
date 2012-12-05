
.. i18n: .. module:: partner_informations
.. i18n:     :synopsis: Partner informations 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: partner_informations
    :synopsis: Partner informations 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/partner_informations"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/partner_informations"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Partner informations (*partner_informations*)
.. i18n: =============================================
.. i18n: :Module: partner_informations
.. i18n: :Name: Partner informations
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Sistheo
.. i18n: :Directory: partner_informations
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Add turnover and manpower information on partner definition.
..

::

  Add turnover and manpower information on partner definition.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/partner_informations.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/partner_informations.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/partner_informations.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/partner_informations.zip>`_

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

.. i18n:  * \* INHERIT res.partner.form.inherit (form)
..

 * \* INHERIT res.partner.form.inherit (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Partner turnover (res.partner.turnover)
.. i18n: ###############################################
..

Object: Partner turnover (res.partner.turnover)
###############################################

.. i18n: :currency_id: Currency, many2one
..

:currency_id: Currency, many2one

.. i18n: :manpower: Manpower, float
..

:manpower: Manpower, float

.. i18n: :partner_id: Partner, many2one
..

:partner_id: Partner, many2one

.. i18n: :name: Period, char
..

:name: Period, char

.. i18n: :turnover: Turn over (Value), float
..

:turnover: Turn over (Value), float
