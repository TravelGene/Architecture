//Author: Qiankun Zhuang

function loadInfo(city,id)
{
  var xmlhttp;
  if (window.XMLHttpRequest)
{// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
}
else
{// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
}
xmlhttp.onreadystatechange=function()
{
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
  {
    var obj = JSON.parse(xmlhttp.responseText);
    x=document.getElementsByClassName("location");
    x[0].innerHTML = obj.address;      
    x=document.getElementsByClassName("activity_name");
    x[0].innerHTML = obj.name;            
  }
}
xmlhttp.open("GET","http://127.0.0.1:5000/ActivityInfo/"+city+"/"+id,true);
xmlhttp.send();
}