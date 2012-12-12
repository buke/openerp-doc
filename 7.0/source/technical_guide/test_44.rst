
.. module:: test_44
    :synopsis: Test New Features 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/test_44"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Test New Features (*test_44*)
=============================
:Module: test_44
:Name: Test New Features
:Version: 5.0.1.0
:Author: Tiny
:Directory: test_44
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  The module adds google map field in partner address
  so that we can directly open google map from the
  url widget.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/test_44.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/test_44.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`sale`

Reports
-------

None


Menus
-------

 * Testing
 * Testing/Testing

Views
-----

 * Testing Temporal Data (form)


Objects
-------

Object: test.temporal (test.temporal)
#####################################



:line_ids: Lines, one2many





:state: State, selection





:partner_id: Partner, many2one





:partner_ids: Partners, many2many





:name: Name, char, required




Object: test.temporal.line (test.temporal.line)
###############################################



:temporal_id: Temporal, many2one





:length: Size, integer





:name: Name, char, required


