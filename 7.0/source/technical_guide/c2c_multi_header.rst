
.. module:: c2c_multi_header
    :synopsis: c2c_multi_header 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_multi_header"></div>
    <script src="http://js-kit.com/ratings.js"></script>

c2c_multi_header (*c2c_multi_header*)
=====================================
:Module: c2c_multi_header
:Name: c2c_multi_header
:Version: 5.0.1.0
:Author: Camptocamp SA
:Directory: c2c_multi_header
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  c2c_multi_header

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Administration/Users/Company's Structure/Header IMG
 * Administration/Users/Company's Structure/Header RML

Views
-----

 * \* INHERIT res.company.form.inherit (form)
 * res.company.header.img (form)
 * res.company.header.rml (form)


Objects
-------

Object: c2c.header_rml (c2c.header_rml)
#######################################



:name: Name, char, required





:rml: RML, text




Object: c2c.header_img (c2c.header_img)
#######################################



:name: Name, char, required





:img: Image, binary


