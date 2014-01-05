$(document).ready(function(){
    var pageLoadEvent, setUI, bindEvents;
    pageLoadEvent = function(){
        setUI;
        };

    setUI = function(){
        $('#rooms > ul').mixitup();
        };

    bindEvents = function(){
        $('li.mix').on('click',function(){});
        };

    (function(){pageLoadEvent()})();
    });
