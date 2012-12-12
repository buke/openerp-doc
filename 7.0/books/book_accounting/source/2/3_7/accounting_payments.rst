.. index::
   single: payments

Automate your Payments
======================

OpenERP gives you forms to prepare, validate and execute payment orders. This enables you to manage issues such as:

    #.      Payment provided on several due dates.

    #.      Automatic payment dates.

    #.      Separating payment preparation and payment approval in your company.

    #.      Preparing an order during the week containing several payments, then validating a payment order at
            the end of the week.

    #.      Splitting payments depending on the balances available in your various bank accounts.
    
    #.      Printing the Payment Order and send it to the bank.

Supplier Payments
-----------------

.. index::
   single: module; account_payment

To use the tool for managing payment orders you should first install the module :mod:`account_payment` or check the ``Supplier Payment Management`` option from the `Add More Features` Wizard. Supplier Payments are part of the core OpenERP system.

The system lets you enter a series of payments to be carried out from your various bank accounts. Once the different payments have been registered, you can validate the payment orders. During validation you can modify and approve the payment orders.

For example, if you have to pay a supplier's invoice for a large amount you can split the payments amongst several bank accounts according to their available balance. To do this, you can prepare several draft orders and validate them once you are satisfied that the split is correct.

This process can also be regularly scheduled. In some companies, a payment order is kept in ``Draft`` state and payments are added to the draft list each day. At the end of the week, the accountant reviews and confirms all the waiting payment orders.

Once the payment order is confirmed, there is still a validation step for an accountant to carry out.
You could imagine that these orders would be prepared by an accounts clerk, and then approved by a manager to go ahead with payment.

.. tip:: Payment Workflow

        An OpenERP workflow is associated with each payment order. Select a payment order, and
        if you are in the GTK client click :menuselection:`Plugins --> Print workflow` from the top menu.

        You can integrate more complex workflow rules to manage payment orders by adapting the workflow.
        For example, in some companies payments must be approved by a manager under certain cash flow or
        value limit conditions.

.. figure::  images/account_payment_flow61.png
   :scale: 75
   :align: center

   *Payments Workflow*

In small businesses it is usually the same person who enters the payment orders and who validates them. In this case you should just click the two buttons, one after the other, to confirm the payment.

First configure the :guilabel:`Payment Modes` you want to use. Consider these as the bank accounts from which you want to pay your suppliers. This can be a bank account or a credit card account to name some. Go to the menu :menuselection:`Accounting --> Configuration --> Miscellaneous --> Payment Mode`. Enter the name of the Payment mode, choose a bank journal and the related bank account (IBAN or normal bank account).

Some examples are:

* Cheques

* Bank transfer,

* Visa card on a bank account,

* Petty cash.

To enter a payment order, go to the menu :menuselection:`Accounting --> Payment --> Payment Orders` and click ``Create``.

.. figure::  images/account_payment_order.png
   :align: center
   :scale: 80

   *Entering a Payment Order*

OpenERP proposes a reference number for your payment order; this number can also be changed from the :menuselection:`Administration --> Configuration --> Sequences & Identifiers --> Sequences` menu. Use the sequence of the `Payment Order` type if you want to adapt the reference number that will be proposed automatically for each new payment order.

You then have to select a payment mode from the various methods available for your company (cfr. configuring Payment Modes).

The :guilabel:`Preferred date` for the payment allows you to determine when the payments have to be executed:

* ``Due date``: each operation will be effected at the due date specified on the invoice (the default option),

* ``Directly``: the operations will be effected when the orders are validated, i.e. the payment date will be the order validation date,

* ``Fixed date``: you have to specify an effective payment date in the :guilabel:`Scheduled date if fixed` field that follows.

The date is particularly important for the preparation of electronic transfers, because banking interfaces enable you to select a future execution date for each operation. The default option of OpenERP is to pay all invoices automatically at their due date.

.. tip:: Electronic Files

    By default, OpenERP does not provide an electronic payment order.

Now select the invoices to pay. Invoices and advance payments (even when not linked to an actual document) can be entered manually in the payment lines block, but you can also add them automatically. Simply click the :guilabel:`Select Invoices to Pay` button and OpenERP will propose documents according to the specified due date. For each due date you can see:

* the invoice :guilabel:`Payment Date`,

* the reference :guilabel:`Invoice Ref.`,

* the deadline for the invoice,

* the amount to be paid in the partner's default currency.

You can then accept the payment proposed by OpenERP, or select the entries that you will pay or not pay on that order. OpenERP gives you all the necessary information to make a payment decision for each line item:

* account,

* supplier's bank account,

* amount that will be paid,

* amount to pay,

* the supplier,

* total amount owed to the supplier,

* due date,

* date of creation.

You can modify the first three fields on each line: the account, the supplier's bank account and the amount that will be paid. This arrangement is very practical because it gives you complete visibility of all the company's trade payables. You can pay only a part of an invoice, for example,
and in preparing your next payment order OpenERP automatically suggests payment of the remainder owed.

When the payment has been prepared correctly, click :guilabel:`Confirm Payments`. The payment then changes to the \ ``Confirmed``\   state and a new button appears that can be used to start the payment process.

You can print the payment order to send it to the bank by clicking the :guilabel:`Payment Order` at the right side of the screen.

Automatic Reconciliation
------------------------

For automatic reconciliation, you will be asking OpenERP to search for entries to reconcile in a series of accounts. OpenERP tries to find entries for each partner where the amounts correspond.

Depending on the level of complexity that you choose (= power) when you start running the tool, the software could reconcile from two to nine entries at the same time. For example, if you select level 5, OpenERP will reconcile, for instance, three invoices and two payments if the total amounts correspond.
Note that you can also choose a maximum write-off amount, if you allow payment differences to be posted (:guilabel:`Allow write off`).

.. figure::  images/account_reconcile_auto.png
   :scale: 75
   :align: center

   *Automatic Reconciliation*

To start the reconciliation tool, click :menuselection:`Accounting --> Periodical Processing --> Reconciliation --> Automatic Reconciliation`.

A form opens, asking you for the following information:

* :guilabel:`Accounts to Reconcile` : you can select one, several or all reconcilable accounts,

* the dates of the entries to take into consideration (:guilabel:`Starting Date` / :guilabel:`Ending Date`),

* the Reconciliation :guilabel:`Power`  (from \ ``2``\   to \ ``9``\  ),

* checkbox :guilabel:`Allow write off` to determine whether you will allow for payment differences.

* information needed for the adjustment (details for the :guilabel:`Write-Off Move`).

.. note:: Reconciling

        You can reconcile any account, but the most common accounts are:

        * all the Accounts Receivable – your customer accounts of type Debtor,

        * all the Accounts Payable – your supplier accounts of type Creditor.

The write-off option enables you to reconcile entries even if their amounts are not exactly equivalent. For example, OpenERP permits foreign customers whose accounts are in different currencies to have a difference of up to, say, 0.50 units of currency and put the difference in a write-off account.

When you run the wizard, OpenERP will show the reconciliation results in a separate window.

.. index::
   single: adjustment; limit

.. tip:: Limit Write-off Adjustments

        You should not make the adjustment limits too large. Companies that introduced substantial automatic
        write-off adjustments have found that all employee expense reimbursements below the limit were
        written off automatically!
