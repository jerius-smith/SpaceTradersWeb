window.onload = function () {
    document.getElementById('welcome_txt').innerHTML =
        "Welcome " + sessionStorage.getItem("current_name")
        + "!\nWe're excited you have "
        + "decided to begin your \n"
        + " journey through the Space Trader Universe!"
};