var time = 1;
let is_running = false;
let score = 0;
document.getElementById("end").style.display = "none";
document.getElementById("button1").style.display = "none";

start = function () {
    is_running = true;
    if (is_running) {
        let interval = setInterval(start = function() {
        if (!is_running) {
            clearInterval(interval);
            document.getElementById("button1").style.display = "none";
        } else {
            document.getElementById("countdown").innerHTML = time + " second remaining";
            time++;
        }
        }, 1000)
        document.getElementById("button1").style.display = "inline";
        document.getElementById("start").style.display = "none";
    }
}

stop = function() {
    is_running = false;
    time = 1;
    document.getElementById("countdown").innerHTML = "Game Over";
    document.getElementById("end").style.display = "inline";
}