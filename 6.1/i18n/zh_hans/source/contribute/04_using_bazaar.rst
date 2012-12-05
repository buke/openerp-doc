.. i18n: .. _bazaar-link:
.. i18n: 
.. i18n: Bazaar, the version control system
.. i18n: ----------------------------------
..

.. _bazaar-link:

Bazaar 版本控制工具
----------------------------------

.. i18n: .. index::
.. i18n:    single: Bazaar
.. i18n:    single: version control system
.. i18n: .. 
..

.. index::
   single: Bazaar
   single: version control system
.. 

.. i18n: The new development process uses Bazaar via launchpad.net instead of Subversion.
.. i18n: Bazaar offers flexibility with this distributed model. You can see our
.. i18n: branches on https://code.launchpad.net/~openerp.
..

The new development process uses Bazaar via launchpad.net instead of Subversion.
Bazaar offers flexibility with this distributed model. You can see our
branches on https://code.launchpad.net/~openerp.

.. i18n: .. describe:: Explanation of directories:
..

.. describe:: Explanation of directories:

.. i18n: Two teams have been created on launchpad:
..

Two teams have been created on launchpad:

.. i18n:   * OpenERP quality teams --> they can commit on:
.. i18n: 
.. i18n:     - lp:~openerp/openobject-addons/4.2
.. i18n:     - lp:~openerp/openobject-addons/trunk
.. i18n:     - lp:~openerp/openobject-addons/4.2-extra-addons
.. i18n:     - lp:~openerp/openobject-addons/trunk-extra-addons
.. i18n:     - lp:~openerp/openobject-bi/trunk-addons
.. i18n:     - lp:~openerp/openobject-bi/trunk-cli
.. i18n:     - lp:~openerp/openobject-bi/trunk-client-web
.. i18n:     - lp:~openerp/openobject-client/4.2
.. i18n:     - lp:~openerp/openobject-client/trunk
.. i18n:     - lp:~openerp/openobject-client-web/4.2
.. i18n:     - lp:~openerp/openobject-client-web/trunk
.. i18n:     - lp:~openerp/openobject-server/4.2
.. i18n:     - lp:~openerp/openobject-server/trunk
.. i18n: 
.. i18n:   * OpenERP-commiter --> They can commit on:
.. i18n: 
.. i18n:     - lp:~openerp/openobject-addons/4.2-extra-addons
.. i18n:     - lp:~openerp/openobject-addons/trunk-extra-addons
..

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

.. i18n: In this group, we include some of our partners who will be selected on merit by the quality team.
..

In this group, we include some of our partners who will be selected on merit by the quality team.

.. i18n:   * Contributors --> They can commit on:
.. i18n: 
.. i18n:     - lp:~openerp-community
..

  * Contributors --> They can commit on:

    - lp:~openerp-community

.. i18n: .. describe:: How can I be included in OpenERP-commiter team ?
..

.. describe:: How can I be included in OpenERP-commiter team ?

.. i18n: To become a committer a contributor must show interest
.. i18n: on working for openerp project and ability to do it properly as
.. i18n: selection is based on merit. It can be by proposing bug
.. i18n: fixes, features requested on our :ref:`bug tracker <bug-tracker-link>` system.
.. i18n: You can even suggest additional modules and/or functionality on our :ref:`bug
.. i18n: tracker <bug-tracker-link>` system.
..

To become a committer a contributor must show interest
on working for openerp project and ability to do it properly as
selection is based on merit. It can be by proposing bug
fixes, features requested on our :ref:`bug tracker <bug-tracker-link>` system.
You can even suggest additional modules and/or functionality on our :ref:`bug
tracker <bug-tracker-link>` system.

.. i18n: .. describe:: How can I suggest some additional modules or functionality ?
..

.. describe:: How can I suggest some additional modules or functionality ?

.. i18n: To create additional modules and/or functionality and include them in
.. i18n: the project:
..

To create additional modules and/or functionality and include them in
the project:

