'use strict'

/*
  Setting up the elements and changing their styling on events handler
*/
const loginForm = document.querySelector('form.login')
const signupForm = document.querySelector('form.signup')
const loginBtn = document.querySelector('label.text-login')
const signupBtn = document.querySelector('label.text-signup')
const loginText = document.querySelector('.title-text .login')
const signupText = document.querySelector('.title-text .signup')

signupForm.style.display = 'none'

signupBtn.onclick = () => {
  signupForm.style.display = 'block'
  loginForm.style.marginLeft = '-50%'
  loginText.style.marginLeft = '-50%'
  loginBtn.style.color='#232323';
  loginBtn.style.backgroundColor='white';
  signupBtn.style.backgroundColor='#fcb900';
}

loginBtn.onclick = () => {
  loginForm.style.display = 'block'
  loginForm.style.marginLeft = '0%'
  loginText.style.marginLeft = '0%'
  signupBtn.style.color='#232323';
  signupBtn.style.backgroundColor='white';
  loginBtn.style.backgroundColor='#fcb900';
  delysignup()
}

function delysignup() {
  setTimeout(()=>{
    signupForm.style.display = 'none'
  },300)
}

const blur = ()=> {
  if (pass.value.length < 8 ) {
    alertpass.style.display = 'block'
  }
  if (pass.value == '') {
    alertpass.style.display = 'none'
  }
}

const keydown = ()=> {
  if (pass.value.length >= 8 ) {
    alertpass.style.display = 'none'
    }
}

pass.addEventListener('blur', blur)
pass.addEventListener('keydown', keydown)

cpass.addEventListener('blur',()=>{
  if (cpass.value != pass.value) {
    alertcpass.style.display = 'block'
  }
  if (cpass.value == '') {
    alertcpass.style.display = 'none'
  }
})

cpass.addEventListener('keyup',()=>{
  if (cpass.value == pass.value) {
    alertcpass.style.display = 'none'
  }
})

email.addEventListener('blur',()=>{
  if (email.value == ''){
    lemail.style.top = '50%'
  }
})

email.addEventListener('keydown',()=>{
  if (email.value != '') {
    lemail.style.top = '0%'
  }
})

// grab everything we need for small screen
const btn = document.querySelector("button.mobile-menu-button");
const menu = document.querySelector(".mobile-menu");


// Get the elements
const aboutButton = document.getElementById('about');
const popupContainer = document.getElementById('popupContainer');
const closeButton = document.getElementById('closeButton');

// Event listener for the open button
aboutButton.addEventListener('click', function() {
  popupContainer.style.display = 'block';
});

// Event listener for the close button
closeButton.addEventListener('click', function() {
  popupContainer.style.display = 'none';
});
