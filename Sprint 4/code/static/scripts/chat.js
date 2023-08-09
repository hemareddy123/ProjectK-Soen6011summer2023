const socket = io({autoConnect: false, reconnection: false});
var empId = $('#holder').data('emp-id');
var studId = $('#holder').data('student-id');
var initater = $('#holder').data('initater');
var list = $('#chat-messages');
list.scrollTop(list.prop("scrollHeight"));

socket.connect();

socket.on("chat", function(data) {

    var resEmpId = data["empId"];
    var resStudId = data["studId"];

    if(resEmpId == empId && resStudId == studId){

        // var newListItem = $("<li>").text($("<b>").text(data["username"]+ ": ") +data["message"]);
        var newListItem = $("<li>").append($("<b>").text(data["username"] + ": ")).append(data["message"]);


        initater = data["initater"];

        if(initater === "employer"){
            newListItem.addClass("container darker");
        }else if(initater === "student"){
            newListItem.addClass("container");
        }

        list.append(newListItem);

        console.log(list.prop("scrollHeight"));
        list.scrollTop(list.prop("scrollHeight"));
        //socket.disconnect();
        //socket.connect();

    }

})

$("#userInput").keyup(function(event) {
    if (event.which === 13) {
        $(".send-button").click();
    }
});

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

    

    $.ajax({
        url: 'http://127.0.0.1:5000/createChat',
        type: 'POST',
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function (response) {
            // Handle the response from the servers
            window.alert(response);
            $("#userInput").val("");
            // if (!socket.connected) {
            //     socket.connect();
            // }
            // socket.once("connect", function(){
            //     socket.emit("new_message",text,initater,empId,studId);
            // })
            socket.emit("new_message", text, initater, empId, studId);
        },
        error: function (error) {
            // Handle any errors that occur during the request
            console.error(error);
        }
    });

})
