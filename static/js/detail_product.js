function getCartData(){
  return JSON.parse(localStorage.getItem('cart'));
}

function setCartData(o){
  localStorage.setItem('cart', JSON.stringify(o));
  return false;
}

function addToCart(e, count){
	var cartData = getCartData() || {},
		itemSlug = e.target.getAttribute('data-slug')
		itemNode = e.target.parentNode.parentNode.parentNode;
		itemTitle = itemNode.getElementsByClassName('itemTitle')[0].innerHTML,
		itemPrice = itemNode.getElementsByClassName('itemPrice')[0].innerHTML,
		itemPicture = itemNode.getElementsByClassName('itemPicture')[0].getAttribute('src')

	if(cartData.hasOwnProperty(itemSlug) && (cartData[itemSlug] != null)){
		cartData[itemSlug][3] += Number(count)
	}else{
		cartData[itemSlug] = [itemTitle, itemPrice, itemPicture, Number(count)]
	}
	setCartData(cartData)

	popOutMessage('Товар добавлен в корзину')
}

let toCart = document.querySelector('#toCart')
let inputCount = document.querySelector('#quantity')
toCart.addEventListener('click', function(e){
    console.log(inputCount.value)
    addToCart(e, inputCount.value)
})

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