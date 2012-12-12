
.. i18n: .. module:: sale_advertising
.. i18n:     :synopsis: Sales: Advertising Sales 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: sale_advertising
    :synopsis: Sales: Advertising Sales 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_advertising"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_advertising"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Sales: Advertising Sales (*sale_advertising*)
.. i18n: =============================================
.. i18n: :Module: sale_advertising
.. i18n: :Name: Sales: Advertising Sales
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Tiny
.. i18n: :Directory: sale_advertising
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Sales: Advertising Sales (*sale_advertising*)
=============================================
:Module: sale_advertising
:Name: Sales: Advertising Sales
:Version: 5.0.0.1
:Author: Tiny
:Directory: sale_advertising
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
.. i18n:   This module allow you to use the Sale Management to encode your advertising sales ... TODO
..

::

  This module allow you to use the Sale Management to encode your advertising sales ... TODO

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/sale_advertising.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/sale_advertising.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/sale_advertising.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/sale_advertising.zip>`_

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

.. i18n:  * Sales Management/Advertising
.. i18n:  * Sales Management/Advertising/Advertising Issue
.. i18n:  * Sales Management/Advertising/Advertising Proof
.. i18n:  * Sales Management/Advertising/All Advertising Sale Orders
..

 * Sales Management/Advertising
 * Sales Management/Advertising/Advertising Issue
 * Sales Management/Advertising/Advertising Proof
 * Sales Management/Advertising/All Advertising Sale Orders

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT sale.order.form.inherit (form)
.. i18n:  * \* INHERIT sale.order.form.inherit.line (form)
.. i18n:  * \* INHERIT sale.order.line.form.inherit.line2 (form)
.. i18n:  * sale.advertising.issue.form (form)
.. i18n:  * sale.advertising.issue.tree (tree)
.. i18n:  * sale.advertising.proof.form (form)
.. i18n:  * sale.advertising.proof.tree (tree)
.. i18n:  * \* INHERIT product.product.form.inherit (form)
..

 * \* INHERIT sale.order.form.inherit (form)
 * \* INHERIT sale.order.form.inherit.line (form)
 * \* INHERIT sale.order.line.form.inherit.line2 (form)
 * sale.advertising.issue.form (form)
 * sale.advertising.issue.tree (tree)
 * sale.advertising.proof.form (form)
 * sale.advertising.proof.tree (tree)
 * \* INHERIT product.product.form.inherit (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Sale Advertising Issue (sale.advertising.issue)
.. i18n: #######################################################
..

Object: Sale Advertising Issue (sale.advertising.issue)
#######################################################

.. i18n: :issue_date: Issue Date, date, required
..

:issue_date: Issue Date, date, required

.. i18n: :medium: Medium, many2one, required
..

:medium: Medium, many2one, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :default_note: Default Note, text
..

:default_note: Default Note, text

.. i18n: :state: State, selection
..

:state: State, selection

.. i18n: Object: Sale Advertising Proof (sale.advertising.proof)
.. i18n: #######################################################
..

Object: Sale Advertising Proof (sale.advertising.proof)
#######################################################

.. i18n: :address_id: Delivery Address, many2one, required
..

:address_id: Delivery Address, many2one, required

.. i18n: :target_id: Target, many2one, required
..

:target_id: Target, many2one, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :number: Number of Copies, integer, required
..

:number: Number of Copies, integer, required
