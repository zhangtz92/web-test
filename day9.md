# 后端开发

##回到flask
- 在flask中，bootstrap、datetimepicker、jQuery均需要放到文件根目录的static文件夹下
标准引入：
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>主页面</title>
    <link rel="stylesheet" href="/static/plugins/bootstrap-3.4.1/css/bootstrap.css">
    <link rel="stylesheet" href="/static/plugins/font-awesome-4.7.0/css/font-awesome.css">
</head>
<body>
<script src="/static/js/jquery-3.6.0.min.js"></script>
<script src="/static/plugins/bootstrap-3.4.1/js/bootstrap.js"></script>
</body>
</html>
```
问题：其内容完全是被写死的

##flask动态写入数据
```html
<h2>{{title}}</h2>
```
```python
@app.route("/base/info")
def index():
    #1、找到网页index.html的内容，读取所有内容
    #2、找到内容中的特殊占位符，将数据替换
    #3、特殊的占位符用{{xxx}}表示
    return render_template("index.html",title="网页制作")
```

##特殊的占位符
1、for循环
```html
<h2>{{title}}</h2>
<ul class="list-group">
    {% for item in datalist %}
    <li class="list-group-item">{{item}}</li>
    {% endfor %}
</ul>
```
```python
info=["王二","sophie","tommy","milliy"]
```

![image](./image/day09-01.png)<br>