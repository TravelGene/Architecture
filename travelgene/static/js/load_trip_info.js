function loadTripInfo() 
{ 
	var url=location.href; 
	var temp=url.split("?")[1]; 
	var tripArr=temp.split("&"); 
	var destination = tripArr[0].split("=")[1];
	var goDate = tripArr[1].split("=")[1];
	var returnDate = tripArr[2].split("=")[1];


	// date form : 2015-03-23

	// alert(destination);
	// console.log(goDate);
	// console.log(returnDate);
	// console.log(tripArr);
	// console.log(temp);


} 