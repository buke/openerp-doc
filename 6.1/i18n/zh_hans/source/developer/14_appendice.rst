.. i18n: =========
.. i18n: Appendice
.. i18n: =========
..

====
附录
====

.. i18n: Conventions
.. i18n: ===========
..

约定事项
========

.. i18n: Guidelines
.. i18n: ----------
.. i18n: For guidelines and general recommendations with regard to the development of OpenERP modules,
.. i18n: please refer to the :ref:`Guidelines <contribution_guidelines-link>` of the
.. i18n: :doc:`Contribution section </contribute/index>`.
..

指南
----
关于 OpenERP 模块的开发指南和一般建议，
请参阅 :doc:`贡献 </contribute/index>` 文件里的
:ref:`指南 <contribution_guidelines-link>` 

.. i18n: Module structure and file names
.. i18n: -------------------------------
..

模块结构和文件名称
------------------

.. i18n: The structure of a module should be::
.. i18n: 
.. i18n:     /module/
.. i18n: 
.. i18n:         /__init__.py
.. i18n:         /__openerp__.py
.. i18n:         /module.py
.. i18n:         /module_other.py
.. i18n:         /module_view.xml
.. i18n:         /module_data.xml
.. i18n:         /module_demo.xml
.. i18n: 
.. i18n:         /wizard/
.. i18n:         /wizard/__init__.py
.. i18n:         /wizard/wizard_name.py
.. i18n: 
.. i18n:         /report/
.. i18n:         /report/
.. i18n:         /report/__init__.py
.. i18n:         /report/report_name.sxw
.. i18n:         /report/report_name.rml
.. i18n:         /report/report_name.py
..

模块的结构应该如下::

    /module/

        /__init__.py
        /__openerp__.py
        /module.py
        /module_other.py
        /module_view.xml
        /module_data.xml
        /module_demo.xml

        /wizard/
        /wizard/__init__.py
        /wizard/wizard_name.py

        /report/
        /report/
        /report/__init__.py
        /report/report_name.sxw
        /report/report_name.rml
        /report/report_name.py

.. i18n: Naming conventions
.. i18n: ------------------
..

命名方式约定
------------

