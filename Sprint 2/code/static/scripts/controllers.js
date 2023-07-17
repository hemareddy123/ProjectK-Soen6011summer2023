$('#signupForm').submit(function (event) {
  
    event.preventDefault();
  
    // Get the form data and convert it to JSON format
    var formData = {
        username: $('input[name="username"]').val(),
        password: $('input[name="password"]').val(),
        usertype: $('input[name="role"]:checked').val(),
        useremail: $('input[name="useremail"]').val()
    };
    console.log(formData);
    
    //Send the POST request with JSON data
    $.ajax({
        url: 'http://127.0.0.1:5000/signUp',
        type: 'POST',
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function (response) {
            // Handle the response from the server
            if(response === "user created successfully"){
                console.log("User created Successfully");
              // load next web page
            }
        },
        error: function (error) {
            // Handle any errors that occur during the request
            console.error(error);
        }
    });
  });

$('#loginForm').submit(function(event) {
    event.preventDefault();
    var formData = {
        username: $('input[name="loginusername"]').val(),
        password: $('input[name="loginpassword"]').val(),
    };
    console.log(formData);
    $.ajax({
        url: 'http://127.0.0.1:5000/login',
        type: 'POST',
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function (response) {
            // Handle the response from the server
            if(response === "user logined success"){
                console.log("user logined success");
              // load next web page
            }
        },
        error: function (error) {
            // Handle any errors that occur during the request
            console.error(error);
        }
    });
})