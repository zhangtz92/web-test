#JavaScript

编程语言，运行于浏览器<br>
##1、bootstrap依赖
bootstrap依赖JavaScript的类库，jQuery<br>
jQuery为第三方模块<br>
下载jQuery，可在页面上应用bootstrap的js类库<br>
https://jquery.com/download/

下载压缩版：https://code.jquery.com/jquery-3.6.0.min.js

下载非压缩版：https://code.jquery.com/jquery-3.6.0.js

在static文件夹下创建js目录，将压缩版放进去

在body中引入：
```html
<script src="./static/js/jquery-3.6.0.min.js"></script>
<script src="./static/plugins/bootstrap-3.4.1/js/bootstrap.min.js"></script>
```

####补充：DOM和BOM
编程语言内置模块，类似python中re、time模块

##2、JavaScript初步
实现页面动态效果
###1.代码存放位置
- 1.在head中：（如果在页面加载中需要展示的内容，就放在head中）
- 2.在body中（推荐,放在head中会在页面加载时先执行出来）：
```html
<script type="text/javascript">
    function myfunc(){
        alert("nihaoya");
    }
</script>
```

###2.代码存在形式
- 1.在当前html中
- 2.在其他js文件中导入使用

创建一个js文件：
```javascript
function f1() {
    alert("12345");
}
```
导入js文件：
```html
<script src="./static/js/f1.js"></script>
```

###补充：关于注释
- html
```html
<!--内容-->
```
- css
```css
/*内容*/
```

- JavaScript
```javascript
// 内容
/*内容*/
```

##3、JavaScript语言基础

###1.声明变量
```javascript
var name="tom";
console.log(name);
```
```html
<script type="text/javascript">
    var name="tom";
    console.log(name);
</script>
```

###2.字符串
```javascript
var name = String("大 帅 哥");
var v1=name.length;
var v2=name[0];
var v3=name.trim();/去除空白
var v4=name.substring(0,2);//字符串切片，左闭右开
```

###3.获取标签对象
可获得id标签的内容<br>
```html
<div id="txt">阿斯顿法国红酒看来围绕太阳与还是杜甫二十度撒旦给</div>
```
```javascript
var tag=document.getElementById("txt");//DOM中内置函数
var data=tag.innerText;
console.log(data);
```

###4.定时器
BOM内置函数
```javascript
setInterval(show,1000);//show为函数名，1000为1000ms
```

####案例：字符跑马灯
```javascript
function f1() {
    var tag=document.getElementById("txt");//DOM中内置函数，指针内联,取ID为“txt”中字符内容
    var data=tag.innerText;//取字符串内容
    var newdata=data.substring(1,data.length)+data[0];//第一个字移到最后
    tag.innerText=newdata;//新值直接赋值
}
setInterval(f1,1000);//f1为函数名，1000为1000ms
```
```html
<body>
    <span class="menus" id="txt">
        阿斯顿法国红酒看来围绕太阳与还是杜甫二十度撒旦给
    </span>
    <script src="./static/js/f1.js" type="text/javascript">

    </script>
</body>
```

###5.数组
```javascript
//定义
var v1=[11,22,33,44];
var v2=Array([11,22,33,44]);
//操作
v1[1]="帅哥";
v1.push("小哥");//尾部加入
v1.unshift("大哥");//头部加入
v1.splice(2,0,"中国");//索引插入，在索引=2的前面插入“中国”，0为保留项
v1.pop();//尾部删除
v1.shift();//头部删除
v1.splice(2,1);//索引删除，把索引=2的元素删除
//循环
for(var item in v1){
    //item为索引
}
for (var i=0;i<v1.length;i++){

}
```

###6.创建标签
```javascript
document.createElement("li");
```
获得标签内容：
```javascript
var tag=document.createElement("li");//创建标签
tag.innerText=text;//向标签中写内容
```
可使用appendChild向id中添加创建的标签<br>

利用javascript创建列表
```html
    <ul id="city">

    </ul>
    <script type="text/javascript">
        var citylist=["beijing","shanghai","shenzhen"];
        for(var count in citylist)
        {
            var text=citylist[count];//读取数组中数据
            var tag=document.createElement("li");//创建新标签
            tag.innerText=text;//新标签中的内容与数组中内容对于
            var parenttag=document.getElementById("city");//找到对应id的标签
            parenttag.appendChild(tag);//添加子标签
        }
    </script>
```

