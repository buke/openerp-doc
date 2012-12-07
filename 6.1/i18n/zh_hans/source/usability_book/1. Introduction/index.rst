.. i18n: ==============
.. i18n: Introduction
.. i18n: ==============
..

==============
介绍
==============

.. i18n: .. toctree::
.. i18n:     :maxdepth: 2
..

.. toctree::
    :maxdepth: 2

.. i18n: Usability book goals
.. i18n: --------------------
..

本章目标
--------------------

.. i18n: OpenERP is a full-featured business application suite, with more than 700 modules. Despite the complexity of technical work and the importance of the community members in the development of such a huge project, our goal is to make software that is easy to use, user friendly, and consistent while remaining fully open.
..

OpenERP 是一个全功能全业务软件套装，超过700模块。无论技术有多复杂、还有众多的社区成员仍在不断开发如此巨大的项目，我们的目标是让软件容易使用、用户友好和保持完全开源。

.. i18n: That's one of our main challenges: provide tons of features while remaining easy to use.
..

我们最大的挑战是：在提供大量的功能同时又要保证易于使用。

.. i18n: OpenERP SA has setup a usability team whose role is to continuously simplify the software, its installation and its configuration. This team is responsible for maintaining this document that covers all usability guidelines for OpenERP developers.
..

OpenERP SA 为此专门成立了一个界面交互团队，持续改进易用性，让安装和配置变的更简单。同时该团队也为开发者维护界面开发指南文档。

.. i18n: The guide is in two parts: one description of every concept of OpenERP and their impacts on usability and a set of guidelines at the end of the book.
..

本指南主要有2部分：一部分是阐述 OpenERP 的界面设计，另外一部分是本章最后部分的各种指南。

.. i18n: A goal for this manual is to include the opinions, advice and help of the community. Indeed, everyone can contribute to the writing of the usability manual thanks to the tools used to write it. The notes of the Usability team will be inserted on the web site and in the manual. The community can also add notes or send its ideas.
..


本指南的另外一个目标是，汇集社区成员的各种观点、意见和建议。实际上，每个人都可以自由贡献、编写本指南。 界面交互团队的备注可以在 web 上插入，或是添加到手册中。社区成员同样也可以提出意见或建议。


.. i18n: Continuous improvement process
.. i18n: ------------------------------
..

持续改进流程
------------------------------

.. i18n: With about 200 full time developers, OpenERP is evolving every day. The usability team continuously looks for ideas to simplify OpenERP for new users.
..

在大约200个全职开发人员的努力下，OpenERP 每天都在改进。界面交互团队也在不断寻找让OpenERP的新用户更容易使用的方法。

.. i18n: These ideas are discussed between OpenERP SA, the official partners and members of the community. In order to discuss about ideas, we have setup an open `usability team on Launchpad`_ to discuss every proposition.
..

OpenERP SA 、官方合作伙伴、社区成员一直在讨论这些方法，为此，我们还在 Launchpad 建立了 `usability team on Launchpad`_ .  来专门讨论。

.. i18n: You can also subscribe to the `usability mailing list`_ to be part of the main discussions about how to improve OpenERP's usability.
..

您可以通过订阅邮件列表 `usability mailing list`_ 来参与讨论如何提高 OpenERP 的界面友好度。

.. i18n: Once an improvement is approved by the usability managers, the community of OpenERP SA develops the software according to the proposed improvements. You can check the `developer guide`_ and `documentation process`_ for more information on how to contribute to OpenERP. 
..

一旦某项改善建议被界面交互团队经理确认，OpenERP SA 社区开发人员，会根据改善建议开始开发。您可以查阅 `developer guide`_ 与 `documentation process`_  开发指南和相关文档来获知如何为OpenERP 贡献。

.. i18n: Main usability improvements are reported in this book as a set of guidelines. The usability team is responsible for synchronizing the book content with the best practices on OpenERP. If you want to contribute to this book, you can work on the `Launchpad documentation branch`_.
..

