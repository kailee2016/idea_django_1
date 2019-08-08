
1.本项目中主要熟悉了从model中生成数据库表的过程
以及将数据库中的数据通过简单查询显示到web页面上，在APP的model文件中
使用python manage.py makemigrate
python manage.py migrate

2.继承模板的方法
{%extend '父模板相对于templates的路径以及文件名.html'%}
父模板中要使用{%block block_name%}
{%endblock block_name%}进行标识

3.超链接的使用方法
注意<a></a>为闭合标签
超链接中
<a href="{% url 'app_name:url_name' paravalue}">...</a>

4.views中的def与模板之间的关联方法
from django.shortcut import render

return render(request,'目标模板相对于templates的路径以及文件名.html',context=context)

5.外键的使用
在查询中外键实际上代表的是该外键所对应的对象（表）中的对象，可以通过"."（点运算符）进行链式调用，详情可以参考index中的authorID