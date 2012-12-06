.. i18n: .. index::
.. i18n:    single: payable
.. i18n:    single: receivable
.. i18n:    single: creditor
.. i18n:    single: debtor
..

.. index::
   single: payable
   single: receivable
   single: creditor
   single: debtor

.. i18n: Get your Money in
.. i18n: =================
..

获取你的资金
=================

.. i18n: OpenERP provides many tools for managing customer and supplier accounts. In this part we will explain:
..

OpenERP provides many tools for managing customer and supplier accounts. In this part we will explain:

.. i18n: * financial analysis of partners, to understand the reports that enable you to carry out an analysis
.. i18n:   of all of your partners,
.. i18n: 
.. i18n: * multi-level reminders, which is an automatic system for preparing reminder letters or emails when
.. i18n:   invoices remain unpaid,
.. i18n: 
.. i18n: * detailed analysis of individual partners.
..

* financial analysis of partners, to understand the reports that enable you to carry out an analysis
  of all of your partners,

* multi-level reminders, which is an automatic system for preparing reminder letters or emails when
  invoices remain unpaid,

* detailed analysis of individual partners.

.. i18n: Financial Analysis of Partners
.. i18n: ------------------------------
..

合作伙伴的财务分析
------------------------------

.. i18n: .. index::
.. i18n:    single: module; board_account
.. i18n:    pair: dashboard; accounting
..

.. index::
   single: module; board_account
   pair: dashboard; accounting

.. i18n: When members of your accounting department sign in to OpenERP, they can immediately be presented with the :guilabel:`Accounting Dashboard`. By default, it contains the customer invoices to approve, a company analysis according to account type, a Treasury graph and a useful graph for analyzing aged receivables. Click the ``Accounting`` button in the top toolbar to open the dashboard. You can also call the dashboard from the menu :menuselection:`Accounting --> Reporting --> Dashboard --> Accounting Dashboard`.
..

When members of your accounting department sign in to OpenERP, they can immediately be presented with the :guilabel:`Accounting Dashboard`. By default, it contains the customer invoices to approve, a company analysis according to account type, a Treasury graph and a useful graph for analyzing aged receivables. Click the ``Accounting`` button in the top toolbar to open the dashboard. You can also call the dashboard from the menu :menuselection:`Accounting --> Reporting --> Dashboard --> Accounting Dashboard`.

.. i18n: .. index:: balance; aged
..

.. index:: balance; aged

.. i18n: In the dashboard, the graph at the right entitled :guilabel:`Aged Receivables` represents your receivables week by week. At a glance, you can see the cumulative amount of what your customers owe you by week.
..

In the dashboard, the graph at the right entitled :guilabel:`Aged Receivables` represents your receivables week by week. At a glance, you can see the cumulative amount of what your customers owe you by week.

.. i18n: All of OpenERP's graphs are dynamic. So you can, for example, filter the data by clicking the graph itself and then :guilabel:`Filter` in the Search form. When you click the graph, data will be displayed in list view. Now you enter extra search criteria and then click the `graph` button to display the data as a graph again.
..

All of OpenERP's graphs are dynamic. So you can, for example, filter the data by clicking the graph itself and then :guilabel:`Filter` in the Search form. When you click the graph, data will be displayed in list view. Now you enter extra search criteria and then click the `graph` button to display the data as a graph again.

.. i18n: To obtain a more detailed report of the aged balance (or order by past date), use the menu :menuselection:`Accounting --> Reporting --> Generic Reporting --> Partners --> Aged Partner Balance`.
..

To obtain a more detailed report of the aged balance (or order by past date), use the menu :menuselection:`Accounting --> Reporting --> Generic Reporting --> Partners --> Aged Partner Balance`.

