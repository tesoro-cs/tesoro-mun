window.setInterval(function() {
    if(window.scrollY > 10){
        if (document.getElementById("navigation").className.includes("colored") == false) {
            document.getElementById("navigation").classList.add("colored");
        }
    }
    else {
        if (document.getElementById("navigation").className.includes("colored") == true) {
            document.getElementById("navigation").classList.remove("colored");
        }
    }
},100);
