function validate(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const pass = document.getElementById('password').value;
    const age = document.getElementById('age').value;
    const msgBox = document.getElementById('message').value;
    let message = '';
    if (email === '') {
        message = 'Please enter your valid e-mail.';
        msgBox.style.color = 'red'; 
    } else if (pass === '') {
        message = 'Password must be at least 8 characters long.';
        msgBox.style.color = 'red';
    } else if (age === '') {
        message = 'Age must be between 12 and 50.';
        msgBox.style.color = 'red';
    }
    else {
         message = 'Login successful!.';
        msgBox.style.color = 'green';
    }
    msgBox.innerText = message;  
}