tailwind.config = {
    theme: {
      fontFamily: {
        sans: ['Inter'],
      },
      extend: {
        colors: {
          primary: '#296CF2',
          'primary-white': '#F2F2F2',
          'primary-light': '#4B83F2',
          'primary-black': '#0D0D0D',
        },
      },
    },
    plugins: [],
  }

let simpleMde = new SimpleMDE({
  element: document.getElementById("description")
})

const mapping = {
  'addJob' : 'postJob',
  'dashboard' : 'listings',
  'allCandidates' : 'studentTable',
  'selectedCandidates' : 'selectedStudentTable',
  'showAllUsers' : 'allUsersTable'
}

$("#addJob, #dashboard, #allCandidates, #selectedCandidates").click(function(event) {
  event.preventDefault();
  $("#addJob, #dashboard, #allCandidates, #selectedCandidates").removeClass("border border-primary-light bg-primary-light/40");
  $(this).addClass("border border-primary-light bg-primary-light/40");
  
  $("#listings, #postJob, #studentTable, #selectedStudentTable").removeClass("hidden");
  $("#listings, #postJob, #studentTable, #selectedStudentTable").addClass("hidden");
  targetDivID = "#" + mapping[$(this).attr("id")]
  $(targetDivID).removeClass("hidden");
})

// Show All User Profiles
$('#showAllUsers').click(function(event) {
  event.preventDefault();

  // $.ajax({
  //     url: 'http://127.0.0.1:5000/showAllUsers',
  //     type: 'GET',
  //     contentType: 'application/json',
  //     success: function (response) {
  //         // Handle the response from the server
  //         message = response.message;
  //         users=response.users;
  //         targetDivID = "#" + mapping[$(this).attr("id")]
  //         $(targetDivID).removeClass("hidden");
  //     },
  //     error: function (error) {
  //         // Handle any errors that occur during the request
  //         console.error(error);
  //     }
  // });

  $(this).removeClass("border border-primary-light bg-primary-light/40");
  $(this).addClass("border border-primary-light bg-primary-light/40");
  
  targetDivID = "#" + mapping[$(this).attr("id")]
  $(targetDivID).removeClass("hidden");

})