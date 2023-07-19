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
            var success=document.getElementById('success');
            success.style.display="block";
            success.textContent="User Created Successfully!!";
            setTimeout(function() {
                location.reload();
              }, 5000);
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
    $.ajax({
        url: 'http://127.0.0.1:5000/login',
        type: 'POST',
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function (response) {
            // Handle the response from the server
            message = response.message;
            console.log(response);
            if(message === 'success'){
               window.location.href = response.redirect_url + "?username="+response.name;
            }
        },
        error: function (error) {
            // Handle any errors that occur during the request
            console.error(error);
        }
    });
})

$('#jobPosting').submit(function(event) {
    event.preventDefault();
    var formData = {
        title: $('input[name="jobTitle"]').val(),
        description: $('textArea[name="description"]').val(),
        startDate: $('input[name="endDate"]').val(),
        endDate: $('input[name="startDate"]').val(),
        location: $('input[name="location"]').val(),
        jobType: $('select[name="jobType"').val()
    };
    function showSuccessDiv() {
        $("#successDiv").fadeIn(500, function() {
          setTimeout(function() {
            $("#successDiv").fadeOut(500);
          }, 2000); // 2000 milliseconds (2 seconds)
        });
      }

    $.ajax({
        url: 'http://127.0.0.1:5000/postJob',
        type: 'POST',
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function (response) {
            // Handle the response from the server
           showSuccessDiv()
           $('#jobPosting').each(function(){
                this.reset();
            });
        },
        error: function (error) {
            // Handle any errors that occur during the request
            console.error(error);
        }
    });

});
