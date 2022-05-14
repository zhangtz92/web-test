#加载图片

## 单张图片插入

- html中需要使用input file模块，通过表单的post形式提交，input file模块一定要有name属性
```html
<form method="post" action="/upload" enctype="multipart/form-data">
    <input type="file" name="upfile" onchange="showimage(this)">
    <div>
        <input type="submit" value="提交">
    </div>

</form>
<img id="upimg" style="height: 80px">
```

- 通过JavaScript显示缩略图
```javascript
function showimage(file){
    var reader= new FileReader();
    reader.onload = function (evt) {
        document.getElementById("upimg").src=evt.target.result;
    }
    reader.readAsDataURL(file.files[0])
}
```

- 在flask中定义页面
```python
from flask import Flask,render_template,request
import os
import random
from datetime import datetime

#获取当前绝对路径
basedir=os.path.abspath(os.path.dirname(__file__))

#Flask为一个类，对其进行实例化
app=Flask(__name__)
@app.route('/upload',methods=['GET','POST'])
def upload():
    img_suffix_com=['jpg','jpeg','png','gif','psd','tif','bmp']
    if request.method=='GET':
        return render_template("upload.html")
    elif request.method=='POST':
        file_upload=request.files.get('upfile')
        if file_upload.filename == '':
            return render_template("upload.html")
        #生成随机数
        else:
            file_suffix=file_upload.filename.rsplit('.',1)[1] #file_upload.filename.rsplit('.',1)[1]：获取文件后缀
            if file_suffix.lower() not in img_suffix_com: #非图片文件上传
                file_upload = None
                return render_template("upload.html")
            else: #上传图片文件
                random_num=random.randint(0,100)
                #图片名称为：时间+随机数+原文件后缀
                filename=datetime.now().strftime("%Y%m%d%H%M%S")+'_'+str(random_num)+'.'+file_suffix
                file_path=basedir+"/static/img/"+filename
                file_upload.save(file_path)
                return render_template("upload.html")
    else:
        return "ERROR"

if __name__ == '__main__':
    app.run(host="localhost",port="3389")
```

## 加载多张图片

- 在html中，input file里加入multiple属性
```html
<h2>上传文件</h2>
<form method="post" action="/upload" enctype="multipart/form-data">
    <input type="file" name="upfile" onchange="showimage(this)" multiple>
    <div>
        <input type="submit" value="提交">
    </div>
</form>
<div id="display">
    <div id="display-image">
    </div>
</div>
```

- flask中，将多个文件返回的信息进行转换，转成字典进行处理
```python
from flask import Flask,render_template,request
import os
import random
from datetime import datetime

#获取当前绝对路径
basedir=os.path.abspath(os.path.dirname(__file__))

#Flask为一个类，对其进行实例化
app=Flask(__name__)
@app.route('/upload',methods=['GET','POST'])
def upload():
    img_suffix_com=['jpg','jpeg','png','gif','psd','tif','bmp']
    if request.method=='GET':
        return render_template("upload.html")
    elif request.method=='POST':
        #print(request.files)
        file_info_dict=dict(request.files)#将ImmutableMultiDict转换为字典
        file_info_list=file_info_dict['upfile']#提取上传文件信息列表
        #print(file_info_list)
        for file_upload in file_info_list:
            # file_upload=file_info.get('upfile')
            print(file_upload)
            if file_upload.filename == '':
                continue
            #生成随机数
            else:
                file_suffix=file_upload.filename.rsplit('.',1)[1] #file_upload.filename.rsplit('.',1)[1]：获取文件后缀
                if file_suffix.lower() not in img_suffix_com: #非图片文件上传
                    file_upload = None
                    continue
                else: #上传图片文件
                    random_num=random.randint(0,100)
                    # 图片名称为：时间+文件计数+随机数+原文件后缀
                    filename=datetime.now().strftime("%Y%m%d%H%M%S")+'_'+str(file_info_list.index(file_upload))+'_'+str(random_num)+'.'+file_suffix
                    file_path=basedir+"/static/img/"+filename
                    file_upload.save(file_path)
        return render_template("upload.html")
    else:
        return "ERROR"

if __name__ == '__main__':
    app.run(host="localhost",port="3389")
```

- 对于显示多个缩略图：
```javascript
function showimage(file){
    document.getElementById('display-image').remove();//将原标签删除，以更新缩略图
    var divtag=document.getElementById("display");
    var tag_d=document.createElement("div");
    tag_d.setAttribute("id","display-image");
    divtag.appendChild(tag_d);//重新创建用于显示缩略图的标签
    for(i=0;i<file.files.length;i++){
        displayimage(file.files[i]);
    }
}
function displayimage(file){
    var imagetag=document.getElementById("display-image");
    var tag=document.createElement("img");//创建标签
    var reader= new FileReader();
    reader.onload = function (evt) {
        tag.src = evt.target.result;
    };
    reader.readAsDataURL(file);
    tag.setAttribute("style","height:100px;float:left");
    imagetag.appendChild(tag);
}
```