.. i18n:   #. open a branch in launchpad
.. i18n:   #. report and suggest your work via your new branch to our :ref:`bug tracker
.. i18n:      <bug-tracker-link>` system (there are two ways: bugs report for bug and
.. i18n:      blueprint for idea / functionality)
.. i18n:   #. wait for approval by our quality team
..

  #. open a branch in launchpad
  #. report and suggest your work via your new branch to our :ref:`bug tracker
     <bug-tracker-link>` system (there are two ways: bugs report for bug and
     blueprint for idea / functionality)
  #. wait for approval by our quality team

.. i18n: Or the quality team approved your work and merge it into the official branch
.. i18n: (like explained in the :ref:`bug tracker <bug-tracker-link>` section), or they
.. i18n: refuse it and ask you to improve your work before merging it in our official
.. i18n: branch.
..

Or the quality team approved your work and merge it into the official branch
(like explained in the :ref:`bug tracker <bug-tracker-link>` section), or they
refuse it and ask you to improve your work before merging it in our official
branch.

.. i18n: Installing Bazaar
.. i18n: +++++++++++++++++
..

安装 Bazaar
+++++++++++++++++

.. i18n: .. index::
.. i18n:    single: Bazaar; installation
.. i18n:    single: Installation; Bazaar
.. i18n: .. 
..

.. index::
   single: Bazaar; installation
   single: Installation; Bazaar
.. 

.. i18n: Get Bazaar version control to pull the source from Launchpad.
..

Get Bazaar version control to pull the source from Launchpad.

.. i18n: To install bazaar on any ubuntu distribution, you can edit /etc/apt/sources.list by
..

To install bazaar on any ubuntu distribution, you can edit /etc/apt/sources.list by

.. i18n: ::
.. i18n: 
.. i18n:   sudo gedit /etc/apt/sources.list
..

::

  sudo gedit /etc/apt/sources.list

.. i18n: and put these lines in it:
..

and put these lines in it:

.. i18n: ::
.. i18n: 
.. i18n:   deb http://ppa.launchpad.net/bzr/ubuntu intrepid main
.. i18n:   deb-src http://ppa.launchpad.net/bzr/ubuntu intrepid main
..

::

  deb http://ppa.launchpad.net/bzr/ubuntu intrepid main
  deb-src http://ppa.launchpad.net/bzr/ubuntu intrepid main

.. i18n: Then, do the following
..

接下来要做的

.. i18n: ::
.. i18n: 
.. i18n:   sudo apt-get install bzr
..

::

  sudo apt-get install bzr

.. i18n: To work correctly, bzr version must be at least 1.3. Check it with the command:
..

To work correctly, bzr version must be at least 1.3. Check it with the command:

.. i18n: ::
.. i18n: 
.. i18n:   bzr --version
..

::

  bzr --version

.. i18n: If you have an older version check this url: http://bazaar-vcs.org/Download
.. i18n: On debian, in any distribution, the 1.5 version is working, you can get it on this url: http://backports.org/debian/pool/main/b/bzr/bzr_1.5-1~bpo40+1_i386.deb
..

If you have an older version check this url: http://bazaar-vcs.org/Download
On debian, in any distribution, the 1.5 version is working, you can get it on this url: http://backports.org/debian/pool/main/b/bzr/bzr_1.5-1~bpo40+1_i386.deb

.. i18n: If you experience problems with Bazaar, please read the :ref:`bazaar-faq-link` before asking any questions.
..

If you experience problems with Bazaar, please read the :ref:`bazaar-faq-link` before asking any questions.

.. i18n: Quick Summary
.. i18n: +++++++++++++
..

快速摘要
+++++++++++++

.. i18n: .. index::
.. i18n:    single: Bazaar; summary
.. i18n: .. 
..

.. index::
   single: Bazaar; summary
.. 

.. i18n: This is the official and proposed way to contribute on OpenERP and OpenObject.
..

This is the official and proposed way to contribute on OpenERP and OpenObject.

.. i18n: To download the latest sources and create your own local branches of OpenERP, do this::
.. i18n: 
.. i18n:   mkdir openerp
.. i18n:   cd openerp
.. i18n:   bzr branch lp:~openerp/openobject-server/trunk server
.. i18n:   bzr branch lp:~openerp/openobject-addons/trunk addons
.. i18n:   bzr branch lp:~openerp-commiter/openobject-addons/trunk-extra-addons addons-extra
.. i18n:   bzr branch lp:~openerp-community/openobject-addons/trunk-addons-community addons-community
.. i18n:   bzr branch lp:~openerp/openerp-web/trunk web
.. i18n:   bzr branch lp:~openerp/openobject-client/trunk client
.. i18n:   bzr branch lp:~openerp-community/openobject-doc/6.1 doc
..

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

.. i18n: This will download all components of openerp (server, client, addons) and create links of modules in addons on your server so that you can use it directly. You can change the bzr_set.py file to select what you want to download exactly. Now, you can edit the code and commit in your local branch.::
.. i18n: 
.. i18n:   EDIT addons/account/account.py
.. i18n:   cd addons
.. i18n:   bzr ci -m "Testing Modifications"
..

This will download all components of openerp (server, client, addons) and create links of modules in addons on your server so that you can use it directly. You can change the bzr_set.py file to select what you want to download exactly. Now, you can edit the code and commit in your local branch.::

  EDIT addons/account/account.py
  cd addons
  bzr ci -m "Testing Modifications"

.. i18n: Once your code is good enough and follow the :ref:`coding-guidelines-link`, you
.. i18n: can push your branch in launchpad. You may have to create an account on
.. i18n: launchpad first, register your public key, and subscribe to the `openerp-community <https://launchpad.net/~openerp-community>`_ team. Then, you
.. i18n: can push your branch. Suppose you want to push your addons::
.. i18n: 
.. i18n:   cd addons
.. i18n:   bzr push lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME
.. i18n:   bzr bind lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME
..

