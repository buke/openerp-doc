
.. i18n: .. module:: edi
.. i18n:     :synopsis: EDI 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: edi
    :synopsis: EDI 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/edi"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/edi"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: EDI (*edi*)
.. i18n: ===========
.. i18n: :Module: edi
.. i18n: :Name: EDI
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: edi
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

EDI (*edi*)
===========
:Module: edi
:Name: EDI
:Version: 5.0.1.0
:Author: Tiny
:Directory: edi
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
.. i18n:   Used for the communication with others proprietary ERP's. Has been tested in the food industries process, communicating with SAP. This module is able to import order and export delivery notes.
..

::

  Used for the communication with others proprietary ERP's. Has been tested in the food industries process, communicating with SAP. This module is able to import order and export delivery notes.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/edi.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/edi.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/edi.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/edi.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`sale`
..

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

.. i18n:  * Sales Management/Edi
.. i18n:  * Sales Management/Edi/View Logs
..

 * Sales Management/Edi
 * Sales Management/Edi/View Logs

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * edi.log.line.tree (tree)
.. i18n:  * edi.log.tree (tree)
.. i18n:  * edi.log.form (form)
.. i18n:  * \* INHERIT sale.order.form.pvc (form)
.. i18n:  * \* INHERIT sale.order.line.form.pvc (form)
..

 * edi.log.line.tree (tree)
 * edi.log.tree (tree)
 * edi.log.form (form)
 * \* INHERIT sale.order.form.pvc (form)
 * \* INHERIT sale.order.line.form.pvc (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: EDI log (edi.log)
.. i18n: #########################
..

Object: EDI log (edi.log)
#########################

.. i18n: :name: Log name, char, required
..

:name: Log name, char, required

.. i18n: :log_line: Log Lines, one2many, readonly
..

:log_line: Log Lines, one2many, readonly

.. i18n: Object: EDI Log Line (edi.log.line)
.. i18n: ###################################
..

Object: EDI Log Line (edi.log.line)
###################################

.. i18n: :sender: Partner, many2one, readonly
..

:sender: Partner, many2one, readonly

.. i18n: :log_id: Log Ref, many2one
..

:log_id: Log Ref, many2one

.. i18n: :timestamp: Order date, char
..

:timestamp: Order date, char

.. i18n: :logdesc: Description, text
..

:logdesc: Description, text

.. i18n: :order_num: Edi Order Id, char
..

:order_num: Edi Order Id, char

.. i18n: :name: Name, char, required
..

:name: Name, char, required
