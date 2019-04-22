window.onload = function() {
    var xhttp = new XMLHttpRequest();

    req = {"email": sessionStorage.getItem("email"), "pswrd": sessionStorage.getItem("pswrd")};

    var data = " ";
    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4) {
            if (xhttp.status == 200) {
                data = xhttp.responseText;
                document.getElementById("location").innerText = "Location: " + data.substring(1, data.length-2);
            }
        }
    };

    xhttp.open("GET", "https://1331a9f2.ngrok.io/get_location/" + sessionStorage.getItem("email") , true);
    xhttp.setRequestHeader("Access-Control-Allow-Origin", '*');
    xhttp.send();

    var xhttp_cred = new XMLHttpRequest();

    xhttp_cred.onreadystatechange = function () {
        if (xhttp_cred.readyState == 4) {
            if (xhttp_cred.status == 200) {
                cred_data = xhttp_cred.responseText;
                document.getElementById("credits").innerText = "Credits: " + cred_data;
            }
        }
    };

    xhttp_cred.open("GET", "https://1331a9f2.ngrok.io/get_credits/" + sessionStorage.getItem("email") , true);
    xhttp_cred.setRequestHeader("Access-Control-Allow-Origin", '*');
    xhttp_cred.send();


};