.. i18n:     * modules: modules must be written in lower case, with underscores. The name of the module is the name of the directory in the addons path of the server. If the module depends on other modules, you can write several module names separated by underscores, starting by the most important name. Example:
.. i18n:           + sale
.. i18n:           + sale_commission 
.. i18n: 
.. i18n:     * objects: the name of an object must be of the form name_of_module.name1.name2.name3.... The namei part of the object must go from the most important name to the least important one, from left to right, in lower case. Try not to use plurals in object names and to avoid shortcuts in the names. Example:
.. i18n:           + sale.order
.. i18n:           + sale.order.line
.. i18n:           + sale.shop
.. i18n:           + sale_commission.commission.rate 
.. i18n: 
.. i18n:     * fields: field must be in lowercase, separated by underscores. Try to use commonly used names for fields: name, state, active, partner_id, eso. Conventions for the field name depends on the field type:
.. i18n:           + many2one: must end by '_id' (eg: partner_id, order_line_id)
.. i18n:           + many2many: must end by '_ids' (eg: category_ids)
.. i18n:           + one2many: must end by '_ids' (eg: line_ids
..

    * 模块: 模块名称应该使用下划线(_)，加上小写字母。模块的名称就是服务器上插件所在的路径名称。如果某个模块依赖其他的模块，你可以用最重要的模块作为名称的开始，把其他几个模块的名称用下划线分别串起来。例如:
          + sale
          + sale_commission 

    * 物件: 物件的名称必须依照以下的形式 模块名称.物件名称1.物件名称2.物件名称3.... 物件名称i 的排列顺序必须是由最重要的到最不重要的，由左到右，而且要是小写字母。尽量不要在物件名称里使用复数形式，同时要避免在名称里使用捷径。例如:
          + sale.order
          + sale.order.line
          + sale.shop
          + sale_commission.commission.rate 

    * 字段: 字段必须是小写，加上分隔的下划线。尽量使用一般常用的字段名称，例如：name, state, active, partner_id, 等等。字段名称是依据字段的属性来约定的:
          + 多对一: 必须在结尾加上 '_id' (例如: partner_id, order_line_id)
          + 多对多: 必须在结尾加上'_ids' (例如: category_ids)
          + 一对多: 必须在结尾加上'_ids' (例如: line_ids)

.. i18n: Translations
.. i18n: ============
..

翻译
====

.. i18n: OpenERP is multilingual. You can add as many languages as you wish. Each user may work with the interface in his own language. Moreover, some resources (the text of reports, product names, etc.) may also be translated.
..

OpenERP 是多语言的。你想要加进多少种语言都没问题。每个用户都可以用他自己的语言作为工作界面，而且某些资源 (报表的内容，产品名称等等) 也可以翻译成想要的语言。

.. i18n: This section explains how to change the language of the program shown to individual users, and how to add new languages to OpenERP.
..

这一段说明了如何改变每个用户看到的语言，以及如何在 OpenERP 里新增语言。

.. i18n: Nearly all the labels used in the interface are stored on the server. In the same way, the translations are also stored on the server. By default the English dictionary is stored on the server, so if the users want to try OpenERP in a language other than English you must store these languages definitions on the server.
..

几乎所有在使用界面里用到的标签都有储存在服务器上，同样的，标签的翻译也都有储存在服务器上。服务器的预设值是把英文的字典储存在服务器上，所以如果用户想要尝试除了英文以外的语言，这些语言的定义(字典)必须要储存在服务器上。

.. i18n: However, it is not possible to store "everything" on the server. Indeed, the user gets some menus, buttons, etc... that must contain some text *even before* being connected to the server. These few words and sentences are translated using GETTEXT. The chosen language by default for these is the language of the computer from which the user connects.
..

然而，要把 "所有的东西" 存在服务器上是不可能的。实际上，在连上服务器 *之前* ，一定会有一些文字显示在某些菜单，按键等等使用者界面上，这些为数不多的文字和句子是使用 GETTEXT 来翻译的；系统预设会依照用户(连上服务器的)电脑的语言来翻译以上的文字和句子。

.. i18n: The translation system of OpenERP is not limited to interface texts; it also works with reports and the "content" of some database fields. Obviously, not all the database fields need to be translated. The fields where the content is multilingual are marked thus by a flag icon.
..

OpenERP 的翻译系统不限于使用界面的文字；它对报表及某些数据库里的字段 "内容" 同样有效。显然并非所有的数据库字段都需要翻译，所以如果字段内容需要是多语言的，这个字段会有一个旗标图标作为标示。

.. i18n: .. TODO: add image
.. i18n: .. .. figure:: images/field_flag.png
.. i18n: ..    :scale: 120
.. i18n: ..    :align: left
.. i18n: 
.. i18n: 	
.. i18n: How to change the language of the user interface ?
.. i18n: --------------------------------------------------
..

.. TODO: add image
.. .. figure:: images/field_flag.png
..    :scale: 120
..    :align: left

	
如何变更用户使用界面的语言？
----------------------------

.. i18n: The language is a user preference. To change the language of the current user, click on the menu: User > Preferences.
..

用户可以设定偏好的语言。当前用户要改变语言设定，在菜单上按：用户 > 偏好选项。

.. i18n: .. TODO: add image
.. i18n: .. .. figure:: images/trans_user_pref.png
.. i18n: ..    :scale: 120
.. i18n: ..    :align: left
..

.. TODO: add image
.. .. figure:: images/trans_user_pref.png
..    :scale: 120
..    :align: left

.. i18n: An administrator may also modify the preferences of a user (including the language of the interface) in the menu: Administration > Users > Users. He merely has to choose a user and toggle on "preferences".
..

系统管理员也可以在菜单里修改用户的偏好语言(包含用户的使用界面语言)：系统管理 > 用户群 > 用户群。系统管理员只需要选择一个用户，然后切换 "偏好选项" ，就可以完成偏好语言的修改。

.. i18n: .. TODO: add image
.. i18n: .. .. figure:: images/menu_bar_pref.png
.. i18n: ..    :scale: 120
.. i18n: ..    :align: left
..

.. TODO: add image
.. .. figure:: images/menu_bar_pref.png
..    :scale: 120
..    :align: left

.. i18n: Store a translation file on the server
.. i18n: --------------------------------------
..

在服务器上储存翻译文件
----------------------

.. i18n: To import a file having translations, use this command:
..

用以下的指令上传包含翻译内容的文件 :

.. i18n:     ./openerp_server.py --i18n-import=file.csv -l **LANG** 
..

    ./openerp_server.py --i18n-import=file.csv -l **LANG** 

.. i18n: where **LANG** is the language of the translation data in the CSV file.
..

这里的 **LANG** 是以 CVS 格式保存的文件，存有这个语言的翻译资料。

.. i18n: Note that the translation file must be encoded in **UTF8!**
..

注意，翻译的文件内容必须使用 **UTF8** 编码!

.. i18n: Translate to a new language
.. i18n: ---------------------------
..

翻译成新的语言
--------------

.. i18n: **Please keep in mind to use the same translation string for identical sources**	. Launchpad Online Translation may give helpful hints.
..

**请时刻记得，对于相同的资源要使用相同的翻译词句**	。在 Launchpad 线上翻译里，可以找到一些有用的提示。

.. i18n: More information on accelerators on this website: http://translate.sourceforge.net/wiki/guide/translation/accelerators
..

在以下这个网站上可以找到更多关于翻译加速器的资讯:
http://translate.sourceforge.net/wiki/guide/translation/accelerators

.. i18n: To translate or modify the translation of a language already translated, you have to:
..

想要翻译成某种语言，或是想要修改某个语言的翻译内容，必须依照以下步奏:

.. i18n: 1. Export all the sentences to translate in a CSV file
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++++++++++
..

1. 把要翻译的所有词句输出到 CSV 文件
++++++++++++++++++++++++++++++++++++

.. i18n: To export this file, use this command:
..

使用以下指令输出这个文件:

.. i18n:         ./openerp_server.py --i18n-export=file.csv -l**LANG** 
..

        ./openerp_server.py --i18n-export=file.csv -l**LANG** 

.. i18n: where **LANG** is the language to which you want to translate the program.
..

这里的 **LANG** 是你想翻译的标的语言。

.. i18n: 2. Translate the last column of the file
.. i18n: ++++++++++++++++++++++++++++++++++++++++
..

2. 翻译文件的最后一列
+++++++++++++++++++++

.. i18n: You can make a translation for a language, which has already been translated or for a new one. If you ask for a language already translated, the sentences already translated will be written in the last column.
..

你可以制作某个语言的翻译文件，不论这个语言是已经被翻译过的还是一个新的语言。如果你处理的是一个已经翻译过的语言，以前翻译好的词句应该要写在最后一列。

.. i18n: For example, here are the first lines of a translation file (Dutch):
.. i18n:  
.. i18n: +--------+------------------------+---------+----------------+--------------------+
.. i18n: | type   | name                   | res_id  |      src       |   value            |
.. i18n: +--------+------------------------+---------+----------------+--------------------+
.. i18n: | field  | "account.account,code" |  0      |    Code        |    Code            |
.. i18n: +--------+------------------------+---------+----------------+--------------------+
.. i18n: |  field | "account.account,name" |  0      |    Name        |   Name             |
.. i18n: +--------+------------------------+---------+----------------+--------------------+
.. i18n: |  model | "account.account,name" |  2      |    Assets      |   Aktiva           |
.. i18n: +--------+------------------------+---------+----------------+--------------------+
.. i18n: |  model | "account.account,name" |  25     |    Results     |   Salden           |
.. i18n: +--------+------------------------+---------+----------------+--------------------+
.. i18n: |  model | "account.account,name" |   61    |    Liabilities |  Verbindlichkeiten |
.. i18n: +--------+------------------------+---------+----------------+--------------------+
..

例如，以下是某个翻译文件(荷兰语)的前几行:
 
+--------+------------------------+---------+----------------+--------------------+
| type   | name                   | res_id  |      src       |   value            |
+--------+------------------------+---------+----------------+--------------------+
| field  | "account.account,code" |  0      |    Code        |    Code            |
+--------+------------------------+---------+----------------+--------------------+
|  field | "account.account,name" |  0      |    Name        |   Name             |
+--------+------------------------+---------+----------------+--------------------+
|  model | "account.account,name" |  2      |    Assets      |   Aktiva           |
+--------+------------------------+---------+----------------+--------------------+
|  model | "account.account,name" |  25     |    Results     |   Salden           |
+--------+------------------------+---------+----------------+--------------------+
|  model | "account.account,name" |   61    |    Liabilities |  Verbindlichkeiten |
+--------+------------------------+---------+----------------+--------------------+

.. i18n: 3. Import this file into OpenERP (as explained in the preceding section)
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
..

3. 把这个文件导入 OpenERP (如同前一节所说明的)
++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: **Notes**
..

**注释**

.. i18n:     * You should perform all these tasks on an empty database, so as to avoid over-writing data. 
..

    * 你应该要在一个空的数据库里进行这些工作，以免覆盖到其他资料。 

.. i18n: To create a new database (named 'terp_test'), use these commands:
..

用以下的指令创建一个新的数据库 (名为 'terp_test'):

.. i18n:     createdb terp_test --encoding=unicode 
.. i18n:     terp_server.py --database=terp_test --init=all 
..

    createdb terp_test --encoding=unicode 
    terp_server.py --database=terp_test --init=all 

.. i18n: Alternatively, you could also delete your current database with these:
..

或者，你也可以用以下的指令删除你当前的数据库 :

.. i18n:     dropdb terp 
.. i18n:     createdb terp --encoding=unicode 
.. i18n:     terp_server.py --init=all 
..

    dropdb terp 
    createdb terp --encoding=unicode 
    terp_server.py --init=all 

.. i18n: 4. Using Launchpad / Rosetta to translate modules and applications
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
..

4. 采用 Launchpad / Rosetta 来翻译模块和应用程序
++++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: A good starting point is here https://launchpad.net/openobject
..

以下的链接是一个很好的开始 https://launchpad.net/openobject

.. i18n: **Online**
..

**线上翻译**

.. i18n: Select the module translation section and enter your translation.
..

选择模块翻译的段落，输入你的翻译。

.. i18n: **Offline**
..

**离线翻译**

.. i18n: Use this, if you want to translate some 100 terms.
..

如果你想一次性翻译100个名词，就采用离线翻译的方式。

.. i18n: It seems mandatory to follow theses steps to successfully complete a translation cycle. (tested on Linux)
..

要成功的完成翻译的一个周期，必须严格遵守以下的步奏。 (在 Linux 上测试的结果)

.. i18n:    1. Download the <po file> from Launchpad
.. i18n:    2. Get the message template file <pot file> from bzr branches
.. i18n:          1. keep in mind that the <pot file> might not always contain all strings, the <pot files> are updated irregularly.
.. i18n:          2. msgmerge <pot file> <po file> -o <new po file> 
.. i18n:    3. translate <new po file> using poedit, kbabel (KDE)
.. i18n:          1. some programs (like kbabel) allow using dictionaries to create rough translations.
.. i18n:          2. It is especially useful to create a complete dictionary from existing translations to reuse existing terms related to the application.
.. i18n:                1. In OpenERP load most/all of the modules
.. i18n:                2. Load your language
.. i18n:                3. export all modules of your language as po file and use this one as dictionary. Depending on context of the module this creates 30-80% exact translations. 
.. i18n:    4. the <new po file> must not contain <fuzzy> comments inserted by kbabel for rough translation
.. i18n:          1. grep -v fuzzy <new po file> > <po file> 
.. i18n:    5. check for correct spelling
.. i18n:          1. msgfmt <po file> -o <mo file> 
.. i18n:    6. check your translation for correct context
.. i18n:          1. import the <po file> (for modules)
.. i18n:          2. install the <mo file> and restart the application (for applications) 
.. i18n:    7. adjust the translation Online in OpenERP
.. i18n:          1. check context
.. i18n:          2. check length of strings
.. i18n:          3. export <po file> 
.. i18n:    8. upload <po file> to Launchpad
.. i18n:          1. keep in mind that Launchpad / Rosetta uses some tags (not sure which) in the header section of the exported <po file> to recognize the imported <po file> as valid.
.. i18n:          2. after some time (hours) you will receive a confirmation E-Mail (success / error) 
..

   1. 从 Launchpad 下载 <po 文件> 。 
   2. 从 bzr 分支找到模板文件 <pot 文件> 
         1. 记得 <pot 文件> 不一定会包含所有字串，因为 <pot 文件> 是不定期更新的。
         2. msgmerge <pot 文件> <po 文件> -o <新 po 文件> 
   3. 采用 poedit, kbabel (KDE) 翻译 <新 po 文件> 
         1. 有些程序 (例如 kbabel) 可以用字典进行大略的翻译。
         2. 有一个特别有用的做法，就是从现有的翻译中创建一个完整的字典，以便能重复使用与应用程序相关的现有词汇。
               1. 在 OpenERP 里载入全部或是大部分的模块
               2. 载入你的语言
               3. 将你的语言的全部模块输出成 po 文件，然后把这个文件当成是字典。依据模块内容的不同，这个做法可以产生准确度 30-80% 的翻译。 
   4.  <新 po 文件> 一定不可以有 kbabel 大略翻译产生的 <模糊> 叙述
         1. grep -v fuzzy <新 po 文件> > <po 文件> 
   5. 检查拼字是否正确
         1. msgfmt <po 文件> -o <mo 文件> 
   6. 检查翻译的连贯性
         1. 导入 (模块的) <po 文件> 
         2. 安装 <mo 文件> ，然后重启应用程序 
   7. 调整 OpenERP 里的线上翻译
         1. 检查连贯性
         2. 检查字串的长度
         3. 输出 <po 文件> 
   8. 把 <po 文件> 上传到 Launchpad
         1. 记住 Launchpad / Rosetta 会抓取某些 (不确定是哪些) 藏在输出文件 <po 文件> 标头段落的标签，来判别导入的 <po 文件> 是否有效。
         2. 一段时间 (几小时) 后， 你会收到一封 E-Mail ， 确认结果是成功还是有错误。 

.. i18n: Using context Dictionary for Translations
.. i18n: -----------------------------------------
..

采用上下文词典进行翻译
----------------------

.. i18n: The context dictionary is explained in details in section "The Objects - Methods - The context Dictionary". If an additional language is installed using the Administration menu, the context dictionary will contain an additional key : lang. For example, if you install the French language then select it for the current user, his or her context dictionary will contain the key lang to which will be associated the value *fr_FR*. 
..

上下文词典在以下段落有详细说明 "物件 - 方法 - 上下文词典". 如果使用管理菜单安装新增加语言，上下文词典里会新增加一个主要 : 语言 。例如，如果安装了法语，而且设置为当前使用者的语言，使用者的上下文词典里会新增加一个主要语言，而且这个主要语言会被连结到 *fr_FR* 这个值上。

.. i18n: .. _tech_memento_link:
.. i18n: 
.. i18n: .. index::
.. i18n:     pair: cheat; sheet
.. i18n:     single: cheatsheet
.. i18n:     single: memento
.. i18n:     single: reference
..

.. _tech_memento_link:

.. index::
    pair: cheat; sheet
    single: cheatsheet
    single: memento
    single: reference

.. i18n: Technical Memento
.. i18n: =================
..

技术备忘录
==========

.. i18n: A technical reference memento is available, to be used as a quick reference guide for
.. i18n: OpenERP developers, often nicknamed a "cheat sheet".
..

技术备忘录，通常被昵称为 "欺骗表(cheat sheet)"，是 OpenERP 开发人员的快速参考指南。

.. i18n: .. |t| image:: ../images/pdf.png
.. i18n:     :target: http://doc.openerp.com/memento
.. i18n:     :align: bottom
..

.. |t| image:: ../images/pdf.png
    :target: http://doc.openerp.com/memento
    :align: bottom

.. i18n: * |t| `Technical Memento <http://doc.openerp.com/memento>`_ 
..

* |t| `技术备忘录 <http://doc.openerp.com/memento>`_ 

.. i18n: The memento is usually updated for each `major version <release_cycle>`_ of OpenERP,
.. i18n: and contains a global overview of OpenERP's Application Programming Interface,
.. i18n: including the declaration of modules, the ORM, the XML syntax, Dynamic views and Workflows.
.. i18n: The memento is not an extensive reference, but a way to quickly find out how
.. i18n: a certain OpenERP feature is accessed or used. Therefore each topic is only described
.. i18n: in a few words, usually with a small example.
..

技术备忘录一般是每个 OpenERP 的 `主要版次 <发行周期>`_ 更新，而且包含了 OpenERP 的程序编程界面(API)的全体概览；
其中有模块的宣告， ORM，XML 语法，动态视窗和工作流程。备忘录并不是一个广泛的参考，而是一个快速找到存取或使用某些 OpenERP 功能的指南。
所以每个主题都只有一小段叙述，通常还附带一个小范例。

.. i18n: The examples in the technical memento all come from the example module ``idea``, which
.. i18n: allows an organisation to manage the generic *ideas* submitted by its members.
..

在技术备忘录里的范例全部是来自范例模块 ``idea`` ；这个模块可以让一个组织管理成员提交的一般 *ideas(想法)* 。

.. i18n: There are 2 versions of the memento. One is suited for printing in A4 landscape mode,
.. i18n: with 3 columns of text per page, so that the whole memento is contained in less than 20
.. i18n: mini-pages (columns). The idea is to print and bind these pages as a reference booklet.
.. i18n: The second version contains some more details and is formatted in A4 portrait
.. i18n: mode, making it easier to read, but larger.
..

备忘录有2种版本，第一种是适合A4横向打印，每一页有3个栏位的文字，整个备忘录只有不到 20 迷你页 (栏位)。
这种设计是为了把这些页打印出来装订在一起，变成参考手册。
第二种版本包含了许多细节资讯，依照A4纵向排版，这样比较容易阅读内容，但是尺寸大些。

.. i18n: All versions of the technical memento (including previous ones) can be found at this
.. i18n: location: |t| `Technical Memento <http://doc.openerp.com/memento>`_
..

所有版次的技术备忘录 (包含以前的版次) ，都可以在这里找到 : |t| `技术备忘录 <http://doc.openerp.com/memento>`_

.. i18n: Information Repository
.. i18n: ======================
..

信息库
=====

.. i18n: The information repository is a semantics tree in which the data that are not the resources are stored. We find in this structure:
..

信息库是一种树状结构的语义描述方式，用于描述所储存的资料，而不是资源。 信息库的结构如下:

.. i18n:    1. the values by default
.. i18n:    2. the conditional values;
.. i18n:           * the state depends on the zip code,
.. i18n:           * the payment method depends of the partner, ...
.. i18n:    3. the reactions to the events client;
.. i18n:           * click on the invoice menu,
.. i18n:           * print an invoice,
.. i18n:           * action on a partner, ...
..

   1. 预设的值
   2. 有条件的值；
          * 州（省）取决于邮编，
          * 付款方法取决于伙伴，
   3. 事件客户端的反应动作；
          * 滑鼠在请款单菜单上单击，
          * 打印一份请款单，
          * 对一个伙伴的动作， ...

.. i18n: The IR has 3 methods;
..

信息库(IR)有 3 个物件方法；

.. i18n:     * add a value in the tree
.. i18n:     * delete a value in the tree
.. i18n:     * obtain all the values of a selected sheet
..

    * 在语义树里增加值
    * 在语义树里删除值
    * 在一个选定表单里取得所有值

.. i18n: Setting Value
.. i18n: -------------
..

设定数值
-------

.. i18n: The ir_set tag allows you to insert new values in the  "Information
.. i18n: Repository". This tag must contain several *field* tags with *name* and *eval*
.. i18n: attributes.
..

ir_set（信息库_设置） 标签让你能在 "信息库" 里新增数值。 这个标签必须包含数个 *字段（field）* 标签，这些字段标签要具备 *name* 及 *eval*
属性。

.. i18n: The attributes are those defined by the access methods to the information
.. i18n: repository. We must provide it with several attributes: *keys*, *args*, *name*,
.. i18n: *value*, *isobject*, *replace*, *meta* and some optional fields.
..

这些属性是依据存取信息库的方法定义的；我们必须在提供标签时设置以下属性：*keys*, *args*, *name*, *value*, *isobject*, *replace*, *meta*, 和其他一些可选的属性。

.. i18n: Example:
..

范例:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <ir_set>
.. i18n:         <field name="keys" eval="[('action','client_print_multi'),('res_model','account.invoice')]"/>
.. i18n:         <field name="args" eval="[]"/>
.. i18n:         <field name="name">Print Invoices</field>
.. i18n:         <field name="value" eval="'ir.actions.report.xml,'+str(l0)"/>
.. i18n:         <field name="isobject" eval="True"/>
.. i18n:         <field name="replace" eval="False"/>
.. i18n:     </ir_set>
..

.. code-block:: xml

    <ir_set>
        <field name="keys" eval="[('action','client_print_multi'),('res_model','account.invoice')]"/>
        <field name="args" eval="[]"/>
        <field name="name">Print Invoices</field>
        <field name="value" eval="'ir.actions.report.xml,'+str(l0)"/>
        <field name="isobject" eval="True"/>
        <field name="replace" eval="False"/>
    </ir_set>

.. i18n: IR Methods
.. i18n: -----------
..

信息库物件方法
------------

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     def ir_set(cr, uid, key, key2, name, models, value, replace=True, isobject=False, meta=None)
..

.. code-block:: python

    def ir_set(cr, uid, key, key2, name, models, value, replace=True, isobject=False, meta=None)

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     def ir_get(cr, uid, key, key2, models, meta=False, context={}, res_id_req=False)
..

.. code-block:: python

    def ir_get(cr, uid, key, key2, models, meta=False, context={}, res_id_req=False)

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     def ir_del(cr, uid, id):
..

.. code-block:: python

    def ir_del(cr, uid, id):

.. i18n: :Description of the fields:
..

:字段描述:

.. i18n:    1. key:
.. i18n:    2. key2:
.. i18n:    3. name:
.. i18n:    4. models:
.. i18n:    5. value:
.. i18n:    6. isobject:
.. i18n:    7. replace: whether or not the action described should override an existing action or be appended to the list of actions.
.. i18n:    8. meta:
..

   1. key:
   2. key2:
   3. name:
   4. models):
   5. value:
   6. isobject:
   7. replace: 所描述的动作是否应该覆盖现有的动作， 或是应该被加到现在的动作清单里。
   8. meta:

