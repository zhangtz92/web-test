#BootStrap

- Bootstrap是美国Twitter公司的设计师Mark Otto和Jacob Thornton合作基于HTML、CSS、JavaScript 开发的简洁、直观、强悍的前端开发框架，使得 Web 开发更加快捷。
- Bootstrap提供了优雅的HTML和CSS规范，它即是由动态CSS语言Less写成。
<br>

##1、下载bootstrap

https://v3.bootcss.com/getting-started/#download

##2、使用bootstrap

- 在页面上引入bootstrap
- 在编写html时，按照bootstrap的规定来编写
- 加入自定制

###1.导入bootstrap样式
```css
    <!--开发版本-->
    <link rel="stylesheet" href="./static/plugins/bootstrap-3.4.1/css/bootstrap.css">
    <!--生产版本-->
    <link rel="stylesheet" href="./static/plugins/bootstrap-3.4.1/css/bootstrap.min.css">
```

###2.bootstrap导航
https://v3.bootcss.com/components/

可设置一系列样式
使用导航条，可把nav改为div

###3.栅格系统
可自动适应屏幕宽度<br>
在全局css中找到栅格系统
https://v3.bootcss.com/css/#grid
- 响应式：
<br>行内内容开始是堆叠在一起的，当大于这些阈值时将变为水平排列
```html
.col-lg-  1170px
.col-md-  970px
.col-sm-  750px
```
- 非响应式：
<br>行内内容随页面缩放始终按比例显示
```html
    <div class="col-xs-8" style="background-color: #419641">.col-md-8</div>
    <div class="col-xs-4" style="background-color: palevioletred">.col-md-4</div>
```

- 列偏移
```html
<div class="row">
    <div class="col-md-4" style="background-color: orangered">.col-md-4</div>
    <div class="col-md-2 col-md-offset-2" style="background-color: blue">.col-md-4 .col-md-offset-4</div>
</div>
```
col-md-offset-x为向右侧偏移x个栅格

- container
<br>设置左右留白，container为大留白，container-fluid为小留白
```html
<div class="container">
    <div class="col-md-4" style="background-color: orangered">.col-md-4</div>
    <div class="col-md-4 col-md-offset-4" style="background-color: blue">.col-md-4 .col-md-offset-4</div>
</div>
<div class="container-fluid">
    <div class="col-md-4" style="background-color: orangered">.col-md-4</div>
    <div class="col-md-4 col-md-offset-4" style="background-color: blue">.col-md-4 .col-md-offset-4</div>
</div>
```

###补充
设置边框阴影：box-shadow：水平（正值在右边，负值在左边）、垂直（正值在下边，负值在上边）、模糊距离、阴影颜色

###关于图标
bootstrap中提供的图标有限，从fontawesome中找图标<br>
https://fontawesome.dashgame.com/
<br>将文件夹解压到plugins文件夹
```css
<link rel="stylesheet" href="./static/plugins/font-awesome-4.7.0/css/font-awesome.css">
```
可添加各种图标






