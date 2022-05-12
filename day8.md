#添加数据页面
##案例：人员信息录入系统

- 用户名
- 年龄
- 薪资
- 部门
- 入职时间（*）

####对于时间的选择框（插件）
datatimepicker基于bootstrap的时间管理插件<br>
http://www.bootcss.com/p/bootstrap-datetimepicker/
<br>下载插件并应用，将文件夹解压到static/plugins文件夹中，并在script与css中分别引入<br>
```html
<link rel="stylesheet" href="./static/plugins/bootstrap-datetimepicker-master/css/bootstrap-datetimepicker.css">
<script src="./static/plugins/bootstrap-datetimepicker-master/js/bootstrap-datetimepicker.js"></script>
```
调用：
```html
<div class="col-sm-6">
    <input type="text" id="datetime">
</div>
```
```html
<script>
    $("#datetime").datetimepicker({
        format:'yyyy-mm-dd',//显示格式
        minView:'month',//只显示到月、日
        autoclose:true,//自动关闭
    });
</script>
```
显示中文：
```html
<script src="./static/plugins/bootstrap-datetimepicker-master/js/locales/bootstrap-datetimepicker.zh-CN.js"></script>
<script >
    $("#datetime").datetimepicker({
        format:'yyyy-mm-dd',//显示格式
        minView:'month',//只显示到月、日
        autoclose:true,//自动关闭
        language:'zh-CN',//显示中文
    });
</script>
```

如果起始时间设置为当日：startDate:'0',

##补充：也可以使用datepicker！



