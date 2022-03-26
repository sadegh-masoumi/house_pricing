let modal = document.querySelector(".modal");
let apartment_list = document.querySelector(".apartment-list");

function showSearchForm() {
    modal.classList.add('visible');
    apartment_list.classList.add('blur');
}

function hideSearchForm() {
    modal.classList.remove('visible');
    apartment_list.classList.remove('blur');
}

document.getElementById('search').addEventListener('click', showSearchForm)
document.getElementById('close-search').addEventListener('click', hideSearchForm)

