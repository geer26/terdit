const socket = io({
  withCredentials: true
});


function send_message(message, event='test'){
    socket.emit(event, message);
}
