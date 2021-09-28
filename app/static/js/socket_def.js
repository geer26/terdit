var socket = io({
  withCredentials: true
});


function send_message(message, event='test'){
    show_loader();
    socket.emit(event, message);
}


socket.on('loginattempt', (data) => {
        //console.log(data);
        hide_loader();
        switch (data['status']) {
            case 0:
                console.log('Must be redirected');
                $("#loginform").submit()
                break;
            case 1:
                $('.errormessage').text(data['message']);
                $('.errormessage').show()
                break;
            case 2:
                $('.errormessage').text(data['message']);
                $('.errormessage').show()
                break;
        }
    });


