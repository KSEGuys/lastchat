$(document).ready(function(){
    var pageLoadEvent, setUI, bindEvent;
    pageLoadEvent = function(){
        setUI();
        bindEvent();
        };

    setUI = function(){
        };

    bindEvent = function(){
        $('button.action.send').on('click',function(){
            var data, identity, roomId, content;
            identity = $.cookie('identity');
            roomId = $('#roomId').val().trim();
            content = $('.chatbox textarea').val().trim();

            if(content === '') return;
            data = {
                'Identity':identity,
                'Content':content,
                'RoomId':roomId};
            
            $.post('/message',data).done(function(data){
                // success
                $('.chatbox textarea').val('');
                });

            });
        };

    (function(){
        pageLoadEvent();
    })();
    });