Once your code is good enough and follow the :ref:`coding-guidelines-link`, you
can push your branch in launchpad. You may have to create an account on
launchpad first, register your public key, and subscribe to the `openerp-community <https://launchpad.net/~openerp-community>`_ team. Then, you
can push your branch. Suppose you want to push your addons::

  cd addons
  bzr push lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME
  bzr bind lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME

.. i18n: After having done that, your branch is public on Launchpad, in the `OpenObject
.. i18n: project <https://code.launchpad.net/openobject>`_, and committers can work on
.. i18n: it, review it and propose for integration in the official branch. The last line
.. i18n: allows you to rebind your branch to the one which is on launchpad, after having
.. i18n: done this, your commit will be applied on launchpad directly (unless you use ``--local``)::
.. i18n: 
.. i18n:   bzr pull    # Get modifications on your branch from others
.. i18n:   EDIT STUFF
.. i18n:   bzr ci    # commit your changes on your public branch
..

After having done that, your branch is public on Launchpad, in the `OpenObject
project <https://code.launchpad.net/openobject>`_, and committers can work on
it, review it and propose for integration in the official branch. The last line
allows you to rebind your branch to the one which is on launchpad, after having
done this, your commit will be applied on launchpad directly (unless you use ``--local``)::

  bzr pull    # Get modifications on your branch from others
  EDIT STUFF
  bzr ci    # commit your changes on your public branch

.. i18n: If your changes fix a public bug on launchpad, you can use this to mark the bug as fixed by your branch::
.. i18n: 
.. i18n:   bzr ci --fixes=lp:453123   # Where 453123 is a bug ID
..

If your changes fix a public bug on launchpad, you can use this to mark the bug as fixed by your branch::

  bzr ci --fixes=lp:453123   # Where 453123 is a bug ID

.. i18n: Once your branch is mature, mark it as mature in the web interface of launchpad
.. i18n: and request for merging in the official release. Your branch will be reviewed
.. i18n: by a committer and then the quality team to be merged in the official release.
..

Once your branch is mature, mark it as mature in the web interface of launchpad
and request for merging in the official release. Your branch will be reviewed
by a committer and then the quality team to be merged in the official release.

.. i18n: .. _how-to-get-the-latest-trunk-source-code-link:
.. i18n: 
.. i18n: How to get the latest trunk source code
.. i18n: +++++++++++++++++++++++++++++++++++++++
..

.. _how-to-get-the-latest-trunk-source-code-link:

