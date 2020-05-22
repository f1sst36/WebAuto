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

let under_slider_blocks = document.getElementsByClassName('under_slider_block');
under_slider_blocks = [...under_slider_blocks];

function openBlock(e){
	if(e.target.dataset.name == "block_main"){
		e.target.dataset.name = "block_main_none";

		animateCSS(e.target.nextElementSibling, 'zoomOutDown', 'fast', function(){
			e.target.nextElementSibling.style.display = 'none';
		});

		e.target.nextElementSibling.nextElementSibling.style.zIndex = 2;
		e.target.nextElementSibling.style.zIndex = 1;
		e.target.nextElementSibling.nextElementSibling.style.display = 'block';
		animateCSS(e.target.nextElementSibling.nextElementSibling, 'zoomInUp', 'fast', function(){
			e.target.dataset.name = "block_main";
			if(e.target.dataset.status == 'true'){
				closeBlock(e);
			}
		});
	}
}

function closeBlock(e){
	e.target.dataset.status = 'true';
	if(e.target.dataset.name == "block_main"){	
		e.target.dataset.name = "block_main_none";

		animateCSS(e.target.nextElementSibling.nextElementSibling, 'zoomOutUp', 'fast', function(){
			e.target.nextElementSibling.nextElementSibling.style.display = 'none';
		});

		e.target.nextElementSibling.style.zIndex = 2;
		e.target.nextElementSibling.nextElementSibling.style.zIndex = 1;
		e.target.nextElementSibling.style.display = 'block';
		animateCSS(e.target.nextElementSibling, 'zoomInDown', 'fast', function(){
			e.target.dataset.name = "block_main";
			e.target.dataset.status = 'false';
		});
	}
}

document.querySelector('#under_slider_blocks').addEventListener('mouseover', function(e){
	openBlock(e);
})

document.querySelector('#under_slider_blocks').addEventListener('mouseout', function(e){
	closeBlock(e);
})
