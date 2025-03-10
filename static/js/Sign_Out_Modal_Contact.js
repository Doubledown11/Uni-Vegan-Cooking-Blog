// JavaScript Code for the Sign-Out Modal  


document.addEventListener('DOMContentLoaded', function () {

    console.log('JavaScript for sign out modal on Contact has opened')

    // Get Modal 
    let _modal = document.getElementById('logout_modal_contact'); 
    if (_modal) {
        console.log('_modal on contact found');
    };



    // Get button
    let sign_out_button_ = document.getElementById('header_button_modal_contact');
    if (sign_out_button_) {
        console.log('sign_out_button_ on contact found');
    };


    // When button is clicked, modal opens 
    sign_out_button_.addEventListener('click', function () {
        _modal.style.display = 'block';
        console.log('sign_out_button_ on contact event click captured');
    });



    // Get the span which closes the modal 
    let close_modal_ = document.getElementById('close_modal_contact');



    // When span clicked, modal closes
    close_modal_.addEventListener('click', function () {
        _modal.style.display = 'none';
    });


    // Users clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == _modal) {
            _modal.style.display = 'none';
        }; 
    };
});
