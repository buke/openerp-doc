.. i18n: .. _bug_management:
.. i18n: 
.. i18n: Bug Reports and Bug Processing
.. i18n: ------------------------------
..

.. _bug_management:

Bug 的提交和 Bug 的处理
------------------------------

.. i18n: .. _bug-tracker-link:
.. i18n: 
.. i18n: Bug Tracker
.. i18n: +++++++++++
..

.. _bug-tracker-link:

Bug 跟踪
+++++++++++

.. i18n: As described in the :ref:`community_platform` section, OpenERP uses
.. i18n: Launchpad as the bug tracker platform.
..

As described in the :ref:`community_platform` section, OpenERP uses
Launchpad as the bug tracker platform.

.. i18n: Anyone is free to report new bugs or give feedback on existing ones
.. i18n: in OpenERP's Launchpad bugtracker.
.. i18n: The only requirement is to `sign up on Launchpad <https://login.launchpad.net/+new_account>`_ 
.. i18n: and join the `OpenERP Community <https://launchpad.net/~openerp-community/+join>`_ team,
.. i18n: which only requires a few clicks.
..

Anyone is free to report new bugs or give feedback on existing ones
in OpenERP's Launchpad bugtracker.
The only requirement is to `sign up on Launchpad <https://login.launchpad.net/+new_account>`_ 
and join the `OpenERP Community <https://launchpad.net/~openerp-community/+join>`_ team,
which only requires a few clicks.

.. i18n: .. note:: Some additional team memberships are required in order to accomplish specific
.. i18n:           tasks, as explained in the :ref:`bug_processing` section below.
..

.. note:: Some additional team memberships are required in order to accomplish specific
          tasks, as explained in the :ref:`bug_processing` section below.

.. i18n: Any issue you notice in OpenERP should be reported on the appropriate
.. i18n: project on LaunchPad. A link to report a new bug can be found on the 
.. i18n: top right side of the homepage of each Launchpad project.
.. i18n: Here is a quick overview of the direct links for reporting bugs on
.. i18n: each OpenERP project:
..

Any issue you notice in OpenERP should be reported on the appropriate
project on LaunchPad. A link to report a new bug can be found on the 
top right side of the homepage of each Launchpad project.
Here is a quick overview of the direct links for reporting bugs on
each OpenERP project:

.. i18n: +--------------------------+-------------------------------------------------+
.. i18n: | Project                  | Bug report interface                            |
.. i18n: +--------------------------+-------------------------------------------------+
.. i18n: | OpenERP Addons           | http://bugs.launchpad.net/openobject-addons     |
.. i18n: +--------------------------+-------------------------------------------------+
.. i18n: | OpenERP Server           | http://bugs.launchpad.net/openobject-server     |
.. i18n: +--------------------------+-------------------------------------------------+
.. i18n: | OpenERP GTK Client       | http://bugs.launchpad.net/openobject-client     |
.. i18n: +--------------------------+-------------------------------------------------+
.. i18n: | OpenERP Web Client (6.0) | http://bugs.launchpad.net/openobject-client-web |
.. i18n: +--------------------------+-------------------------------------------------+
.. i18n: | OpenERP Web (6.1)        | http://bugs.launchpad.net/openerp-web           |
.. i18n: +--------------------------+-------------------------------------------------+
..

+--------------------------+-------------------------------------------------+
| Project                  | Bug report interface                            |
+--------------------------+-------------------------------------------------+
| OpenERP Addons           | http://bugs.launchpad.net/openobject-addons     |
+--------------------------+-------------------------------------------------+
| OpenERP Server           | http://bugs.launchpad.net/openobject-server     |
+--------------------------+-------------------------------------------------+
| OpenERP GTK Client       | http://bugs.launchpad.net/openobject-client     |
+--------------------------+-------------------------------------------------+
| OpenERP Web Client (6.0) | http://bugs.launchpad.net/openobject-client-web |
+--------------------------+-------------------------------------------------+
| OpenERP Web (6.1)        | http://bugs.launchpad.net/openerp-web           |
+--------------------------+-------------------------------------------------+

.. i18n: .. important::
.. i18n: 
.. i18n:     The LaunchPad bug tracker automatically proposes bugs that look
.. i18n:     similar to your bug title when you attempt to report a new one.
.. i18n:     It is important to avoid reporting the same bug several times.
.. i18n:     Be careful to double-check the proposed bugs to avoid
.. i18n:     creating duplicates. However do not forget to proceed further
.. i18n:     should none of the existing bugs match yours.
..