###7.对象
类似python中的字典
```javascript
//创建
info={
    name:"大帅哥",
    age:20
};
delete info[age];
```
利用javascript创建表格
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>test</title>
</head>
<body>
    <h2>试验表格</h2>
    <table border="1px">
        <thead id="table-head">

        </thead>
        <tbody id="table-body">

        </tbody>
    </table>
    <script type="text/javascript">
        /*表格对象具体信息*/
        var info=[{name:"大帅哥", age:20,gender:"男"},
            {name:"王二", age:30,gender:"男"},
            {name:"高富帅", age:25,gender:"男"},
            {name:"莉莉", age:25,gender:"女"},
            {name:"索菲", age:25,gender:"女"}];
        /*处理表头*/
        var tr_head_tag=document.createElement("tr");//创建一个表格表头的行的标签
        for(var head_info in info[0])//表头行有多少列
        {
            var head_elements=document.createElement("th");//创建一个表格表头的内容的标签
            head_elements.innerText=head_info;//元素的内容为对象info中内容
            tr_head_tag.appendChild(head_elements);//将元素添加到行标签
        }
        var tr_head=document.getElementById("table-head");//找到对应id的表头标签
        tr_head.appendChild(tr_head_tag);//将行标签添加到对应id的表头
        /*处理表格内容*/
        for(var count in info)//表格有多少行
        {
            tags=info[count];//提取每个对象，每个对象为一行
            var tr_body_tag=document.createElement("tr");////创建一个表格内容的行的标签
            for(var item in tags)//每一行有多少列
            {
                body_info=tags[item];//提取每个元素信息
                var body_elements=document.createElement("td");//创建一个表格元素的标签
                body_elements.innerText=body_info;//元素的内容为对象info中内容
                tr_body_tag.appendChild(body_elements);//将元素添加到行标签
            }
            var tr_body=document.getElementById("table-body");//找到对应id的表格内容标签
            tr_body.appendChild(tr_body_tag);//将行添加到表格
        }

    </script>
</body>
</html>
```

![图片](./image/day06-01.png)<br>

###8.条件语句
```javascript
if()
{

}
else if ()
{

}
else
{

}
```
###9.函数
```javascript
function f1() {
    
}
```

##4、DOM
DOM模块可以对HTML页面中的标签进行操作<br>
```javascript
//根据ID获取标签
var tag=document.getElementById("xxx");

//获取标签中文本
tag.innerText;

//修改标签中文本
tag.innerText="hahahaha";
```
```javascript
//创建标签<div></div>
var tag=document.createElement("div");

//写标签内容
tag.innerText="hahahaha";
```
```html
<ul id="city">
<!--    进行动态创建-->
</ul>
<script type="text/javascript">
    var tag=document.getElementById("city");
    var newtag=document.createElement("li");
    newtag.innerText="beijing";
    
    tag.appendChild(newtag);
</script>
```

##5、事件的绑定
通过函数与标签动作进行绑定
- 对于button：
<br>单击：onclick
<br>双击：ondblclick

- 对于input系列中text、textarea等文本输入：
<br>通过.value获得用户输入内容

####实例：
将用户输入内容显示在页面上，并清空输入框
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>test3</title>
</head>
<body>
    <div id="dis">
        <textarea name="text" id="txt"></textarea>
        <input type="button" value="提交" onclick="display()">
    </div>
    <script>
        function display() {
            //1.通过id找到用户输入框
            var texttag=document.getElementById("txt");
            //2.提取输入框内容
            var text_info=texttag.value;
            //3.创建新标签
            var newtag=document.createElement("div");
            //4.将新标签内容修改为输入框中提取到的信息
            newtag.innerText=text_info;
            //5.将新标签与所属标签进行关联
            var tag=document.getElementById("dis");
            tag.appendChild(newtag);
            //6.清空输入框内容
            texttag.value="";
        }
    </script>
</body>
</html>
```
![图片](./image/day06-02.png)<br>

##6、alert提示
```javascript
alert("输入不能为空");
```