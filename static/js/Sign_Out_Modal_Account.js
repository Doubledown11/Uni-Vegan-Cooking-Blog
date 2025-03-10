// JavaScript Code for the Sign-Out Modal  


document.addEventListener('DOMContentLoaded', function () {

    console.log('JavaScript for modal has opened')

    // Get Modal 
    let _modal = document.getElementById('logout_modal_account');


    // Get button
    let sign_out_button = document.getElementById('header_button_modal_account');


    // When button is clicked, modal opens 
    sign_out_button.addEventListener('click', function () {
        //modal_.classList.toggle('logout_modal_open');
        _modal.style.display = 'block';
    });



    // Get the span which closes the modal 
    let close_modal = document.getElementById('close_signout_modal_account');


    // When span clicked, modal closes
    close_modal.addEventListener('click', function () {
        _modal.style.display = 'none';
    });

    // Users clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == _modal) {
            _modal.style.display = 'none';
        }; 
    };
});
