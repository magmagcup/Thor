start = () => {
    var x = document.getElementById("start");
    setTimeout(function() { x.value="1"}, 1000);
    setTimeout(function() { x.value="2"}, 2000);
    setTimeout(function() { x.value="3"}, 3000);
    setTimeout(function() { x.value="start"}, 4000);
}