.. _technical-guidelines-link:

Contribution Guidelines
-----------------------

Bug reporting
+++++++++++++

For all details regarding bug reports and bug processing, please
refer to the :ref:`bug_management` section.

.. _merge_proposals:

Merge Proposals & Patches
+++++++++++++++++++++++++

It is quite easy to make a patch and propose it for merging on any
OpenERP project, be it to fix a bug, improve an existing feature,
or add something new.

However, in order to tremendously increase the chances of getting
your patch noticed and merged, you should pay attention to the
:ref:`merge_proposals_policy` and then carefully follow the
:ref:`merge_proposals_guidelines`.


.. _merge_proposals_policy:

Merge Proposal Acceptance Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OpenERP's R&D expects to receive merge proposals from the Community in these areas:

  - patches to correct a bug in an official addons
  - patches to improve an existing official addon, such as extending a feature or adding one

OpenERP's R&D does **not** expect to receive merge proposals from the Community in these areas:

  - addition of an extra feature to an official addons, when the feature should really
    provided by a separate (new) module
  - addition of a new module to the official addons

For these last cases, it is better to put the feature into new modules entirely maintained
by their authors in their own Launchpad repository, and published on OpenERP Apps,
to be visible by the whole Community. This is totally unrelated to the quality of the
proposition: there are tons of great community modules on OpenERP Apps, some of them already
downloaded thousands of times!

However, including a module in the official release is a big commitment in terms of review
maintenance, support, etc. In addition, it would quickly bloat the OpenERP core if done too
often, compromising its agility and maintainability, and thus the future of the product.
On the other hand, by progressively integrating OpenERP Apps better in the product, we should
reach the same visibility for Community modules, without incurring these risks.

Therefore the process of including a community module into the official addons is entirely 
driven by OpenERP R&D based on the product strategy. In addition to features selected by
OpenERP Product Managers, features that are considered *REQUIRED* to use OpenERP in a certain
market/domain will also be considered for inclusion.
Deciding whether a feature is *REQUIRED* is quite subjective, but the following hints are useful:

 - if most established competitors on the given market/domain implement this feature, and
   this domain is normally addressed by official OpenERP addons, then it's likely *REQUIRED*.
 - on the other hand, if **no** established software competitors on the given market/domain
   implement this feature, then it's probably *NOT REQUIRED*.

This certainly doesn't mean we don't want to innovate (that's the part where Product Managers
choose new features!), this is only for deciding that a module is *REQUIRED* and thus it is
*necessary* to include it in the default installations.

Of course, on top of the above, a merge proposal needs to pass the functional and technical 
review by OpenERP's R&D, and even though we do our best to process them in a timely fashion,
there is no guarantee it will be accepted, nor when.


.. _merge_proposals_guidelines:

Merge Proposal Guidelines
^^^^^^^^^^^^^^^^^^^^^^^^^

The basic procedure is the following:

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


The following guidelines will give you further advice in getting
your patch through:

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


