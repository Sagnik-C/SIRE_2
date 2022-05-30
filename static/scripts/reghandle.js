// alert("hi there!");
function validatelogin() {
    form = document.forms["regform"];
    username = form["username"].value;
    fname = form["fname"].value;
    lname = form["lname"].value;
    mail = form["email"].value;
    pass1 = form["pass1"].value;
    pass2 = form["pass2"].value;

    if(username.length>10){
        alert("Username should be limited to 10 characters");
        return false;
    }
    if(username=="" || fname=="" || lname=="" || mail=="" || pass1=="" || pass2==""){
        alert("All field are required!");
        return false;
    }
    for (var i = 0; i < username.length; i++) {
        var char1 = username.charAt(i);
        var cc = char1.charCodeAt(0);

        if ((cc > 47 && cc < 58) || (cc > 64 && cc < 91) || (cc > 96 && cc < 123)) {
        } else {
            alert("Input is not alphanumeric");
            return false;
        }
    }
    if(pass1 != pass2){
        alert("Passwords do not match!");
        return false;
    }
    if(pass1.length<8){
        alert("Password must contain atleast 8 characters!");
        return false;
    }
    form.submit();
    return true;
}