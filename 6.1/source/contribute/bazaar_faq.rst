
.. i18n: .. _bazaar-faq-link:
.. i18n: 
.. i18n: F.A.Q on Bazaar version control system
.. i18n: --------------------------------------
..

.. _bazaar-faq-link:

F.A.Q on Bazaar version control system
--------------------------------------

.. i18n: .. contents::
..

.. contents::

.. i18n: How to install bazaar ?
.. i18n: +++++++++++++++++++++++
..

How to install bazaar ?
+++++++++++++++++++++++

.. i18n: To install bazaar on any ubuntu distribution, you can use::
.. i18n: 
.. i18n:   apt-get install bzr
..

To install bazaar on any ubuntu distribution, you can use::

  apt-get install bzr

.. i18n: To work correctly, bzr version must be at least 1.3. Check it with the command::
.. i18n: 
.. i18n:   bzr --version
..

To work correctly, bzr version must be at least 1.3. Check it with the command::

  bzr --version

.. i18n: If you have an older version check this url: http://bazaar-vcs.org/Download
..

If you have an older version check this url: http://bazaar-vcs.org/Download

.. i18n: On debian, in any distribution, the 1.5 version is working, you can get it on
.. i18n: this url: http://backports.org/debian/pool/main/b/bzr/bzr_1.5-1~bpo40+1_i386.deb
..

On debian, in any distribution, the 1.5 version is working, you can get it on
this url: http://backports.org/debian/pool/main/b/bzr/bzr_1.5-1~bpo40+1_i386.deb

.. i18n: How to create a login on launchpad ?
.. i18n: ++++++++++++++++++++++++++++++++++++
..

How to create a login on launchpad ?
++++++++++++++++++++++++++++++++++++

.. i18n: Before you can commit on launchpad, you need to create a login.
..

Before you can commit on launchpad, you need to create a login.

.. i18n: Go to: https://launchpad.net --> log in / register on top right.
..

Go to: https://launchpad.net --> log in / register on top right.

.. i18n: Enter your e-mail address and wait for an e-mail which will guide you through the process needed to create your login.
..

Enter your e-mail address and wait for an e-mail which will guide you through the process needed to create your login.

.. i18n: This login is only needed if you intend to commit on bazaar on openerp-commiter or on your own branch.
..

This login is only needed if you intend to commit on bazaar on openerp-commiter or on your own branch.

.. i18n: How to commit ?
.. i18n: +++++++++++++++
..

How to commit ?
+++++++++++++++

.. i18n: Once your login is created, you need to create some ssh keys and insert them on
.. i18n: your login page (see create ssh keys on the left). These ssh keys are needed to
.. i18n: commit.
..

Once your login is created, you need to create some ssh keys and insert them on
your login page (see create ssh keys on the left). These ssh keys are needed to
commit.

.. i18n: I advise you to follow these instructions to complete the creation of your
.. i18n: ssh keys: https://help.launchpad.net/YourAccount/CreatingAnSSHKeyPair
..

I advise you to follow these instructions to complete the creation of your
ssh keys: https://help.launchpad.net/YourAccount/CreatingAnSSHKeyPair

.. i18n: How to use Bazaar ?
.. i18n: +++++++++++++++++++
..

How to use Bazaar ?
+++++++++++++++++++

.. i18n: There are two ways to work on bzr. Either you make a checkout or create a local branch.
..

There are two ways to work on bzr. Either you make a checkout or create a local branch.

.. i18n: Checkout method::
.. i18n: 
.. i18n:   bzr co lp:~openerp/openobject-addons/trunk -- to make a checkout
.. i18n:   bzr up                                     -- to make an update
.. i18n:   bzr ci                                     -- to commit
..

Checkout method::

  bzr co lp:~openerp/openobject-addons/trunk -- to make a checkout
  bzr up                                     -- to make an update
  bzr ci                                     -- to commit

.. i18n: Creating a branch::
.. i18n: 
.. i18n:   bzr branch lp:~<url> <local dir>             -- to create a branch locally
.. i18n:   bzr pull                                     -- to update the branch
.. i18n:   bzr push lp:~<url>                           -- to include your changes in the remote branch
..

Creating a branch::

  bzr branch lp:~<url> <local dir>             -- to create a branch locally
  bzr pull                                     -- to update the branch
  bzr push lp:~<url>                           -- to include your changes in the remote branch

.. i18n: In any case, when you experience some problems, you can do::
.. i18n: 
.. i18n:   bzr help
..

In any case, when you experience some problems, you can do::

  bzr help

.. i18n: or ``bzr help <command>``. e.g.::
.. i18n: 
.. i18n:   bzr help branch
..

or ``bzr help <command>``. e.g.::

  bzr help branch

.. i18n: Some problems
.. i18n: +++++++++++++
..

Some problems
+++++++++++++

.. i18n: Checkout does not work, I have this message error::
.. i18n: 
.. i18n:   bzr lp:~<url> 
.. i18n:   bzr: ERROR: Repository KnitPackRepository is not compatible with repository RemoteRepository
..

Checkout does not work, I have this message error::

  bzr lp:~<url> 
  bzr: ERROR: Repository KnitPackRepository is not compatible with repository RemoteRepository

.. i18n: There are two ways to correct it.
..

There are two ways to correct it.

.. i18n: Instead of using ``bzr co lp:~<url>``, use ``bzr co bzr+ssh://<yourlaunchpad login>@bazaar.launchpad.net/~<url>``
..

Instead of using ``bzr co lp:~<url>``, use ``bzr co bzr+ssh://<yourlaunchpad login>@bazaar.launchpad.net/~<url>``

.. i18n: check this url: https://bugs.launchpad.net/bzr/+bug/205579. Generally, you do::
.. i18n: 
.. i18n:  bzr branch lp:~<url> 
.. i18n:  bzr reconfigure --checkout
..

check this url: https://bugs.launchpad.net/bzr/+bug/205579. Generally, you do::

 bzr branch lp:~<url> 
 bzr reconfigure --checkout
