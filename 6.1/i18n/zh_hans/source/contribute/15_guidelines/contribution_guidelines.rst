.. i18n: .. _technical-guidelines-link:
.. i18n: 
.. i18n: Contribution Guidelines
.. i18n: -----------------------
..

.. _technical-guidelines-link:

贡献指南
-----------------------

.. i18n: Bug reporting
.. i18n: +++++++++++++
..

提交Bug
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

合并申请 & 修补程序
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

.. i18n:     #. Register on Launchpad if not done yet
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
.. i18n:        ..note:: If you want to avoid downloading many times the large history
.. i18n:                 of OpenERP's source code, you may want to create a proper
.. i18n:                 shared repository.
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

    #. Register on Launchpad if not done yet
    #. If you wish to be able to easily publish your changes, setup
       an SSH private/public key pair and register your public key
       on your LaunchPad profile page, then use the following command
       to provide your LP login to Bazaar::

        $ bzr launchpad-login <your-launchpad-login> 

    #. Grab a local copy of the branch you want to patch, e.g. for the
       development version of the OpenERP server, that would be::

        $ bzr branch lp:openobject-server

       ..note:: If you want to avoid downloading many times the large history
                of OpenERP's source code, you may want to create a proper
                shared repository.

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

.. i18n: .. _shared_repositories:
.. i18n: 
.. i18n: Using shared repositories to speed up branch management
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++++++++++
..

.. _shared_repositories:

使用共享库以加快分支管理
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: Bazaar is a distributed version control system, and this means that every time
.. i18n: you copy, upload or download a bazaar branch, you are carrying around a complete
.. i18n: repository. OpenERP's repositories now contain several hundred megabytes of
.. i18n: history, and this may represent a fair bit of bandwidth and time whenever
.. i18n: you transfer a branch over the network (for example when you want to
.. i18n: :ref:`create a merge proposal <merge_proposals_guidelines>`).
..

Bazaar is a distributed version control system, and this means that every time
you copy, upload or download a bazaar branch, you are carrying around a complete
repository. OpenERP's repositories now contain several hundred megabytes of
history, and this may represent a fair bit of bandwidth and time whenever
you transfer a branch over the network (for example when you want to
:ref:`create a merge proposal <merge_proposals_guidelines>`).

.. i18n: There are ways to avoid this overhead if you learn to master the concepts of
.. i18n: *shared repositories*  and *stacked branches* of Bazaar and Launchpad.
..

There are ways to avoid this overhead if you learn to master the concepts of
*shared repositories*  and *stacked branches* of Bazaar and Launchpad.

.. i18n: Shared Repositories
.. i18n: ^^^^^^^^^^^^^^^^^^^
..

Shared Repositories
^^^^^^^^^^^^^^^^^^^

.. i18n: A "shared repository" allows several branches to be stored under an umbrella
.. i18n: repository that centralizes the history of the branches, avoiding duplication
.. i18n: of the revisions. Importing a new branch in such a shared repo will only
.. i18n: require the download of the history delta: the revisions in the new branch
.. i18n: that are not yet known in the shared repository.
.. i18n: It works in your local copy of the branches as long as you make sure to
.. i18n: branch/pull inside a relevant shared repository.
..

A "shared repository" allows several branches to be stored under an umbrella
repository that centralizes the history of the branches, avoiding duplication
of the revisions. Importing a new branch in such a shared repo will only
require the download of the history delta: the revisions in the new branch
that are not yet known in the shared repository.
It works in your local copy of the branches as long as you make sure to
branch/pull inside a relevant shared repository.

.. i18n: A shared repository is created using the ``bzr init-repo`` command.
.. i18n: For mode details have a look at the shared repository tutorial:
.. i18n: http://wiki.bazaar.canonical.com/SharedRepositoryTutorial
..

A shared repository is created using the ``bzr init-repo`` command.
For mode details have a look at the shared repository tutorial:
http://wiki.bazaar.canonical.com/SharedRepositoryTutorial

.. i18n: Stacked branches
.. i18n: ^^^^^^^^^^^^^^^^
..

Stacked branches
^^^^^^^^^^^^^^^^

.. i18n: As described in the official Bazaar documentation,
.. i18n: a *stacked branch* is a branch that knows how to find revisions in another
.. i18n: branch (the stacked-on branch). Stacked branches store just the unique
.. i18n: revisions that are not in the stacked-on branch, making them faster to create
.. i18n: and more storage efficient.
..

As described in the official Bazaar documentation,
a *stacked branch* is a branch that knows how to find revisions in another
branch (the stacked-on branch). Stacked branches store just the unique
revisions that are not in the stacked-on branch, making them faster to create
and more storage efficient.

