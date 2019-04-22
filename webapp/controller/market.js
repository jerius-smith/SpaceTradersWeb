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
                getItems();
            }
        }
    };

    xhttp_cred.open("GET", "https://1331a9f2.ngrok.io/get_credits/" + sessionStorage.getItem("email") , true);
    xhttp_cred.setRequestHeader("Access-Control-Allow-Origin", '*');
    xhttp_cred.send();
};


function getItems() {
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4) {
            if (xhttp.status == 200) {
                data = JSON.parse(xhttp.response);
                var res = "";
                for (var key in data) {
                    res += "<option value=" + key.toString() + "><tr>" +
                        "    <td>" + key.toString() + ",    </td>" +
                        "    <td>" + data[key][0] + ",    </td>" +
                        "    <td>" + data[key][1] + ",    </td>" +
                        "    <td>" + data[key][2] + "    </td>" +
                        "  </tr></option>";
                }
                document.getElementById("items").innerHTML = res;
            }
        }
    };

    xhttp.open("GET", "https://1331a9f2.ngrok.io/get_inventories/" + sessionStorage.getItem("email") , true);
    xhttp.setRequestHeader("Access-Control-Allow-Origin", '*');
    xhttp.send();
}

function sellItem() {
    var xhttp = new XMLHttpRequest();

    item = document.getElementById("market").elements.namedItem("items").value;

    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4) {
            if (xhttp.status == 200) {
                if (xhttp.responseText.substring(1, 4) == "You" ) {
                    window.alert(xhttp.responseText);
                } else {
                    getItems();
                    document.getElementById("credits").innerText = "Credits: " + xhttp.responseText;
                }
            }
        }
    };

    xhttp.open("POST", "https://1331a9f2.ngrok.io/sell_item/" + sessionStorage.getItem("email"), true);
    xhttp.setRequestHeader("Access-Control-Allow-Origin", '*');
    xhttp.send(JSON.stringify(item));
}

function buyItem() {
    var xhttp = new XMLHttpRequest();

    item = document.getElementById("market").elements.namedItem("items").value;

    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4) {
            if (xhttp.status == 200) {
                if (xhttp.responseText.substring(1, xhttp.responseText.length - 2) == "Item is out of stock.") {
                    window.alert(xhttp.responseText);
                } else if (xhttp.responseText.substring(1, xhttp.responseText.length - 2) == "You do not have enough credits.") {
                    window.alert(xhttp.responseText);
                } else {
                    getItems();
                    document.getElementById("credits").innerText = "Credits: " + xhttp.responseText;
                }
            }
        }
    };

    xhttp.open("POST", "https://1331a9f2.ngrok.io/buy_item/" + sessionStorage.getItem("email"), true);
    xhttp.setRequestHeader("Access-Control-Allow-Origin", '*');
    xhttp.send(JSON.stringify(item));
}

