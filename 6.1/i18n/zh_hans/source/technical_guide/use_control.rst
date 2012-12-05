
.. i18n: .. module:: use_control
.. i18n:     :synopsis: On Demand Open Object - Subscription Control 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: use_control
    :synopsis: On Demand Open Object - Subscription Control 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/use_control"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/use_control"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: On Demand Open Object - Subscription Control (*use_control*)
.. i18n: ============================================================
.. i18n: :Module: use_control
.. i18n: :Name: On Demand Open Object - Subscription Control
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Tiny
.. i18n: :Directory: use_control
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

On Demand Open Object - Subscription Control (*use_control*)
============================================================
:Module: use_control
:Name: On Demand Open Object - Subscription Control
:Version: 5.0.1.1
:Author: Tiny
:Directory: use_control
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
.. i18n:   This module provides reports to control your on demand subscription.
.. i18n:   You can not uninstall or delete it.
..

::

  This module provides reports to control your on demand subscription.
  You can not uninstall or delete it.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n: (No download links available)
..

(No download links available)

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

.. i18n:  * Administration/On Demand Control
.. i18n:  * Administration/On Demand Control/Hours per User
.. i18n:  * Administration/On Demand Control/Hours per Month
..

 * Administration/On Demand Control
 * Administration/On Demand Control/Hours per User
 * Administration/On Demand Control/Hours per Month

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * use.control.time.month.user.graph (graph)
.. i18n:  * use.control.time.month.user.form (form)
.. i18n:  * use.control.time.month.user.tree (tree)
.. i18n:  * use.control.time.month.graph (graph)
.. i18n:  * use.control.time.month.tree (tree)
..

 * use.control.time.month.user.graph (graph)
 * use.control.time.month.user.form (form)
 * use.control.time.month.user.tree (tree)
 * use.control.time.month.graph (graph)
 * use.control.time.month.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: use.control.time (use.control.time)
.. i18n: ###########################################
..

Object: use.control.time (use.control.time)
###########################################

.. i18n: :date: Date, datetime
..

:date: Date, datetime

.. i18n: :duration: Duration, float
..

:duration: Duration, float

.. i18n: :user_id: User, many2one
..

:user_id: User, many2one

.. i18n: :uploaded: Uploaded, boolean
..

:uploaded: Uploaded, boolean

.. i18n: Object: Time of Use per Month (use.control.time.month.user)
.. i18n: ###########################################################
..

Object: Time of Use per Month (use.control.time.month.user)
###########################################################

.. i18n: :date: Month, date
..

:date: Month, date

.. i18n: :duration: Duration, float
..

:duration: Duration, float

.. i18n: :user_id: User, many2one
..

:user_id: User, many2one

.. i18n: Object: Time of Use per Month (use.control.time.month)
.. i18n: ######################################################
..

Object: Time of Use per Month (use.control.time.month)
######################################################

.. i18n: :date: Month, date
..

:date: Month, date

.. i18n: :duration: Duration, float
..

:duration: Duration, float

.. i18n: Object: Containt the blocking message (use.control.db.block)
.. i18n: ############################################################
..

Object: Containt the blocking message (use.control.db.block)
############################################################

.. i18n: :name: Block message, text
..

:name: Block message, text
