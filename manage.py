from flask import Flask,render_template,request

#Flask为一个类，对其进行实例化
app=Flask(__name__)

#创建了网址下的/base/info和函数index间的关系
#在浏览器中访问网址+/base/info，网站自动执行index函数中内容

@app.route("/base/info")
def index():
    #return "Web-Day1"
    #通过render_template，flask会自动打开文件
    #默认去当前项目目录的templates文件夹中读取
    info=["王二","sophie","tommy","milliy"]
    return render_template("index.html",title="网页制作",datalist=info)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/tests/test",methods=['GET'])
def test():
    return render_template("test.html")

@app.route("/exec/reg")
def exec_reg():
    #接收用户通过GET形式发送过来的数据
    print(request.args)
    #给用户再返回数据
    return "success"

@app.route("/exec/post_reg",methods=["POST"])
def exec_post_reg():
    #接收用户通过GET形式发送过来的数据
    print(request.form)
    city=request.form.get("city")
    more = request.form.get("more")
    habit=request.form.getlist("habit")
    print(more,city,habit)
    #给用户再返回数据
    return "post_success"

if __name__ == '__main__':
    app.run(host="localhost",port="3389")