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