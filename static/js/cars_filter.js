const forms = document.querySelector('form[name=filter]');

forms.addEventListener('submit', function (e) {
    // Получаем данные из формы
    e.preventDefault();

    let url = this.action;
    let params = new URLSearchParams(new FormData(this)).toString();
    ajaxSend(url, params);
});

let html = `
{{#cars}}
    <div class="car-card">
        <div class="car-img-outer">
            <img class="car-img" src="/media/{{ poster }}" alt="">
            <div class="img-tile"></div>
        </div>
        <div class="car-title">
            <h3>AUDI {{ model }} {{ line }}</h3>
            <h5>от {{ price }} руб. вкл. НДС</h5>
        </div>
        <div class="car-button">
            <a href="/car/{{ slug }}"><i class="fa fa-angle-right" aria-hidden="true"></i> Обзор</a>
        </div>
    </div>
{{/cars}}`
