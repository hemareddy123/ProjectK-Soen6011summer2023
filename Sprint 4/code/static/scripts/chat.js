
// using the socket IO websocket from the client side to the server side
const socket = io({autoConnect: false, reconnection: false});

// Getting the employer Id and Student Id in the respective chat session
var empId = $('#holder').data('emp-id');
var studId = $('#holder').data('student-id');
var initater = $('#holder').data('initater');
var list = $('#chat-messages');
list.scrollTop(list.prop("scrollHeight"));

socket.connect();

// Socket handler from the response from the server socket
socket.on("chat", function(data) {

    var resEmpId = data["empId"];
    var resStudId = data["studId"];

    if(resEmpId == empId && resStudId == studId){

        // var newListItem = $("<li>").text($("<b>").text(data["username"]+ ": ") +data["message"]);
        var newListItem = $("<li>").append($("<b>").text(data["username"] + ": ")).append(data["message"]);

        // Getting the message from the server socket, creating the <li> 
        // populating the <li>
        initater = data["initater"];

        if(initater === "employer"){
            newListItem.addClass("container darker");
        }else if(initater === "student"){
            newListItem.addClass("container");
        }

        // Appending to the <ul> and newly formed <li>
        list.append(newListItem);

        console.log(list.prop("scrollHeight"));
        list.scrollTop(list.prop("scrollHeight"));
        //socket.disconnect();
        //socket.connect();

    }

})

// Handling the 'Enter' event from the chat input session.
$("#userInput").keyup(function(event) {
    if (event.which === 13) {
        $(".send-button").click();
    }
});

// Sending the websocket message from the client to the server socket 
// and saving it in db simuntionsly.
$('.send-button').click(function(event){
    event.preventDefault();

    text = $('#userInput').val();

    initater = $('#holder').data('initater');

    var formData = {
        text: text,
        empId: empId,
        initater: initater,
        studId: studId
    };

    // Hitting the backend api for saving the chat b/w employer and student 
    // or vice-versa, after successfull response sending the client websocket
    // to the server websocket

    $.ajax({
        url: 'http://127.0.0.1:5000/createChat',
        type: 'POST',
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function (response) {
            // Handle the response from the servers
            //window.alert(response);
            $("#userInput").val("");
            socket.emit("new_message", text, initater, empId, studId);
        },
        error: function (error) {
            // Handle any errors that occur during the request
            console.error(error);
        }
    });

})
