
.. i18n: .. _technical-guidelines-link:
.. i18n: 
.. i18n: Contribution Guidelines
.. i18n: -----------------------
..

.. _technical-guidelines-link:

Contribution Guidelines
-----------------------

.. i18n: Bug reporting
.. i18n: +++++++++++++
..

Bug reporting
+++++++++++++

.. i18n: For all details regarding bug reports and bug processing, please
.. i18n: refer to the :ref:`bug_management` section.
..

For all details regarding bug reports and bug processing, please
refer to the :ref:`bug_management` section.

.. i18n: .. _merge_proposals:
.. i18n: 
.. i18n: Merge Proposals & Patches
.. i18n: +++++++++++++++++++++++++
..

.. _merge_proposals:

Merge Proposals & Patches
+++++++++++++++++++++++++

.. i18n: It is quite easy to make a patch and propose it for merging on any
.. i18n: OpenERP project, be it to fix a bug, improve an existing feature,
.. i18n: or add something new.
..

It is quite easy to make a patch and propose it for merging on any
OpenERP project, be it to fix a bug, improve an existing feature,
or add something new.

.. i18n: However, in order to tremendously increase the chances of getting
.. i18n: your patch noticed and merged, you should pay attention to the
.. i18n: :ref:`merge_proposals_policy` and then carefully follow the
.. i18n: :ref:`merge_proposals_guidelines`.
..

However, in order to tremendously increase the chances of getting
your patch noticed and merged, you should pay attention to the
:ref:`merge_proposals_policy` and then carefully follow the
:ref:`merge_proposals_guidelines`.

.. i18n: .. _merge_proposals_policy:
.. i18n: 
.. i18n: Merge Proposal Acceptance Policy
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..

.. _merge_proposals_policy:

Merge Proposal Acceptance Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: OpenERP's R&D expects to receive merge proposals from the Community in these areas:
..

OpenERP's R&D expects to receive merge proposals from the Community in these areas:

.. i18n:   - patches to correct a bug in an official addons
.. i18n:   - patches to improve an existing official addon, such as extending a feature or adding one
..

  - patches to correct a bug in an official addons
  - patches to improve an existing official addon, such as extending a feature or adding one

.. i18n: OpenERP's R&D does **not** expect to receive merge proposals from the Community in these areas:
..

OpenERP's R&D does **not** expect to receive merge proposals from the Community in these areas:

.. i18n:   - addition of an extra feature to an official addons, when the feature should really
.. i18n:     provided by a separate (new) module
.. i18n:   - addition of a new module to the official addons
..

  - addition of an extra feature to an official addons, when the feature should really
    provided by a separate (new) module
  - addition of a new module to the official addons

.. i18n: For these last cases, it is better to put the feature into new modules entirely maintained
.. i18n: by their authors in their own Launchpad repository, and published on OpenERP Apps,
.. i18n: to be visible by the whole Community. This is totally unrelated to the quality of the
.. i18n: proposition: there are tons of great community modules on OpenERP Apps, some of them already
.. i18n: downloaded thousands of times!
..

For these last cases, it is better to put the feature into new modules entirely maintained
by their authors in their own Launchpad repository, and published on OpenERP Apps,
to be visible by the whole Community. This is totally unrelated to the quality of the
proposition: there are tons of great community modules on OpenERP Apps, some of them already
downloaded thousands of times!

.. i18n: However, including a module in the official release is a big commitment in terms of review
.. i18n: maintenance, support, etc. In addition, it would quickly bloat the OpenERP core if done too
.. i18n: often, compromising its agility and maintainability, and thus the future of the product.
.. i18n: On the other hand, by progressively integrating OpenERP Apps better in the product, we should
.. i18n: reach the same visibility for Community modules, without incurring these risks.
..

However, including a module in the official release is a big commitment in terms of review
maintenance, support, etc. In addition, it would quickly bloat the OpenERP core if done too
often, compromising its agility and maintainability, and thus the future of the product.
On the other hand, by progressively integrating OpenERP Apps better in the product, we should
reach the same visibility for Community modules, without incurring these risks.

