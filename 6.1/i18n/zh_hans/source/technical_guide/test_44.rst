
.. i18n: .. module:: test_44
.. i18n:     :synopsis: Test New Features 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: test_44
    :synopsis: Test New Features 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/test_44"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/test_44"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Test New Features (*test_44*)
.. i18n: =============================
.. i18n: :Module: test_44
.. i18n: :Name: Test New Features
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: test_44
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   The module adds google map field in partner address
.. i18n:   so that we can directly open google map from the
.. i18n:   url widget.
..

::

  The module adds google map field in partner address
  so that we can directly open google map from the
  url widget.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/test_44.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/test_44.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/test_44.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/test_44.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`sale`
..

 * :mod:`base`
 * :mod:`sale`

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

.. i18n:  * Testing
.. i18n:  * Testing/Testing
..

 * Testing
 * Testing/Testing

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * Testing Temporal Data (form)
..

 * Testing Temporal Data (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: test.temporal (test.temporal)
.. i18n: #####################################
..

Object: test.temporal (test.temporal)
#####################################

.. i18n: :line_ids: Lines, one2many
..

:line_ids: Lines, one2many

.. i18n: :state: State, selection
..

:state: State, selection

.. i18n: :partner_id: Partner, many2one
..

:partner_id: Partner, many2one

.. i18n: :partner_ids: Partners, many2many
..

:partner_ids: Partners, many2many

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: test.temporal.line (test.temporal.line)
.. i18n: ###############################################
..

Object: test.temporal.line (test.temporal.line)
###############################################

.. i18n: :temporal_id: Temporal, many2one
..

:temporal_id: Temporal, many2one

.. i18n: :length: Size, integer
..

:length: Size, integer

.. i18n: :name: Name, char, required
..

:name: Name, char, required
