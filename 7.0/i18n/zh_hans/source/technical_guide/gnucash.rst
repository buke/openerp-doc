
.. i18n: .. module:: gnucash
.. i18n:     :synopsis: Module for Import from file 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: gnucash
    :synopsis: Module for Import from file 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/gnucash"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/gnucash"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Module for Import from file (*gnucash*)
.. i18n: =======================================
.. i18n: :Module: gnucash
.. i18n: :Name: Module for Import from file
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: P. Christeas
.. i18n: :Directory: gnucash
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Module for Import from file (*gnucash*)
=======================================
:Module: gnucash
:Name: Module for Import from file
:Version: 5.0.0.1
:Author: P. Christeas
:Directory: gnucash
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
.. i18n:   Gnucash Import from file
..

::

  Gnucash Import from file

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/gnucash.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/gnucash.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/gnucash.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/gnucash.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`product`
..

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`

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

.. i18n:  * Administration/GnuCash
.. i18n:  * Administration/GnuCash/Gnucash Mappings
.. i18n:  * Administration/GnuCash/Import GnuCash File
..

 * Administration/GnuCash
 * Administration/GnuCash/Gnucash Mappings
 * Administration/GnuCash/Import GnuCash File

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * gnucash.index.form (form)
.. i18n:  * gnucash.index.tree (tree)
..

 * gnucash.index.form (form)
 * gnucash.index.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: gnucash.index (gnucash.index)
.. i18n: #####################################
..

Object: gnucash.index (gnucash.index)
#####################################

.. i18n: :noupdate: Non Updatable, boolean
..

:noupdate: Non Updatable, boolean

.. i18n: :parent_book: Parent book, many2one
..

:parent_book: Parent book, many2one

.. i18n: :date_init: Init Date, datetime
..

:date_init: Init Date, datetime

.. i18n: :date_update: Update Date, datetime
..

:date_update: Update Date, datetime

.. i18n: :module: Module, char, required
..

:module: Module, char, required

.. i18n: :to_delete: Should be deleted, boolean, required
..

:to_delete: Should be deleted, boolean, required

.. i18n: :model: Object, char, required
..

:model: Object, char, required

.. i18n: :guid: Gnucash UID, char, required
..

:guid: Gnucash UID, char, required

.. i18n: :res_id: Resource ID, integer
..

:res_id: Resource ID, integer
