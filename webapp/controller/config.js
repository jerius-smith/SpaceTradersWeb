function updateSkillPoints() {
    var ment = document.getElementById('config_player')
    document.getElementById("rem_skills").innerHTML = 16 - sumSkills();
}

function sumSkills(){
    var ment = document.getElementById('config_player')
    var pilotPoints = (parseInt(ment.elements.namedItem('pilot_points').value) || 0);
    var fighterPoints =(parseInt(ment.elements.namedItem('fighter_points').value) || 0);
    var traderPoints = (parseInt(ment.elements.namedItem('trader_points').value) || 0);
    var engineerPoints = (parseInt(ment.elements.namedItem('engineer_points').value) || 0);

    sum = pilotPoints + fighterPoints + traderPoints + engineerPoints;

    document.getElementById('pilotPoint').setAttribute('max', 16 - sum + pilotPoints);
    document.getElementById('engineerPoint').setAttribute('max', 16 - sum + engineerPoints);
    document.getElementById('fighterPoint').setAttribute('max', 16 - sum + fighterPoints);
    document.getElementById('traderPoint').setAttribute('max', 16 - sum + traderPoints);
    return sum
}

function newPlayer() {
    if (sumSkills() == 16) {
        var xhttp = new XMLHttpRequest();
        var player = document.getElementById("config_player");

        var player_info = {
            "name": player.elements.namedItem('player_name').value,
            "prefDifficulty": player.elements.namedItem('prefDifficulty').value,
            "skillPoints": {
                "pilot_points": parseInt(player.elements.namedItem('pilot_points').value),
                "fighter_points": parseInt(player.elements.namedItem('fighter_points').value),
                "trader_points": parseInt(player.elements.namedItem('trader_points').value),
                "engineer_points": parseInt(player.elements.namedItem('engineer_points').value)
            }
        };

        console.log("Creating player: " + player_info);

        sessionStorage.setItem("current_name", player.elements.namedItem('player_name').value);
        xhttp.onreadystatechange = function () {
            if (xhttp.readyState == 4) {
                if (xhttp.status == 200) {
                    window.location.href = "../view/welcome.html";
                }
            }
        };
        req = {
            "email": sessionStorage.getItem("email"),
            "pswrd": sessionStorage.getItem("pswrd"), 'data': player_info
        };
        xhttp.open("POST", "https://287b63b6.ngrok.io/create_new_player", true);
        xhttp.setRequestHeader("Access-Control-Allow-Origin", '*');
        xhttp.send(JSON.stringify(req));
    } else if (sumSkills() < 16) {
        window.alert("Please use all 16 skill points.")
    } else {
        window.alert("You can only use 16 skill points.")
    }
}

function loadExisting() {
    window.location.href = "../view/load_existing.html"
}
