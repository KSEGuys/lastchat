var page = window.page || {};
page.room = page.room || {};
page.room.utils = page.room.utils || 
{
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
            console.log(message);
            page.room.utils.appendMessage(message);
        };


    };


    (function(){
        pageLoadEvent();
    }());
});