.. i18n: When you click that report, OpenERP shows a wizard asking you for the chart of accounts, the start date of the analysis period and the size of the interval to be analysed (in days). The start date will determine which documents will be included in the report (document date until the selected start date) and it will serve as a reference date to calculate the amounts due for the selected interval.
.. i18n: You can print an aged partner balance for Receivable Accounts or Payable Accounts of for both at the same time. The analysis direction may be ``Past`` (for entries that are due) or ``Future`` to keep track of your cash flow in the next days or weeks (according to your selection). OpenERP then calculates a table of credit balance by period. So, if you request an interval of 30 days, OpenERP generates an analysis of creditors for the past month, past two months, and so on.
.. i18n: An ageing balance will indicate how much of the accounts receivable is overdue. It also reports how far overdue the accounts are (number of days).
..

When you click that report, OpenERP shows a wizard asking you for the chart of accounts, the start date of the analysis period and the size of the interval to be analysed (in days). The start date will determine which documents will be included in the report (document date until the selected start date) and it will serve as a reference date to calculate the amounts due for the selected interval.
You can print an aged partner balance for Receivable Accounts or Payable Accounts of for both at the same time. The analysis direction may be ``Past`` (for entries that are due) or ``Future`` to keep track of your cash flow in the next days or weeks (according to your selection). OpenERP then calculates a table of credit balance by period. So, if you request an interval of 30 days, OpenERP generates an analysis of creditors for the past month, past two months, and so on.
An ageing balance will indicate how much of the accounts receivable is overdue. It also reports how far overdue the accounts are (number of days).

.. i18n: .. tip:: Aged Partner Balance
.. i18n: 
.. i18n:     This report works best of you use payment terms or if you set a due date yourself.
..

.. tip:: Aged Partner Balance

    This report works best of you use payment terms or if you set a due date yourself.

.. i18n: .. figure::  images/account_aged_balance.png
.. i18n:    :scale: 85
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Aged Balance in the Past using a 30-days Period*
..

.. figure::  images/account_aged_balance.png
   :scale: 85
   :align: center

   *Aged Balance in the Past using a 30-days Period*

.. i18n: .. figure::  images/account_aged_balance_fut.png
.. i18n:    :scale: 85
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Aged Balance in the Future using a 30-days Period*
..

.. figure::  images/account_aged_balance_fut.png
   :scale: 85
   :align: center

   *Aged Balance in the Future using a 30-days Period*

.. i18n: For an analysis by partner, you can use the partner balance that you get through the menu :menuselection:`Accounting --> Reporting --> Generic Reporting --> Partners --> Partner Balance`. The system then supplies you with a PDF report containing one line per partner representing debit, credit and balance. The total is displayed per account receivable.
..

For an analysis by partner, you can use the partner balance that you get through the menu :menuselection:`Accounting --> Reporting --> Generic Reporting --> Partners --> Partner Balance`. The system then supplies you with a PDF report containing one line per partner representing debit, credit and balance. The total is displayed per account receivable.

.. i18n: .. figure::  images/account_partner_balance_61.png
.. i18n:    :scale: 85
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Partner Balance*
..

.. figure::  images/account_partner_balance_61.png
   :scale: 85
   :align: center

   *Partner Balance*

.. i18n: .. index:: ledger
..

.. index:: ledger

.. i18n: If you want detailed information about all invoices, credit notes and payments related to partner, print the partner ledger from the menu :menuselection:`Accounting --> Reporting --> Generic Reporting --> Partners --> Partner Ledger`. You can choose to print one partner per page.
..

If you want detailed information about all invoices, credit notes and payments related to partner, print the partner ledger from the menu :menuselection:`Accounting --> Reporting --> Generic Reporting --> Partners --> Partner Ledger`. You can choose to print one partner per page.

.. i18n: .. figure::  images/account_partner_ledger_61.png
.. i18n:    :scale: 85
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Partner Ledger*
..

.. figure::  images/account_partner_ledger_61.png
   :scale: 85
   :align: center

   *Partner Ledger*

