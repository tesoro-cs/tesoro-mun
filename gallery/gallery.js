var currentSlide = 1;
var slides = document.getElementsByClassName("slide");
var thumbs = document.getElementsByClassName("thumbnail");
show(currentSlide);

function next() {
    currentSlide+=1;
    show(currentSlide);
}

function prev() {
    currentSlide-=1;
    show(currentSlide);
}

function show(slide) {
    if(slide > slides.length) {
        slide = 1;
    } else if(slide < 1) {
        slide = slides.length
    }
    currentSlide = slide;
    
    for(var i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slide-1].style.display = "block";
    document.getElementById("caption").innerHTML = thumbs[slide-1].alt;
}