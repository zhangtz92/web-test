-
Day2:
-
html标签

1、编码
```html
<meta charset="UTF-8">
```

2、title

title标签中内容即为网页显示标题

```html
<head>
    <meta charset="UTF-8">
    <title>Day1</title>
</head>
```

3、标题
```html
<h1>1级标题</h1>
<h2>2级标题</h2>
<h3>3级标题</h3>
<h4>4级标题</h4>
<h5>5级标题</h5>
<h6>6级标题</h6>
```

4、div和span

内容标签
```html
<div>内容</div>

<span>内容</span>
```
- div标签独占网页的一行，块级标签

- span标签在网页中占一行的一个区域，行内标签，内容多大占多大

    素标签，需要配合css样式
```html
<body>
    <h2>Day2-web</h2>
    <div>
        <span style="color: red">时间：</span>
        <span>2022.04.29</span>
    </div>
    <div>
        关于html标签
    </div>
</body>
```
![图片](./image/day02-01.png)<br>

5、超链接
```html
<a href="跳转地址">点击跳转</a>
```
需要跳转到新打开的页面：
```html
<a href="跳转地址" target="_blank">点击跳转</a>
```

6、图片    
行内标签
```html
<img src="图片地址" />
```

引入别的网站图片地址（可能会有防盗链）
```html
<img src="https://t7.baidu.com/it/u=508006830,4042443322&fm=193&f=GIF" />
```

显示自己的图片   
对于flask，需要在自己项目中创建：static目录，图片要放在static目录中,否则图片不显示
```html
<img src="/static/103358aloddojctjo9ptfd.jpg" />
```

对图片高度、宽度进行设置：
```html
<img style="height: 100px;width: 80px" src="图片地址" />
```
或者按照百分比设置：
```html
<img style="height: 10%;width: 10%" src="图片地址" />
```

7、列表  

无序列表
```html
<ul>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
</ul>
``` 

有序列表:列表前面有序号
```html
<ol>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
</ol>
```
注意：列表中的行不受div的影响，例：
```html
<ul>
    <li>北京</li>
    <li>上海</li>
    <li>广州</li>
    <li>深圳</li>
</ul>
<div>
    <ul>
        <li>北京</li>
        <li>上海</li>
        <li>广州</li>
        <li>深圳</li>
    </ul>
</div>
<ol>
    <li>北京</li>
    <li>上海</li>
    <li>广州</li>
    <li>深圳</li>
</ol>
<div>
    <ol>
        <li>北京</li>
        <li>上海</li>
        <li>广州</li>
        <li>深圳</li>
    </ol>
</div>
```
![图片](./image/day02-02.png)<br>


8、表格  
标签：  
table：表格,border="1"表示加上边框  
thead：表头  
tbody：表的内容  
tr：表的一行  
th：嵌套在tr中使用，表头中某一行对应的内容  
td：嵌套在tr中使用，表的内容中某一行对应的内容  
例：
```html
<table border="1">
    <thead>
        <tr><th>姓名</th><th>年龄</th><th>等级</th></tr>
    </thead>
    <tbody>
        <tr><td>James</td><td>20</td><td>王者</td></tr>
        <tr><td>Simon</td><td>23</td><td>青铜</td></tr>
        <tr><td>Sophie</td><td>27</td><td>白银</td></tr>
        <tr><td>Tommy</td><td>21</td><td>黄金</td></tr>
    </tbody>
</table>
```
![图片](./image/day02-03.png)<br>

9、input系列  
明文输入、密码输入、文件输入
```html
<input type="text">
<input type="password">
<input type="file">
```
选择框，相同的name为单选框
```html
<input type="radio" name="n1" value="1">男
<input type="radio" name="n1" value="2">女
```
复选框
```html
<input type="checkbox" name="habit" value="1">篮球
<input type="checkbox" name="habit" value="2">足球
<input type="checkbox" name="habit" value="3">乒乓球
<input type="checkbox" name="habit" value="4">游泳
```
按钮  
button为普通按钮，submit可提交表单
```html
<input type="button" value="提交">
<input type="submit" value="提交">
```

10、下拉框
```html
<select name="city">
    <option value="bj">北京</option>
    <option value="sh">上海</option>
    <option value="gz">广州</option>
    <option value="sz">深圳</option>
</select>
```
多选的下拉框(按住shift可多选，但不是很好用)
```html
<select name="city" multiple>
    <option value="bj">北京</option>
    <option value="sh">上海</option>
    <option value="gz">广州</option>
    <option value="sz">深圳</option>
</select>
```

11、多行输入文本
```html
<textarea name="text"></textarea>
```

默认给出三行的输入范围（可以输入多行，只能文本框高度为3行）
```html
<textarea rows=3 name="text"></textarea>
```

12、form表单和提交    
method="get"表示以get形式提交  
method="post"表示以post形式提交    
action="提交的地址"  
如果form标签中有submit按钮，点击该按钮即可提交form标签中所有数据  
botton只是普通效果的按钮     
页面上数据需要提交到后台：   
1.form标签需要包裹需要提交的数据：提交方式与提交地址、submit按钮
2.在form中，input标签一定要写name属性
```html
<form method="get" action="/exec/reg">
    <div>
        用户名：<input type="text" name="user">
    </div>
    <div>
        密码：<input type="password" name="pwd">
    </div>
    <div>
        <input type="submit" value="提交">
        <input type="button" value="取消">
    </div>
</form>
```
在manage中添加"/exec/reg"的跳转页面与request接收：
```python
@app.route("/exec/reg")
def exec_reg():
    #接收用户通过GET形式发送过来的数据
    print(request.args)
    #给用户再返回数据
    return "success"
```
```python
from flask import Flask,render_template,request
```
输入的用户名和密码可被接收到：
![图片](./image/day02-04.png)<br>
![图片](./image/day02-05.png)<br>

如果通过POST形式提交：   
```html
<h1>提交测试POST</h1>
    <form method="post" action="/exec/post_reg">
        <div>
            用户名：<input type="text" name="user">
        </div>
        <div>
            密码：<input type="password" name="pwd">
        </div>
        <div>
            <input type="submit" value="提交">
            <input type="button" value="取消">
        </div>
    </form>
```
在manage.py中添加post跳转页面：
```python
@app.route("/exec/post_reg",methods=["POST"])
def exec_post_reg():
    #接收用户通过GET形式发送过来的数据
    print(request.form)
    #给用户再返回数据
    return "post_success"
```
输入的用户名和密码可被接收到，但URL中无相关数据：
![图片](./image/day02-06.png)<br>
![图片](./image/day02-07.png)<br>

.get与.getlist可获得各提交的值：
```python
city=request.form.get("city")
more = request.form.get("more")
habit=request.form.getlist("habit")
print(more,city,habit)
```
