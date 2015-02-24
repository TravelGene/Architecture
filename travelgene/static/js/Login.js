



function logfbpup(){
  // window.open("logfb.html", "", "toolbar=no, height=300,width=500, top=200, left=400");
  // return false;
  document.getElementById("signin").style.display="none";
  document.getElementById("view-signin").style.display="none";
  document.getElementById("view-signup").style.display="block";
}


function openpopin(){
	document.getElementById("popupsign").style.display="block";
	document.getElementById("view-signin").style.display="block";
	document.getElementById("view-signup").style.display="none";
	document.getElementById("overlay").style.display="block";
  document.getElementById("signin").style.display="block";
//    document.getElementById("logPart").src="static/img/LogPart2.png";
  // document.getElementById("logPart").style.height="180px";
}
// function openpopup(){
// 	document.getElementById("popupsign").style.display="block";
// 	document.getElementById("overlay").style.display="block";
// 	document.getElementById("view-signup").style.display="block";
// 	document.getElementById("view-signin").style.display="none";
//   // document.getElementById("logPart").src="img/LogPart.png";
//   // document.getElementById("logPart").style.height="300px";
// }

function closepop(){
	document.getElementById("popupsign").style.display="none";
	document.getElementById("overlay").style.display="none";

}

function getAccount(){
  document.getElementById("popupsign").style.display="none";
  document.getElementById("account").style.display="block";
  document.getElementById("siin").style.display="none";
  document.getElementById("siup").style.display="none";
  document.getElementById("overlay").style.display="none";

}

function login(){
  document.getElementById("popupsign").style.display="none";
  document.getElementById("account").style.display="block";
  document.getElementById("siin").style.display="none";
  document.getElementById("siup").style.display="none";
  document.getElementById("overlay").style.display="none";
  var x=document.getElementById("username_in").value;
  var y=document.getElementById("userpwd_in").value;




}



//to judge the input of login and sigin in column

    var _pass;

    //---------------------------------------------------------------------------
    function checkUsername(){
     var username;
     username = document.getElementById('username_in').value;

     if (username == "") {
      document.getElementById('username_error').innerHTML = "Please input your name";
      document.getElementById('username_in').style.border="1px solid red";
      } else {
       if (/^\w{1,10}$/.test(username)) {
        document.getElementById('username_error').innerHTML = "";
        document.getElementById('username_in').style.border="1px solid #ccc";
        } else {
        document.getElementById('username_error').innerHTML = "Only[0-9][a-z-A-Z]within 1~10 length";
        document.getElementById('username_in').style.border="1px solid red";
        }
     }
    }
    function checkEmail(){
     var email;
     email = document.getElementById('email_up').value;
     
     if (email == "") {
      document.getElementById('email_error').innerHTML = "Please input your Email";
      document.getElementById('email_up').style.border="1px solid red";
      } else {
       if (/^[\w-]+[\.]*[\w-]+[@][\w\-]{1,}([.]([\w\-]{1,})){1,3}$/.test(email)) {
        document.getElementById('email_error').innerHTML = "";
        document.getElementById('email_up').style.border="1px solid #ccc";
        } else {
        document.getElementById('email_error').innerHTML = "Invalid Email Address";
        document.getElementById('email_up').style.border="1px solid red";
        }      
      }
     }


    function checkPwd(){
     var pass;
     pass = document.getElementById('userpwd_in').value;


 
     if (pass == "") {
      document.getElementById('userpwd_error').innerHTML = "Please input the password";
      document.getElementById('userpwd_in').style.border="1px solid red";

      } else {
       if (/^\w{6,20}$/.test(pass)) {
        document.getElementById('userpwd_error').innerHTML = "";
        document.getElementById('userpwd_in').style.border="1px solid #ccc";
        } else {
        document.getElementById('userpwd_error').innerHTML = "Only[0-9][a-z-A-Z]within 6~20 length";
        document.getElementById('userpwd_in').style.border="1px solid red";
        }      
      }
     }

  
    function checkUserName2(){
     var username;
     username = document.getElementById('username_up').value;

     if (username == "") {
      document.getElementById('username2_error').innerHTML = "Please input your name";
      document.getElementById('username_up').style.border="1px solid red";
      } else {
       if (/^\w{1,10}$/.test(username)) {
        document.getElementById('username2_error').innerHTML = "";
        document.getElementById('username_up').style.border="1px solid #ccc";
        } else {
        document.getElementById('username2_error').innerHTML = "Only[0-9][a-z-A-Z]within 1~10 length";
        document.getElementById('username_up').style.border="1px solid red";
        }
     }
    }

    function checkPwdUp(){
     var pass;
     pass = document.getElementById('userpwd_up').value;
     rpass = document.getElementById('ruserpwd_up').value;
     _pass = pass;
 	 if(rpass==""){
      if (pass == "") {
      document.getElementById('pwd_error').innerHTML = "Please input the password";
      document.getElementById('userpwd_up').style.border="1px solid red";

      } else {
       if (/^\w{6,20}$/.test(pass)) {
        document.getElementById('pwd_error').innerHTML = "";
        document.getElementById('userpwd_up').style.border="1px solid #ccc";
        } else {
        document.getElementById('pwd_error').innerHTML = "Only[0-9][a-z-A-Z]within 6~20 length";
        document.getElementById('userpwd_up').style.border="1px solid red";
        }      
      }
  	 }else if(pass!=rpass){
  	  document.getElementById('rpwd_error').innerHTML = "Password missmatch";
      document.getElementById('ruserpwd_up').style.border="1px solid red";
      document.getElementById('userpwd_up').style.border="1px solid red";
  	 }else{
  	  document.getElementById('rpwd_error').innerHTML = "";
  	  document.getElementById('ruserpwd_up').style.border="1px solid #ccc";
      document.getElementById('userpwd_up').style.border="1px solid #ccc";
  	 }
    }



    function checkRPwdUp(){
     var rpass;
     rpass = document.getElementById('ruserpwd_up').value;
     
     if (rpass == "") {
      document.getElementById('rpwd_error').innerHTML = "Reinput the password";
      document.getElementById('ruserpwd_up').style.border="1px solid red";
      } 
     else if (rpass != _pass) {
      document.getElementById('rpwd_error').innerHTML = "Password missmatch";
      document.getElementById('ruserpwd_up').style.border="1px solid red";
      document.getElementById('userpwd_up').style.border="1px solid red";
      }
     else {
      document.getElementById('rpwd_error').innerHTML = "";
      document.getElementById('ruserpwd_up').style.border="1px solid #ccc";
      document.getElementById('userpwd_up').style.border="1px solid #ccc";
      }    
     }


function signUp(){
  alert("hahha");
  




}

     

     

