function requestActivity(city,id,elem){
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
      elem.link = obj.link;
      href = '/Activities.html/'+obj.id;
      elem.onclick="location.href=\'"+href+"\'";
      console.log(elem.nodeValue);
  }
 }
  xmlhttp.open("GET","http://127.0.0.1:5000/ActivityInfo/"+city+"/"+id,true);
  xmlhttp.send();
}
function loadActivities(city){
    var child = document.getElementById("draggable1").childNodes;
    console.log(child);
    for(i = 0; i < child.length; i++){
       requestActivity(city,i, child[i]);
    }
}

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
function writeInfo(activitiesId, date, userid, city){
  var xmlhttp;
    if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
    }else{// code for IE6, IE5
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.open("GET","http://127.0.0.1:5000/addTrip?activitiesId="+activitiesId+"&userid="+userid+"&city="+city+"&date="+date,false);
    xmlhttp.send();
}

function writeActivities(date, user, dst){
  x = document.getElementsById("droppable");
  activitiesId = x[0].childNodes[0].nodeValue;
  for(i=1;i<x[0].childNodes.length;i++){
    activitiesId += ("$"+x[0].childNodes.nodeValue[i]);
  }
  console.log(activitiesId);
  writeInfo(activitiesId, date, user, dst);
}