.. important::

    The LaunchPad bug tracker automatically proposes bugs that look
    similar to your bug title when you attempt to report a new one.
    It is important to avoid reporting the same bug several times.
    Be careful to double-check the proposed bugs to avoid
    creating duplicates. However do not forget to proceed further
    should none of the existing bugs match yours.

.. i18n: .. _bug_definition:
.. i18n: 
.. i18n: Definition of a bug
.. i18n: +++++++++++++++++++
.. i18n: At the risk of stating the obvious, here are a few key points to keep in mind
.. i18n: concerning the definition of an OpenERP bug.
..

.. _bug_definition:

Bug 的定义
+++++++++++++++++++
At the risk of stating the obvious, here are a few key points to keep in mind
concerning the definition of an OpenERP bug.

.. i18n: Is usually considered a bug:
..

Is usually considered a bug:

.. i18n:     * Any system failure with a complete stop or traceback
.. i18n:     * Any abnormal behavior of the system resulting from an
.. i18n:       issue with OpenERP code, without changing the original
.. i18n:       functional scope or specification
.. i18n:     * Any security breach in the code of the software
.. i18n:     * Non compliance with the law for an existing feature
.. i18n:       of a certified accounting module
..

    * Any system failure with a complete stop or traceback
    * Any abnormal behavior of the system resulting from an
      issue with OpenERP code, without changing the original
      functional scope or specification
    * Any security breach in the code of the software
    * Non compliance with the law for an existing feature
      of a certified accounting module

.. i18n: Is usually **not** considered a bug:
..

Is usually **not** considered a bug:

.. i18n:     * Non compliance with a customer specific need
.. i18n:     * Abnormal system behavior due to defective
.. i18n:       installation or configuration
.. i18n:     * Security breach resulting from defective 
.. i18n:       installation or configuration
.. i18n:     * Any usage of the software which would not 
.. i18n:       comply with some industry standard
..

    * Non compliance with a customer specific need
    * Abnormal system behavior due to defective
      installation or configuration
    * Security breach resulting from defective 
      installation or configuration
    * Any usage of the software which would not 
      comply with some industry standard

.. i18n: Everything else is probably either a wishlist or should be made into
.. i18n: a blueprint for change/improvement.
..

Everything else is probably either a wishlist or should be made into
a blueprint for change/improvement.

.. i18n: .. _bug_processing:
.. i18n: 
.. i18n: Bug Processing
.. i18n: ++++++++++++++
..

.. _bug_processing:

Bug 的处理
++++++++++++++

.. i18n: The following figure depicts the generic Bug Handling Process currently applied
.. i18n: at OpenERP, and more specifically on the **trunk** branch,
.. i18n: also known as **development version** (see also the :ref:`bug_policy` section)
..

The following figure depicts the generic Bug Handling Process currently applied
at OpenERP, and more specifically on the **trunk** branch,
also known as **development version** (see also the :ref:`bug_policy` section)

.. i18n: .. figure:: bug_management.png
.. i18n:     :alt: Bug Management Process
..

.. figure:: bug_management.png
    :alt: Bug Management Process

.. i18n: The processing of bugs is divided up into several successive main stages:
..

The processing of bugs is divided up into several successive main stages:

.. i18n:     #. **Incoming** bugs are reported on Launchpad by the whole OpenERP Community
.. i18n:     #. **Qualification** of new bugs is performed by a dedicated team within
.. i18n:        OpenERP SA, assisted by the `Drivers Team <https://launchpad.net/openerp-drivers>`_,
.. i18n:        a group of experienced Community Members.
.. i18n:     #. Actual bug **Resolution** is usually performed by the various OpenERP R&D teams,
.. i18n:        unless the **Qualification** step was directly able to take care of the fix,
.. i18n:        for example thanks to a :ref:`patch <merge_proposals>` contributed along with the bug report.
.. i18n:     #. The last step before a bugfix is fully released into the official trunk
.. i18n:        branches is a final technical and functional review of the fix by the
.. i18n:        Team Leader and/or the Quality Team.
..

    #. **Incoming** bugs are reported on Launchpad by the whole OpenERP Community
    #. **Qualification** of new bugs is performed by a dedicated team within
       OpenERP SA, assisted by the `Drivers Team <https://launchpad.net/openerp-drivers>`_,
       a group of experienced Community Members.
    #. Actual bug **Resolution** is usually performed by the various OpenERP R&D teams,
       unless the **Qualification** step was directly able to take care of the fix,
       for example thanks to a :ref:`patch <merge_proposals>` contributed along with the bug report.
    #. The last step before a bugfix is fully released into the official trunk
       branches is a final technical and functional review of the fix by the
       Team Leader and/or the Quality Team.

