icon = document.querySelector('.menuicon');
nav_bar = document.querySelector('.navbar2');
navbar2link = document.querySelector('.drop_down_link_');
navbar2dp = document.querySelector('.drop_down_menu_');

icon.addEventListener('click', () => {
    if (nav_bar.style.display == 'block') {
        nav_bar.style.display = 'none';
        navbar2dp.style.display = 'none';
    } else {
        nav_bar.style.display = 'block';
    }
});


navbar2link.addEventListener('click', () => {
    if (navbar2dp.style.display == 'block') {
        navbar2dp.style.display = 'none';
    } else {
        navbar2dp.style.display = 'block';
    }
});

function display_form_card(x) {
    card = document.querySelector('.select_card_body_' + x);
    list = document.querySelector('.select_form_card_' + x);
    list.style.display = 'block';
    card.style.display = 'none';
    console.log(x);
}

function display_card_body(x) {
    card = document.querySelector('.select_card_body_' + x);
    list = document.querySelector('.select_form_card_' + x);
    list.style.display = 'none';
    card.style.display = 'block';
    console.log(x);
}