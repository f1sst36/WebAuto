function productTabsInfo() {

    let buttons = document.querySelectorAll('.info_btn');

    buttons.forEach(function(button){

        button.addEventListener('click', function(event) {

            let active_btn = document.querySelector('.active_btn');
            let prod_tabs_active = document.querySelector('.prod_tabs_active');

            let prod_more_inf = document.querySelector('.prod_more_inf');
            let prod_feature = document.querySelector('.prod_feature');
            let prod_review = document.querySelector('.prod_review');

            active_btn.classList.remove('active_btn');
            button.classList.add('active_btn');

            prod_tabs_active.classList.remove('prod_tabs_active');

            if (button.id == 'btn_more'){
                prod_more_inf.classList.add('prod_tabs_active');
            } else if(button.id == 'btn_feature') {
                prod_feature.classList.add('prod_tabs_active');
            } else {
                prod_review.classList.add('prod_tabs_active');
            }
        });
    });

}

productTabsInfo();
