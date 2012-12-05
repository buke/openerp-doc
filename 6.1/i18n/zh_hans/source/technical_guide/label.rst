
.. i18n: .. module:: label
.. i18n:     :synopsis: Partner labels 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: label
    :synopsis: Partner labels 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/label"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/label"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Partner labels (*label*)
.. i18n: ========================
.. i18n: :Module: label
.. i18n: :Name: Partner labels
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Zikzakmedia SL
.. i18n: :Directory: label
.. i18n: :Web: www.zikzakmedia.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Partner labels (*label*)
========================
:Module: label
:Name: Partner labels
:Version: 5.0.1.0
:Author: Zikzakmedia SL
:Directory: label
:Web: www.zikzakmedia.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Flexible partner labels:
.. i18n:     * Definition of page sizes, label manufacturers and label formats
.. i18n:     * Flexible label formats (page size, portrait or landscape, manufacturer, rows, columns, width, height, top margin, left margin, ...)
.. i18n:     * Initial data for page sizes and label formats (from Avery and Apli manufacturers)
.. i18n:     * Wizard to print labels. The label format, the printer margins, the font type and size, the first label (row and column) to print on the first page can be set.
..

::

  Flexible partner labels:
    * Definition of page sizes, label manufacturers and label formats
    * Flexible label formats (page size, portrait or landscape, manufacturer, rows, columns, width, height, top margin, left margin, ...)
    * Initial data for page sizes and label formats (from Avery and Apli manufacturers)
    * Wizard to print labels. The label format, the printer margins, the font type and size, the first label (row and column) to print on the first page can be set.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/label.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/label.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/label.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/label.zip>`_

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

.. i18n:  * Partners/Configuration/Page Sizes
.. i18n:  * Partners/Configuration/Label Manufacturers
.. i18n:  * Partners/Configuration/Label Formats
..

 * Partners/Configuration/Page Sizes
 * Partners/Configuration/Label Manufacturers
 * Partners/Configuration/Label Formats

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * report.pagesize.tree (tree)
.. i18n:  * report.pagesize (form)
.. i18n:  * report.label.tree (tree)
.. i18n:  * report.label (form)
..

 * report.pagesize.tree (tree)
 * report.pagesize (form)
 * report.label.tree (tree)
 * report.label (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: report.pagesize (report.pagesize)
.. i18n: #########################################
..

Object: report.pagesize (report.pagesize)
#########################################

.. i18n: :width: Width, char, required
..

:width: Width, char, required

.. i18n:     *Numeric width of the page ended with the unit (cm or in). For example, A4 is 21cm and letter is 8.5in*
..

    *Numeric width of the page ended with the unit (cm or in). For example, A4 is 21cm and letter is 8.5in*

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :height: Height, char, required
..

:height: Height, char, required

.. i18n:     *Numeric height of the page ended with the unit (cm or in). For example, A4 is 29.7cm and letter is 11in*
..

    *Numeric height of the page ended with the unit (cm or in). For example, A4 is 29.7cm and letter is 11in*

.. i18n: Object: report.label.manufacturer (report.label.manufacturer)
.. i18n: #############################################################
..

Object: report.label.manufacturer (report.label.manufacturer)
#############################################################

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: report.label (report.label)
.. i18n: ###################################
..

Object: report.label (report.label)
###################################

.. i18n: :rows: Number of Rows, integer, required
..

:rows: Number of Rows, integer, required

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: :label_height: Label Height, char, required
..

:label_height: Label Height, char, required

.. i18n:     *Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*
..

    *Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*

.. i18n: :label_width: Label Width, char, required
..

:label_width: Label Width, char, required

.. i18n:     *Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*
..

    *Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*

.. i18n: :pagesize_id: Page Size, many2one, required
..

:pagesize_id: Page Size, many2one, required

.. i18n: :cols: Number of Columns, integer, required
..

:cols: Number of Columns, integer, required

.. i18n: :width_incr: Width Increment, char, required
..

:width_incr: Width Increment, char, required

.. i18n:     *Width between start positions of 2 labels. Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*
..

    *Width between start positions of 2 labels. Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*

.. i18n: :margin_top: Top Margin, char, required
..

:margin_top: Top Margin, char, required

.. i18n:     *Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*
..

    *Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*

.. i18n: :margin_left: Left Margin, char, required
..

:margin_left: Left Margin, char, required

.. i18n:     *Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*
..

    *Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*

.. i18n: :height_incr: Height Increment, char, required
..

:height_incr: Height Increment, char, required

.. i18n:     *Height between start positions of 2 labels. Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*
..

    *Height between start positions of 2 labels. Numeric value ended with the unit (cm or in). For example 29.7cm or 11in*

.. i18n: :manufacturer_id: Manufacturer, many2one
..

:manufacturer_id: Manufacturer, many2one

.. i18n: :landscape: Landscape, boolean
..

:landscape: Landscape, boolean

.. i18n:     *No check -> Portrait. Check -> Landscape*
..

    *No check -> Portrait. Check -> Landscape*

.. i18n: :name: Name, char, required
..

:name: Name, char, required
