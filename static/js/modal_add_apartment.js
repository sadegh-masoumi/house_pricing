let modal_form = document.querySelector(".modal");
let manage = document.querySelector(".manage");

function showSearchForm() {
    modal_form.classList.add('visible');
    manage.classList.add('blur');
}

function hideSearchForm() {
    modal_form.classList.remove('visible');
    manage.classList.remove('blur');
}

document.getElementById('search').addEventListener('click', showSearchForm)
document.getElementById('close-search').addEventListener('click', hideSearchForm)

