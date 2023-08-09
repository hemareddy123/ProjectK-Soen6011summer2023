
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

const mapping = {
    'jobpostings' : 'listings',
    'showAllUsers' : 'allUsersTable'
}

// Show All User Profiles
$('#showAllUsers, #jobpostings').click(function(event) {
  event.preventDefault();

  $("#jobpostings, #showAllUsers").removeClass("border border-primary-light bg-primary-light/40");
  $(this).addClass("border border-primary-light bg-primary-light/40");

  $("#listings, #allUsersTable").removeClass("hidden");
  $("#listings, #allUsersTable").addClass("hidden");

  targetDivID = "#" + mapping[$(this).attr("id")]
  $(targetDivID).removeClass("hidden");

})