let Fio = document.querySelector("#FIO")
let IIN = document.querySelector("#IIN")
let Phone = document.querySelector("#Phone")
let Birthday = document.querySelector("#Birthday")
let SelectEducation = document.querySelector("#education")
let BirthPlace = document.querySelector("#BirthPlace")
let email = document.querySelector("#email")
let Dolzhnost = document.querySelector("#Dolzhnost")


IIN.onchange = function () {
    httpGet("IIN=" + IIN.value)
}

Fio.onchange = function () {
    httpGet("IIN=" + IIN.value + "&" + "FIO=" + Fio.value)
}

Phone.onchange = function () {
    httpGet("IIN=" + IIN.value + "&" + "Phone=" + Phone.value)
}

Birthday.onchange = function () {
    httpGet("IIN=" + IIN.value + "&" + "Birthday=" + Birthday.value)
}

SelectEducation.onchange = function () {
    httpGet("IIN=" + IIN.value + "&" + "SelectEducation=" + SelectEducation.value)
}

BirthPlace.onchange = function () {
    httpGet("IIN=" + IIN.value + "&" + "BirthPlace=" + BirthPlace.value)
}

email.onchange = function () {
    httpGet("IIN=" + IIN.value + "&" + "email=" + email.value)
}

Dolzhnost.onchange = function () {
    httpGet("IIN=" + IIN.value + "&" + "Dolzhnost=" + Dolzhnost.value)
}

function httpGet(url) {
    let xmlHttp = new XMLHttpRequest()

    xmlHttp.open("POST", JSON.stringify(url), false)
    xmlHttp.send(null)
    return xmlHttp.responseText
}
