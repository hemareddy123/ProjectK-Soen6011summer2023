const socket = io({autoConnect: false, reconnection: false});
var empId = $('#holder').data('emp-id');
var studId = $('#holder').data('student-id');
var initater = $('#holder').data('initater');
var list = $('#chat-messages');
list.scrollTop(list.prop("scrollHeight"));


socket.on("chat", function(data) {

    var newListItem = $("<li>").text(data["message"]);

    initater = data["initater"];

    if(initater === "employer"){
        newListItem.addClass("container darker");
    }

    list.append(newListItem);

    console.log(list.prop("scrollHeight"));
    list.scrollTop(list.prop("scrollHeight"));
    socket.disconnect();
})

$("#userInput").keyup(function(event) {
    if (event.which === 13) {
        $(".send-button").click();
    }
});

$('.send-button').click(function(event){
    event.preventDefault();

    text = $('#userInput').val();

    var formData = {
        text: text,
        empId: empId,
        initater: initater,
        studId: studId
    };

    $.ajax({
        url: 'http://127.0.0.1:5000/createChat',
        type: 'POST',
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function (response) {
            // Handle the response from the servers
            window.alert(response);
            $("#userInput").val("");
            socket.connect();
            socket.on("connect", function(){
                socket.emit("new_message",text,initater);
            })
        },
        error: function (error) {
            // Handle any errors that occur during the request
            console.error(error);
        }
    });

})
