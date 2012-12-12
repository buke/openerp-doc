
.. module:: chemical
    :synopsis: Module for Chemical Industries (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/chemical"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  Module for Chemical Industries

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/chemical.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/chemical.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`
 * :mod:`stock`

Reports
-------

None


Menus
-------

 * Products/Configuration/Chimie
 * Products/Configuration/Chimie/product risque
 * Products/Configuration/Chimie/product securite
 * Products/Configuration/Chimie/product danger

Views
-----

 * \* INHERIT product.normal.form (form)
 * product.risque.tree (tree)
 * product.risque.form (form)
 * product.securite.tree (tree)
 * product.securite.form (form)
 * product.danger.tree (tree)
 * product.danger.form (form)


Objects
-------

Object: Risques Produits (product.risque)
#########################################



:libelle: libelle, char, required





:name: Risque, char, required




Object: Securite Produits (product.securite)
############################################



:libelle: libelle, char, required





:name: Security, char, required




Object: Dangers Product (product.danger)
########################################



:libelle: libelle, char, required





:name: Danger, char, required


