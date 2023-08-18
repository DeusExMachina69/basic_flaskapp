const loginForm = document.getElementById('login_form');
const userName = document.getElementById('login_username'); 
const password = document.getElementById('login_password'); 

//control form submission 
loginForm.addEventListener('submit', function(e) {
    if (userName.value == null || userName.value == '' || password.value == null || password.value == '') {
        e.preventDefault()
    } else {
        e.submit();
    }
});