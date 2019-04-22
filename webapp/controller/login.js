function newUser() {
    var xhttp = new XMLHttpRequest();
    var user = document.getElementById("user_creds");

    sessionStorage.setItem("email", user.elements.namedItem('email').value);
    sessionStorage.setItem("pswrd", user.elements.namedItem('pswrd').value);
    console.log("Creating new user...");

    req = {"email": sessionStorage.getItem("email"),
        "pswrd": sessionStorage.getItem("pswrd")};

    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4) {
            if (xhttp.status == 200) {
                window.location.href = "../view/config.html";
            }
        }
    };

    xhttp.open("POST", "https://287b63b6.ngrok.io/new_user", true);
    xhttp.send(JSON.stringify(req));
}

function loginUser() {
    var user = document.getElementById("user_creds");
    if (user.elements.namedItem('pswrd').value.length >= 6) {

        var xhttp = new XMLHttpRequest();

        sessionStorage.setItem("email", user.elements.namedItem('email').value);
        sessionStorage.setItem("pswrd", user.elements.namedItem('pswrd').value);

        req = {
            "email": sessionStorage.getItem("email"),
            "pswrd": sessionStorage.getItem("pswrd")
        };

        console.log("Logging in...");
        xhttp.open("POST", "https://287b63b6.ngrok.io/login", true);
        xhttp.setRequestHeader("Access-Control-Allow-Origin", '*');
        xhttp.send(JSON.stringify(req));
        console.log(xhttp.responseText);
        window.location.href = "../view/config.html";
    } else {
        window.alert("Password must be greater than 5 characters.");
    }
}
