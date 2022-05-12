# jQuery

jQuery是JavaScript第三方模块
- 基于jQuery，自己开发一个功能
- 现成的工具依赖jQuery，例如bootstrip的动态效果

##1、快速上手
- 下载jQuery
- 一个简单的功能，修改标签内容
```html
<body>
    <h2 id="txt">是大风刮过</h2>

    <script src="./static/js/jquery-3.6.0.min.js"></script>
    <script type="text/javascript">
        //利用jQuery中的功能实现效果
        //1.找到id=txt的标签
        //2.内容修改
        $("#txt").text("erew");
    </script>
</body>
```

##2、寻找标签
- 基于ID选择
```html
<h1 id="c1">shshs</h1>
```
```javascript
$("#c1")
```

- 基于样式选择
```html
<h1 class="c1">shshs</h1>
```
```javascript
$(".c1")
```

- 标签选择
```html
<h1 class="c1">shshs</h1>
<div class="c1">shshs</div>
<span class="c1">shshs</span>
```
```javascript
$("h1")
$("div")
```

- 层级选择
```html
<div class="c1">
    <div class="c2">
        <a href="http://www.baidu.com">搜索</a>
    </div>
</div>
```
```javascript
$(".c1 .c2 a")
```

- 多选择器
```javascript
$("#c1,#c2,#c3")
```

- 属性选择器
```html
<input type="text",name="n1">
<input type="text",name="n2">
<input type="text",name="n3">
```
```javascript
$("input[name='n1']")
```

##3、间接寻找标签
- 找到上一个兄弟
```html
<div>
    <div>beijing</div>
    <div class="c1">shanghai</div>
    <div>shenzhen</div>
</div>  
```
```javascript
$(".c1").prev()//找到c1标签的上一个兄弟，就是beijing标签
```
- 找到下一个兄弟
```javascript
$(".c1").next()//找到c1标签的下一个兄弟，就是shenzhen标签
```
```javascript
$(".c1").next().next()//找到c1标签的下一个的下一个兄弟
```

- 找到所有的兄弟
```javascript
$(".c1").siblings()//找到c1标签的所有兄弟
```

- 找父子
```javascript
$(".c1").parent()//找到c1标签的父亲
```
```javascript
$(".c1").children()//找到c1标签的所有儿子
$(".c1").children(".p10")//找到c1标签的所有儿子中class='p10'的
```
```javascript
$(".c1").find()//找到c1标签的子孙
$(".c1").find("div")//找到c1标签的子孙中的div标签
$(".c1").find(".p10")//找到c1标签的子孙中的class='p10'的
```
##4、处理标签
- 加入样式
```javascript
$(".c1").next().addClass("hide");
```

- 删除样式
```javascript
$(".c1").next().removeClass("hide");
```

- 样式是否存在
```javascript
var hasclass = $(".c1").next().hasClass("hide");
```

####补充：
样式中添加cursor=pointer表示鼠标放置在该区域，鼠标指针变成小手

###案例：
制作城市列表，以省为单位；
点击省打开城市列表，同时关闭其他已经打开的列表；
点击已经打开的列表，则将其关闭；
<br>方案一:通过css中hover样式实现
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>City-list</title>
    <style>
        .city-list{
            width: 200px;
            height: 800px;
            background-color: #9acfea;
            border: solid 1px pink;
            margin-bottom: 0;
        }
        .city-list .city-name{
            padding: 5px 5px;
            font-size: 18px;
        }
        .city-list .city-name .area{
            display: none;
        }
        .city-list .city-name:hover .area{
            display: block;
        }
    </style>
</head>
<body>
    <div class="city-list">
        <div class="city-name">
            北京
            <ul class="area">
                <li>朝阳区</li>
                <li>海淀区</li>
                <li>大兴区</li>
                <li>昌平区</li>
            </ul>
        </div>
        <div class="city-name">
            上海
            <ul class="area">
                <li>静安区</li>
                <li>青浦区</li>
                <li>徐汇区</li>
                <li>宝山区</li>
            </ul>
        </div>
        <div class="city-name">
            深圳
            <ul class="area">
                <li>龙华区</li>
                <li>南山区</li>
                <li>宝安区</li>
                <li>福田区</li>
            </ul>
        </div>
    </div>
