
.. _bazaar-link:

Bazaar, the version control system
----------------------------------

.. index::
   single: Bazaar
   single: version control system
.. 

The new development process uses Bazaar via launchpad.net instead of Subversion.
Bazaar offers flexibility with this distributed model. You can see our
branches on https://code.launchpad.net/~openerp.

.. describe:: Explanation of directories:

Two teams have been created on launchpad:

  * OpenERP quality teams --> they can commit on:

    - lp:~openerp/openobject-addons/4.2
    - lp:~openerp/openobject-addons/trunk
    - lp:~openerp/openobject-addons/4.2-extra-addons
    - lp:~openerp/openobject-addons/trunk-extra-addons
    - lp:~openerp/openobject-bi/trunk-addons
    - lp:~openerp/openobject-bi/trunk-cli
    - lp:~openerp/openobject-bi/trunk-client-web
    - lp:~openerp/openobject-client/4.2
    - lp:~openerp/openobject-client/trunk
    - lp:~openerp/openobject-client-web/4.2
    - lp:~openerp/openobject-client-web/trunk
    - lp:~openerp/openobject-server/4.2
    - lp:~openerp/openobject-server/trunk

  * OpenERP-commiter --> They can commit on:

    - lp:~openerp/openobject-addons/4.2-extra-addons
    - lp:~openerp/openobject-addons/trunk-extra-addons

In this group, we include some of our partners who will be selected on merit by the quality team.

  * Contributors --> They can commit on:

    - lp:~openerp-community

.. describe:: How can I be included in OpenERP-commiter team ?

To become a committer a contributor must show interest
on working for openerp project and ability to do it properly as
selection is based on merit. It can be by proposing bug
fixes, features requested on our :ref:`bug tracker <bug-tracker-link>` system.
You can even suggest additional modules and/or functionality on our :ref:`bug
tracker <bug-tracker-link>` system.

.. describe:: How can I suggest some additional modules or functionality ?

To create additional modules and/or functionality and include them in
the project:

  #. open a branch in launchpad
  #. report and suggest your work via your new branch to our :ref:`bug tracker
     <bug-tracker-link>` system (there are two ways: bugs report for bug and
     blueprint for idea / functionality)
  #. wait for approval by our quality team

Or the quality team approved your work and merge it into the official branch
(like explained in the :ref:`bug tracker <bug-tracker-link>` section), or they
refuse it and ask you to improve your work before merging it in our official
branch.

Installing Bazaar
+++++++++++++++++

.. index::
   single: Bazaar; installation
   single: Installation; Bazaar
.. 

Get Bazaar version control to pull the source from Launchpad.

To install bazaar on any ubuntu distribution, you can edit /etc/apt/sources.list by

::

  sudo gedit /etc/apt/sources.list

and put these lines in it:

::

  deb http://ppa.launchpad.net/bzr/ubuntu intrepid main
  deb-src http://ppa.launchpad.net/bzr/ubuntu intrepid main

Then, do the following

::

  sudo apt-get install bzr

To work correctly, bzr version must be at least 1.3. Check it with the command:

::

  bzr --version

If you have an older version check this url: http://bazaar-vcs.org/Download
On debian, in any distribution, the 1.5 version is working, you can get it on this url: http://backports.org/debian/pool/main/b/bzr/bzr_1.5-1~bpo40+1_i386.deb

If you experience problems with Bazaar, please read the :ref:`bazaar-faq-link` before asking any questions.

Quick Summary
+++++++++++++

.. index::
   single: Bazaar; summary
.. 

This is the official and proposed way to contribute on OpenERP and OpenObject.

To download the latest sources and create your own local branches of OpenERP, do this::

  mkdir openerp
  cd openerp
  bzr branch lp:~openerp/openobject-server/trunk server
  bzr branch lp:~openerp/openobject-addons/trunk addons
  bzr branch lp:~openerp-commiter/openobject-addons/trunk-extra-addons addons-extra
  bzr branch lp:~openerp-community/openobject-addons/trunk-addons-community addons-community
  bzr branch lp:~openerp/openerp-web/trunk web
  bzr branch lp:~openerp/openobject-client/trunk client
  bzr branch lp:~openerp-community/openobject-doc/6.1 doc

This will download all components of openerp (server, client, addons) and create links of modules in addons on your server so that you can use it directly. You can change the bzr_set.py file to select what you want to download exactly. Now, you can edit the code and commit in your local branch.::

  EDIT addons/account/account.py
  cd addons
  bzr ci -m "Testing Modifications"

Once your code is good enough and follow the :ref:`coding-guidelines-link`, you
can push your branch in launchpad. You may have to create an account on
launchpad first, register your public key, and subscribe to the `openerp-community <https://launchpad.net/~openerp-community>`_ team. Then, you
can push your branch. Suppose you want to push your addons::

  cd addons
  bzr push lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME
  bzr bind lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME

