close_modal();

function close_modal(){
    $('.modalback').hide();
}


function show_login(){
    close_modal();
    $('#loginback').show();
}


function show_reg(){
    close_modal();
    $('#regback').show();
}


function hide_error(){
    $('.errormessage').hide();
}


function loginattempt(){
    var username = $('#login-username').val();
    var password = $('#login-password').val();
    var remember = $('#remember_me').prop('checked');
    send_message({username: username, password: password, remember_me: remember_me}, 'loginattempt');
}


socket.on('loginattempt', (data) => {
        switch (data['status']) {
            case 0:
                $("#loginform").submit()
                break;
            case 1:
                hide_loader();
                $('.errormessage').text(data['message']);
                $('.errormessage').show()
                break;
            case 2:
                hide_loader();
                $('.errormessage').text(data['message']);
                $('.errormessage').show()
                break;
        }
    });