.. i18n: Bug Qualification
.. i18n: *****************
.. i18n: In order to properly qualify each bug, the following attributes must be
.. i18n: properly set:
..

Bug 的信息
*****************
In order to properly qualify each bug, the following attributes must be
properly set:

.. i18n:     * the branch(es) it's **affecting** must be correct
.. i18n:     * the *reproducibility* of the bug must be verified, as well as the possible
.. i18n:       duplication (if it's a duplicate, mark it as such and stop processing it)
.. i18n:     * the **status** must be correctly set, as explained in the next section
.. i18n:     * the **importance** must be correctly set, as explained in the next section
.. i18n:     * if the bug is valid and must be solved (now or in the future), it must
.. i18n:       be **assigned** to the corresponding R&D Team
.. i18n:     * if the bug is not solved yet, the **milestone** should **not** be set except
.. i18n:       by the assigned R&D Team, to indicate when they plan to release the fix
..

    * the branch(es) it's **affecting** must be correct
    * the *reproducibility* of the bug must be verified, as well as the possible
      duplication (if it's a duplicate, mark it as such and stop processing it)
    * the **status** must be correctly set, as explained in the next section
    * the **importance** must be correctly set, as explained in the next section
    * if the bug is valid and must be solved (now or in the future), it must
      be **assigned** to the corresponding R&D Team
    * if the bug is not solved yet, the **milestone** should **not** be set except
      by the assigned R&D Team, to indicate when they plan to release the fix

.. i18n: Leaving a bug as **New** or **Confirmed**, but not assigning a proper Team is
.. i18n: not useful.
..

Leaving a bug as **New** or **Confirmed**, but not assigning a proper Team is
not useful.

.. i18n: .. rubric:: Qualified Bug Status
..

.. rubric:: Qualified Bug Status

.. i18n: One of the following status values must be set on a bug when qualifying it:
..

One of the following status values must be set on a bug when qualifying it:

.. i18n:     * **Confirmed**: this means that the bug has been reproduced or is considered valid,
.. i18n:       and has been accepted. Bugs in this state are considered *open*. Can be set also for
.. i18n:       Wishlists that we plan to implement in a future release.
.. i18n:     * **Incomplete**: the bug description does not contain enough information to properly
.. i18n:       handle it, and prevents from reproducing it (such as missing version, no steps to
.. i18n:       reproduce, or some other important information missing).
.. i18n:       Keep in mind that bugs in this state might be updated with a response
.. i18n:       (in Launchpad bug search you can filter on *Incomplete with response* or *Incomplete without response*).
.. i18n:       As we have enabled auto-bug expiry on Launchpad these bugs will be put in status *Expired*
.. i18n:       automatically by Launchpad after 60 days of inactivity, and no answer.
.. i18n:       Bugs in this state are still considered open until they are Expired.
.. i18n:     * **Invalid**: the bug cannot be reproduced at all or is incorrect, for example because
.. i18n:       the poster has misunderstood OpenERP's features or is misusing the system.
.. i18n:       Bugs in this state are considered closed.
.. i18n:       Note: If this looks like it could become a Frequently Asked Question, don't hesitate to
.. i18n:       *Convert to a question* before answering (link is on top-right of bug page).
.. i18n:       This will mark the bug *Invalid* automatically, and then you can provide the answer on
.. i18n:       the linked Question.
.. i18n:     * **Won't Fix**: bugs or wishlists that we can't or don't
.. i18n:       want to fix/implement. Bugs in this state are considered closed.
.. i18n:     * **Triaged**: this status means that the qualifier is not sure if the bug should be
.. i18n:       confirmed or refused. Set this status and assign a Team to indicate that a Team Leader still
.. i18n:       needs to confirm/refuse this bug before starting to work on it.
.. i18n:       Bugs in this state are considered open.
.. i18n:     * **Fix Released**: if you know the bug was valid and has been fixed since it was reported,
.. i18n:       it may of course be marked directly as such (you may also set the appropriate milestone
.. i18n:       if you know it) 
..

    * **Confirmed**: this means that the bug has been reproduced or is considered valid,
      and has been accepted. Bugs in this state are considered *open*. Can be set also for
      Wishlists that we plan to implement in a future release.
    * **Incomplete**: the bug description does not contain enough information to properly
      handle it, and prevents from reproducing it (such as missing version, no steps to
      reproduce, or some other important information missing).
      Keep in mind that bugs in this state might be updated with a response
      (in Launchpad bug search you can filter on *Incomplete with response* or *Incomplete without response*).
      As we have enabled auto-bug expiry on Launchpad these bugs will be put in status *Expired*
      automatically by Launchpad after 60 days of inactivity, and no answer.
      Bugs in this state are still considered open until they are Expired.
    * **Invalid**: the bug cannot be reproduced at all or is incorrect, for example because
      the poster has misunderstood OpenERP's features or is misusing the system.
      Bugs in this state are considered closed.
      Note: If this looks like it could become a Frequently Asked Question, don't hesitate to
      *Convert to a question* before answering (link is on top-right of bug page).
      This will mark the bug *Invalid* automatically, and then you can provide the answer on
      the linked Question.
    * **Won't Fix**: bugs or wishlists that we can't or don't
      want to fix/implement. Bugs in this state are considered closed.
    * **Triaged**: this status means that the qualifier is not sure if the bug should be
      confirmed or refused. Set this status and assign a Team to indicate that a Team Leader still
      needs to confirm/refuse this bug before starting to work on it.
      Bugs in this state are considered open.
    * **Fix Released**: if you know the bug was valid and has been fixed since it was reported,
      it may of course be marked directly as such (you may also set the appropriate milestone
      if you know it) 

.. i18n: .. rubric:: Qualified Bug Importance
..

.. rubric:: Qualified Bug Importance

.. i18n: Assessing the importance of a bug is a difficult and often subjective task.
.. i18n: In order to have common criteria, we propose the following definition
.. i18n: for the severity levels on Launchpad bugs
..

Assessing the importance of a bug is a difficult and often subjective task.
In order to have common criteria, we propose the following definition
for the severity levels on Launchpad bugs

.. i18n:     * **Critical**: security issue (e.g. system compromised or arbitrary 
.. i18n:       code execution possible), or system completely unusable, for many users. 
.. i18n:       Any kind of data loss.
.. i18n:     * **High**: major part of an application not working correctly and blocking
.. i18n:       for many users: like the impossibility to display Sale Orders
.. i18n:       for all users (not just for a peculiar setup, but in most cases)
.. i18n:     * **Medium**: a minor part of an applications not working correctly (not
.. i18n:       really blocking), or a major feature not working for few users only
.. i18n:       or for a specific configuration only.
.. i18n:     * **Low**: the rest, mostly usability issues (eg. presentation/layout issues)
.. i18n:       that don't prevent to use any of the features.
.. i18n:     * **Wishlist**: nice to have features/patches, propositions to enhance/modify
.. i18n:       the current logic.
..

    * **Critical**: security issue (e.g. system compromised or arbitrary 
      code execution possible), or system completely unusable, for many users. 
      Any kind of data loss.
    * **High**: major part of an application not working correctly and blocking
      for many users: like the impossibility to display Sale Orders
      for all users (not just for a peculiar setup, but in most cases)
    * **Medium**: a minor part of an applications not working correctly (not
      really blocking), or a major feature not working for few users only
      or for a specific configuration only.
    * **Low**: the rest, mostly usability issues (eg. presentation/layout issues)
      that don't prevent to use any of the features.
    * **Wishlist**: nice to have features/patches, propositions to enhance/modify
      the current logic.

.. i18n: .. rubric:: Qualified Bug Assignation
..

.. rubric:: Qualified Bug Assignation

.. i18n: In order to be actually solved, a bug should be assigned to the R&D Team in charge
.. i18n: of this area of OpenERP. Each team will assign milestones to indicate when they
.. i18n: plan to release the fix for each bug. The main R&D teams and their responsibilities
.. i18n: are currently:
..

In order to be actually solved, a bug should be assigned to the R&D Team in charge
of this area of OpenERP. Each team will assign milestones to indicate when they
plan to release the fix for each bug. The main R&D teams and their responsibilities
are currently:

.. i18n:     * `Addons Team 1 <http://launchpad.net/~openerp-dev-addons1>`_ is responsible for CRM, Project, Plugins, Knowledge, Tools
.. i18n:     * `Addons Team 2 <http://launchpad.net/~openerp-dev-addons2>`_ is responsible for MRP, Stock, Purchase, Procurement, Marketing
.. i18n:     * `Addons Team 3 <http://launchpad.net/~openerp-dev-addons3>`_ is responsible for Account, Sales, Point of sale, Association, HR
.. i18n:     * `Framework Team <http://launchpad.net/~openerp-dev-framework>`_ is responsible for the Server/Framework
.. i18n:     * `GTK Team <http://launchpad.net/~openerp-dev-gtk>`_ is responsible for the GTK Native Client
.. i18n:     * `Web Team <http://launchpad.net/~openerp-dev-web>`_ is responsible for the Web Interface
..

    * `Addons Team 1 <http://launchpad.net/~openerp-dev-addons1>`_ is responsible for CRM, Project, Plugins, Knowledge, Tools
    * `Addons Team 2 <http://launchpad.net/~openerp-dev-addons2>`_ is responsible for MRP, Stock, Purchase, Procurement, Marketing
    * `Addons Team 3 <http://launchpad.net/~openerp-dev-addons3>`_ is responsible for Account, Sales, Point of sale, Association, HR
    * `Framework Team <http://launchpad.net/~openerp-dev-framework>`_ is responsible for the Server/Framework
    * `GTK Team <http://launchpad.net/~openerp-dev-gtk>`_ is responsible for the GTK Native Client
    * `Web Team <http://launchpad.net/~openerp-dev-web>`_ is responsible for the Web Interface

.. i18n: .. rubric:: Milestone Assignation
..

.. rubric:: Milestone Assignation

.. i18n: Milestones should be set only for bugs that have been fixed, to track when it happened,
.. i18n: or by the R&D team to indicate when they plan to release the fix.
..

Milestones should be set only for bugs that have been fixed, to track when it happened,
or by the R&D team to indicate when they plan to release the fix.

.. i18n: .. _bug_policy:
.. i18n: 
.. i18n: Bug Management Policy
.. i18n: +++++++++++++++++++++
..

.. _bug_policy:

Bug 管理策略
+++++++++++++++++++++

.. i18n: .. topic:: OpenERP Bug Policy
.. i18n: 
.. i18n:     The official OpenERP policy is different depending on the version/branch the bug affects.
.. i18n:     Bugs reported against the **trunk/development** branch are all processed as described in the
.. i18n:     :ref:`bug_processing` section. Bugs reported on a **stable** branch follow a much stricter
.. i18n:     qualification process, to limit the risk of regressions on these production-grade versions.
.. i18n: 
.. i18n:         .. rubric:: **trunk**
.. i18n: 
.. i18n:         All bugs and wishlists should be reported on Launchpad, and 
.. i18n:         will be qualified by the OpenERP Launchpad Qualification
.. i18n:         team. :ref:`Valid bugs <bug_definition>` will be confirmed and scheduled for
.. i18n:         resolution according to their importance. Wishlists will be
.. i18n:         accepted depending on the R&D strategy, and scheduled in the
.. i18n:         R&D backlog at the discretion of the R&D Teams.
.. i18n: 
.. i18n:         .. rubric:: **stable**
.. i18n: 
.. i18n:         Bugs on stable releases may be reported:
.. i18n: 
.. i18n:             + via Launchpad for High/Critical importance (no guaranteed response time)
.. i18n:             + via the OpenERP Enterprise channel (former Publisher's Warranty) for Customers
.. i18n:               (guaranteed response time according to the
.. i18n:               `contract <http://www.openerp.com/services/subscribe-onsite>`_)
.. i18n: 
.. i18n:         :ref:`Valid bugs <bug_definition>` that also affect trunk
.. i18n:         will be fixed in trunk, but the fix will only be applied to
.. i18n:         stable if their importance requires the release of an updated version (security issue,
.. i18n:         major issue affecting important features, etc.) Anything that looks
.. i18n:         like a change or improvement will not be accepted on stable.
.. i18n: 
.. i18n:     You will find the complete rationale for this policy below. You may also want to have
.. i18n:     a look at the :ref:`bug_policy_faq`.
..

.. topic:: OpenERP Bug Policy

    The official OpenERP policy is different depending on the version/branch the bug affects.
    Bugs reported against the **trunk/development** branch are all processed as described in the
    :ref:`bug_processing` section. Bugs reported on a **stable** branch follow a much stricter
    qualification process, to limit the risk of regressions on these production-grade versions.

        .. rubric:: **trunk**

        All bugs and wishlists should be reported on Launchpad, and 
        will be qualified by the OpenERP Launchpad Qualification
        team. :ref:`Valid bugs <bug_definition>` will be confirmed and scheduled for
        resolution according to their importance. Wishlists will be
        accepted depending on the R&D strategy, and scheduled in the
        R&D backlog at the discretion of the R&D Teams.

        .. rubric:: **stable**

        Bugs on stable releases may be reported:

            + via Launchpad for High/Critical importance (no guaranteed response time)
            + via the OpenERP Enterprise channel (former Publisher's Warranty) for Customers
              (guaranteed response time according to the
              `contract <http://www.openerp.com/services/subscribe-onsite>`_)

        :ref:`Valid bugs <bug_definition>` that also affect trunk
        will be fixed in trunk, but the fix will only be applied to
        stable if their importance requires the release of an updated version (security issue,
        major issue affecting important features, etc.) Anything that looks
        like a change or improvement will not be accepted on stable.

    You will find the complete rationale for this policy below. You may also want to have
    a look at the :ref:`bug_policy_faq`.

.. i18n: .. rubric:: Rationale for the Bug Policy
..

.. rubric:: Rationale for the Bug Policy

.. i18n: As of November 2010, OpenERP has started to enforce a stricter policy, which
.. i18n: means that you may be surprised to see that more Launchpad bugs are
.. i18n: closed with status *Invalid* or *Won't Fix*. The goal being pursued is to
.. i18n: really improve the stability of the stable versions.
..

As of November 2010, OpenERP has started to enforce a stricter policy, which
means that you may be surprised to see that more Launchpad bugs are
closed with status *Invalid* or *Won't Fix*. The goal being pursued is to
really improve the stability of the stable versions.

.. i18n: OpenERP used to have developers working on all bugs reported via Launchpad,
.. i18n: regardless of the OpenERP release they were reported on, and without a strict
.. i18n: policy on what is accepted as a bug and what is not.
.. i18n: A few years of working in this manner has shown us that this is not efficient,
.. i18n: as it leads to long processing times for some bugs, and too often to the introduction
.. i18n: of regressions in the stable branches:
..

OpenERP used to have developers working on all bugs reported via Launchpad,
regardless of the OpenERP release they were reported on, and without a strict
policy on what is accepted as a bug and what is not.
A few years of working in this manner has shown us that this is not efficient,
as it leads to long processing times for some bugs, and too often to the introduction
of regressions in the stable branches:

.. i18n:     - The main trouble with past stable versions
.. i18n:       was that developers did too many changes on
.. i18n:       the stable branch and introduced regressions (because
.. i18n:       the Support/Maintenance team was fixing a maximum of requests
.. i18n:       on stable branch reported by the
.. i18n:       community). This was too risky for a stable version.
.. i18n:     - Only very few of these changes were impacting customers ;
.. i18n:       changing a stable branch used by customers in production is always a
.. i18n:       risk that should be minimized.
.. i18n:     - Most of these requests (65% of bugs according to a
.. i18n:       recent bug qualification sprint) were feature improvements, not bugs.
.. i18n:     - The distinction was not clear between bugs fixed through the
.. i18n:       OpenERP Enterprise contract with a guaranteed response time, 
.. i18n:       and those fixed for free on Launchpad. The Support team did its
.. i18n:       best to fix both.
..

    - The main trouble with past stable versions
      was that developers did too many changes on
      the stable branch and introduced regressions (because
      the Support/Maintenance team was fixing a maximum of requests
      on stable branch reported by the
      community). This was too risky for a stable version.
    - Only very few of these changes were impacting customers ;
      changing a stable branch used by customers in production is always a
      risk that should be minimized.
    - Most of these requests (65% of bugs according to a
      recent bug qualification sprint) were feature improvements, not bugs.
    - The distinction was not clear between bugs fixed through the
      OpenERP Enterprise contract with a guaranteed response time, 
      and those fixed for free on Launchpad. The Support team did its
      best to fix both.

.. i18n: In order to improve the situation, OpenERP has split up the teams assigned to the resolution of bugs
.. i18n: and the corresponding processes, separating the management of general purpose
.. i18n: community bug reports (improving the product for the future) and the management
.. i18n: of day-to-day issues encountered on production systems
.. i18n: (ensuring stability in a conservative manner):
..

In order to improve the situation, OpenERP has split up the teams assigned to the resolution of bugs
and the corresponding processes, separating the management of general purpose
community bug reports (improving the product for the future) and the management
of day-to-day issues encountered on production systems
(ensuring stability in a conservative manner):

.. i18n:     * The **OpenERP Launchpad team** is dedicated to processing all bugs reported via
.. i18n:       Launchpad, qualifying them as quickly as possible, and getting them solved
.. i18n:       by the R&D teams. They must not touch the stable branches directly, and any
.. i18n:       important issue reported on a stable branch will be passed on to the
.. i18n:       **OpenERP Enterprise team**.
.. i18n: 
.. i18n:     * The **OpenERP Enterprise team** (formerly OpenERP Publisher's Warranty) is in
.. i18n:       charge of receiving issues reported directly by customers via the OpenERP
.. i18n:       Publisher's Warranty, providing high-level expertise within short response times,
.. i18n:       including workarounds and patches when available.
.. i18n:       They carefully select the fixes to apply to the stable branches, to be published
.. i18n:       every month.
..

    * The **OpenERP Launchpad team** is dedicated to processing all bugs reported via
      Launchpad, qualifying them as quickly as possible, and getting them solved
      by the R&D teams. They must not touch the stable branches directly, and any
      important issue reported on a stable branch will be passed on to the
      **OpenERP Enterprise team**.

    * The **OpenERP Enterprise team** (formerly OpenERP Publisher's Warranty) is in
      charge of receiving issues reported directly by customers via the OpenERP
      Publisher's Warranty, providing high-level expertise within short response times,
      including workarounds and patches when available.
      They carefully select the fixes to apply to the stable branches, to be published
      every month.

.. i18n: This way the responsibilities of the teams are clear, and we can appropriately
.. i18n: implement continuous improvement, with distinct **goals**!
..

This way the responsibilities of the teams are clear, and we can appropriately
implement continuous improvement, with distinct **goals**!

.. i18n: .. _bug_policy_faq:
.. i18n: 
.. i18n: Bug Management FAQ
.. i18n: ******************
.. i18n: .. topic:: 1. What is the policy regarding bugs encountered by users of the OpenERP Online Offer?
.. i18n: 
.. i18n:     Customers of `OpenERP's Online Offer <http://www.openerp.com/services>`_ are automatically
.. i18n:     subscribed to an OpenERP Enterprise contract so any bug they report via their
.. i18n:     dedicated Support/Maintenance channel will be handled accordingly.
..

.. _bug_policy_faq:

Bug 管理 FAQ
******************
.. topic:: 1. What is the policy regarding bugs encountered by users of the OpenERP Online Offer?

    Customers of `OpenERP's Online Offer <http://www.openerp.com/services>`_ are automatically
    subscribed to an OpenERP Enterprise contract so any bug they report via their
    dedicated Support/Maintenance channel will be handled accordingly.

.. i18n: .. topic:: 2. My Launchpad bug report was refused for the stable release I reported! How can I get it
.. i18n:            fixed for my important projects/customers?
.. i18n: 
.. i18n:    It is the responsibility of OpenERP Enterprise team (former OpenERP Publisher's Warranty) to
.. i18n:    maintain the maximum stability of the stable branches, and this implies being very strict on
.. i18n:    what can be considered important enough to qualify for a patch on a stable branch.
.. i18n: 
.. i18n:    Note that if the bug affects the trunk as well, you can simply try to apply or backport the fix that was
.. i18n:    or will be provided for trunk. Other community contributors may also provide patches for the stable
.. i18n:    branch even if the bug was 
..

.. topic:: 2. My Launchpad bug report was refused for the stable release I reported! How can I get it
           fixed for my important projects/customers?

   It is the responsibility of OpenERP Enterprise team (former OpenERP Publisher's Warranty) to
   maintain the maximum stability of the stable branches, and this implies being very strict on
   what can be considered important enough to qualify for a patch on a stable branch.

   Note that if the bug affects the trunk as well, you can simply try to apply or backport the fix that was
   or will be provided for trunk. Other community contributors may also provide patches for the stable
   branch even if the bug was 

.. i18n: .. topic:: 3. My Launchpad bug report/feature request was closed as Invalid or Won't Fix, but I can prove that
.. i18n:            it really is valid! How can I get it fixed/implemented for my important projects/customers?
.. i18n: 
.. i18n:    This may happen and is not necessarily an error. OpenERP cannot cover all possible cases and does
.. i18n:    not want to. The idea is to support the most important and common features, and try to avoid
.. i18n:    becoming overcomplicated or bloated.
.. i18n:    However OpenERP is also easily extensible and customizable, so you could instead handle your
.. i18n:    special cases or features in customization modules (if done well and often requested,
.. i18n:    they could later be included in the official addons)
..

.. topic:: 3. My Launchpad bug report/feature request was closed as Invalid or Won't Fix, but I can prove that
           it really is valid! How can I get it fixed/implemented for my important projects/customers?

   This may happen and is not necessarily an error. OpenERP cannot cover all possible cases and does
   not want to. The idea is to support the most important and common features, and try to avoid
   becoming overcomplicated or bloated.
   However OpenERP is also easily extensible and customizable, so you could instead handle your
   special cases or features in customization modules (if done well and often requested,
   they could later be included in the official addons)

.. i18n: .. topic:: 4. What's the matter with OpenERP Web Client bugs being all closed as *Won't Fix*?
.. i18n: 
.. i18n:    As you certainly noticed, bugs reported against the 6.0 web client series had not
.. i18n:    been receiving a lot of attention lately on Launchpad.
.. i18n: 
.. i18n:    The reason is that the OpenERP Web Client from the 6.0 series will not be developed further
.. i18n:    in the future, as it was becoming too hard to maintain, due to its aging architecture.
.. i18n:    For the 6.1 series, a
.. i18n:    `new web frontend <https://launchpad.net/openerp-web>`_ is under development, rewritten from
.. i18n:    scratch with a clean (HTML5/Javascript) state-of-the-art architecture. This will make future
.. i18n:    improvements and maintenance much easier.
.. i18n: 
.. i18n:    The :ref:`OpenERP Bug Management Policy <bug_policy>` explains that R&D developers solve
.. i18n:    bugs reported on Launchpad in the trunk development branch, in order to improve the
.. i18n:    product for the future, for everyone. As this project will no longer be used in 6.1,
.. i18n:    these R&D efforts would now be wasted.
.. i18n: 
.. i18n:    Concerning the correction of bugs in the stable series, this is the responsibility of the
.. i18n:    *OpenERP Enterprise* (OPW) maintenance team, for all the reasons explained
.. i18n:    :ref:`above <bug_policy>`, and they will of course continue to do it as long as the 6.0 LTS
.. i18n:    series is :ref:`supported<release_cycle>`.
.. i18n: 
.. i18n:    The R&D Web Team can therefore dedicate all its efforts to finishing the new
.. i18n:    OpenERP 6.1 client, and making it very robust, stable, easy to improve and maintain.
..

.. topic:: 4. What's the matter with OpenERP Web Client bugs being all closed as *Won't Fix*?

   As you certainly noticed, bugs reported against the 6.0 web client series had not
   been receiving a lot of attention lately on Launchpad.

   The reason is that the OpenERP Web Client from the 6.0 series will not be developed further
   in the future, as it was becoming too hard to maintain, due to its aging architecture.
   For the 6.1 series, a
   `new web frontend <https://launchpad.net/openerp-web>`_ is under development, rewritten from
   scratch with a clean (HTML5/Javascript) state-of-the-art architecture. This will make future
   improvements and maintenance much easier.

   The :ref:`OpenERP Bug Management Policy <bug_policy>` explains that R&D developers solve
   bugs reported on Launchpad in the trunk development branch, in order to improve the
   product for the future, for everyone. As this project will no longer be used in 6.1,
   these R&D efforts would now be wasted.

   Concerning the correction of bugs in the stable series, this is the responsibility of the
   *OpenERP Enterprise* (OPW) maintenance team, for all the reasons explained
   :ref:`above <bug_policy>`, and they will of course continue to do it as long as the 6.0 LTS
   series is :ref:`supported<release_cycle>`.

   The R&D Web Team can therefore dedicate all its efforts to finishing the new
   OpenERP 6.1 client, and making it very robust, stable, easy to improve and maintain.