After having done that, your branch is public on Launchpad, in the `OpenObject
project <https://code.launchpad.net/openobject>`_, and committers can work on
it, review it and propose for integration in the official branch. The last line
allows you to rebind your branch to the one which is on launchpad, after having
done this, your commit will be applied on launchpad directly (unless you use ``--local``)::

  bzr pull    # Get modifications on your branch from others
  EDIT STUFF
  bzr ci    # commit your changes on your public branch

If your changes fix a public bug on launchpad, you can use this to mark the bug as fixed by your branch::

  bzr ci --fixes=lp:453123   # Where 453123 is a bug ID

Once your branch is mature, mark it as mature in the web interface of launchpad
and request for merging in the official release. Your branch will be reviewed
by a committer and then the quality team to be merged in the official release.

.. _how-to-get-the-latest-trunk-source-code-link:

How to get the latest trunk source code
+++++++++++++++++++++++++++++++++++++++

Get a clone of each repository::

  bzr clone lp:~openerp/openobject-server/trunk server
  bzr clone lp:~openerp/openobject-client/trunk client
  bzr clone lp:~openerp/openobject-client-web/trunk client-web
  bzr clone lp:~openerp/openobject-addons/trunk addons

If you want to get a clone of the extra-addons repository, you can execute this command::

  bzr clone lp:~openerp-commiter/openobject-addons/trunk-extra-addons extra-addons

run the setup scripts in the respective directories::

  python2.5 setup.py build
  sudo python2.5 setup.py install

Currently the initialisation procedure of the server parameter --init=all to
populate the database seems to be broken in trunk.

It is recommended to create a new database via the gtk-client. Until then the web-client will not work.

Start OpenERP server like this: ::

  ./openerp-server.py --addons-path=~/home/workspace/stable/addons

The ``bin/addons`` will be considered as default addons directory which can be
overridden by the ``~/home/workspace/stable/addons``. That is if an addon exists in
``bin/addons`` as well as ``~/home/workspace/stable/addons`` (custom path) the later one will
be given preference over the ``bin/addons`` (default path).

How to commit Your Work
+++++++++++++++++++++++

If you want to contribute on OpenERP or OpenObject, here is the proposed method:

  * You create a branch on launchpad on the project that interests you. It's
    important that you create your branch on launchpad and not on your local
    system so that we can easily merge, share code between projects and
    centralize future developments.
  * You develop your own features or bugfixes
    in your own branch on launchpad. Don't forget to set the status of your
    branch (new, experimental, development, mature, ...) so that contributors
    know what they can and cannot use.
  * Once your code is good enough, propose your branch for merging
  * Your work will be evaluated by a member of the committers team.

    - If they accept your branch for integration in the official version, they
      will submit to the quality team that will review and merge in the official
      branch.
    - If the commiter team refuses your branch, they will explain why
      so that you can review the code to better fit the guidelines (problem for
      future migrations, ...)

The `extra-addons branch <https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-extra-addons>`_,
that stores all extra modules, is directly accessible to all committers. If you
are a committer, you can work directly on this branch and commit your own work.
This branch does not require validation by the quality team. You should put
there your special modules for your own customers.

If you want to propose or develop new modules, we suggest creating your
own branch in the `openobject-addons project <https://launchpad.net/openobject-addons>`_
and develop within your branch. You can fill in a bug to request that
your modules are integrated in one of the two branches:

  * `extra-addons branch <https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-extra-addons>`_ : if your module touches a few companies
  * `addons <https://code.launchpad.net/~openerp/openobject-addons/trunk>`_ : if your module will be useful for most of the companies

We invite all our partners and contributors to work in that way so that we can
easily integrate and share the work done between the different projects.

Use Case Developers
++++++++++++++++++++

