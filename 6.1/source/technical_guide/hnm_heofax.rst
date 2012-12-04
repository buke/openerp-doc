
.. module:: hnm_heofax
    :synopsis: HeoFAX 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

HeoFAX (*hnm_heofax*)
=====================
:Module: hnm_heofax
:Name: HeoFAX
:Version: 0.01
:Author: Heonium
:Directory: hnm_heofax
:Web: http://www.heonium.com/contributions/developpement/envoyer-des-fax-avec-openerptinyerp.html
:Official module: no
:Quality certified: no

Description
-----------

::

  Add a possibility (wizard) to FAX any documents (PDF/PS/Text) from OpenERP.
  It get fax number and other information from OpenERP's partners database. To use this module
  YOU NEED to decompress it in 'addons' directory. This is because you need to have a 'coverpage'
  directory accessible to use it
  
  Currently you can
  ---------------
  - Send PDF/PS/TIFF documents (only one by one) from partner environment
  to one or more recipient (mass fax mailing) (beware to disk space on hylafax
  server).
  - Send sale documents directly by FAX.
  - Using or not FaxCover when sending.
  - Define FaxCover by user or group.
  - Chose FaxCover when you send fax.
  - Possibility to record this operation in partner event.
  - You receive by mail the status of your send (success or error)
  - Send by fax sales doc. (sale order, confirmation order,  ...).'
  - Send by fax purchases doc. (purchase order, confirmation purchase order,  ...).'
  
  Install
  -------
  See README for details.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/hnm_heofax.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hnm_heofax.zip>`_

 			

Dependencies
------------

 * :mod:`base`
 * :mod:`sale`
 * :mod:`purchase`

Reports
-------

None


Menus
-------


None


Views
-----


None



Objects
-------

None
