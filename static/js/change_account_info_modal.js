// JavaScript Code for the Account Information Modal  


document.addEventListener('DOMContentLoaded', function () {

    console.log('JavaScript for account information modal has opened')

    // Get Modal 
    modal_ = document.getElementById('account_info_change_modal');

    // Get button
    account_change = document.getElementById('account_info_change_button');

    // When button is clicked, modal opens 
    account_change.addEventListener('click', function () {
        // modal.style.display='block';
        modal_.classList.toggle('change_account_modal_open');
        modal_.style.display = 'block';
    });

    // Get the span which closes the modal 
    close_modal = document.getElementById('close_account_change_modal');

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
