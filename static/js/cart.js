function getCartData(){
  return JSON.parse(localStorage.getItem('cart'));
}

function setCartData(o){
  localStorage.setItem('cart', JSON.stringify(o));
  return false;
}

function OpenCart(){
	let cartData = getCartData(),
		cartItemsNode = document.querySelector('#cartItems'),
		totalPrice = document.querySelector('.total-price-number'),
		productsPrice = document.querySelector('.products-price'),
		price = 0,
		template

	cartItemsNode.innerHTML = ''
	if(cartData != null){
		for(var item in cartData){
			if(cartData[item] == null) continue;
			template = `
				<div class="items-holder">
					<div class="row cart-item">
			    		<div class="col-lg-2">
			    			<div class="item-picture">
			    				<img src="${cartData[item][2]}" alt="">
			    			</div>
			    		</div>
			    		<div class="col-lg-4">
			    			<div class="item-name">
			    				<a href="#">${cartData[item][0]}</a>
			    			</div>
			    		</div>
			    		<div class="col-lg-3">
			    			<div class="item-count">
			    				<button>+</button>
				    			<input type="text" value="${cartData[item][3]}" readonly>
				    			<button>-</button>
			    			</div>
			    		</div>
			    		<div class="col-lg-3">
			    			<div class="item-price">
			    				<p>${cartData[item][1]}</p>
			    				<i style="cursor: pointer;" class="fa fa-times RemoveItem" aria-hidden="true" data-key="${item}"></i>
			    			</div>
			    		</div>
			    	</div>
				</div>
			`

            price += Number(cartData[item][1].replace('₽', '')) * Number(cartData[item][3])
			cartItemsNode.insertAdjacentHTML('beforeend', template)
		}


		totalPrice.innerHTML = (price + 400) + '₽'
        productsPrice.innerHTML = price + '.00₽'
	}

	if(cartItemsNode.innerHTML == ''){
        template = `
            <h4>В корзине пусто</h4>
        `
        cartItemsNode.insertAdjacentHTML('beforeend', template)
    }

	let itemHolders = document.getElementsByClassName('items-holder')
	for(let i = 0; i < itemHolders.length; i++){
		itemHolders[i].querySelector('.RemoveItem').addEventListener('click', RemoveCartItem)
	}
}

OpenCart();

function RemoveCartItem(e){
	let cartData = getCartData()
	cartData[this.getAttribute('data-key')] = null
	setCartData(cartData)

	OpenCart();
}
