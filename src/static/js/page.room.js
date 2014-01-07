$(document).ready(function(){
    var pageLoadEvent, setUI, bindEvent, utils;
    pageLoadEvent = function(){
        setUI();
        bindEvent();
        };

    setUI = function(){
        $('.timeago').timeago();
        };

    bindEvent = function(){
        $('button.action.send').on('click',function(){
            var data, identity, roomId, content;
            identity = $.cookie('identity');
            name = $.cookie('name');
            roomId = $('#roomId').val().trim();
            content = $('.chatbox textarea').val().trim();

            if(content === '') return;
            data = {
                'Identity':identity,
                'Content':content,
                'RoomId':roomId};
            
            $.post('/message',data).done(function(data){
                $.get('/messagestyle',function(html){
                    message = $(html);
                    message.addClass('self');
                    message.appendTo('.message-container');
                    
                    message.find('.timeago').attr('datetime',new Date().toLocaleString());
                    message.find('.timeago').timeago();
                    message.find('.name').text(name);
                    message.find('.content span').text(content);
                    }); 
                $('.chatbox textarea').val('');
                });

            });
        };
    (function(){
        pageLoadEvent();
    })();
    });
