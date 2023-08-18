
//form element
const signUpForm = document.getElementById('signup_form');

//form validation 
const firstNameInput = document.getElementById('first_name'); 
const lastNameInput = document.getElementById('last_name'); 
const userNameInput = document.getElementById('user_name'); 
const emailInput = document.getElementById('email'); 
const passwordInput1 = document.getElementById('password_1'); 
const passwordInput2 = document.getElementById('password_2'); 


//password verification
const passwordDisplay = document.getElementById('password_check_display'); 
const passwordDisplayLength = document.getElementById('password_check_length'); 
const passwordDisplayNum = document.getElementById('password_check_num');
const passwordDisplaySpecialChar = document.getElementById('password_check_special_char'); 
const passwordDisplayCapital = document.getElementById('password_check_capital_char'); 
const passwordDisplayLowercase = document.getElementById('password_check_lowercase_char'); 
const passwordMatchMessage = document.getElementById('password_match_message'); 





//check password 1 requirements
function checkPassword() {
    let value = passwordInput1.value.trim();
    const minLength = 9; 
    const hasNum = /\d/.test(value);
    const hasSpecialChar = /[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]/.test(value); 
    const hasCapital = /[A-Z]/.test(value); 
    const hasLowercase = /[a-z]/.test(value); 

    const lenCheckBox = document.getElementById('len_checkbox'); 
    const numCheckBox = document.getElementById('num_checkbox'); 
    const specialCharCheckBox = document.getElementById('special_char_checkbox'); 
    const capitalCheckbox = document.getElementById('capital_checkbox'); 
    const lowercaseCheckbox = document.getElementById('lowercase_checkbox'); 

            
    if (value.length >= minLength) {
       lenCheckBox.style.color = 'green'; 
       passwordDisplayLength.style.backgroundColor = 'lightgreen'; 
    } else {
        lenCheckBox.style.color = 'red'; 
        passwordDisplayLength.style.backgroundColor = 'lightcoral';
    }
    if (hasNum) {
        numCheckBox.style.color = 'green'; 
        passwordDisplayNum.style.backgroundColor = 'lightgreen'; 
    } else {
        numCheckBox.style.color = 'red'; 
        passwordDisplayNum.style.backgroundColor = 'lightcoral'; 
    }
    if (hasSpecialChar) {
        specialCharCheckBox.style.color = 'green'; 
        passwordDisplaySpecialChar.style.backgroundColor = 'lightgreen'; 
    } else {
        specialCharCheckBox.style.color = 'red'; 
        passwordDisplaySpecialChar.style.backgroundColor = 'lightcoral'; 
    }
    if (hasCapital) {
        capitalCheckbox.style.color = 'green'; 
        passwordDisplayCapital.style.backgroundColor = 'lightgreen'; 
    } else {
        capitalCheckbox.style.color = 'red'; 
        passwordDisplayCapital.style.backgroundColor = 'lightcoral'; 
    }
    if (hasLowercase) {
        lowercaseCheckbox.style.color = 'green'; 
        passwordDisplayLowercase.style.backgroundColor = 'lightgreen'; 
    } else {
        lowercaseCheckbox.style.color = 'red'; 
        passwordDisplayLowercase.style.backgroundColor = 'lightcoral'; 
    }
    if (value.length >= minLength && hasNum && hasSpecialChar && hasCapital && hasLowercase) {
        return true;
    } else {
        return false; 
    }

}; 






//verify password matching 
function verifyPasswordMatch() {
    if (passwordInput1.value !== passwordInput2.value) {
        return false; 
    } 
    return true;     
};

//password message display collapse and expand function
function passwordDisplayCollapse() {
    passwordDisplay.style.visibility = 'hidden'; 
    passwordDisplay.style.position = 'absolute'; 
}; 

function passwordDisplayExpand() {
    passwordDisplay.style.visibility = 'visible'; 
    passwordDisplay.style.position = 'inherit'; 
}; 





//password 1 message popup function 
passwordInput1.addEventListener('focus', function(e) {
    passwordDisplayExpand();    
});
//password check event listener, handles styling of requirements as text is inputted 
passwordInput1.addEventListener('input', function(e) {
    checkPassword(); 
});
//password message collapse if unfocused 
passwordInput1.addEventListener('blur', function(e) {
    passwordDisplayCollapse(); 
});


//confirm password pop up box      
/*
passwordInput2.addEventListener('focus', function(e) {
    passwordMatchMessage.style.visibility = 'visible'; 
    passwordMatchMessage.style.position = 'inherit'; 
});*/

//verify password matching on input 
passwordInput2.addEventListener('input', function(e) {
    let pw1 = passwordInput1.value.trim();
    let pw2 = e.target.value.trim(); 
    //if password2 is empty dont show the box 
    if (pw2 == null || pw2 == '') {
        passwordMatchMessage.style.visibility = 'hidden'; 
        passwordMatchMessage.style.position = 'absolute'; 
    }
    //if the passwords match, indicate that they do, but not if they are empty
    if (pw1 === pw2) {
        if (pw2 === null || pw2 == '') {
            passwordMatchMessage.style.visibility = 'hidden'; 
            passwordMatchMessage.style.position = 'absolute';
        } else {
            passwordMatchMessage.style.visibility = 'visible';
            passwordMatchMessage.style.position = 'inherit';
            passwordMatchMessage.innerText = 'Passwords match.'
            passwordMatchMessage.style.backgroundColor = 'lightgreen';
        }
    } else {
        passwordMatchMessage.style.visibility = 'visible';
        passwordMatchMessage.style.position = 'inherit';
        passwordMatchMessage.innerText = 'Passwords don\'t match'; 
        passwordMatchMessage.style.backgroundColor = 'lightcoral'; 
    }
});
//password confirmation unfocus
passwordInput2.addEventListener('blur', function(e) {
    passwordMatchMessage.style.visibility = 'hidden';
    passwordMatchMessage.style.position = 'absolute';

});



//control form submission
signUpForm.addEventListener('submit', function(e) {
    if (!checkPassword() || !verifyPasswordMatch() || passwordInput1.value == null || passwordInput2.value == null) {
        e.preventDefault();
    } else {
        e.submit();
    }
});


