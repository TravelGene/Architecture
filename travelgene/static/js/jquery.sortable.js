/*
 * HTML5 Sortable jQuery Plugin
 * http://farhadi.ir/projects/html5sortable
 * 
 * Copyright 2012, Ali Farhadi
 * Released under the MIT license.
 */
(function($) {
var dragging, placeholders = $();
$.fn.sortable = function(options) {
	var method = String(options);
	options = $.extend({
		connectWith: false
	}, options);
	return this.each(function() {
		if (/^enable|disable|destroy$/.test(method)) {
			var items = $(this).children($(this).data('items')).attr('draggable', method == 'enable');
			if (method == 'destroy') {
				items.add(this).removeData('connectWith items')
					.off('dragstart.h5s dragend.h5s selectstart.h5s dragover.h5s dragenter.h5s drop.h5s');
			}
			return;
		}
		var isHandle, index, items = $(this).children(options.items);
		var placeholder = $('<' + (/^ul|ol$/i.test(this.tagName) ? 'li' : 'div') + ' class="sortable-placeholder">');

		items.find(options.handle).mousedown(function() {
			isHandle = true;

		}).mouseup(function() {
			isHandle = false;

		});
		$(this).data('items', options.items)
		placeholders = placeholders.add(placeholder);
		if (options.connectWith) {
			$(options.connectWith).add(this).data('connectWith', options.connectWith);
		}
		items.attr('draggable', 'true').on('dragstart.h5s', function(e) {
			if (options.handle && !isHandle) {
				return false;
			}
			isHandle = false;
			var dt = e.originalEvent.dataTransfer;
			dt.effectAllowed = 'move';
			dt.setData('Text', 'dummy');
			index = (dragging = $(this)).addClass('sortable-dragging').index();
		}).on('dragend.h5s', function() {
			dragging.removeClass('sortable-dragging').show();
			placeholders.detach();
			if (index != dragging.index()) {
				items.parent().trigger('sortupdate', {item: dragging});

			}
			dragging = null;
		}).not('a[href], img').on('selectstart.h5s', function() {
			this.dragDrop && this.dragDrop();

			return false;
		}).end().add([this, placeholder]).on('dragover.h5s dragenter.h5s drop.h5s', function(e) {
			if (!items.is(dragging) && options.connectWith !== $(dragging).parent().data('connectWith')) {
				return true;
			}

			var lastAlternativeLength = $("#alternative").children().length;
			var lastSelectLength = $("#select").children().length;
			if (e.type == 'drop') {
				
				e.stopPropagation();
				placeholders.filter(':visible').after(dragging);

                if(dragging.parent("ul").attr("id") == "alternative" && lastAlternativeLength != $("#alternative").children().length){
                    // make the selected item become NO    
                    $.getJSON('/update_recommend_list', {
                      place_id : dragging.attr("text"),
                      value: "N"
                    }, function(data) {   
                    	console.log("change to N");
                    	// set the min height of select and alternative
				        
                    });
                    return false;             
                }
                else if (dragging.parent("ul").attr("id") == "select" && lastSelectLength != $("#select").children().length)
                    //console.log("now se");
                    $.getJSON('/update_recommend_list', {
                      place_id : dragging.attr("text"),
                      value: "Y"
                    }, function(data) {
                        console.log("change to Y");
                        for(key in data){
                        	
                        	// flag
                        	var exit = false;
                        	// judge whether alternative already have this recom
                        	$("#alternative").children("li").each(function(){
                        		if($(this).attr("text") == data[key]["place_id"]){
                        			exit = true;
                        			
                        		}
                        	});
                        	// if has
                        	if(exit == true){
                        		continue;
                        	}

                        	// judge whether select has
                        	$("#select").children("li").each(function(){
                        		if($(this).attr("text") == data[key]["place_id"]){
                        			exit = true;
                        			
                        		}
                        	});
                        	// if has
                        	if(exit == true){
                        		continue;
                        	}

                        	//console.log(data[key]["desc"]);
                        	// means not in select or alternative, add it to alternative
                        	var childNode = '<li class="plan" text="';
                        	childNode += data[key]["place_id"];
                        	childNode += '" style=" background-image:url(';
                        	childNode += data[key]["img_url"];
                        	
                        	childNode += ')" draggable="true"><a style="height:100%; width:100%" href="/ActivityInfo/';
							childNode += data[key]["place_id"];
							childNode += '"><span><p>';
							childNode += data[key]["desc"];
							childNode += '</p></span></a></li>';
							$("#alternative").append(childNode);
							
							// activate new draggable item
				            $(".source, .target").sortable({
				                connectWith: ".connected"
				            });
				         	
				     
                        }
                           // set the min height of select and alternative
			            
                    });
					return false;

                //console.log(dragging.attr("text"));
                //console.log(dragging.parent("ul").attr("id"));
				return false;
			}
			 
			e.preventDefault();
			e.originalEvent.dataTransfer.dropEffect = 'move';
			if (items.is(this)) {
				if (options.forcePlaceholderSize) {
					placeholder.height(dragging.outerHeight());
				}

				dragging.hide();
				$(this)[placeholder.index() < $(this).index() ? 'after' : 'before'](placeholder);
				placeholders.not(placeholder).detach();
			} else if (!placeholders.is(this) && !$(this).children(options.items).length) {
				placeholders.detach();

				$(this).append(placeholder);
			}
			return false;
		});
	});
};
})(jQuery);
