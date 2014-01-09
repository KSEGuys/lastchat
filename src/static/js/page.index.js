$(document).ready(function(){
    var bindEvents, loadIdentity, pageOnloadEvent, setUI;

    pageOnloadEvent = function(){
        setUI();
        loadIdentity('',true);
        bindEvents();
    };

    setUI = function(){
        // for IE <=9, set focus
        $('[autofocus]:not(:focus)').eq(0).focus();
    };

    loadIdentity = function(name,auto){
        var identity;
        if(auto){
            // check cookie
            identity = $.cookie('identity');
            if(identity == undefined) return;
        }
        // redirect to /rooms if we had a identity cookie
        $.post('/identity',{'name':name}).done(
                function(data){
                    if(data== undefined) return;
                    window.location.href = '/rooms';
                });
    };

    bindEvents = function(){
        $('button.btn-primary').on('click',function(){
            var username;
            username = $('#Username').val().trim();
            if(username === ''){
                $('#Username').parent().addClass('has-warning');
                return;
            }
            loadIdentity(username,false);
        });
        $('#Username').on('change',function(){
            var username = $(this).val().trim();
            if(username === ''){
                $(this).parent().addClass('has-warning');}
            else{
                $(this).parent().removeClass('has-warning');
            } });
    };

    (function(){
        pageOnloadEvent();
    }());
});

