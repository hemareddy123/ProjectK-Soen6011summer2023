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
  'appliedJobs' : 'appliedJobTable',
  'allJobs' : 'listings',
}

$("#appliedJobs, #allJobs").click(function(event) {
  event.preventDefault();
  $("#appliedJobs, #allJobs").removeClass("border border-primary-light bg-primary-light/40");
  $(this).addClass("border border-primary-light bg-primary-light/40");
  
  $("#listings, #appliedJobTable").removeClass("hidden");
  $("#listings, #appliedJobTable").addClass("hidden");
  targetDivID = "#" + mapping[$(this).attr("id")]
  $(targetDivID).removeClass("hidden");
})