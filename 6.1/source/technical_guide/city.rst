
.. module:: city
    :synopsis: City-Helps to keep homogeneous address data in the Database 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/city"></div>
    <script src="http://js-kit.com/ratings.js"></script>

City-Helps to keep homogeneous address data in the Database (*city*)
====================================================================
:Module: city
:Name: City-Helps to keep homogeneous address data in the Database
:Version: 5.0.1.0
:Author: Pablo Rocandio
:Directory: city
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Creates a model for storing cities
  Zip code, city, state and country fields are replaced with a location field in partner and partner contact forms.
  This module helps to keep homogeneous address data in the database.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/city.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/city.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Partners/Configuration/Localisation/Cities

Views
-----

 * \* INHERIT partners_form_add_location (form)
 * \* INHERIT partners_form_del_city (form)
 * \* INHERIT partners_form_del_citycity (form)
 * \* INHERIT partners_form_del_zip (form)
 * \* INHERIT partners_form_del_state (form)
 * \* INHERIT partners_form_add_location1 (form)
 * \* INHERIT partners_form_del_city1 (form)
 * \* INHERIT partners_form_del_zip1 (form)
 * \* INHERIT partners_form_del_country1 (form)
 * \* INHERIT partners_form_add_location2 (form)
 * \* INHERIT partners_form_del_city2 (form)
 * \* INHERIT partners_form_del_zip2 (form)
 * \* INHERIT partners_form_del_country2 (form)
 * \* INHERIT view_country_state_form2 (form)
 * city.city.tree (tree)
 * city.city.form (form)


Objects
-------

Object: City (city.city)
########################



:state_id: State, many2one, required





:name: City, char, required





:zipcode: ZIP, char, required