.. i18n: Launchpad will automatically try to stack new branches you push onto the
.. i18n: trunk branch. This means that whenever you execute a ``bzr push lp:...``
.. i18n: command, it will only need to upload the revisions that are not present
.. i18n: in the latest trunk.
.. i18n: You can also manually specify the branch to stack on using the ``--stacked-on``
.. i18n: parameter. This may be useful if you are pushing branches that have
.. i18n: significant deltas with the trunk, such as older stable branches.
..

Launchpad will automatically try to stack new branches you push onto the
trunk branch. This means that whenever you execute a ``bzr push lp:...``
command, it will only need to upload the revisions that are not present
in the latest trunk.
You can also manually specify the branch to stack on using the ``--stacked-on``
parameter. This may be useful if you are pushing branches that have
significant deltas with the trunk, such as older stable branches.

.. i18n: For more details on stacked branches, see also the official
.. i18n: `Bazaar documentation <http://doc.bazaar.canonical.com/bzr.2.5/en/user-guide/stacked.html>`_.
..

For more details on stacked branches, see also the official
`Bazaar documentation <http://doc.bazaar.canonical.com/bzr.2.5/en/user-guide/stacked.html>`_.

.. i18n: In a nutshell
.. i18n: ^^^^^^^^^^^^^
..

In a nutshell
^^^^^^^^^^^^^

.. i18n: Practically, here is how you can use shared repositories and stacked branches
.. i18n: to speed up day-to-day branch management.
..

Practically, here is how you can use shared repositories and stacked branches
to speed up day-to-day branch management.

.. i18n: Downstream
.. i18n: **********
..

下载
**********

.. i18n: To initialize a proper shared repository you do the following::
.. i18n: 
.. i18n:     # create an empty repo for addons
.. i18n:     $ bzr init-repo addons
.. i18n:     $ cd addons
.. i18n:     # grab trunk addons -> full download!
.. i18n:     $ bzr branch lp:openobject-addons trunk
..

To initialize a proper shared repository you do the following::

    # create an empty repo for addons
    $ bzr init-repo addons
    $ cd addons
    # grab trunk addons -> full download!
    $ bzr branch lp:openobject-addons trunk

.. i18n: The first download in the repository will be the only full one, because it
.. i18n: starts empty. If you have a local copy of some addons branch somewhere, you can
.. i18n: branch from the local path instead of the ``lp:`` URL, it will be much faster.
..

The first download in the repository will be the only full one, because it
starts empty. If you have a local copy of some addons branch somewhere, you can
branch from the local path instead of the ``lp:`` URL, it will be much faster.

.. i18n: From then on, you can download any remote or local addons branch inside this
.. i18n: shared repo, bzr will automatically detect the shared repo and only download
.. i18n: the revisions that were not know yet in it (the delta).
.. i18n: For example::
.. i18n: 
.. i18n:     # grab 6.1 addons -> delta only
.. i18n:     $ bzr branch lp:openobject-addons/6.1
.. i18n:     # grab 6.0 addons -> delta only
.. i18n:     $ bzr branch lp:openobject-addons/6.0
..

From then on, you can download any remote or local addons branch inside this
shared repo, bzr will automatically detect the shared repo and only download
the revisions that were not know yet in it (the delta).
For example::

    # grab 6.1 addons -> delta only
    $ bzr branch lp:openobject-addons/6.1
    # grab 6.0 addons -> delta only
    $ bzr branch lp:openobject-addons/6.0

.. i18n: .. note:: the `OpenERP 6.1 Release Notes <http://bit.ly/openerp61RN>`_ mention a
.. i18n:     a script that is used by OpenERP developers to initialize a development
.. i18n:     environment. It can automate the creation of the share repository structure.
.. i18n:     You can use it as follows::
.. i18n: 
.. i18n:         $ bzr cat -d lp:~openerp-dev/openerp-tools/trunk setup.sh | sh
.. i18n:         $ make help          # << Read the available commands
.. i18n:         $ make init-trunk    # << Fetch the trunk projects in a shared repo
.. i18n:         $ make server        # << Start OpenERP Server with embedded Web
..

.. note:: the `OpenERP 6.1 Release Notes <http://bit.ly/openerp61RN>`_ mention a
    a script that is used by OpenERP developers to initialize a development
    environment. It can automate the creation of the share repository structure.
    You can use it as follows::

        $ bzr cat -d lp:~openerp-dev/openerp-tools/trunk setup.sh | sh
        $ make help          # << Read the available commands
        $ make init-trunk    # << Fetch the trunk projects in a shared repo
        $ make server        # << Start OpenERP Server with embedded Web

.. i18n: Upstream
.. i18n: ********
..

上传
********

.. i18n: It's a little bit different when you push a branch: there is no shared
.. i18n: repository, but Launchpad will automatically use stacked branches.
.. i18n: Have a look at the metadata of the 6.1 addons branch on Launchpad here:
.. i18n: https://code.launchpad.net/~openerp/openobject-addons/6.1
..