.. i18n: Furthermore, OpenERP also provides statistics about individual account entries, invoices and treasury, for instance. To look up statistic information about your accounting, explore the menu :menuselection:`Accounting --> Reporting --> Statistic Reports`. There you will find ``Invoices Analysis``, ``Entries Analysis`` and ``Treasury Analysis`` to name some. By default these statistics are displayed as a list which you can filter to fit your needs. Standard filter buttons, extended filters and grouping features allow you to make an in-depth analysis of your accounting. But the list is not all OpenERP has to offer. These statistic reports can be displayed as a graph simply by clicking the ``Graph`` button at the top right side of the screen. Notice that graphs allow for only one Group by function at a time.
..

Furthermore, OpenERP also provides statistics about individual account entries, invoices and treasury, for instance. To look up statistic information about your accounting, explore the menu :menuselection:`Accounting --> Reporting --> Statistic Reports`. There you will find ``Invoices Analysis``, ``Entries Analysis`` and ``Treasury Analysis`` to name some. By default these statistics are displayed as a list which you can filter to fit your needs. Standard filter buttons, extended filters and grouping features allow you to make an in-depth analysis of your accounting. But the list is not all OpenERP has to offer. These statistic reports can be displayed as a graph simply by clicking the ``Graph`` button at the top right side of the screen. Notice that graphs allow for only one Group by function at a time.

.. i18n: .. figure::  images/account_entries_anal.png
.. i18n:    :scale: 85
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Entries Analysis List View*
..

.. figure::  images/account_entries_anal.png
   :scale: 85
   :align: center

   *Entries Analysis List View*

.. i18n: .. figure::  images/account_entries_anal_graph.png
.. i18n:    :scale: 85
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Entries Analysis Graph View*
..

.. figure::  images/account_entries_anal_graph.png
   :scale: 85
   :align: center

   *Entries Analysis Graph View*

.. i18n: .. tip:: Exporting Entries
.. i18n: 
.. i18n:         Remember that you can export all types of resources in OpenERP.
.. i18n:         From the web client, you need to navigate to a search list for the resource, then click the :guilabel:`Export` link at the bottom left of the list. From the GTK client, you would use the menu :menuselection:`Form --> Export data`. The Export feature enables you to easily create your own analysis in tools such as Microsoft Excel or Calc (LibreOffice or OpenOffice), simply by exporting accounting entries.
..

.. tip:: Exporting Entries

        Remember that you can export all types of resources in OpenERP.
        From the web client, you need to navigate to a search list for the resource, then click the :guilabel:`Export` link at the bottom left of the list. From the GTK client, you would use the menu :menuselection:`Form --> Export data`. The Export feature enables you to easily create your own analysis in tools such as Microsoft Excel or Calc (LibreOffice or OpenOffice), simply by exporting accounting entries.

.. i18n: .. index::
.. i18n:    single: follow-up
.. i18n:    single: reminder
.. i18n:    single: module; account_followup
.. i18n:    single: overdue payments
..

.. index::
   single: follow-up
   single: reminder
   single: module; account_followup
   single: overdue payments

.. i18n: Multi-step Reminders
.. i18n: --------------------
..

多级提醒
--------------------

.. i18n: To automate the management of follow-ups (reminders) you should install the module :mod:`account_followup` (or check the `Followups Management` option in the `Add More Features` wizard).
..

To automate the management of follow-ups (reminders) you should install the module :mod:`account_followup` (or check the `Followups Management` option in the `Add More Features` wizard).

.. i18n: This module is integrated with the email features of OpenERP. Ask your system administrator to define the smtp server through the menu :menuselection:`Settings --> Configuration --> Email --> Outgoing Mail Servers`.
..

This module is integrated with the email features of OpenERP. Ask your system administrator to define the smtp server through the menu :menuselection:`Settings --> Configuration --> Email --> Outgoing Mail Servers`.

.. i18n: Once the module is installed, configure your levels of follow-up using the menu :menuselection:`Accounting --> Configuration --> Miscellaneous --> Follow-Ups`.
..

