//request the info from py, and receive what from that
function requestActivity(city,id,elem){
  var xmlhttp;
  if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
   xmlhttp=new XMLHttpRequest();
  }else{// code for IE6, IE5
   xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
 }
 xmlhttp.onreadystatechange=function(){
   if (xmlhttp.readyState==4 && xmlhttp.status==200){
      return xmlhttp.responseText.split("$");
      var obj = JSON.parse(xmlhttp.responseText);

      elem.nodeValue = obj['a_id'];
      elem.onclick= function(){
        location.href= href;
      };

  }
 }
  console.log(city,id);
  xmlhttp.open("GET","http://127.0.0.1:5000/ActivityInfo/"+city+"/"+id,true);
  xmlhttp.send();
}
function loadActivities(city){
    var child = document.getElementById("draggable1").childNodes;

    console.log(child[2].className);
    console.log("===");
    var cnt = 0;
    requestActivity(city,cnt++, child[i]);
    for(i = 0; i < child.length; i++){
       var strId = ""+(child[i].id);
       if(strId.indexOf("test")>=0){
            //click and jump to the detail of this activity
            //why we don't add at the draggable onclick function???
            href = './Activities?'+"city="+obj['a_id'].split('_')[0]+'&id='+obj['a_id'].split('_')[1];
            console.log(child[i].id);
       }
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
function writeInfo(activitiesId, date1,date2, userid, city){
  var xmlhttp;
    if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
    }else{// code for IE6, IE5
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.open("GET","http://127.0.0.1:5000/addTrip?activitiesId="+activitiesId+"&userid="+userid+"&city="+city+"&date1="+date1+"&date2="+date2,true);
    xmlhttp.send();
}

function writeActivities(date1,date2, user, dst){
  x = document.getElementsById("droppable");//undefined exception, no droppable in html file
  activitiesId = x[0].childNodes[0].nodeValue;
  for(i=1;i<x[0].childNodes.length;i++){
    activitiesId += ("$"+x[0].childNodes.nodeValue[i]);
  }
  console.log(activitiesId);
  writeInfo(activitiesId, date1,date2, user, dst);
}