怎么获取最新的主干代码
+++++++++++++++++++++++++++++++++++++++

.. i18n: Get a clone of each repository::
.. i18n: 
.. i18n:   bzr clone lp:~openerp/openobject-server/trunk server
.. i18n:   bzr clone lp:~openerp/openobject-client/trunk client
.. i18n:   bzr clone lp:~openerp/openobject-client-web/trunk client-web
.. i18n:   bzr clone lp:~openerp/openobject-addons/trunk addons
..

Get a clone of each repository::

  bzr clone lp:~openerp/openobject-server/trunk server
  bzr clone lp:~openerp/openobject-client/trunk client
  bzr clone lp:~openerp/openobject-client-web/trunk client-web
  bzr clone lp:~openerp/openobject-addons/trunk addons

.. i18n: If you want to get a clone of the extra-addons repository, you can execute this command::
.. i18n: 
.. i18n:   bzr clone lp:~openerp-commiter/openobject-addons/trunk-extra-addons extra-addons
..

If you want to get a clone of the extra-addons repository, you can execute this command::

  bzr clone lp:~openerp-commiter/openobject-addons/trunk-extra-addons extra-addons

.. i18n: run the setup scripts in the respective directories::
.. i18n: 
.. i18n:   python2.5 setup.py build
.. i18n:   sudo python2.5 setup.py install
..

run the setup scripts in the respective directories::

  python2.5 setup.py build
  sudo python2.5 setup.py install

.. i18n: Currently the initialisation procedure of the server parameter --init=all to
.. i18n: populate the database seems to be broken in trunk.
..

Currently the initialisation procedure of the server parameter --init=all to
populate the database seems to be broken in trunk.

.. i18n: It is recommended to create a new database via the gtk-client. Until then the web-client will not work.
..

It is recommended to create a new database via the gtk-client. Until then the web-client will not work.

.. i18n: Start OpenERP server like this: ::
.. i18n: 
.. i18n:   ./openerp-server.py --addons-path=~/home/workspace/stable/addons
..

Start OpenERP server like this: ::

  ./openerp-server.py --addons-path=~/home/workspace/stable/addons

.. i18n: The ``bin/addons`` will be considered as default addons directory which can be
.. i18n: overridden by the ``~/home/workspace/stable/addons``. That is if an addon exists in
.. i18n: ``bin/addons`` as well as ``~/home/workspace/stable/addons`` (custom path) the later one will
.. i18n: be given preference over the ``bin/addons`` (default path).
..

The ``bin/addons`` will be considered as default addons directory which can be
overridden by the ``~/home/workspace/stable/addons``. That is if an addon exists in
``bin/addons`` as well as ``~/home/workspace/stable/addons`` (custom path) the later one will
be given preference over the ``bin/addons`` (default path).

.. i18n: How to commit Your Work
.. i18n: +++++++++++++++++++++++
..

怎样提交你的成果
+++++++++++++++++++++++

.. i18n: If you want to contribute on OpenERP or OpenObject, here is the proposed method:
..

If you want to contribute on OpenERP or OpenObject, here is the proposed method:

.. i18n:   * You create a branch on launchpad on the project that interests you. It's
.. i18n:     important that you create your branch on launchpad and not on your local
.. i18n:     system so that we can easily merge, share code between projects and
.. i18n:     centralize future developments.
.. i18n:   * You develop your own features or bugfixes
.. i18n:     in your own branch on launchpad. Don't forget to set the status of your
.. i18n:     branch (new, experimental, development, mature, ...) so that contributors
.. i18n:     know what they can and cannot use.
.. i18n:   * Once your code is good enough, propose your branch for merging
.. i18n:   * Your work will be evaluated by a member of the committers team.
.. i18n: 
.. i18n:     - If they accept your branch for integration in the official version, they
.. i18n:       will submit to the quality team that will review and merge in the official
.. i18n:       branch.
.. i18n:     - If the commiter team refuses your branch, they will explain why
.. i18n:       so that you can review the code to better fit the guidelines (problem for
.. i18n:       future migrations, ...)
..

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

