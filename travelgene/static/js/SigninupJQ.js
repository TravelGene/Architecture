	
$(document).ready(function(){
	$("#signin").click(function(){
		$("#view-signin").css("display","none");
		$("#view-signup").css("display","block");
		$("#logPart").css("height","300px").attr("src","img/LogPart.png");

	});
	$("#signup").click(function(){
		$("#view-signup").css("display","none");
		$("#view-signin").css("display","block");
		$("#logPart").css("height","180px").attr("src","img/LogPart2.png");
	});
});