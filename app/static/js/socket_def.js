var socket = io({
  withCredentials: true
});


function send_message(message, event='test'){
    show_loader();
    socket.emit(event, message);
}



