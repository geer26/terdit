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

function login(){
    console.log('LOGIN TRIGGERED');
}