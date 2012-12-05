
.. i18n: .. module:: city
.. i18n:     :synopsis: City-Helps to keep homogeneous address data in the Database 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: city
    :synopsis: City-Helps to keep homogeneous address data in the Database 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/city"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/city"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: City-Helps to keep homogeneous address data in the Database (*city*)
.. i18n: ====================================================================
.. i18n: :Module: city
.. i18n: :Name: City-Helps to keep homogeneous address data in the Database
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Pablo Rocandio
.. i18n: :Directory: city
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Creates a model for storing cities
.. i18n:   Zip code, city, state and country fields are replaced with a location field in partner and partner contact forms.
.. i18n:   This module helps to keep homogeneous address data in the database.
..

::

  Creates a model for storing cities
  Zip code, city, state and country fields are replaced with a location field in partner and partner contact forms.
  This module helps to keep homogeneous address data in the database.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/city.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/city.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/city.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/city.zip>`_

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

.. i18n:  * Partners/Configuration/Localisation/Cities
..

 * Partners/Configuration/Localisation/Cities

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT partners_form_add_location (form)
.. i18n:  * \* INHERIT partners_form_del_city (form)
.. i18n:  * \* INHERIT partners_form_del_citycity (form)
.. i18n:  * \* INHERIT partners_form_del_zip (form)
.. i18n:  * \* INHERIT partners_form_del_state (form)
.. i18n:  * \* INHERIT partners_form_add_location1 (form)
.. i18n:  * \* INHERIT partners_form_del_city1 (form)
.. i18n:  * \* INHERIT partners_form_del_zip1 (form)
.. i18n:  * \* INHERIT partners_form_del_country1 (form)
.. i18n:  * \* INHERIT partners_form_add_location2 (form)
.. i18n:  * \* INHERIT partners_form_del_city2 (form)
.. i18n:  * \* INHERIT partners_form_del_zip2 (form)
.. i18n:  * \* INHERIT partners_form_del_country2 (form)
.. i18n:  * \* INHERIT view_country_state_form2 (form)
.. i18n:  * city.city.tree (tree)
.. i18n:  * city.city.form (form)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: City (city.city)
.. i18n: ########################
..

Object: City (city.city)
########################

.. i18n: :state_id: State, many2one, required
..

:state_id: State, many2one, required

.. i18n: :name: City, char, required
..

:name: City, char, required

.. i18n: :zipcode: ZIP, char, required
..

:zipcode: ZIP, char, required