.. i18n: The `extra-addons branch <https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-extra-addons>`_,
.. i18n: that stores all extra modules, is directly accessible to all committers. If you
.. i18n: are a committer, you can work directly on this branch and commit your own work.
.. i18n: This branch does not require validation by the quality team. You should put
.. i18n: there your special modules for your own customers.
..

The `extra-addons branch <https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-extra-addons>`_,
that stores all extra modules, is directly accessible to all committers. If you
are a committer, you can work directly on this branch and commit your own work.
This branch does not require validation by the quality team. You should put
there your special modules for your own customers.

.. i18n: If you want to propose or develop new modules, we suggest creating your
.. i18n: own branch in the `openobject-addons project <https://launchpad.net/openobject-addons>`_
.. i18n: and develop within your branch. You can fill in a bug to request that
.. i18n: your modules are integrated in one of the two branches:
..

If you want to propose or develop new modules, we suggest creating your
own branch in the `openobject-addons project <https://launchpad.net/openobject-addons>`_
and develop within your branch. You can fill in a bug to request that
your modules are integrated in one of the two branches:

.. i18n:   * `extra-addons branch <https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-extra-addons>`_ : if your module touches a few companies
.. i18n:   * `addons <https://code.launchpad.net/~openerp/openobject-addons/trunk>`_ : if your module will be useful for most of the companies
..

  * `extra-addons branch <https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-extra-addons>`_ : if your module touches a few companies
  * `addons <https://code.launchpad.net/~openerp/openobject-addons/trunk>`_ : if your module will be useful for most of the companies

.. i18n: We invite all our partners and contributors to work in that way so that we can
.. i18n: easily integrate and share the work done between the different projects.
..

We invite all our partners and contributors to work in that way so that we can
easily integrate and share the work done between the different projects.

.. i18n: Use Case Developers
.. i18n: ++++++++++++++++++++
..

Use Case Developers
++++++++++++++++++++

.. i18n: This page presents the approach you should follow on how to contribute in
.. i18n: OpenObject. Suppose you want to develop new features in the addons or simply
.. i18n: correct some bugfixes.
..

This page presents the approach you should follow on how to contribute in
OpenObject. Suppose you want to develop new features in the addons or simply
correct some bugfixes.

.. i18n: If you have the right to modify the branch you plan to change, you can
.. i18n: do it directly. For example, a quality team member doing a bugfix can do it
.. i18n: directly on the main branch. Or committers can work directly on the
.. i18n: extra-addons. If you don't have the right to modify the branch you plan to
.. i18n: change or if you want to branch because you are starting big developments
.. i18n: that may break the code, the first thing to do is to branch the repository
.. i18n: you plan to modify::
.. i18n: 
.. i18n:   bzr branch lp:openobject-addons lp:~openerp-commiter/openobject-addons/trunk-new-reporting
..

If you have the right to modify the branch you plan to change, you can
do it directly. For example, a quality team member doing a bugfix can do it
directly on the main branch. Or committers can work directly on the
extra-addons. If you don't have the right to modify the branch you plan to
change or if you want to branch because you are starting big developments
that may break the code, the first thing to do is to branch the repository
you plan to modify::

  bzr branch lp:openobject-addons lp:~openerp-commiter/openobject-addons/trunk-new-reporting

.. i18n: In that case, the branch created will be for the openerp-commiter team. If you
.. i18n: are not a committer, you can create the branch for the community team
.. i18n: openerp-community or just for yourself, depending if you allow others to
.. i18n: directly commit on your branch or not. For all Tiny employees, we propose to
.. i18n: create all branches for the team openerp-commiter. An OpenERP service company
.. i18n: may create a team for their company and create branches at the name of their
.. i18n: team. This prevents others changing their
.. i18n: customer branch.
..

In that case, the branch created will be for the openerp-commiter team. If you
are not a committer, you can create the branch for the community team
openerp-community or just for yourself, depending if you allow others to
directly commit on your branch or not. For all Tiny employees, we propose to
create all branches for the team openerp-commiter. An OpenERP service company
may create a team for their company and create branches at the name of their
team. This prevents others changing their
customer branch.

.. i18n: Once the branch is created, you must checkout a local copy to work on::
.. i18n: 
.. i18n:   bzr co lp:~openerp-commiter/openobject-addons/trunk-new-reporting
..

