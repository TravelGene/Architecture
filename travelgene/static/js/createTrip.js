//Author: Qiankun Zhuang

function writeInfo(activitiesId, date1, date2, city){
  activitiesId = activitiesId.substring(0,activitiesId.length-1);
  console.log(activitiesId);
  var xmlhttp;
    if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
    }else{// code for IE6, IE5
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.open("GET","http://localhost:5000/addTrip?activitiesId="+activitiesId+"&city="+city+"&date1="+date1+"&date2="+date2,true);
    xmlhttp.send();
}

function writeActivities(date1,date2, dst){
  child = document.getElementById("select").childNodes;
  activitiesId = "";
    //console.log(date1);
    //console.log(date2);
    //console.log(dst);
    //console.log(child.length);
  for(i=1;i<child.length;i++) {
      //var strId = ""+(child[i].data);
      console.log(child[i]);

          //console.log(i);
          //console.log(child[i]);
          //console.log(child[i].getAttribute("text"));
          activitiesId += (child[i].getAttribute("text")+"$");



  }
  writeInfo(activitiesId, date1,date2, dst);
}