function loadInfo(City,para){
  var xmlhttp;
  if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
   xmlhttp=new XMLHttpRequest();
  }else{// code for IE6, IE5
   xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
 }
 xmlhttp.onreadystatechange=function(){
   if (xmlhttp.readyState==4 && xmlhttp.status==200){
      console.log(xmlhttp.responseText);
      var obj = JSON.parse(xmlhttp.responseText);
      x=document.getElementsByClassName("location");
      x[0].innerHTML = obj.address;      
      x=document.getElementsByClassName("activity_name");
      console.log(obj.name);
      x[0].innerHTML = obj.name;            
  }
 }
  xmlhttp.open("GET","http://127.0.0.1:5000/CityInfo/"+City+"/"+para,true);
  xmlhttp.send();
}
function writeInfo(id,City){
  var xmlhttp;
    if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
    }else{// code for IE6, IE5
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.open("GET","http://127.0.0.1:5000/addActivity/"+City+"/"+id,false);
    xmlhttp.send();
 }
}
function writeActivities(user,City){
  x = document.getElementsById("droppable");
  for(i=0;i<x[0].childNodes.length;i++){
    writeInfo(x[0].childNodes[i].nodeValue,user,City);
  }
}