
.. i18n: .. module:: base_module_quality
.. i18n:     :synopsis: Base module quality (Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: base_module_quality
    :synopsis: Base module quality (Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_module_quality"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_module_quality"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Base module quality (*base_module_quality*)
.. i18n: ===========================================
.. i18n: :Module: base_module_quality
.. i18n: :Name: Base module quality
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: base_module_quality
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: yes
..

Base module quality (*base_module_quality*)
===========================================
:Module: base_module_quality
:Name: Base module quality
:Version: 5.0.1.0
:Author: Tiny
:Directory: base_module_quality
:Web: http://www.openerp.com
:Official module: no
:Quality certified: yes

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module's aim is to check the quality of other modules.
.. i18n:   
.. i18n:   It defines a wizard on the list of modules in OpenERP, which allow you to
.. i18n:   evaluate them on different criteria such as: the respect of OpenERP coding
.. i18n:   standards, the speed efficiency...
.. i18n:   
.. i18n:   This module also provides generic framework to define your own quality test.
.. i18n:   For further info, coders may take a look into base_module_quality\README.txt
.. i18n:   
.. i18n:   WARNING: This module can not work as a ZIP file, you must unzip it before
.. i18n:   using it, otherwise it may crash.
..

::

  This module's aim is to check the quality of other modules.
  
  It defines a wizard on the list of modules in OpenERP, which allow you to
  evaluate them on different criteria such as: the respect of OpenERP coding
  standards, the speed efficiency...
  
  This module also provides generic framework to define your own quality test.
  For further info, coders may take a look into base_module_quality\README.txt
  
  WARNING: This module can not work as a ZIP file, you must unzip it before
  using it, otherwise it may crash.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/base_module_quality.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/base_module_quality.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/base_module_quality.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/base_module_quality.zip>`_

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

.. i18n:  * Results of Quality Checks (tree)
.. i18n:  * Results of Quality Checks (form)
.. i18n:  * Results of Quality Checks with detail (form)
.. i18n:  * Results of Quality Checks with detail (tree)
..

 * Results of Quality Checks (tree)
 * Results of Quality Checks (form)
 * Results of Quality Checks with detail (form)
 * Results of Quality Checks with detail (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: module.quality.check (module.quality.check)
.. i18n: ###################################################
..

Object: module.quality.check (module.quality.check)
###################################################

.. i18n: :final_score: Final Score (%), char
..

:final_score: Final Score (%), char

.. i18n: :name: Rated Module, char
..

:name: Rated Module, char

.. i18n: :check_detail_ids: Tests, one2many
..

:check_detail_ids: Tests, one2many

.. i18n: Object: module.quality.detail (module.quality.detail)
.. i18n: #####################################################
..

Object: module.quality.detail (module.quality.detail)
#####################################################

.. i18n: :name: Name, char
..

:name: Name, char

.. i18n: :detail: Details, text
..

:detail: Details, text

.. i18n: :summary: Summary, text
..

:summary: Summary, text

.. i18n: :note: Note, text
..

:note: Note, text

.. i18n: :state: State, selection
..

:state: State, selection

.. i18n:     *The test will be completed only if the module is installed or if the test may be processed on uninstalled module.*
..

    *The test will be completed only if the module is installed or if the test may be processed on uninstalled module.*

.. i18n: :score: Score (%), float
..

:score: Score (%), float

.. i18n: :quality_check_id: Quality, many2one
..

:quality_check_id: Quality, many2one

.. i18n: :ponderation: Ponderation, float
..

:ponderation: Ponderation, float

.. i18n:     *Some tests are more critical than others, so they have a bigger weight in the computation of final rating*
..

    *Some tests are more critical than others, so they have a bigger weight in the computation of final rating*

.. i18n: :message: Message, char
..

:message: Message, char
