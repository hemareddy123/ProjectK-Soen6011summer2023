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

$("#addJob, #dashboard, #candidates, #settings").click(function(event) {
  event.preventDefault();
  $("#addJob, #dashboard, #candidates, #settings").removeClass("border border-primary-light bg-primary-light/40");
  $(this).addClass("border border-primary-light bg-primary-light/40");
})

$("#addJob, #dashboard").click(function(event) {
  event.stopPropagation();
  document.getElementById('postJob').style.display='block';
  // $("#listings, #postJob").toggleClass("invisible");
})

$("#logout").click(function(event) {
  window.location.href = 'http://127.0.0.1:5000/';
})

  