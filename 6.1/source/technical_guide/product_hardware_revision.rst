
.. module:: product_hardware_revision
    :synopsis: Product Hardware Revision 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

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

Description
-----------

::

  Product Hardware Revision: every product can have n revisions and
  also have a current default revision. Then when receiving a product, in the incoming picking,
  if a stock.production.lot (eg serial number here) is to be created, then a first line of stock.production.lot.revision
  is created in the stock.production.lot with values copied from the product default revision.
  The user can still choose an other revision manually before it gets copied. This is really useful
  to track the exact hardware of a product with electronic products fro instance. 
      
Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_hardware_revision.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_hardware_revision.zip>`_

Dependencies
------------

 * :mod:`product`
 * :mod:`stock`
 * :mod:`mrp_prodlot_autosplit`

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
