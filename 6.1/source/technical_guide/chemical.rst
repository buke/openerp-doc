
.. i18n: .. module:: chemical
.. i18n:     :synopsis: Module for Chemical Industries (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: chemical
    :synopsis: Module for Chemical Industries (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/chemical"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/chemical"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Module for Chemical Industries (*chemical*)
.. i18n: ===========================================
.. i18n: :Module: chemical
.. i18n: :Name: Module for Chemical Industries
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: H&D
.. i18n: :Directory: chemical
.. i18n: :Web: http://www.hu-div.fr
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Module for Chemical Industries (*chemical*)
===========================================
:Module: chemical
:Name: Module for Chemical Industries
:Version: 5.0.1.0
:Author: H&D
:Directory: chemical
:Web: http://www.hu-div.fr
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module for Chemical Industries
..

::

  Module for Chemical Industries

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/chemical.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/chemical.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/chemical.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/chemical.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`stock`
..

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`
 * :mod:`stock`

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

.. i18n:  * Products/Configuration/Chimie
.. i18n:  * Products/Configuration/Chimie/product risque
.. i18n:  * Products/Configuration/Chimie/product securite
.. i18n:  * Products/Configuration/Chimie/product danger
..

 * Products/Configuration/Chimie
 * Products/Configuration/Chimie/product risque
 * Products/Configuration/Chimie/product securite
 * Products/Configuration/Chimie/product danger

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT product.normal.form (form)
.. i18n:  * product.risque.tree (tree)
.. i18n:  * product.risque.form (form)
.. i18n:  * product.securite.tree (tree)
.. i18n:  * product.securite.form (form)
.. i18n:  * product.danger.tree (tree)
.. i18n:  * product.danger.form (form)
..

 * \* INHERIT product.normal.form (form)
 * product.risque.tree (tree)
 * product.risque.form (form)
 * product.securite.tree (tree)
 * product.securite.form (form)
 * product.danger.tree (tree)
 * product.danger.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Risques Produits (product.risque)
.. i18n: #########################################
..

Object: Risques Produits (product.risque)
#########################################

.. i18n: :libelle: libelle, char, required
..

:libelle: libelle, char, required

.. i18n: :name: Risque, char, required
..

:name: Risque, char, required

.. i18n: Object: Securite Produits (product.securite)
.. i18n: ############################################
..

Object: Securite Produits (product.securite)
############################################

.. i18n: :libelle: libelle, char, required
..

:libelle: libelle, char, required

.. i18n: :name: Security, char, required
..

:name: Security, char, required

.. i18n: Object: Dangers Product (product.danger)
.. i18n: ########################################
..

Object: Dangers Product (product.danger)
########################################

.. i18n: :libelle: libelle, char, required
..

:libelle: libelle, char, required

.. i18n: :name: Danger, char, required
..

:name: Danger, char, required
