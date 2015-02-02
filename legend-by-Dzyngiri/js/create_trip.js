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