It's a little bit different when you push a branch: there is no shared
repository, but Launchpad will automatically use stacked branches.
Have a look at the metadata of the 6.1 addons branch on Launchpad here:
https://code.launchpad.net/~openerp/openobject-addons/6.1

.. i18n: You'll see mentioned at the bottom: ``Stacked on: lp:openobject-addons``.
.. i18n: It means that the 6.1 branch is stacked on the trunk branch.
..

You'll see mentioned at the bottom: ``Stacked on: lp:openobject-addons``.
It means that the 6.1 branch is stacked on the trunk branch.

.. i18n: This happens transparently whenever you push a branch in a LP project: bazaar
.. i18n: will automatically stack it on the trunk branch. But you can specify the
.. i18n: stacking branch yourself if you prefer, which is useful sometimes (see below).
..

This happens transparently whenever you push a branch in a LP project: bazaar
will automatically stack it on the trunk branch. But you can specify the
stacking branch yourself if you prefer, which is useful sometimes (see below).

.. i18n: Let's say I write a bugfix following the `merge_proposals_guidelines`_ .
.. i18n: When I do the ``push`` this is what I will see::
.. i18n: 
.. i18n:     $ bzr push lp:~openerp-community/openobject-addons/trunk-bug-123456
.. i18n:     Using default stacking branch /+branch-id/243984 at chroot-71245584:///~openerp-community/openobject-addons/
.. i18n:     (...)
..

Let's say I write a bugfix following the `merge_proposals_guidelines`_ .
When I do the ``push`` this is what I will see::

    $ bzr push lp:~openerp-community/openobject-addons/trunk-bug-123456
    Using default stacking branch /+branch-id/243984 at chroot-71245584:///~openerp-community/openobject-addons/
    (...)

.. i18n: This cryptic message means my branch was stacked on trunk, so only the
.. i18n: revisions that are not present in trunk will need to be uploaded. As a result,
.. i18n: pushing a bugfix branch on trunk usually only takes a few seconds.
..

This cryptic message means my branch was stacked on trunk, so only the
revisions that are not present in trunk will need to be uploaded. As a result,
pushing a bugfix branch on trunk usually only takes a few seconds.

.. i18n: Now if you're working on a stable branch rather than trunk, there may still be a large
.. i18n: delta to upload because there are many revisions that were added to in stable after
.. i18n: it was forked off trunk (the largest ones being the translations!)
.. i18n: In that case you can manually tell bzr to stack on the 6.1 branch rather than trunk,
.. i18n: as follows::
.. i18n: 
.. i18n:     $ bzr push lp:~openerp-community/openobject-addons/6.1-bug-123456 --stacked-on bzr+ssh://bazaar.launchpad.net/~openerp/openobject-addons/6.1
..

Now if you're working on a stable branch rather than trunk, there may still be a large
delta to upload because there are many revisions that were added to in stable after
it was forked off trunk (the largest ones being the translations!)
In that case you can manually tell bzr to stack on the 6.1 branch rather than trunk,
as follows::

    $ bzr push lp:~openerp-community/openobject-addons/6.1-bug-123456 --stacked-on bzr+ssh://bazaar.launchpad.net/~openerp/openobject-addons/6.1

.. i18n: There are a couple of caveats with this stacking mechanism:
..

There are a couple of caveats with this stacking mechanism:

.. i18n:     - the ``--stacked-on`` parameter must use the full ``bzr+ssh://bazaar.launchpad.net``
.. i18n:       protocol prefix, the usual ``lp:`` shortcut does not work
.. i18n:       (`yet? <https://bugs.launchpad.net/bzr/+bug/296592>`_)
.. i18n:     - the stacking cannot be modified on remote branches, so if you get it wrong the
.. i18n:       first time (or it simply fails) you must go on the branch URL on Launchpad
.. i18n:       (``https://code.launchpad.net/full_name_of_branch``) and delete it, then
.. i18n:       push again.
..

    - the ``--stacked-on`` parameter must use the full ``bzr+ssh://bazaar.launchpad.net``
      protocol prefix, the usual ``lp:`` shortcut does not work
      (`yet? <https://bugs.launchpad.net/bzr/+bug/296592>`_)
    - the stacking cannot be modified on remote branches, so if you get it wrong the
      first time (or it simply fails) you must go on the branch URL on Launchpad
      (``https://code.launchpad.net/full_name_of_branch``) and delete it, then
      push again.

.. i18n: This certainly takes a bit of getting used to, but once you understand the key
.. i18n: ideas you will almost never need full branch uploads/downloads anymore.
..

This certainly takes a bit of getting used to, but once you understand the key
ideas you will almost never need full branch uploads/downloads anymore.
