$('#signupForm').submit(function (event) {
  
    event.preventDefault();
  
    // Get the form data and convert it to JSON format
    var formData = {
        username: $('input[name="username"]').val(),
        password: $('input[name="password"]').val(),
        usertype: $('input[name="role"]:checked').val(),
        useremail: $('input[name="useremail"]').val()
    };
    
    
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
            var success = document.getElementById('success');
            success.style.display="block";
            success.textContent = "User Created Successfully";
            setTimeout(function(){
                location.reload();
            },5000);
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
            userType = response.type;
            console.log(response);
            if(message === 'success' && userType === 'employer'){
               window.location.href = response.redirect_url + "?username="+response.name;
            }else if(message === 'success' && userType === 'student'){
                window.location.href = response.redirect_url + "?id="+response.userId;
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

$('.selectCandidate').click(function(event) {
    event.preventDefault();
    var empId = $(this).data('emp-id');
    var studId = $(this).data('student-id');
    //var clickedElement = $(this);
    //clickedElement.addClass('disabled-link');

    var formData = {
        'emp_id' : empId,
        'stud_id' : studId
    }


    $.ajax({
        url: 'http://127.0.0.1:5000/selectStudent',
        type: 'POST',
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function (response) {
            // Handle the response from the server

            $('.selectCandidate').addClass('disabled-link');

            $("#toast-success").fadeIn(500,function(){
                setTimeout(function() {
                    $("#toast-success").fadeOut(500);
                },2000);
            })
        },
        error: function (error) {
            // Handle any errors that occur during the request
            console.error(error);
        }
    });
    
})

$('#createProfile').click(function(event) {
    event.preventDefault();

    const formData = {
        username: $('#user').val(),
        highestQualification: $('#education').val(),
        work_experience: $('#experience').val(),
        achivements: $('#achievments').val(),
        email: $('#mail').val(),
        gender: $('input[name="gender"]:checked').val(),
        age: $('#age').val(),
        address: $('#address').val(),
        phone: $('#phone').val()     
    }
    var userId = $('#mylink').data('user-id');

    $.ajax({
        url: 'http://127.0.0.1:5000/studentProfilePostReq',
        type: 'POST',
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function (response) {
            // Handle the response from the server
            window.location.href = 'http://127.0.0.1:5000/studentDashBoard' + "?id="+response.studentId + "&userId="+userId;
        },
        error: function (error) {
            // Handle any errors that occur during the request
            console.error(error);
        }
    });
    
})
