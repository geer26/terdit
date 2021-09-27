const socket = io({
  withCredentials: true
});


function send_message(message, event='test'){
    socket.emit(event, message);
}


/*
socket.on('connect', () => {
        console.log('SOCKET CONNECTED');
        var data = {data: 'Socket connected!'};
        send_message(data, 'test');
    });
*/

/*
socket.on('test', (data) => {
        console.log('SOMETHING CAME BACK!');
        console.log(data);
    });
*/


socket.on('loginattempt', (data) => {
        //console.log(data);
        switch (data['status']) {
            case 0:
                //console.log('Must be redirected');
                window.location.replace(window.location.hostname);
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


