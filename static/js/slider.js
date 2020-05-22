function animateCSS(element, animationName, speed, callback) {
    const node = element
    node.classList.add('animated', animationName, speed)

    function handleAnimationEnd() {
        node.classList.remove('animated', animationName)
        node.removeEventListener('animationend', handleAnimationEnd)

        if (typeof callback === 'function') callback()
    }

    node.addEventListener('animationend', handleAnimationEnd)
}

function slideImage(){
	clickSlide = false;
	if(currentI < 0) currentI = images.length - 1;
	if(currentI >= images.length) currentI = 0;

	previousI = currentI - 1;
	if(previousI >= images.length) previousI = 0;
	if(previousI <= -1) previousI = images.length - 1;
	
	animateCSS(images[previousI], 'slideOutLeft', 'fast', function(){
		images[previousI].style.visibility = 'hidden';
	})

	animateCSS(images[currentI], 'slideInRight', 'fast', function(){
		images[currentI - 1].style.visibility = 'visible';
		clickSlide = true;
	})

	currentI++;
}

function slideImageLeft(){
	clickSlide = false;
	if(currentI < 0) currentI = images.length - 1;
	if(currentI >= images.length) currentI = 0;

	previousI = currentI + 1;
	if(previousI >= images.length) previousI = 0;
	if(previousI <= -1) previousI = images.length - 1;

	animateCSS(images[previousI], 'slideOutRight', 'fast', function(){
		images[previousI].style.visibility = 'hidden';
	})

	animateCSS(images[currentI], 'slideInLeft', 'fast', function(){
		images[currentI + 1].style.visibility = 'visible';
		clickSlide = true;
	})

	currentI--;
}

let images = [...document.getElementsByClassName('slider_img')],
	slider = false,
	clickSlide = true;

var currentI = 0, previousI = 0;
let interval = setInterval(function(){
	slideImage();
}, 7000);

document.getElementById('main_header').addEventListener('mouseover', function(e){
	clearInterval(interval);
	slider = true;
});

document.getElementById('main_header').addEventListener('mouseout', function(e){
	if(slider){
		interval = setInterval(function(){
			slideImage();
		}, 7000);
		slider = false;
	}
});

document.getElementsByClassName('arr_right')[0].addEventListener('click', function(){
	if(clickSlide) slideImage();
})

document.getElementsByClassName('arr_left')[0].addEventListener('click', function(){
	if(clickSlide) slideImageLeft();
})


window.addEventListener('blur', function(){
	clearInterval(interval);
	slider = true;
})

window.addEventListener('focus', function(){
	if(slider){
		interval = setInterval(function(){
			slideImage();
		}, 7000);
		slider = false;
	}
})