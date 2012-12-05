
.. i18n: .. module:: product_hardware_revision
.. i18n:     :synopsis: Product Hardware Revision 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: product_hardware_revision
    :synopsis: Product Hardware Revision 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />
..

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Product Hardware Revision (*product_hardware_revision*)
.. i18n: =======================================================
.. i18n: :Module: product_hardware_revision
.. i18n: :Name: Product Hardware Revision
.. i18n: :Version: 0.1
.. i18n: :Author: Smile.fr
.. i18n: :Directory: product_hardware_revision
.. i18n: :Web: http://www.smile.fr
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Product Hardware Revision (*product_hardware_revision*)
=======================================================
:Module: product_hardware_revision
:Name: Product Hardware Revision
:Version: 0.1
:Author: Smile.fr
:Directory: product_hardware_revision
:Web: http://www.smile.fr
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Product Hardware Revision: every product can have n revisions and
.. i18n:   also have a current default revision. Then when receiving a product, in the incoming picking,
.. i18n:   if a stock.production.lot (eg serial number here) is to be created, then a first line of stock.production.lot.revision
.. i18n:   is created in the stock.production.lot with values copied from the product default revision.
.. i18n:   The user can still choose an other revision manually before it gets copied. This is really useful
.. i18n:   to track the exact hardware of a product with electronic products fro instance. 
.. i18n:       
.. i18n: Download links
.. i18n: --------------
..

::

  Product Hardware Revision: every product can have n revisions and
  also have a current default revision. Then when receiving a product, in the incoming picking,
  if a stock.production.lot (eg serial number here) is to be created, then a first line of stock.production.lot.revision
  is created in the stock.production.lot with values copied from the product default revision.
  The user can still choose an other revision manually before it gets copied. This is really useful
  to track the exact hardware of a product with electronic products fro instance. 
      
Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/product_hardware_revision.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/product_hardware_revision.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_hardware_revision.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_hardware_revision.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`product`
.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`mrp_prodlot_autosplit`
..

 * :mod:`product`
 * :mod:`stock`
 * :mod:`mrp_prodlot_autosplit`

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