</body>
</html>
```

方案二：通过jQuery实现
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>City-list</title>
    <style>
        .city-list{
            width: 200px;
            height: 800px;
            background-color: #9acfea;
            border: solid 1px pink;
            margin-bottom: 0;
        }
        .city-list .city-name{
            cursor: pointer;
            margin: 10px 5px;
            font-size: 18px;
        }
        .city-list .city-name .area{
            display: none;
        }
    </style>
</head>
<body>
    <div class="city-list">
        <div class="city-name" onclick="display(this)">
            北京
            <ul class="area">
                <li>朝阳区</li>
                <li>海淀区</li>
                <li>大兴区</li>
                <li>昌平区</li>
            </ul>
        </div>
        <div class="city-name" onclick="display(this)">
            上海
            <ul class="area">
                <li>静安区</li>
                <li>青浦区</li>
                <li>徐汇区</li>
                <li>宝山区</li>
            </ul>
        </div>
        <div class="city-name" onclick="display(this)">
            深圳
            <ul class="area">
                <li>龙华区</li>
                <li>南山区</li>
                <li>宝安区</li>
                <li>福田区</li>
            </ul>
        </div>
    </div>
    <script src="./static/js/jquery-3.6.0.min.js"></script>
    <script type="text/javascript">
        function display(self) {
            var hasclass=$(self).find("ul").hasClass("area");//寻找点击标签的后代标签中的有.area样式的"ul"标签
            if (hasclass)//如果击标签的后代标签中的有.area样式的"ul"标签
            {
                $(self).parent().find("ul").addClass("area");//给所有的"ul"标签加上display=none的样式
                $(self).find("ul").removeClass("area");//给点击标签的后代标签中的"ul"标签去除display=none样式
            }
            else
            {
                $(self).find("ul").addClass("area");//给点击标签的后代标签中的"ul"标签加上display=none样式
            }
        }
    </script>
</body>
</html>
```

##5、值的操作
```html
<div id="c1">内容</div>
```
```javascript
$("#c1").text();//获取文本内容
$("#c1").text("中国");//设置文本内容
```
如果为input输入框
```html
<input type="text" id="c2">
```
```javascript
$("#c2").val();//获取用户输入内容
$("#c2").val("中国");//修改用户输入内容
```

##6、创建标签
```javascript
var newli = $("<li>").text("asdf");//内容为asdf
$("#view").append(newli);//将创建的标签添加到id=view的标签下
```
###案例：动态创建数据
输入用户名和密码，显示在页面上
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Test3</title>
</head>
<body>
    <div>
        <input type="text" id="username" placeholder="用户名">
        <input type="password" id="pwd" placeholder="密码">
    </div>
    <div>
        <input type="button" value="提交" onclick="display()">
    </div>
    <div>
        <ul id="view"></ul>
    </div>
    <script src="./static/js/jquery-3.6.0.min.js"></script>
    <script type="text/javascript">
        function display() {
            var user_name=$("#username").val();
            var user_pwd=$("#pwd").val();
            var display_info=user_name+' - '+user_pwd;
            var newli = $("<li>").text(display_info);//内容为display_info
            $("#view").append(newli);
        }
    </script>
</body>
</html>
```
![图片](./image/day07-01.png)<br>

##7、jQuery绑定事件
```html
<ul>
    <li>baidu</li>
    <li>google</li>
    <li>sougo</li>
</ul>
<script>
    $("li").click(function() {
        //点击li标签时，自动执行这个函数
        //$(this) 表示你当前点击的标签  
    })
</script>
```

jQuery特有的加载：<br>
```javascript
$(function() {
    //当页面框架加载完成之后，自动就执行
    }
)
```

##8、删除标签
```javascript
$("#c1").remove();//删除id=c1的标签
```


##9、标准引入
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Base</title>
    <link rel="stylesheet" href="./static/plugins/bootstrap-3.4.1/css/bootstrap.css">
    <link rel="stylesheet" href="./static/plugins/font-awesome-4.7.0/css/font-awesome.css">
</head>
<body>
    <script src="./static/js/jquery-3.6.0.min.js"></script>
    <script src="./static/plugins/bootstrap-3.4.1/js/bootstrap.js"></script>
</body>
</html>
```
