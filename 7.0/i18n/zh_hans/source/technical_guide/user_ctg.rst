
.. i18n: .. module:: user_ctg
.. i18n:     :synopsis: user_ctg 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: user_ctg
    :synopsis: user_ctg 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/user_ctg"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/user_ctg"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: CTG points Management (*user_ctg*)
.. i18n: ==================================
..

CTG points Management (*user_ctg*)
==================================

.. i18n: :Module: user_ctg
.. i18n: :Name: CTG points Management
.. i18n: :Version: 0.0.5
.. i18n: :Author: Tiny
.. i18n: :Directory: user_ctg
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

:Module: user_ctg
:Name: CTG points Management
:Version: 0.0.5
:Author: Tiny
:Directory: user_ctg
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: This Module is managed User CTG points (called CTG points as 'Contribution To Growth points') for * DMS: Added CTG points to Document's Author  when sent feedback by other people after downloading document through the DMS * Developments: Added CTG points to Developer  based on LP karma  * Marketing: Added CTG points to Marketing  base on number of incoming visitors on our website * Sales: Added CTG points to Saleman  that sold something and points accordingly to amount sold * Customer Satisfaction: Added CTG points to responsible person of project when customer send feedback for a service/an integration  
..

This Module is managed User CTG points (called CTG points as 'Contribution To Growth points') for * DMS: Added CTG points to Document's Author  when sent feedback by other people after downloading document through the DMS * Developments: Added CTG points to Developer  based on LP karma  * Marketing: Added CTG points to Marketing  base on number of incoming visitors on our website * Sales: Added CTG points to Saleman  that sold something and points accordingly to amount sold * Customer Satisfaction: Added CTG points to responsible person of project when customer send feedback for a service/an integration  

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/user_ctg.zip>`_ 
..

  * `trunk <http://www.openerp.com/download/modules/trunk/user_ctg.zip>`_ 

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:   * :mod:`base`
.. i18n:   * :mod:`sale`
.. i18n:   * :mod:`document`
.. i18n:   * :mod:`account_invoice_salesman`
.. i18n:   * :mod:`project`
..

  * :mod:`base`
  * :mod:`sale`
  * :mod:`document`
  * :mod:`account_invoice_salesman`
  * :mod:`project`

.. i18n: Reports
.. i18n: -------
.. i18n: None
..

Reports
-------
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

.. i18n:   * ctg.type.tree (tree)
.. i18n:   * ctg.type.form (form)
.. i18n:   * ctg.line.tree (tree)
.. i18n:   * ctg.line.form (form)
.. i18n:   * \* INHERIT users.inherit.form (form)
.. i18n:   * \* INHERIT users.inherit.form (form)
.. i18n:   * report.ctg.line.tree (tree)
.. i18n:   * report.ctg.line.form (form)
.. i18n:   * CTG Line -Graph (graph)
.. i18n:   * ctg.feedback.tree (tree)
.. i18n:   * ctg.feedback.form (form)
.. i18n:   * user.history.tree (tree)
.. i18n:   * user.history.form (form)
..

  * ctg.type.tree (tree)
  * ctg.type.form (form)
  * ctg.line.tree (tree)
  * ctg.line.form (form)
  * \* INHERIT users.inherit.form (form)
  * \* INHERIT users.inherit.form (form)
  * report.ctg.line.tree (tree)
  * report.ctg.line.form (form)
  * CTG Line -Graph (graph)
  * ctg.feedback.tree (tree)
  * ctg.feedback.form (form)
  * user.history.tree (tree)
  * user.history.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n:   * ctg.line
.. i18n:   * report.ctg.line
.. i18n:   * ctg.feedback
..

  * ctg.line
  * report.ctg.line
  * ctg.feedback
