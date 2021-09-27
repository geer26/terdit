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
    //console.log(username, ' : ', password);
    send_message({username: username, password: password}, 'loginattempt');
}