function carEquipments() {

    let buttons = document.querySelectorAll('.car-button');

    buttons.forEach(function(button){

        button.addEventListener('click', function(event) {

            let active_btn = document.querySelector('.equipment_active_btn');
            let car_equipment_active = document.querySelector('.car_equipment_active');

            let car_body_design = document.querySelector('.car_body_design');
            let car_comfort = document.querySelector('.car_comfort');
            let car_dynamics_and_control = document.querySelector('.car_dynamics_and_control');

            //active_btn.classList.remove('active_btn');
            //button.classList.add('active_btn');

            if(car_equipment_active) {
                active_btn.classList.remove('equipment_active_btn');
                car_equipment_active.classList.remove('car_equipment_active');
            }

            button.classList.add('equipment_active_btn');

            if (button.id == 'design'){
                car_body_design.classList.add('car_equipment_active');
            } else if(button.id == 'comfort') {
                car_comfort.classList.add('car_equipment_active');
            } else {
                car_dynamics_and_control.classList.add('car_equipment_active');
            }
        });
    });

}

carEquipments();