// JavaScript Code for the Sign-Out Modal  


document.addEventListener('DOMContentLoaded', function () {

    console.log('JavaScript for modal has opened')

    // Get Modal 
    modal_ = document.getElementById('logout_modal');

    // Get button
    sign_out_button = document.getElementById('header_button_modal');

    // When button is clicked, modal opens 
    sign_out_button.addEventListener('click', function () {
        // modal.style.display='block';
        modal_.classList.toggle('logout_modal_open');
        modal_.style.display = 'block';
    });

    // Get the span which closes the modal 
    close_modal = document.getElementById('close_modal');

    // When span clicked, modal closes
    close_modal.addEventListener('click', function () {
        modal_.style.display='none';
    });

    // Users clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal_) {
            modal_.style.display = 'none';
        }; 
    };
});
