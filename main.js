window.setInterval(function() {
    if(window.scrollY > 10 || document.getElementById("menu-small") != null){
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

let x = document.getElementsByClassName("leader");
for (var i = 0; i < x.length; i++){
    x[i].childNodes[5].childNodes[0].addEventListener("click", function(e){
        if (e.target.id =="contact-isa"){
            window.location="mailto:test@test.com";
        }
        else if (e.target.id =="contact-gabriel"){
            window.location="mailto:test@test.com";
        }
        else if (e.target.id =="contact-daniel"){
            window.location="mailto:test@test.com";
        }
        else if (e.target.id =="contact-armin"){
            window.location="mailto:test@test.com";
        }
    });
}
document.getElementById("hamburger").addEventListener("click", function(){
    if (document.getElementById("menu-small") == null){
        var nav = document.getElementById("navigation");
        var hamburger = document.getElementById("hamburger");
        nav.classList.add("colored");
        hamburger.className = "fa fa-close menu-item";
        el = document.createElement("div");
        el.id="menu-small";
        el.innerHTML = hamburger.parentNode.innerHTML;
        el.lastChild.remove();
        el.lastChild.remove();
        document.getElementById("navigation").parentNode.appendChild(el);
    }
    else{
        var hamburger = document.getElementById("hamburger");
        document.getElementById("menu-small").remove();
        hamburger.className = "fa fa-bars menu-item";
    }
});