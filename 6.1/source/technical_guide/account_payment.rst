
.. i18n: .. module:: account_payment
.. i18n:     :synopsis: Payment Management (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_payment
    :synopsis: Payment Management (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_payment"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_payment"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Payment Management (*account_payment*)
.. i18n: ======================================
.. i18n: :Module: account_payment
.. i18n: :Name: Payment Management
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Tiny
.. i18n: :Directory: account_payment
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Payment Management (*account_payment*)
======================================
:Module: account_payment
:Name: Payment Management
:Version: 5.0.1.1
:Author: Tiny
:Directory: account_payment
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
.. i18n:   This module provide :
.. i18n:       * a more efficient way to manage invoice payment.
.. i18n:       * a basic mechanism to easily plug various automated payment.
..

::

  This module provide :
      * a more efficient way to manage invoice payment.
      * a basic mechanism to easily plug various automated payment.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/account_payment.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/account_payment.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/account_payment.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/account_payment.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/account_payment.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_payment.zip>`_

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

.. i18n:  * Payment Order
..

 * Payment Order

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Financial Management/Payment
.. i18n:  * Financial Management/Configuration/Payment
.. i18n:  * Financial Management/Configuration/Payment/Payment Mode
.. i18n:  * Financial Management/Payment/Payment Orders
.. i18n:  * Financial Management/Payment/Payment Orders/Draft Payment Order
.. i18n:  * Financial Management/Payment/Payment Orders/Payment Orders to Validate
.. i18n:  * Financial Management/Payment/Payment Orders/New Payment Order
..

 * Financial Management/Payment
 * Financial Management/Configuration/Payment
 * Financial Management/Configuration/Payment/Payment Mode
 * Financial Management/Payment/Payment Orders
 * Financial Management/Payment/Payment Orders/Draft Payment Order
 * Financial Management/Payment/Payment Orders/Payment Orders to Validate
 * Financial Management/Payment/Payment Orders/New Payment Order

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT account.move.line.form.inherit (form)
.. i18n:  * account.move.line.tree (tree)
.. i18n:  * payment.type.form (form)
.. i18n:  * payment.mode.tree (tree)
.. i18n:  * payment.mode.form (form)
.. i18n:  * payment.order.form (form)
.. i18n:  * payment.order.tree (tree)
.. i18n:  * Payment Line (form)
.. i18n:  * Payment Lines (tree)
.. i18n:  * \* INHERIT account.bank.statement.form.inherit (form)
.. i18n:  * \* INHERIT account.invoice.supplier.form.inherit (form)
..

 * \* INHERIT account.move.line.form.inherit (form)
 * account.move.line.tree (tree)
 * payment.type.form (form)
 * payment.mode.tree (tree)
 * payment.mode.form (form)
 * payment.order.form (form)
 * payment.order.tree (tree)
 * Payment Line (form)
 * Payment Lines (tree)
 * \* INHERIT account.bank.statement.form.inherit (form)
 * \* INHERIT account.invoice.supplier.form.inherit (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Payment type (payment.type)
.. i18n: ###################################
..

Object: Payment type (payment.type)
###################################

.. i18n: :suitable_bank_types: Suitable bank types, many2many
..

:suitable_bank_types: Suitable bank types, many2many

.. i18n: :code: Code, char, required
..

:code: Code, char, required

.. i18n:     *Specify the Code for Payment Type*
..

    *Specify the Code for Payment Type*

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n:     *Payment Type*
..

    *Payment Type*

.. i18n: Object: Payment mode (payment.mode)
.. i18n: ###################################
..

Object: Payment mode (payment.mode)
###################################

.. i18n: :journal: Journal, many2one, required
..

:journal: Journal, many2one, required

.. i18n:     *Cash Journal for the Payment Mode*
..

    *Cash Journal for the Payment Mode*

.. i18n: :type: Payment type, many2one, required
..

:type: Payment type, many2one, required

.. i18n:     *Select the Payment Type for the Payment Mode.*
..

    *Select the Payment Type for the Payment Mode.*

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n:     *Mode of Payment*
..

    *Mode of Payment*

.. i18n: :bank_id: Bank account, many2one, required
..

:bank_id: Bank account, many2one, required

.. i18n:     *Bank Account for the Payment Mode*
..

    *Bank Account for the Payment Mode*

.. i18n: Object: Payment Order (payment.order)
.. i18n: #####################################
..

Object: Payment Order (payment.order)
#####################################

.. i18n: :date_prefered: Preferred date, selection, required
..

:date_prefered: Preferred date, selection, required

.. i18n:     *Choose an option for the Payment Order:'Fixed' stands for a date specified by you.'Directly' stands for the direct execution.'Due date' stands for the scheduled date of execution.*
..

    *Choose an option for the Payment Order:'Fixed' stands for a date specified by you.'Directly' stands for the direct execution.'Due date' stands for the scheduled date of execution.*

.. i18n: :user_id: User, many2one, required
..

:user_id: User, many2one, required

.. i18n: :date_done: Execution date, date, readonly
..

:date_done: Execution date, date, readonly

.. i18n: :reference: Reference, char, required
..

:reference: Reference, char, required

.. i18n: :date_planned: Scheduled date if fixed, date
..

:date_planned: Scheduled date if fixed, date

.. i18n:     *Select a date if you have chosen Preferred Date to be fixed.*
..

    *Select a date if you have chosen Preferred Date to be fixed.*

.. i18n: :state: State, selection
..

:state: State, selection

.. i18n: :mode: Payment mode, many2one, required
..

:mode: Payment mode, many2one, required

.. i18n:     *Select the Payment Mode to be applied.*
..

    *Select the Payment Mode to be applied.*

.. i18n: :date_created: Creation date, date, readonly
..

:date_created: Creation date, date, readonly

.. i18n: :line_ids: Payment lines, one2many
..

:line_ids: Payment lines, one2many

.. i18n: :total: Total, float, readonly
..

:total: Total, float, readonly

.. i18n: Object: Payment Line (payment.line)
.. i18n: ###################################
..

Object: Payment Line (payment.line)
###################################

.. i18n: :company_currency: Company Currency, many2one, readonly
..

:company_currency: Company Currency, many2one, readonly

.. i18n: :ml_inv_ref: Invoice Ref., many2one, readonly
..

:ml_inv_ref: Invoice Ref., many2one, readonly

.. i18n: :create_date: Created, datetime, readonly
..

:create_date: Created, datetime, readonly

.. i18n: :name: Your Reference, char, required
..

:name: Your Reference, char, required

.. i18n: :state: Communication Type, selection, required
..

:state: Communication Type, selection, required

.. i18n: :order_id: Order, many2one, required
..

:order_id: Order, many2one, required

.. i18n: :communication: Communication, char, required
..

:communication: Communication, char, required

.. i18n:     *Used as the message between ordering customer and current company. Depicts 'What do you want to say to the recipient about this order ?'*
..

    *Used as the message between ordering customer and current company. Depicts 'What do you want to say to the recipient about this order ?'*

.. i18n: :bank_id: Destination Bank account, many2one
..

:bank_id: Destination Bank account, many2one

.. i18n: :communication2: Communication 2, char
..

:communication2: Communication 2, char

.. i18n:     *The successor message of Communication.*
..

    *The successor message of Communication.*

.. i18n: :currency: Partner Currency, many2one, required
..

:currency: Partner Currency, many2one, required

.. i18n: :amount: Amount in Company Currency, float, readonly
..

:amount: Amount in Company Currency, float, readonly

.. i18n:     *Payment amount in the company currency*
..

    *Payment amount in the company currency*

.. i18n: :info_partner: Destination Account, text, readonly
..

:info_partner: Destination Account, text, readonly

.. i18n:     *Address of the Ordering Customer.*
..

    *Address of the Ordering Customer.*

.. i18n: :date: Payment Date, date
..

:date: Payment Date, date

.. i18n:     *If no payment date is specified, the bank will treat this payment line directly*
..

    *If no payment date is specified, the bank will treat this payment line directly*

.. i18n: :ml_date_created: Effective Date, date, readonly
..

:ml_date_created: Effective Date, date, readonly

.. i18n:     *Invoice Effective Date*
..

    *Invoice Effective Date*

.. i18n: :move_line_id: Entry line, many2one
..

:move_line_id: Entry line, many2one

.. i18n:     *This Entry Line will be referred for the information of the ordering customer.*
..

    *This Entry Line will be referred for the information of the ordering customer.*

.. i18n: :info_owner: Owner Account, text, readonly
..

:info_owner: Owner Account, text, readonly

.. i18n:     *Address of the Main Partner*
..

    *Address of the Main Partner*

.. i18n: :amount_currency: Amount in Partner Currency, float, required
..

:amount_currency: Amount in Partner Currency, float, required

.. i18n:     *Payment amount in the partner currency*
..

    *Payment amount in the partner currency*

.. i18n: :partner_id: Partner, many2one, required
..

:partner_id: Partner, many2one, required

.. i18n:     *The Ordering Customer*
..

    *The Ordering Customer*

.. i18n: :ml_maturity_date: Maturity Date, date, readonly
..

:ml_maturity_date: Maturity Date, date, readonly
