$(document).ready(function(){
    $('.carousel').carousel({
        //fullWidth: true,
        indicators: true
    });
  });

function get_data(){
    send_message({event: '1000'}, 'admin_stream');
}


socket.on('admin_stream', (data) => {
        hide_loader();
        switch (data['status']) {
            case 0:
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