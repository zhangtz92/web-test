var v1=[11,22,33,44];
var v2=Array([11,22,33,44]);
//操作
v1[1]="帅哥";
v1.push("小哥");
console.log(v1);
function f1() {
    var tag=document.getElementById("txt");//DOM中内置函数
    var data=tag.innerText;
    var newdata=data.substring(1,data.length)+data[0];
    tag.innerText=newdata;
}
setInterval(f1,1000);