Once the module is installed, configure your levels of follow-up using the menu :menuselection:`Accounting --> Configuration --> Miscellaneous --> Follow-Ups`.

.. i18n: .. note:: Follow-ups
.. i18n: 
.. i18n:     You can define only one follow-up cycle per company, because you cannot link the follow-up cycle to a partner.
..

.. note:: Follow-ups

    You can define only one follow-up cycle per company, because you cannot link the follow-up cycle to a partner.

.. i18n: The levels of follow-up are relative to the due date; when no payment term is specified, the invoice date will be considered as the due date.
..

The levels of follow-up are relative to the due date; when no payment term is specified, the invoice date will be considered as the due date.

.. i18n: For each level, you should define the number of days and create a note which will automatically be added into the reminder letter. The order in which you define the various follow-up levels determines the order in which letters will be sent.
..

For each level, you should define the number of days and create a note which will automatically be added into the reminder letter. The order in which you define the various follow-up levels determines the order in which letters will be sent.

.. i18n: .. csv-table::  Example of Configuring Follow-up Levels
.. i18n:    :header: "Sequence","Level","Days","Description"
.. i18n:    :widths: 5, 5, 15, 15
.. i18n: 
.. i18n:    "1","Level 1","15 days net","First payment reminder"
.. i18n:    "2","Level 2","30 days net","Second reminder"
.. i18n:    "3","Level 3","45 days from end of month","Put on notice"
..

.. csv-table::  Example of Configuring Follow-up Levels
   :header: "Sequence","Level","Days","Description"
   :widths: 5, 5, 15, 15

   "1","Level 1","15 days net","First payment reminder"
   "2","Level 2","30 days net","Second reminder"
   "3","Level 3","45 days from end of month","Put on notice"

.. i18n: You can send your reminders by mail and/or email with the menu :menuselection:`Accounting --> Periodical Processing --> Billing --> Send followups`.
..

You can send your reminders by mail and/or email with the menu :menuselection:`Accounting --> Periodical Processing --> Billing --> Send followups`.

.. i18n: .. figure::  images/account_followup_wizard.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Prepare Reminders*
..

.. figure::  images/account_followup_wizard.png
   :scale: 75
   :align: center

   *Prepare Reminders*

.. i18n: OpenERP allows you to plan your reminders in the future; you could start a cycle today for invoices due at the end of the week, for instance.
.. i18n: OpenERP presents you with a list of partners who are due to be reminded, which you can modify before starting the procedure. On the ``Email Settings`` tab of the form, you can supply the information you will send in the email reminder.
..

OpenERP allows you to plan your reminders in the future; you could start a cycle today for invoices due at the end of the week, for instance.
OpenERP presents you with a list of partners who are due to be reminded, which you can modify before starting the procedure. On the ``Email Settings`` tab of the form, you can supply the information you will send in the email reminder.

.. i18n: You can either print the reminders or send them by email. From the ``Email Settings`` tab, you can select the ``Test Print`` checkbox to print the reminders as a preview only, without adding follow-up data to the reminded invoices. This way you can easily preview reminders to be sent.
..

You can either print the reminders or send them by email. From the ``Email Settings`` tab, you can select the ``Test Print`` checkbox to print the reminders as a preview only, without adding follow-up data to the reminded invoices. This way you can easily preview reminders to be sent.

.. i18n: The system then gives you a PDF report with all of the reminder letters for each partner. Each letter is produced in the language of the partner (if that is specified), so it is possible to have letters in different languages in the same PDF on several pages.
..

The system then gives you a PDF report with all of the reminder letters for each partner. Each letter is produced in the language of the partner (if that is specified), so it is possible to have letters in different languages in the same PDF on several pages.

.. i18n: From the ``Journal Items`` view, you can check the due date of customers before starting the reminder procedure. You will get a list of unreconciled entries only by clicking the ``Unreconciled`` button. The best thing to do is open the unreconciled line in Form view; select the line and click the ``Form`` button at the top of the page. You can then easily modify the duedate, the last follow-up and the reminder level for each entry.
..