.. i18n: Therefore the process of including a community module into the official addons is entirely 
.. i18n: driven by OpenERP R&D based on the product strategy. In addition to features selected by
.. i18n: OpenERP Product Managers, features that are considered *REQUIRED* to use OpenERP in a certain
.. i18n: market/domain will also be considered for inclusion.
.. i18n: Deciding whether a feature is *REQUIRED* is quite subjective, but the following hints are useful:
..

Therefore the process of including a community module into the official addons is entirely 
driven by OpenERP R&D based on the product strategy. In addition to features selected by
OpenERP Product Managers, features that are considered *REQUIRED* to use OpenERP in a certain
market/domain will also be considered for inclusion.
Deciding whether a feature is *REQUIRED* is quite subjective, but the following hints are useful:

.. i18n:  - if most established competitors on the given market/domain implement this feature, and
.. i18n:    this domain is normally addressed by official OpenERP addons, then it's likely *REQUIRED*.
.. i18n:  - on the other hand, if **no** established software competitors on the given market/domain
.. i18n:    implement this feature, then it's probably *NOT REQUIRED*.
..

 - if most established competitors on the given market/domain implement this feature, and
   this domain is normally addressed by official OpenERP addons, then it's likely *REQUIRED*.
 - on the other hand, if **no** established software competitors on the given market/domain
   implement this feature, then it's probably *NOT REQUIRED*.

.. i18n: This certainly doesn't mean we don't want to innovate (that's the part where Product Managers
.. i18n: choose new features!), this is only for deciding that a module is *REQUIRED* and thus it is
.. i18n: *necessary* to include it in the default installations.
..

This certainly doesn't mean we don't want to innovate (that's the part where Product Managers
choose new features!), this is only for deciding that a module is *REQUIRED* and thus it is
*necessary* to include it in the default installations.

.. i18n: Of course, on top of the above, a merge proposal needs to pass the functional and technical 
.. i18n: review by OpenERP's R&D, and even though we do our best to process them in a timely fashion,
.. i18n: there is no guarantee it will be accepted, nor when.
..

Of course, on top of the above, a merge proposal needs to pass the functional and technical 
review by OpenERP's R&D, and even though we do our best to process them in a timely fashion,
there is no guarantee it will be accepted, nor when.

.. i18n: .. _merge_proposals_guidelines:
.. i18n: 
.. i18n: Merge Proposal Guidelines
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^
..

.. _merge_proposals_guidelines:

Merge Proposal Guidelines
^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: The basic procedure is the following:
..

The basic procedure is the following:

.. i18n:     #. Register on LaunchPad if not done yet
.. i18n:     #. If you wish to be able to easily publish your changes, setup
.. i18n:        an SSH private/public key pair and register your public key
.. i18n:        on your LaunchPad profile page, then use the following command
.. i18n:        to provide your LP login to Bazaar::
.. i18n: 
.. i18n:         $ bzr launchpad-login <your-launchpad-login> 
.. i18n: 
.. i18n:     #. Grab a local copy of the branch you want to patch, e.g. for the
.. i18n:        development version of the OpenERP server, that would be::
.. i18n: 
.. i18n:         $ bzr branch lp:openobject-server
.. i18n: 
.. i18n:     #. Work on the local branch, and commit your changes with relevant
.. i18n:        commit messages. Do not forget to add the `--fixes` parameter
.. i18n:        if your work fixes a specific LaunchPad bug::
.. i18n: 
.. i18n:         $ ... patch the code ...
.. i18n:         $ bzr ci --fixes lp:12345 -m '[FIX] fixed formatting of date field' 
.. i18n: 
.. i18n:     #. Push your work as a new branch on LaunchPad, either into your personal
.. i18n:        space, or in any of the relevant teams you may be member of 
.. i18n:        (e.g. openerp-community)::
.. i18n: 
.. i18n:         $ bzr push lp:~openerp-community/openobject-server/trunk-bugfix-12345
.. i18n: 
.. i18n:     #. Finally go to the LaunchPad page for your branch and click on the
.. i18n:        *Propose for merging* link, choose the appropriate target project and
.. i18n:        branch, and provide a useful description of your work.
.. i18n:        The URL of the new branch is in the form::
.. i18n: 
.. i18n:         https://code.launchpad.net/~openerp-community/openobject-server/trunk-bugfix-12345
..

    #. Register on LaunchPad if not done yet
    #. If you wish to be able to easily publish your changes, setup
       an SSH private/public key pair and register your public key
       on your LaunchPad profile page, then use the following command
       to provide your LP login to Bazaar::

        $ bzr launchpad-login <your-launchpad-login> 

    #. Grab a local copy of the branch you want to patch, e.g. for the
       development version of the OpenERP server, that would be::

        $ bzr branch lp:openobject-server

    #. Work on the local branch, and commit your changes with relevant
       commit messages. Do not forget to add the `--fixes` parameter
       if your work fixes a specific LaunchPad bug::

        $ ... patch the code ...
        $ bzr ci --fixes lp:12345 -m '[FIX] fixed formatting of date field' 

    #. Push your work as a new branch on LaunchPad, either into your personal
       space, or in any of the relevant teams you may be member of 
       (e.g. openerp-community)::

        $ bzr push lp:~openerp-community/openobject-server/trunk-bugfix-12345

    #. Finally go to the LaunchPad page for your branch and click on the
       *Propose for merging* link, choose the appropriate target project and
       branch, and provide a useful description of your work.
       The URL of the new branch is in the form::

        https://code.launchpad.net/~openerp-community/openobject-server/trunk-bugfix-12345

