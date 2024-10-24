function validateForm() {
    var username = document.getElementById('username').value;
    var usernamePattern = /^[a-zA-Z0-9_]{5,20}$/;

    if(usernamePattern.test(username)) {
        return true;

    }else{
        alert('wrong username Pattren'); 
    }

}