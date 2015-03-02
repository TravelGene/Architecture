function conveyTripInfo(){
	var destination = document.getElementById("destination").value;
	var goDate = document.getElementById("goDate").value;
	var returnDate = document.getElementById("returnDate").value;

	var myUrl = "CreateTrip.html" + "?" +  "destination=" + destination + "&goDate=" + goDate + "&returnDate=" + returnDate;
	window.location.assign(myUrl);

}