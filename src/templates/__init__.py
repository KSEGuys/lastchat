from lib.web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def layout (content):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<html>\n'])
    extend_([u'    <head>\n'])
    extend_([u'        <meta http-equiv="content-type" content="text/html; charset=utf-8" />\n'])
    extend_([u'        <title>', escape_(content.title, True), u'</title>\n'])
    extend_([u'        <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css" title="" type="text/css" />\n'])
    extend_([u'    </head>\n'])
    extend_([u'    </head>\n'])
    extend_([u'    <body>\n'])
    extend_([u'        ', escape_(content, False), u'\n'])
    extend_([u'        <script type="text/javascript" charset="utf-8" src="https://code.jquery.com/jquery-1.10.2.min.js"></script>\n'])
    extend_([u'        <script type="text/javascript" charset="utf-8" src="//netdna.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>\n'])
    extend_([u'    </body>\n'])
    extend_([u'</html>\n'])

    return self

layout = CompiledTemplate(layout, 'templates/layout.html')
join_ = layout._join; escape_ = layout._escape

# coding: utf-8
def message (message):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div class= "message ', escape_(message.styleClass, True), u'">\n'])
    extend_([u'    <div class="avatar"></div>\n'])
    extend_([u'    <div class="text">\n'])
    extend_([u'        <div class="info">\n'])
    extend_([u'            <span class="name">', escape_(message.name, True), u'</span>\n'])
    extend_([u'            <span class="timestamp">', escape_(message.timestamp, True), u'</span>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <div class="content">\n'])
    extend_([u'            <span>', escape_(message.content, True), u'</span>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

message = CompiledTemplate(message, 'templates/message.html')
join_ = message._join; escape_ = message._escape

# coding: utf-8
def room (render,messages):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    self['title'] = join_(u'Talk here! - Homepage')
    extend_([u'\n'])
    extend_([u'<button class="btn btn-primary btn-lg" data-toggle="modal" data-target="#default-room-1">\n'])
    extend_([u'    Default room\n'])
    extend_([u'</button>\n'])
    extend_([u'\n'])
    extend_([u'<link rel="stylesheet" href="/static/css/room.css" title="" type="text/css" />\n'])
    extend_([u'<div class="room modal fade" id="default-room-1">\n'])
    extend_([u'    <div class="modal-dialog">\n'])
    extend_([u'        <div class="modal-content">\n'])
    extend_([u'            <div class="topic modal-header">\n'])
    extend_([u'                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n'])
    extend_([u'                <h4>Chris leaves</h4>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="message-container modal-body">\n'])
    for message in loop.setup(messages):
        extend_(['                ', escape_(render.message(message), False), u'\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="editor modal-footer">\n'])
    extend_([u'                <div class="chatbox">\n'])
    extend_([u'                    <textarea class="form-control" rows="3"></textarea>\n'])
    extend_([u'                </div>\n'])
    extend_([u'                <div>\n'])
    extend_([u'                    <button type="button" class="btn btn-default" data-dismiss="modal">Clear</button>\n'])
    extend_([u'                    <button type="button" class="btn btn-primary send action">Send</button>\n'])
    extend_([u'                </div>\n'])
    extend_([u'            </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'\n'])
    extend_([u'\n'])
    extend_([u'<script type="text/javascript" src="/_ah/channel/jsapi"></script>\n'])

    return self

room = CompiledTemplate(room, 'templates/room.html')
join_ = room._join; escape_ = room._escape

