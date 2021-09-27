var upstream = io('/upstream');
var downstream = io('/downstream')


function send_message(message, event='event'){
    upstream.emit(event, message);
}


upstream.on('connect', () => {
        console.log('CONNECTED');
        var data = {data: 'I\'m connected!'}
        send_message(data, 'event')
    });


downstream.on('event', (data) => {
        console.log('SOMETHING CAME BACK!');
        console.log(data);
    });