
.. module:: base_contact_city
    :synopsis: City for Base Contact 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_contact_city"></div>
    <script src="http://js-kit.com/ratings.js"></script>

City for Base Contact (*base_contact_city*)
===========================================
:Module: base_contact_city
:Name: City for Base Contact
:Version: 5.0.1.0
:Author: Pablo Rocandio
:Directory: base_contact_city
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Zip code, city, state and country fields are replaced with a location field in partner form when base_contact module is installed.
  This module helps to keep homogeneous address data in our database.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/base_contact_city.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/base_contact_city.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`base_contact`
 * :mod:`city`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT partners_form_inherit_add_location (form)
 * \* INHERIT partners_form_inherit_del_city (form)
 * \* INHERIT partners_form_inherit_del_zip (form)
 * \* INHERIT partners_form_inherit_del_state (form)


Objects
-------

None
