
.. i18n: .. module:: multilogin_portal
.. i18n:     :synopsis: Multilogin portal 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: multilogin_portal
    :synopsis: Multilogin portal 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/multilogin_portal"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/multilogin_portal"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Multilogin portal (*multilogin_portal*)
.. i18n: =======================================
.. i18n: :Module: multilogin_portal
.. i18n: :Name: Multilogin portal
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Ferme Urbaine
.. i18n: :Directory: multilogin_portal
.. i18n: :Web: http://www.lafermedusart.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Multilogin portal (*multilogin_portal*)
=======================================
:Module: multilogin_portal
:Name: Multilogin portal
:Version: 5.0.1.0
:Author: Ferme Urbaine
:Directory: multilogin_portal
:Web: http://www.lafermedusart.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Allows xmlrpc queries from partners email+password as:
.. i18n:   	- Customer standard user
.. i18n:   	- Provider standard user
.. i18n:   
.. i18n:   Allows xmlrpc queries from computers (IP automatically recognized) as:
.. i18n:   	- Computer standard user
.. i18n:   
.. i18n:   Standard users are set into res.company.
.. i18n:   For multi-company, please alter this code.
..

::

  Allows xmlrpc queries from partners email+password as:
  	- Customer standard user
  	- Provider standard user
  
  Allows xmlrpc queries from computers (IP automatically recognized) as:
  	- Computer standard user
  
  Standard users are set into res.company.
  For multi-company, please alter this code.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/multilogin_portal.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/multilogin_portal.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/multilogin_portal.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/multilogin_portal.zip>`_

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

.. i18n:  * Administration/Configuration/Computers
..

 * Administration/Configuration/Computers

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT res.company.form (form)
.. i18n:  * res.computer.tree (tree)
..

 * \* INHERIT res.company.form (form)
 * res.computer.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Computers (res.computer)
.. i18n: ################################
..

Object: Computers (res.computer)
################################

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :state: State, selection, required
..

:state: State, selection, required

.. i18n: :ip_address: IP address, char, required
..

:ip_address: IP address, char, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required