.. i18n: The following guidelines will give you further advice in getting
.. i18n: your patch through:
..

The following guidelines will give you further advice in getting
your patch through:

.. i18n:     #. Carefully select the **appropriate target branch** for your patch.
.. i18n:        For example if your patch introduces an improvement but does not
.. i18n:        technically fix a bug, do not bother proposing it for merging on
.. i18n:        a stable branch. Stable branches are **only** for bugfixes, so rather
.. i18n:        propose it on a trunk branch. See also the definition of a bug above.
.. i18n:     #. Obviously, **pay attention** to the
.. i18n:        :ref:`Coding Guidelines <coding-guidelines-link>`.
.. i18n:     #. While following coding guidelines, avoid being over-zealous. If existing
.. i18n:        code does not meet the guidelines, you should usually fix only the lines
.. i18n:        that you are modifying, not the rest. Otherwise you will quickly find
.. i18n:        yourself modifying everything, and your patch will be refused.
.. i18n:     #. Please **review** your own changes before committing them, to avoid
.. i18n:        introducing useless noise in the merge proposal, like additional
.. i18n:        whitespace, etc.
.. i18n:        Use ``bzr status``, then ``bzr diff`` or ``bzr cdiff`` to know 
.. i18n:        exactly what you changed, before committing.
.. i18n:     #. Don't hesitate to revert a bad commit, it's the right time to do it
.. i18n:        before you push or propose your branch. ``bzr uncommit`` is a useful
.. i18n:        tool when working locally.
.. i18n:     #. Work on a separate feature/bug/whatever at a time. Do not mix lots of
.. i18n:        changes in one merge proposal, as it will be too complicated to review,
.. i18n:        thus refused.
.. i18n:     #. Make **separate branches and merge proposals** for separate changes.
.. i18n:     #. The **smaller** and **cleaner** a merge proposal, the **higher** the 
.. i18n:        chance of seeing it merged.
.. i18n:     #. **Avoid any kind of automatic formatting**, like white-space
.. i18n:        conversion or re-wrapping. Even if the original code is ugly, this 
.. i18n:        will make it possibly much harder to review. 
.. i18n:        If you really want to do it, make it a separate branch and
.. i18n:        merge proposal for that, clearly stating why you did so.
.. i18n:     #. Be very accurate and honest in the description of your patch, and in
.. i18n:        the commit messages. Do not propose a patch claiming that it contains
.. i18n:        "*just some layout improvements*" and try to slip into it some
.. i18n:        functional changes as well, or new fields that you added, etc.
.. i18n:        In fact you should explicitly warn the reviewers about these parts,
.. i18n:        if you could not split them in separate merge proposals.
.. i18n:        Indeed the layout changes could be reviewed easily by testing the
.. i18n:        updated views, but any Python change needs to be reviewed carefully,
.. i18n:        and should *never* go unnoticed.
.. i18n:     #. If your patch is very long (say, more than 100 lines), consider 
.. i18n:        splitting it in separate atomic patches, that will be easier to review.
.. i18n:        You can make several successive merge proposals that depend on each
.. i18n:        other. This is also useful when you work on different projects
.. i18n:        (e.g. a patch to *addons* that depends on another patch for *server*).
.. i18n:     #. If your patch still needs to change a lot of lines at once into a
.. i18n:        core branch (it's not likely you have a valid reason to do so), and
.. i18n:        if it cannot be split into separate parts (like a proposal for one
.. i18n:        refactoring, then one functional change, then one layout change, etc.),
.. i18n:        then you must absolutely consider providing dedicated tests in it.
.. i18n:        These tests should prove the correctness of the system after applying
.. i18n:        your patch, and will help reviewers assess the impact of your changes,
.. i18n:        and verify that your patch does not break existing functionality.
.. i18n:     #. One more time for good measure: keep your merge proposals as
.. i18n:        **small** as possible. This is normally quite possible if you keep
.. i18n:        the merge proposal in mind as soon as you start working on the code.
..

    #. Carefully select the **appropriate target branch** for your patch.
       For example if your patch introduces an improvement but does not
       technically fix a bug, do not bother proposing it for merging on
       a stable branch. Stable branches are **only** for bugfixes, so rather
       propose it on a trunk branch. See also the definition of a bug above.
    #. Obviously, **pay attention** to the
       :ref:`Coding Guidelines <coding-guidelines-link>`.
    #. While following coding guidelines, avoid being over-zealous. If existing
       code does not meet the guidelines, you should usually fix only the lines
       that you are modifying, not the rest. Otherwise you will quickly find
       yourself modifying everything, and your patch will be refused.
    #. Please **review** your own changes before committing them, to avoid
       introducing useless noise in the merge proposal, like additional
       whitespace, etc.
       Use ``bzr status``, then ``bzr diff`` or ``bzr cdiff`` to know 
       exactly what you changed, before committing.
    #. Don't hesitate to revert a bad commit, it's the right time to do it
       before you push or propose your branch. ``bzr uncommit`` is a useful
       tool when working locally.
    #. Work on a separate feature/bug/whatever at a time. Do not mix lots of
       changes in one merge proposal, as it will be too complicated to review,
       thus refused.
    #. Make **separate branches and merge proposals** for separate changes.
    #. The **smaller** and **cleaner** a merge proposal, the **higher** the 
       chance of seeing it merged.
    #. **Avoid any kind of automatic formatting**, like white-space
       conversion or re-wrapping. Even if the original code is ugly, this 
       will make it possibly much harder to review. 
       If you really want to do it, make it a separate branch and
       merge proposal for that, clearly stating why you did so.
    #. Be very accurate and honest in the description of your patch, and in
       the commit messages. Do not propose a patch claiming that it contains
       "*just some layout improvements*" and try to slip into it some
       functional changes as well, or new fields that you added, etc.
       In fact you should explicitly warn the reviewers about these parts,
       if you could not split them in separate merge proposals.
       Indeed the layout changes could be reviewed easily by testing the
       updated views, but any Python change needs to be reviewed carefully,
       and should *never* go unnoticed.
    #. If your patch is very long (say, more than 100 lines), consider 
       splitting it in separate atomic patches, that will be easier to review.
       You can make several successive merge proposals that depend on each
       other. This is also useful when you work on different projects
       (e.g. a patch to *addons* that depends on another patch for *server*).
    #. If your patch still needs to change a lot of lines at once into a
       core branch (it's not likely you have a valid reason to do so), and
       if it cannot be split into separate parts (like a proposal for one
       refactoring, then one functional change, then one layout change, etc.),
       then you must absolutely consider providing dedicated tests in it.
       These tests should prove the correctness of the system after applying
       your patch, and will help reviewers assess the impact of your changes,
       and verify that your patch does not break existing functionality.
    #. One more time for good measure: keep your merge proposals as
       **small** as possible. This is normally quite possible if you keep
       the merge proposal in mind as soon as you start working on the code.
