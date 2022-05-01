
#Day3:


CSS样式，用来美化html标签    
当一个标签上有style时，就是定义其样式


##1、CSS应用方式   
###1.在标签上直接写
```html
<div>
    <span style="color: red">时间：</span>
    <span>2022.04.29</span>
</div>
<img style="height: 10%;width: 10%" src="https://t7.baidu.com/it/u=508006830,4042443322&fm=193&f=GIF" />
```
###2.在head标签中写style标签（方便对样式进行复用）（常用）
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>用户注册</title>
    <style>
        .c1{
            color:red;
        }
    </style>
</head>
<body>
    <h1 class="c1">主页面</h1>
</body>
</html>
```
###3.在文件中写入样式
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>用户注册</title>
    <link rel="stylesheet" href="../style/common.css">
</head>
<body>
    <h1 class="c1">主页面</h1>
</body>
</html>
```
在style文件夹中新建common.css文件
```css
.c1{
    color: blue;
}
```

在flask中，css文件需要放置在static文件夹中，并通过/static/common.css引用

##2、CSS选择器    

###1.类选择器：
class="c1"去style中找.c1的样式（用的最多）
```html
.c1{

}
<div class="c1"></div>
```
###2.ID选择器：
id="c2"去style中找#c2的样式（一个页面只能用一个id）
```html
#c1{

}
<div id="c1"></div>
```
###3.标签选择器：
如果在style中设置li的样式，则页面所有的li标签都会使用该样式
```html
div{

}
<div>xxx</div>
```
###4.属性选择器：
对input中某个属性设置样式
```html
input[type='text']{
    border:1px red;
}
<input type="text">
```
###5.后代选择器：
对某个class下的某一类标签设置样式
去子子孙孙里面找：
```html
.yy li{
    color: red;
}
<div class="yy">
    <li>aa</li>
    <li>bb</li>
</div>
```
去儿子里面找：
```html
.yy>li{
    color: red;
}
<div class="yy">
    <li>aa</li>
    <li>bb</li>
</div>
```

###6.关于多个样式和覆盖：  
对于选择多个样式，所有的样式全部应用，但重复的样式会选用style中下面的样式
```html
.c1{
    color:red;
    border: 1px solid red;
}
.c2{
    color:blue;
    font-size:10px;
}
<div class="c1 c2">xxx</div>
```
如果就是头铁，要用style中上面的样式，则在样式中加上!important
```html
.c1{
    color:red !important;
    border: 1px solid red;
}
.c2{
    color:blue;
    font-size:10px;
}
<div class="c1 c2">xxx</div>
```

##3、CSS具体的样式  
###1.高度和宽度：
height=300px;width=100px;
宽度支持百分比：width=20%;
高度与宽度对行内标签默认无效

###2.块级和行内标签：
标签->display:inline-block
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>用户注册</title>
    <style>
        .c1{
            display: inline-block;
            height: 300px;
            width: 200px;
            border: red solid 1px;
        }
    </style>

</head>
<body>
    <span class="c1">主页面</span>
</body>
</html>
```
可见span行内标签也可以定义高度与宽度
![图片](./image/day03-01.png)<br>

行内标签和块级标签页可以通过样式相互转化
```html
<div style="display: inline">xxx</div>
<span style="display: block">yyy</span>
```

###3.字体大小：
font-size=10px;
###4.字体加粗：
font-weight=400;
###5.字体：
font-family:Microsoft Yahei;
###6.文字在水平方向上居中：
text-align:center;
###7.文字在垂直方向上居中：
line-height=height;（height为块的高度）

###8.浮动
```html
<div>
    <span>LEFT</span>
    <span style="float: right">RIGHT</span>
</div>
```
div默认为块级标签，比较霸道，但浮动起来就不一样了，自己有多宽占多宽
但会导致div脱离文档流，漂浮在页面上，需要在最后加上style="clear:both"给div拽回来

###9.内边距  
padding、padding-top、padding-bottom、padding-left、padding-right
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>用户注册</title>
    <style>
        .out{
            height: 200px;
            width: 200px;
            border:1px solid red;
            padding-top: 30px;
        }
    </style>

</head>
<body>
    <div class="out">
        <div style="color: gold">2002年的第一场雪</div>
        <div>记不得了</div>
    </div>
</body>
</html>
```

###10.外边距：我距离别人的距离（内边距为自身空出一段距离）  
margin-top、margin-bottom、margin-left、margin-right
如果不想body中的白色边框，则在style中：
```css
body{
    margin: 0;
}
```
如需要块居中，则设置margin:0 auto;<br>
文本居中：text-align:center;

##4、如果想要别的网站的样式，使用google chrome
![图片](./image/day03-02.png)<br>


##补充：
如果a标签不想要下划线，则在样式中加入text.decoration:none即可

如果鼠标放到链接上，链接变色，则在加入样式a:hover{color:red}

a标签是行内标签，其高度与内外边距无效，需要是将其转换为块级-行内标签

透明度设置：opacity（0到1之间，1为正常，0为透明）
