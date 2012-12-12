OpenERP 中文文档翻译计划
================


简介
-----------
这是一个OpenERP 的官方文档 http://doc.openerp.com 的中文翻译计划，目标是让 OpenERP 官方文档也出现我们的方块字。本翻译计划由OpenERP 开发群的资深同学定期与LP同步，翻译结果也会提交到官方LP中去。

文档预览：http://oedoc601.mrshelly.com/


参与说明
-----------

*  本翻译计划不设门槛，人人都可以参与。
*  翻译者可以直接在 github 上直接编辑，或用git commit ，建议直接在github 上直接编辑。
*  参与翻译需要一个github 帐号，有帐号的同学直接将github 帐号发给 wangbuke，来获取编辑权限。

翻译说明
-----------

*  只有 openerp-doc / 6.1 / i18n / zh_hans / source  目录下的文档是需要翻译的，其他文档请勿修改！
*  模块技术指南部分（openerp-doc / 6.1 / source / technical_guide ） ，社区意见是暂时先不要翻译，理由是：非常技术化，而且过时了
* 下面是个超链格式,下划线后面的空格必须保留 （请到 Code、RAW 方式查看）
  `下载页 <http://www.openerp.com/downloads>`_    ':'. 

不要修改
* 请注意 rst 文件中. 以 ".. i18n " 打头的 严禁修改. 不小心修改的, 请及时改回.
* 编辑表格的时候，特别注意要补足空格，恢复原有样式。否则表格有可能丢失
* '====' 或 '-------' 等章节标记 至少和文字行一样长, 更长也行。这个特别是中文长度大于英文时，要注意。
* 冲突的情况。翻译的时候，难免会遇到大家同时编辑一个页面，提交编辑就会提示冲突。这时请勿惊慌，赶紧复制您翻译的文字，以免丢失，然后重新进入您要编辑的页面，点击编辑，在这里要注意看有么有与您翻译部分不同的地方，如果没有就大胆提交吧。


初次参与翻译请看（高手跳过）
------------------------------

图文教程请看 http://shine-it.net/index.php/topic,4536.msg12575.html

* 需要翻译的文件都是 reStructuredText (rst) 文件，翻译前请花几分钟看看 reStructuredText简明教程 https://github.com/buke/openerp-doc/wiki/reStructuredText%E7%AE%80%E6%98%8E%E6%95%99%E7%A8%8B
* 您可以直接在web 界面编辑翻译，在https://github.com/buke/openerp-doc/tree/master/6.1/i18n/zh_hans/source 上选择要翻译的文件，比如 https://github.com/buke/openerp-doc/blob/master/6.1/i18n/zh_hans/source/faqs.rst 
* 选择好文件之后，正常您会进入到 source view 模式，这时文件内容右上角 有个 Edit/Raw/Blame/History 按钮，点击 "Edit" 即可进入编辑模式。
* 好了，您已经进入 编辑模式，这时候可以就可以对RST 文件进行翻译了。翻译时注意不要删除或修改 rst 的格式代码。
* 仔细检查有没有破坏 rst 格式，检查无误后，点击页面右下方的 “Commit Changes”
* 如果没有出错提示，那么恭喜您轻松搞定！如果有提示冲突，请按照上面的 “翻译说明” 进行操作。
* 如果有任何疑问，可以进入OpenERP-开发群(qq) 69195329 或 212904 咨询 。


翻译进度管理
--------------
https://github.com/buke/openerp-doc/wiki/%E7%BF%BB%E8%AF%91%E8%BF%9B%E5%BA%A6
* 翻译的同学，请在上面的页面自行登记下自己要翻译的章节。
* 准备翻译的同学，翻译前也请看看上面的认领情况，以免冲突。
* 打算翻译几分钟就跑的同学，呃，你自便吧。。。

术语表
--------------
https://github.com/buke/openerp-doc/wiki/%E6%9C%AF%E8%AF%AD%E8%A1%A8
* 翻译中遇到不太明白的术语，可以先到上面链接查查。
* 如果自己觉得对大家有帮助的术语翻译，也劳烦您放到上面的术语表中。


参阅
-----------
1. reStructuredText简明教程 https://github.com/buke/openerp-doc/wiki/reStructuredText%E7%AE%80%E6%98%8E%E6%95%99%E7%A8%8B
2. OpenERP 官方文档 http://doc.openerp.com
3. 维基百科: 科技条目翻译指引 http://zh.wikipedia.org/wiki/Wikipedia:%E7%A7%91%E6%8A%80%E6%9D%A1%E7%9B%AE%E7%BF%BB%E8%AF%91%E6%8C%87%E5%BC%95
4. CNKI 翻译助手 http://dict.cnki.net/