let inputName = document.querySelector("input[name=name]"),
    inputSurName = document.querySelector("input[name=surname]"),
    inputMail = document.querySelector("input[name=mail]"),
    inputPhone = document.querySelector("input[name=phone]"),
    selectAuto = document.querySelector('#selectAuto'),
    selectTime = document.querySelector('#selectTime'),
    buttonSubmit = document.querySelector("button[type=submit]")

inputName.addEventListener('blur', () => {
    if(inputName.value.length == 0){
        return inputName.parentNode.style.borderBottom = "2px solid #c62f2d"
    }else if(inputName.value.length > 200){
        return inputName.parentNode.style.borderBottom = "2px solid #c62f2d"
    }

    return inputName.parentNode.style.borderBottom = "2px solid #22a221"
})

inputSurName.addEventListener('blur', () => {
    if(inputSurName.value.length == 0){
        return inputSurName.parentNode.style.borderBottom = "2px solid #c62f2d"
    }else if(inputSurName.value.length > 200){
        return inputSurName.parentNode.style.borderBottom = "2px solid #c62f2d"
    }

    return inputSurName.parentNode.style.borderBottom = "2px solid #22a221"
})

inputMail.addEventListener('blur', () => {
    if(!(/^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/.test(inputMail.value))){
        //inputMail.parentNode.classList.remove('focus');
        return inputMail.parentNode.style.borderBottom = "2px solid #c62f2d"
    }else if(inputMail.value.length > 200){
        return inputMail.parentNode.style.borderBottom = "2px solid #c62f2d"
    }

    return inputMail.parentNode.style.borderBottom = "2px solid #22a221"
})

inputPhone.addEventListener('blur', () => {
    if(!(/^(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?$/.test(inputPhone.value))){
        //inputMail.parentNode.classList.remove('focus');
        return inputPhone.parentNode.style.borderBottom = "2px solid #c62f2d"
    }else if(inputPhone.value.length > 200){
        return inputPhone.parentNode.style.borderBottom = "2px solid #c62f2d"
    }

    return inputPhone.parentNode.style.borderBottom = "2px solid #22a221"
})
/*
buttonSubmit.addEventListener('submit', function(){
    console.log(selectAuto.value)
    if((selectAuto.value == "None") || (!selectAuto.value)){
        selectAuto.parentNode.style.borderBottom = "2px solid #c62f2d"
        console.log('123')

    }
    return false
})
*/
function SubmitForm(){
    if((selectAuto.value == "None") || (!selectAuto.value)){
        selectAuto.parentNode.style.borderBottom = "2px solid #c62f2d"
        return false
    }else{
        selectAuto.parentNode.style.borderBottom = "2px solid #22a221"
    }
    if((selectTime.value == "None") || (!selectTime.value)){
        selectTime.parentNode.style.borderBottom = "2px solid #c62f2d"
        return false
    }else{
        selectTime.parentNode.style.borderBottom = "2px solid #22a221"
    }

    return true
}