This page presents the approach you should follow on how to contribute in
OpenObject. Suppose you want to develop new features in the addons or simply
correct some bugfixes.

If you have the right to modify the branch you plan to change, you can
do it directly. For example, a quality team member doing a bugfix can do it
directly on the main branch. Or committers can work directly on the
extra-addons. If you don't have the right to modify the branch you plan to
change or if you want to branch because you are starting big developments
that may break the code, the first thing to do is to branch the repository
you plan to modify::

  bzr branch lp:openobject-addons lp:~openerp-commiter/openobject-addons/trunk-new-reporting

In that case, the branch created will be for the openerp-commiter team. If you
are not a committer, you can create the branch for the community team
openerp-community or just for yourself, depending if you allow others to
directly commit on your branch or not. For all Tiny employees, we propose to
create all branches for the team openerp-commiter. An OpenERP service company
may create a team for their company and create branches at the name of their
team. This prevents others changing their
customer branch.

Once the branch is created, you must checkout a local copy to work on::

  bzr co lp:~openerp-commiter/openobject-addons/trunk-new-reporting

This will download the branch on your local computer. You can then start
developing on it. From time to time, you should commit the work done::

  bzr ci

This will send your modification to the branch:
lp:~openerp-commiter/openobject-addons/trunk-new-reporting. Don't forget to
change the status of the branch to show other contributors the status of your
current work on
https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-new-reporting

For instance, you can switch the status to "In Development" to show you are
working on it and put the status to "Mature" when you'd like to have your code
integrated in the official release.

During your development, if you want to receive the latest modifications from
the parent branches, you can merge it::

  bzr merge

Once your development on this branch are OK, you can ask a committer to review
and merge it or fill in a bug in the bugtracker. A committer will then review
your work and merge it to the official branch if it's good enough.

Commit Guidelines
+++++++++++++++++

When committing your work to Launchpad, please respect these policies:

The stable branch is for bugfixes
"""""""""""""""""""""""""""""""""

The stable branch must be used for bugfixes. **Only bugfixes**.

The new features (+the bugfixes on these new functionality) have to be done
in the trunk branch.

.. note:: We will periodically backport all the fixes from stable to trunk.

Set the author's name, if it's different from the committer
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Always set the author's name, if it's different from the committer. It is not
acceptable at all to commit a contributor's work without at least his/her name in
the commit message. We have to respect them and their work, so
please use ``--author="<author_name>"`` when merging work or patching features
from community.

::

  e.g: bzr commit --author="<author_name>"

Write a helpful commit message
""""""""""""""""""""""""""""""

Use a *commit tag* in **each** message. This tag should be one of:

* **[IMP]**
* **[FIX]**
* **[REF]**
* **[ADD]**
* **[REM]**

:[IMP]: For improvements

:[FIX]: For bug fixes

:[REF]: For refactoring (improvements of the source code, without changing the
  functionality or behavior. See http://en.wikipedia.org/wiki/Refactoring for
  further details)

:[ADD]: For adding new resources

:[REM]: For removing of resources

* Always put a meaningful commit message. Commit message should be self
  explanatory including the name of the module that has been changed. No more
  *"bugfix"* or *"improvements"* anymore! (the only single word commit message
  accepted is "merge")

* If you are fixing the bugs use ``--fixes=lp:<bug_number>`` instead of putting the
  number of the bug in the commit message.

* Use the revision id instead of the revision number when you make reference to
  a revision in your commit message. You can get this revision id, by using the
  command ``bzr version-info``.

::

  e.g:

    Not Correct : bzr commit -m “[FIX]: reverted bad revision (cannot install new db) 
      with revision number:525425”

    Correct : bzr commit -m “[FIX]: reverted bad revision (cannot install new db) 
    with revision number id: qdp@tinyerp.com-20090602143202-ehmntlift166mrnn”

    Not Correct : bzr commit -m "Bug 568889 : typo corrected"

    Correct : bzr commit --fixes=lp:568889 -m "[FIX] account module: typo corrected"

.. note:: How to handle translations ?

    use **[IMP]** if you translated a message in a po file

    use **[ADD]** if you added an new po file

Avoid big commits
"""""""""""""""""

Don't make a commit that will impact lots of modules. Try to split it into
different commits where impacted modules are different (It will be
helpful when we are going to revert that module separately).