Once the branch is created, you must checkout a local copy to work on::

  bzr co lp:~openerp-commiter/openobject-addons/trunk-new-reporting

.. i18n: This will download the branch on your local computer. You can then start
.. i18n: developing on it. From time to time, you should commit the work done::
.. i18n: 
.. i18n:   bzr ci
..

This will download the branch on your local computer. You can then start
developing on it. From time to time, you should commit the work done::

  bzr ci

.. i18n: This will send your modification to the branch:
.. i18n: lp:~openerp-commiter/openobject-addons/trunk-new-reporting. Don't forget to
.. i18n: change the status of the branch to show other contributors the status of your
.. i18n: current work on
.. i18n: https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-new-reporting
..

This will send your modification to the branch:
lp:~openerp-commiter/openobject-addons/trunk-new-reporting. Don't forget to
change the status of the branch to show other contributors the status of your
current work on
https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-new-reporting

.. i18n: For instance, you can switch the status to "In Development" to show you are
.. i18n: working on it and put the status to "Mature" when you'd like to have your code
.. i18n: integrated in the official release.
..

For instance, you can switch the status to "In Development" to show you are
working on it and put the status to "Mature" when you'd like to have your code
integrated in the official release.

.. i18n: During your development, if you want to receive the latest modifications from
.. i18n: the parent branches, you can merge it::
.. i18n: 
.. i18n:   bzr merge
..

During your development, if you want to receive the latest modifications from
the parent branches, you can merge it::

  bzr merge

.. i18n: Once your development on this branch are OK, you can ask a committer to review
.. i18n: and merge it or fill in a bug in the bugtracker. A committer will then review
.. i18n: your work and merge it to the official branch if it's good enough.
..

Once your development on this branch are OK, you can ask a committer to review
and merge it or fill in a bug in the bugtracker. A committer will then review
your work and merge it to the official branch if it's good enough.

.. i18n: Commit Guidelines
.. i18n: +++++++++++++++++
..

Commit Guidelines
+++++++++++++++++

.. i18n: When committing your work to Launchpad, please respect these policies:
..

When committing your work to Launchpad, please respect these policies:

.. i18n: The stable branch is for bugfixes
.. i18n: """""""""""""""""""""""""""""""""
..

The stable branch is for bugfixes
"""""""""""""""""""""""""""""""""

.. i18n: The stable branch must be used for bugfixes. **Only bugfixes**.
..

The stable branch must be used for bugfixes. **Only bugfixes**.

.. i18n: The new features (+the bugfixes on these new functionality) have to be done
.. i18n: in the trunk branch.
..

The new features (+the bugfixes on these new functionality) have to be done
in the trunk branch.

.. i18n: .. note:: We will periodically backport all the fixes from stable to trunk.
..

.. note:: We will periodically backport all the fixes from stable to trunk.

