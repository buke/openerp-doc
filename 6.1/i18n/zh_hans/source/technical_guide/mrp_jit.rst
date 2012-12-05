
.. i18n: .. module:: mrp_jit
.. i18n:     :synopsis: MRP JIT (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: mrp_jit
    :synopsis: MRP JIT (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/mrp_jit"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/mrp_jit"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: MRP JIT (*mrp_jit*)
.. i18n: ===================
.. i18n: :Module: mrp_jit
.. i18n: :Name: MRP JIT
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: mrp_jit
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

MRP JIT (*mrp_jit*)
===================
:Module: mrp_jit
:Name: MRP JIT
:Version: 5.0.1.0
:Author: Tiny
:Directory: mrp_jit
:Web: 
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows Just In Time computation of all procurement.
.. i18n:   
.. i18n:       If you install this module, you will not have to run the regular procurement 
.. i18n:       scheduler anymore (but you still need to run the minimum order point rule 
.. i18n:       scheduler, or for example let it run daily.)
.. i18n:       All procurement orders will be processed immediately, which could in some
.. i18n:       cases entail a small performance impact.
.. i18n:   
.. i18n:       It may also increase your stock size because products are reserved as soon
.. i18n:       as possible and the scheduler time range is not taken into account anymore. 
.. i18n:       In that case, you can not use priorities any more on the different picking.
..

::

  This module allows Just In Time computation of all procurement.
  
      If you install this module, you will not have to run the regular procurement 
      scheduler anymore (but you still need to run the minimum order point rule 
      scheduler, or for example let it run daily.)
      All procurement orders will be processed immediately, which could in some
      cases entail a small performance impact.
  
      It may also increase your stock size because products are reserved as soon
      as possible and the scheduler time range is not taken into account anymore. 
      In that case, you can not use priorities any more on the different picking.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/mrp_jit.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/mrp_jit.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/mrp_jit.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/mrp_jit.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`mrp`
.. i18n:  * :mod:`sale`
..

 * :mod:`mrp`
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

.. i18n: None
..

None

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n: None
..

None

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