From the ``Journal Items`` view, you can check the due date of customers before starting the reminder procedure. You will get a list of unreconciled entries only by clicking the ``Unreconciled`` button. The best thing to do is open the unreconciled line in Form view; select the line and click the ``Form`` button at the top of the page. You can then easily modify the duedate, the last follow-up and the reminder level for each entry.

.. i18n: To obtain a detailed statistical report of sent follow-ups go to the menu :menuselection:`Accounting --> Reporting --> Generic Reporting --> Partners --> Follow-ups Sent`. This screen will let you analyse your reminder data in various ways, e.g. by follow-up level, by partner or for a combination of these data. You can also group by ``Latest Followup Date`` or ``Partner``, for instance.
..

To obtain a detailed statistical report of sent follow-ups go to the menu :menuselection:`Accounting --> Reporting --> Generic Reporting --> Partners --> Follow-ups Sent`. This screen will let you analyse your reminder data in various ways, e.g. by follow-up level, by partner or for a combination of these data. You can also group by ``Latest Followup Date`` or ``Partner``, for instance.

.. i18n: The different reports are standard OpenERP screens, so you can filter them and explore the elements in detail.
..

The different reports are standard OpenERP screens, so you can filter them and explore the elements in detail.

.. i18n: .. figure::  images/account_followup.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Reminder Statistics*
..

.. figure::  images/account_followup.png
   :scale: 75
   :align: center

   *Reminder Statistics*

.. i18n: Analyse your Turnover
.. i18n: =====================
..

分析营业额
=====================

.. i18n: Analyse your invoicing in OpenERP through the **Invoices Analysis** screen from the menu :menuselection:`Accounting --> Reporting --> Statistic Reports --> Invoices Analysis`.
..

Analyse your invoicing in OpenERP through the **Invoices Analysis** screen from the menu :menuselection:`Accounting --> Reporting --> Statistic Reports --> Invoices Analysis`.

.. i18n: In this statistic report, the columns displayed will vary according to the selections and grouping made, thus making it a very flexible report to analyse your invoices.
..

In this statistic report, the columns displayed will vary according to the selections and grouping made, thus making it a very flexible report to analyse your invoices.

.. i18n: This report provides an overview of what has been invoiced to your customer as well as the average payment delays. To see the average due delay, make sure to group by ``Due Date``.
.. i18n: You can easily group by partner, product category, ... or select only invoices that have not been confirmed yet.
..

This report provides an overview of what has been invoiced to your customer as well as the average payment delays. To see the average due delay, make sure to group by ``Due Date``.
You can easily group by partner, product category, ... or select only invoices that have not been confirmed yet.

.. i18n: This is also an easy way to check your sales people's impact on turnover. You can see your turnover per product category, per salesman, per partner and many more options.
..

This is also an easy way to check your sales people's impact on turnover. You can see your turnover per product category, per salesman, per partner and many more options.

.. i18n: .. figure::  images/account_invoice_analysis.png
.. i18n:    :scale: 80
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Analysing your Invoices*
..

.. figure::  images/account_invoice_analysis.png
   :scale: 80
   :align: center

   *Analysing your Invoices*

.. i18n: To quickly see the total turnover per customer in a graph view, group by ``Partner`` and click the ``Graph`` button to change to graph mode.
..

To quickly see the total turnover per customer in a graph view, group by ``Partner`` and click the ``Graph`` button to change to graph mode.

.. i18n: .. figure::  images/account_turnover_analysis.png
.. i18n:    :scale: 80
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Analysing your Customer's Turnover*
..

.. figure::  images/account_turnover_analysis.png
   :scale: 80
   :align: center

   *Analysing your Customer's Turnover*

.. i18n: .. Copyright © Open Object Press. All rights reserved.
..

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.
..

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the OpenERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.
..

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.
..

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.
..

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.
..

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium
..

.. Published by Open Object Press, Grand Rosière, Belgium
