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
            if(message === 'success' && userType === 'student'){
               window.location.href = response.redirect_url + "?id="+response.userId;
            }else if(message === 'success' && userType === 'employer'){
                window.location.href = response.redirect_url + "?id="+response.userId;
            }else if(message === 'success' && userType === 'admin'){
                window.location.href = response.redirect_url + "?username="+response.name;
                $('#allUsersTable').addClass("hidden");
            }else{
                incorrectPass.style.display = 'block'
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
    
    //var empId = $('#createJobBtn').data('emp-id');

    var formData = {
        title: $('input[name="jobTitle"]').val(),
        description: $('textArea[name="description"]').val(),
        startDate: $('input[name="startDate"]').val(),
        endDate: $('input[name="endDate"]').val(),
        location: $('input[name="location"]').val(),
        jobType: $('select[name="jobType"').val(),
        employer_id : $('#createJobBtn').data('emp-id')
    };
    function showSuccessDiv() {
        $("#successDiv").fadeIn(500, function() {
          setTimeout(function() {
            $("#successDiv").fadeOut(500);
          }, 2000); // 2000 milliseconds (2 seconds)
        });
      }

      console.log(formData);

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

    console.log(formData);


    $.ajax({
        url: 'http://127.0.0.1:5000/selectStudent',
        type: 'POST',
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function (response) {
            // Handle the response from the server

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

    const formData = new FormData();
    formData.append('username', $('#user').val());
    formData.append('highestQualification', $('#education').val());
    formData.append('work_experience', $('#experience').val());
    formData.append('achivements', $('#achievments').val());
    formData.append('email', $('#mail').val());
    formData.append('gender', $('input[name="gender"]:checked').val());
    formData.append('age', $('#age').val());
    formData.append('address', $('#address').val());
    formData.append('phone', $('#phone').val());
    const resumeFileInput = document.getElementById('resume');
    formData.append('resume', resumeFileInput.files[0]);
    var userId = $('#mylink').data('user-id');

    for (const entry of formData.entries()) {
        console.log(`${entry[0]}: ${entry[1]}`);
    }

    $.ajax({
        url: 'http://127.0.0.1:5000/studentProfilePostReq',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
            // Handle the response from the server
            window.location.href = 'http://127.0.0.1:5000/studentDashBoard' + "?id="+response.studentId + "&userId="+userId;
        },
        error: function (error) {
            // Handle any errors that occur during the request
            console.error(error);
        }
    }); 
});

$('.apply-job-link').click(function(event) {
    
    event.preventDefault();
    var jobId = $(this).data('job-id');
    var studId = $(this).data('student-id');

    console.log(`student is ${studId}`);
    
    var formData = {
        'jobposting_id' : jobId,
        'stud_id' : studId
    }
    
    $.ajax({
        url: 'http://127.0.0.1:5000/applyJob',
        type: 'POST',
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function (response) {
            // Handle the response from the server
            window.alert('successully applied');
        },
        error: function (error) {
            // Handle any errors that occur during the request
            console.error(error);
        }
    });
})

$('.deleteJobPosting').click(function(event) {
    
    event.preventDefault();

    console.log('works');
    var jobId = $(this).data('job-id');

    var formData = {
        'job_id' : jobId,
    }

    $.ajax({
        url: 'http://127.0.0.1:5000/deleteJob',
        type: 'POST',
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function (response) {
            // Handle the response from the server
            alert(response);
            window.reload();
        },
        error: function (error) {
            // Handle any errors that occur during the request
            console.error(error);
        }
    }); 
})

$('.deleteUser').click(function(event) {
    
    event.preventDefault();

    var userId = $(this).data('user-id');

    var formData = {
        'user_id' : userId,
    }

    console.log(formData);

    $.ajax({
        url: 'http://127.0.0.1:5000/deleteUser',
        type: 'POST',
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function (response) {
            // Handle the response from the server
            alert(response);
            window.reload();
        },
        error: function (error) {
            // Handle any errors that occur during the request
            console.error(error);
        }
    }); 
})