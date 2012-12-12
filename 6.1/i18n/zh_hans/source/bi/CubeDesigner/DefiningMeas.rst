.. i18n: Defining Measure
.. i18n: ================
..

定义衡量
================

.. i18n: :ref:`Measure <measure-link>` are the fact or quantitative values. It comes from the fact table configured in the cube.
..

:ref:`Measure <measure-link>` are the fact or quantitative values. It comes from the fact table configured in the cube.

.. i18n: We will make the measure for the same example. Measure type specifies whether it will be column base or sql expression based.
..

我们将使测量相同的例子。测量类型指定是否将列基地或基于sql表达式。

.. i18n: Column Based: 
..

基础列: 

.. i18n: .. image::  images/measure1.png
.. i18n:    :scale: 65
..

.. image::  images/measure1.png
   :scale: 65

.. i18n: SQL Expression Based: 
..

基于SQL表达式: 

.. i18n: .. image::  images/measure2.png
.. i18n:    :scale: 65
..

.. image::  images/measure2.png
   :scale: 65

.. i18n: In the column based measure we will see select the fact table column from the columns of the fact table define in the cube i.e. sale_order and sale_order_line.
..

基础列建立衡量我们将看到选择事实表列的列的事实表定义的多维数据集即销售订单和出售订单行。
.. i18n: .. image::  images/measure3.png
.. i18n:    :scale: 65
..

.. image::  images/measure3.png
   :scale: 65

.. i18n: So finally measure will look like:
..

所以将看最后措施:

.. i18n: .. image::  images/measure4.png
.. i18n:    :scale: 65
..

.. image::  images/measure4.png
   :scale: 65
