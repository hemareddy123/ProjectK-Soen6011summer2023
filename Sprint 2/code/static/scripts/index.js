'use strict'

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
}

loginBtn.onclick = () => {
  loginForm.style.display = 'block'
  loginForm.style.marginLeft = '0%'
  loginText.style.marginLeft = '0%'
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