.. i18n: :Using ir_set and ir_get:
..

:使用 ir_set 和 ir_get:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     ...
.. i18n: 
.. i18n:         res = ir.ir_set(cr, uid, key, key2, name, models, value, replace, isobject, meta)
.. i18n: 
.. i18n:     ...
.. i18n: 
.. i18n:     ...
.. i18n: 
.. i18n:         if not report.menu_id:
.. i18n: 
.. i18n:             ir.ir_set(cr, uid, 'action', 'client_print_multi', name, [(model, False)], action, False, True)
.. i18n: 
.. i18n:         else:
.. i18n: 
.. i18n:             ir.ir_set(cr, uid, 'action', 'tree_but_open', 'Menuitem', [('ir.ui.menu', int(m_id))], action, False, True)
.. i18n: 
.. i18n:     ...
.. i18n: 
.. i18n:     ...
.. i18n: 
.. i18n:         res = ir.ir_get(cr, uid, [('default', self._name), ('field', False)], [('user_id',str(uid))])
.. i18n: 
.. i18n:     ...
.. i18n: 
.. i18n:         account_payable = ir.ir_get(cr, uid, [('meta','res.partner'), ('name','account.payable')], opt)[0][2]
.. i18n: 
.. i18n:     ...
..

.. code-block:: python

    ...

        res = ir.ir_set(cr, uid, key, key2, name, models, value, replace, isobject, meta)

    ...

    ...

        if not report.menu_id:

            ir.ir_set(cr, uid, 'action', 'client_print_multi', name, [(model, False)], action, False, True)

        else:

            ir.ir_set(cr, uid, 'action', 'tree_but_open', 'Menuitem', [('ir.ui.menu', int(m_id))], action, False, True)

    ...

    ...

        res = ir.ir_get(cr, uid, [('default', self._name), ('field', False)], [('user_id',str(uid))])

    ...

        account_payable = ir.ir_get(cr, uid, [('meta','res.partner'), ('name','account.payable')], opt)[0][2]

    ...
