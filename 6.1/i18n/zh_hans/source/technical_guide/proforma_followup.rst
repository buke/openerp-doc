
.. i18n: .. module:: proforma_followup
.. i18n:     :synopsis: Pro-forma invoices and their payments Management 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: proforma_followup
    :synopsis: Pro-forma invoices and their payments Management 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/proforma_followup"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/proforma_followup"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Pro-forma invoices and their payments Management (*proforma_followup*)
.. i18n: ======================================================================
.. i18n: :Module: proforma_followup
.. i18n: :Name: Pro-forma invoices and their payments Management
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: proforma_followup
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Pro-forma invoices and their payments Management (*proforma_followup*)
======================================================================
:Module: proforma_followup
:Name: Pro-forma invoices and their payments Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: proforma_followup
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
.. i18n:   Once a pro-forma invoice is created, the module sends automatically mail 
.. i18n:           and call actions after X days.
.. i18n:           It's the same principle than account_followup but for proforma invoice only. 
.. i18n:           Only followups by email, no need to do reports. 
.. i18n:           Also, at each steps, we should be able to call several functions. 
.. i18n:           (for example, if a pro-forma is cancelled, it will close a delivery order)
..

::

  Once a pro-forma invoice is created, the module sends automatically mail 
          and call actions after X days.
          It's the same principle than account_followup but for proforma invoice only. 
          Only followups by email, no need to do reports. 
          Also, at each steps, we should be able to call several functions. 
          (for example, if a pro-forma is cancelled, it will close a delivery order)

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/proforma_followup.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/proforma_followup.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/proforma_followup.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/proforma_followup.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account`
..

 * :mod:`account`

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

.. i18n:  * Financial Management/Configuration/Proforma Followups
..

 * Financial Management/Configuration/Proforma Followups

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * proforma.proforma.line.tree (tree)
.. i18n:  * proforma.proforma.line.form (form)
.. i18n:  * proforma.proforma.form (form)
.. i18n:  * account.proforma.tree (tree)
..

 * proforma.proforma.line.tree (tree)
 * proforma.proforma.line.form (form)
 * proforma.proforma.form (form)
 * account.proforma.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: proforma.followup_step (proforma.followup_step)
.. i18n: #######################################################
..

Object: proforma.followup_step (proforma.followup_step)
#######################################################

.. i18n: :proforma_line: Proforma Follow-Up Line, one2many
..

:proforma_line: Proforma Follow-Up Line, one2many

.. i18n: :state: Status, selection
..

:state: Status, selection

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :company_id: Company, many2one
..

:company_id: Company, many2one

.. i18n: Object: PRO-Forma Followup Criteria (proforma.followup.line)
.. i18n: ############################################################
..

Object: PRO-Forma Followup Criteria (proforma.followup.line)
############################################################

.. i18n: :function: Function, char
..

:function: Function, char

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :call_function: Call function?, boolean
..

:call_function: Call function?, boolean

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :args: Arguments, text
..

:args: Arguments, text

.. i18n: :days: Days of delay, integer
..

:days: Days of delay, integer

.. i18n: :email_body: E-mail Body, text
..

:email_body: E-mail Body, text

.. i18n: :send_email: Send E-mail?, boolean
..

:send_email: Send E-mail?, boolean

.. i18n: :cancel_invoice: Cancel Invoice?, boolean
..

:cancel_invoice: Cancel Invoice?, boolean

.. i18n: :model: Object, char
..

:model: Object, char

.. i18n: :followup_id: Proforma step, many2one, required
..

:followup_id: Proforma step, many2one, required

.. i18n: :subject: Subject, char
..

:subject: Subject, char