.. i18n: Set the author's name, if it's different from the committer
.. i18n: """""""""""""""""""""""""""""""""""""""""""""""""""""""""""
..

Set the author's name, if it's different from the committer
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. i18n: Always set the author's name, if it's different from the committer. It is not
.. i18n: acceptable at all to commit a contributor's work without at least his/her name in
.. i18n: the commit message. We have to respect them and their work, so
.. i18n: please use ``--author="<author_name>"`` when merging work or patching features
.. i18n: from community.
..

Always set the author's name, if it's different from the committer. It is not
acceptable at all to commit a contributor's work without at least his/her name in
the commit message. We have to respect them and their work, so
please use ``--author="<author_name>"`` when merging work or patching features
from community.

.. i18n: ::
.. i18n: 
.. i18n:   e.g: bzr commit --author="<author_name>"
..

::

  e.g: bzr commit --author="<author_name>"

.. i18n: Write a helpful commit message
.. i18n: """"""""""""""""""""""""""""""
..

Write a helpful commit message
""""""""""""""""""""""""""""""

.. i18n: Use a *commit tag* in **each** message. This tag should be one of:
..

Use a *commit tag* in **each** message. This tag should be one of:

.. i18n: * **[IMP]**
.. i18n: * **[FIX]**
.. i18n: * **[REF]**
.. i18n: * **[ADD]**
.. i18n: * **[REM]**
..

* **[IMP]**
* **[FIX]**
* **[REF]**
* **[ADD]**
* **[REM]**

.. i18n: :[IMP]: For improvements
..

:[IMP]: For improvements

.. i18n: :[FIX]: For bug fixes
..

:[FIX]: For bug fixes

.. i18n: :[REF]: For refactoring (improvements of the source code, without changing the
.. i18n:   functionality or behavior. See http://en.wikipedia.org/wiki/Refactoring for
.. i18n:   further details)
..

:[REF]: For refactoring (improvements of the source code, without changing the
  functionality or behavior. See http://en.wikipedia.org/wiki/Refactoring for
  further details)

.. i18n: :[ADD]: For adding new resources
..

:[ADD]: For adding new resources

.. i18n: :[REM]: For removing of resources
..

:[REM]: For removing of resources

.. i18n: * Always put a meaningful commit message. Commit message should be self
.. i18n:   explanatory including the name of the module that has been changed. No more
.. i18n:   *"bugfix"* or *"improvements"* anymore! (the only single word commit message
.. i18n:   accepted is "merge")
.. i18n: 
.. i18n: * If you are fixing the bugs use ``--fixes=lp:<bug_number>`` instead of putting the
.. i18n:   number of the bug in the commit message.
.. i18n: 
.. i18n: * Use the revision id instead of the revision number when you make reference to
.. i18n:   a revision in your commit message. You can get this revision id, by using the
.. i18n:   command ``bzr version-info``.
..

* Always put a meaningful commit message. Commit message should be self
  explanatory including the name of the module that has been changed. No more
  *"bugfix"* or *"improvements"* anymore! (the only single word commit message
  accepted is "merge")

* If you are fixing the bugs use ``--fixes=lp:<bug_number>`` instead of putting the
  number of the bug in the commit message.

* Use the revision id instead of the revision number when you make reference to
  a revision in your commit message. You can get this revision id, by using the
  command ``bzr version-info``.

.. i18n: ::
.. i18n: 
.. i18n:   e.g:
.. i18n: 
.. i18n:     Not Correct : bzr commit -m “[FIX]: reverted bad revision (cannot install new db) 
.. i18n:       with revision number:525425”
.. i18n: 
.. i18n:     Correct : bzr commit -m “[FIX]: reverted bad revision (cannot install new db) 
.. i18n:     with revision number id: qdp@tinyerp.com-20090602143202-ehmntlift166mrnn”
.. i18n: 
.. i18n:     Not Correct : bzr commit -m "Bug 568889 : typo corrected"
.. i18n: 
.. i18n:     Correct : bzr commit --fixes=lp:568889 -m "[FIX] account module: typo corrected"
..

::

  e.g:

    Not Correct : bzr commit -m “[FIX]: reverted bad revision (cannot install new db) 
      with revision number:525425”

    Correct : bzr commit -m “[FIX]: reverted bad revision (cannot install new db) 
    with revision number id: qdp@tinyerp.com-20090602143202-ehmntlift166mrnn”

    Not Correct : bzr commit -m "Bug 568889 : typo corrected"

    Correct : bzr commit --fixes=lp:568889 -m "[FIX] account module: typo corrected"

.. i18n: .. note:: How to handle translations ?
.. i18n: 
.. i18n:     use **[IMP]** if you translated a message in a po file
.. i18n: 
.. i18n:     use **[ADD]** if you added an new po file
..

.. note:: How to handle translations ?

    use **[IMP]** if you translated a message in a po file

    use **[ADD]** if you added an new po file

.. i18n: Avoid big commits
.. i18n: """""""""""""""""
..

Avoid big commits
"""""""""""""""""

.. i18n: Don't make a commit that will impact lots of modules. Try to split it into
.. i18n: different commits where impacted modules are different (It will be
.. i18n: helpful when we are going to revert that module separately).
..

Don't make a commit that will impact lots of modules. Try to split it into
different commits where impacted modules are different (It will be
helpful when we are going to revert that module separately).
