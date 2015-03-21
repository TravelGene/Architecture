//Author: Qiankun Zhuang


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
        var cnt = 0;
        for(i = 0; i < child.length; i++){
           var strId = ""+(child[i].id);
           if(strId.indexOf("test")>=0){
                child[i].text = ids[cnt];
                shref = './Activities?'+"city="+city+'&id='+ids[cnt];
                child[i].setAttribute('link',shref);
                child[i].setAttribute('text',ids[cnt]);
                child[i].onclick = function(){
                    location.href = this.getAttribute('link');
                }
                console.log(child[i]);
                cnt++;
           }
        }
   }
 }
    xmlhttp.open("GET","http://127.0.0.1:5000/ActivityInfo/"+city);
    xmlhttp.send();
}
function writeInfo(activitiesId, date1, date2, city){
  activitiesId = activitiesId.substring(0,activitiesId.length-1);
  console.log(activitiesId);
  var xmlhttp;
    if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
    }else{// code for IE6, IE5
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.open("GET","http://127.0.0.1:5000/addTrip?activitiesId="+activitiesId+"&city="+city+"&date1="+date1+"&date2="+date2,true);
    xmlhttp.send();
}

function writeActivities(date1,date2, dst){
  child = document.getElementById("droppable").childNodes;
  activitiesId = ""
  for(i=0;i<child.length;i++){
    var strId = ""+(child[i].id);
    if(strId.indexOf("test")>=0){
            console.log(child[i].text);
            activitiesId += (child[i].text+"$");
    }
  }
  writeInfo(activitiesId, date1,date2, dst);
}

$(document).ready(function() {

    var selectedClass = 'ui-state-highlight',
        clickDelay = 600,
        // click time (milliseconds)
        lastClick, diffClick; // timestamps

    $("#droppable div, #draggable1 div")
    // Script to deferentiate a click from a mousedown for drag event
    .bind('mousedown mouseup', function(e) {
        if (e.type == "mousedown") {
            lastClick = e.timeStamp; // get mousedown time
        } else {
            diffClick = e.timeStamp - lastClick;
            if (diffClick < clickDelay) {
                // add selected class to group draggable objects
                $(this).toggleClass(selectedClass);
            }
        }
    })
    .draggable({
        revertDuration: 10,
        // grouped items animate separately, so leave this number low
        containment: '.demo',
        start: function(e, ui) {
            ui.helper.addClass(selectedClass);
            $("#draggable1").css({
                'z-index':19
            });
            $("#droppable").css({
                'z-index':19
            });
        },
        stop: function(e, ui) {
            // reset group positions
            $('.' + selectedClass).css({
                top: 0,
                left: 0
            });
            $('.' + selectedClass).parent().css({
                'z-index':12.
            });
        },
        drag: function(e, ui) {
            // set selected group position to main dragged object
            // this works because the position is relative to the starting position
            $('.' + selectedClass).css({
                top: ui.position.top,
                left: ui.position.left,
                'z-index':100.
            });
            $('.' + selectedClass).parent().css({

                'z-index':99.
            });
        }
    });

    $("#droppable, #draggable1").sortable().droppable({
        drop: function(e, ui) {
            $('.' + selectedClass).appendTo($(this)).add(ui.draggable) // ui.draggable is appended by the script, so add it after
            .removeClass(selectedClass).css({
                top: 0,
                left: 0,
                'z-index':3.
            });
            $('.' + selectedClass).parent().css({

                'z-index':12.
            });

        }
    });

});