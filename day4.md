
#css进阶

##1、hover用法
用于鼠标触碰后改变样式
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>day4-test</title>
    <style>
        .c1{
            color:red;
            font-size: 40px;
        }
        .c1:hover{
            color:black;
            font-size: 60px;
        }
    </style>
</head>
<body>
    <div class="c1">
        今天测试内容
    </div>
    <div>
        测试比对
    </div>
</body>
</html>
```
利用hover显示隐藏图标：<br>
鼠标移走，图片隐藏，鼠标放置在内容位置，图片显示
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>day4-test</title>
    <style>
        .c1{
            color:red;
            font-size: 20px;
        }
        .pic{
            display: none;
        }
        .c1:hover .pic{
            display: block;
        }
    </style>
</head>
<body>
    <div class="c1">
        今天测试内容
        <div class="pic">
            <img src="http://www.sgcc.com.cn/html/files/2022-04/30/20220430085920741199480.jpg" alt="">
        </div>
    </div>
</body>
</html>
```

##2、after
在内部元素尾部加上一些内容
```css
.c1:after{
    content: "XXX";
}
```
对于div漂浮后脱离文档流，除了在最后加上外
```html
<div class="clear:both"></div>
```
也可以在style中加入
```css
.area:after{
    content: "";
    display: block;
    clear: both;
}
```
可清除浮动

##3、position
####fixed：固定在窗口某个位置
```css
.back{
    position: fixed;
    width:60px;
    height:60px;
    border:1px solid red;
    right:10px;
    top:30px;
}
```
如果有多个position时，则设置z-index:number，谁的number大谁在上面

####relative和absolute：
设置子标签在父标签的中的相对位置

##4、border
border-left：左边框<br>
对于边框颜色，如果设置transparent，则为透明色，很多时候配合hover使用

##5、background-color