主要的界面交互方面的改进将会在本书形成一系列的指南。界面交互团队将会把 OpenERP 的最佳实践与本书同步。如果您想在此方面为 OpenERP 做出贡献，您可以在这里 `Launchpad documentation branch`_ 和我们一起工作。

.. i18n: All changes done, regarding important improvements, will be posted on the `OpenERP blog`_ where you can also leave your comments, advice or ideas.
..

所要更改和重大改进，都会发布在博客 `OpenERP blog`_ ，您可以在上面留下您的意见、建议和想法。

.. i18n: In order to benefit from the feedback from any visitor on this web site, everyone can leave a comment on any page of this book. The usability team will review all comments every month and update the book accordingly if required.
..

每个人都可以在这本书的任何页面上发表评论。每个月界面交互团队将查看所有评论，如果有需要还会更新本书。

.. i18n: The book is written only in English, then `translated by community members`_ into several languages.
..

本书用英文写作，然后由 `translated by community members`_  翻译成几种语言。

.. i18n: In order to check that all OpenERP modules respect the usability guidelines, the check of these guidelines is part of the quality certification process of new modules by OpenERP SA. So, we check that all official modules respect the above guidelines in order to make them become official.
..

为了检查模块是否符合界面交互指南，我们把这些检查作为 OpenERP SA 新模块质量检查的一部分。因此，我们会检查所有官方模块是否符合上述方针。

.. i18n: The usability team is also in charge of educating the developer teams. So, when the usability team detects developments which do not conform to these guidelines, they must contact the authors and ask the author of the module to improve his code according to specific guidelines. In this feedback email, the usability team links to each guideline that was infringed.
..

界面交互团队同时对开发人员进行培训。所以，当界面交互团队检查到不符合要求时，他们将会联系作者，并要求作者改善。在这个反馈过程中，界面交互团队将会具体指出违背了那些原则。

.. i18n: Having set this process, a full-time team of several developers and functional experts, we expect OpenERP's usability to improve very quickly over time. If you want to propose a new improvement, the easiest way is to `write to the usability mailing list`_ with your suggestion.
..

Having set this process, a full-time team of several developers and functional experts, we expect OpenERP's usability to improve very quickly over time. If you want to propose a new improvement, the easiest way is to `write to the usability mailing list`_ with your suggestion.

.. i18n: If your improvement is validated by the usability team, we will assign a developer and a member of the usability team will improve the guidelines.
..

If your improvement is validated by the usability team, we will assign a developer and a member of the usability team will improve the guidelines.

.. i18n: .. _usability mailing list:
.. i18n: .. _usability team on Launchpad: https://launchpad.net/~openerp-expert-ergonomy
.. i18n: .. _developer guide: ../../developer/index.html
.. i18n: .. _documentation process: 
.. i18n:     ../../contribute/08_documentation_process.html
.. i18n: .. _Launchpad documentation branch: 
.. i18n:     https://code.launchpad.net/~openerp-community/openobject-doc/trunk
.. i18n: .. _OpenERP blog: http://usability-openerp.blogspot.com/
.. i18n: .. _translated by community members: 
.. i18n:     ../../contribute/09_documentation_translation.html
.. i18n: .. _write to the usability mailing list: 
.. i18n:     mailto:openerp-expert-ergonomy@lists.launchpad.net
..

.. _usability mailing list:
.. _usability team on Launchpad: https://launchpad.net/~openerp-expert-ergonomy
.. _developer guide: ../../developer/index.html
.. _documentation process: 
    ../../contribute/08_documentation_process.html
.. _Launchpad documentation branch: 
    https://code.launchpad.net/~openerp-community/openobject-doc/trunk
.. _OpenERP blog: http://usability-openerp.blogspot.com/
.. _translated by community members: 
    ../../contribute/09_documentation_translation.html
.. _write to the usability mailing list: 
    mailto:openerp-expert-ergonomy@lists.launchpad.net
