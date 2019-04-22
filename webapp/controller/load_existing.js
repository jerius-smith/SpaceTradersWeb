window.onload = function() {
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4) {
            if (xhttp.status == 200) {
                data = JSON.parse(xhttp.response);
                var res = "";
                for (var key in data) {
                    res += "<option value=" + key.toString() + ">" + data[key][0] + " (created on " + data[key][1] + ")</option>";
                }
                document.getElementById("players").innerHTML += res;
            }
        }
    };

    xhttp.open("GET", "http://localhost:5000/get_players/" + sessionStorage.getItem("email") , true);
    xhttp.setRequestHeader("Access-Control-Allow-Origin", '*');
    xhttp.send();
};

function deletePlayer() {
    var xhttp = new XMLHttpRequest();

    player = document.getElementById("load_players").elements.namedItem("players").value;

    xhttp.open("POST", "http://localhost:5000/delete_player/" + sessionStorage.getItem("email"), true);
    xhttp.setRequestHeader("Access-Control-Allow-Origin", '*');
    xhttp.send(JSON.stringify(player));

    window.location.href = "../view/load_existing.html";
}

function loadPlayer() {
    var xhttp = new XMLHttpRequest();

    player = document.getElementById("load_players").elements.namedItem("players").value;

    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4) {
            if (xhttp.status == 200) {
                data = xhttp.responseText;
                sessionStorage.setItem("current_name", data);
                console.log(sessionStorage.getItem("current_name"));

                window.location.href = "../view/welcome.html";
            }
        }
    };

    xhttp.open("POST", "http://localhost:5000/load_player/" + sessionStorage.getItem("email"), true);
    xhttp.setRequestHeader("Access-Control-Allow-Origin", '*');
    xhttp.send(JSON.stringify(player));
}
