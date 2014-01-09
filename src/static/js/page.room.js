var page = window.page || {};
page.room = page.room || {};
page.room.utils = page.room.utils || {
    'appendMessage': function(data){
        $.get('/messagestyle',function(html){
            message = $(html);
            var user = $.cookie('identity');
            if(data.user.id == user){
                message.addClass('self');
            }
            message.appendTo('.message-container');
            message.find('.timeago').attr('datetime',data.time);
            message.find('.timeago').timeago();
            message.find('.name').text(data.user.name).data('uuid',data.user.id);
            message.find('.content span').text(data.content);
        }); 

        page.room.utils.scrollToBottom();
    },
    'scrollToBottom': function(){
        $('div.message-container.modal-body').animate({
            scrollTop: $('div.message-container.modal-body')[0].scrollHeight
        },100);
    }
};
$(document).ready(function(){
    var pageLoadEvent, setUI, bindEvent, utils;
    pageLoadEvent = function(){
        setUI();
        bindEvent();
    };

    setUI = function(){
        // timeago
        $('.timeago').timeago();
        
        // pull left message sent by current user
        var user = $.cookie('identity');
        $('.message').each(function(index,element){
            var element = $(element);
            var identity = element.find('.name').data('uuid').trim();
            if(user == identity){
                element.addClass('self');
            }
        });

        window.setTimeout(page.room.utils.scrollToBottom,500);
    };

    bindEvent = function(){
        $('button.action.clear').on('click',function(){
            $('.chatbox textarea').val('');
        });

        $('button.action.send').on('click',function(){
            var name, data, identity, roomId, content;
            identity = $.cookie('identity');
            name = $.cookie('name');
            roomId = $('#roomId').val().trim();
            content = $('.chatbox textarea').val().trim();

            if(content === '') return;
            data = {
                'Identity':identity,
            'Content':content,
            'RoomId':roomId
            };

            $.post('/message',data).done(function(data){
                $('.chatbox textarea').val('');
            });

        });

        var token = $('#parameters').data('channeltoken');
        var channel = new goog.appengine.Channel(token);
        var socket = channel.open();

        socket.onmessage = function(data){
            var message = JSON.parse(data.data);
            page.room.utils.appendMessage(message);
        };
        
        $('div.chatbox textarea').on('keypress',function(e){
            if(e.which == 13 && !e.shiftKey && !e.ctrlKey){
                e.preventDefault();
                $('button.action.send').trigger('click');
            }
        });

    };


    (function(){
        pageLoadEvent();
    }());
});
