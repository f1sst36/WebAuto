var itemBoxs = document.querySelectorAll('.item');

function getCartData(){
  return JSON.parse(localStorage.getItem('cart'));
}

function setCartData(o){
  localStorage.setItem('cart', JSON.stringify(o));
  return false;
}

function addEvent(elem, type, handler){
	if(elem.addEventListener){
		elem.addEventListener(type, handler, false);
	} else {
		elem.attachEvent('on'+type, function(){ handler.call( elem ); });
	}
	return false;
}

for(var i = 0; i < itemBoxs.length; i++){
	addEvent(itemBoxs[i].querySelector('.cartPlus'), 'click', addToCart);
}

function addToCart(e){
	var cartData = getCartData() || {},
		itemSlug = e.target.getAttribute('data-slug')
		itemNode = e.target.parentNode.parentNode.parentNode.parentNode.parentNode;
		itemTitle = itemNode.getElementsByClassName('itemTitle')[0].innerHTML,
		itemPrice = itemNode.getElementsByClassName('itemPrice')[0].innerHTML,
		itemPicture = itemNode.getElementsByClassName('itemPicture')[0].getAttribute('src')

	if(cartData.hasOwnProperty(itemSlug) && (cartData[itemSlug] != null)){
		cartData[itemSlug][3]++
	}else{
		cartData[itemSlug] = [itemTitle, itemPrice, itemPicture, 1]
	}
	setCartData(cartData)

	popOutMessage('Товар добавлен в корзину')
}

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

var popOutBool = true
function popOutMessage(text){
	if( !popOutBool ) return
	popOutBool = false
	let element = document.querySelector('#pop-out')
	element.innerHTML = text
	element.style.display = 'block'
	animateCSS(element, 'bounceInLeft', 'fast', function(){
		setTimeout(function(){
			animateCSS(element, 'bounceOutLeft', 'fast', function(){
				element.style.display = 'none'
				popOutBool = true
			})
		}, 5000)
	})
}
