
function loadActivities(city){
    var ids;
    var xmlhttp;
      if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
       xmlhttp=new XMLHttpRequest();
      }else{// code for IE6, IE5
       xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
     }
      xmlhttp.onreadystatechange=function(){
   if (xmlhttp.readyState==4 && xmlhttp.status==200){
        idStr = xmlhttp.responseText;
        var child = document.getElementById("draggable1").childNodes;
        var cnt = 0;
        idStr = idStr.substring(0,idStr.length-1);
        ids = idStr.split("$");
        console.log("zxcvz",ids);
        var cnt = 0;
        for(i = 0; i < child.length; i++){
           var strId = ""+(child[i].id);
           if(strId.indexOf("test")>=0){
                child[i].text = ids[cnt];
                shref = './Activities?'+"city="+city+'&id='+ids[cnt++].split('_')[1];
                var ns = shref;
                child[i].text = ids[cnt];
                child[i].onclick = function(){
                    location.href = text;
                }
                console.log("tesT"+child[i].text);
                console.log(child[i].id);
           }
        }
   }
 }
    xmlhttp.open("GET","http://127.0.0.1:5000/ActivityInfo/"+city);
    xmlhttp.send();
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
  activitiesId = activitiesId.substring(0,activitiesId.length-1);
  console.log(activitiesId);
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
  child = document.getElementById("droppable").childNodes;
  activitiesId = ""
  for(i=0;i<child.length;i++){
    var strId = ""+(child[i].id);
    if(strId.indexOf("test")>=0){
            activitiesId += (child[i].text+"$");
    }
  }
  writeInfo(activitiesId, date1,date2, user, dst);
}