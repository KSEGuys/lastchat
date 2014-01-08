from lib.web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def index():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    self['title'] = 'Welcome'
    extend_([u'<link rel="stylesheet" href="/static/css/index.css" type="text/css" />\n'])
    extend_([u'<div class="center-block go-block">\n'])
    extend_([u'    <img class="img-welcome center-block" src="/static/images/welcome.png" alt="Welcome" />\n'])
    extend_([u'    <div class="input-group input-group-lg">\n'])
    extend_([u'        <input type="text" class="form-control"\n'])
    extend_([u'        autofocus="autofocus"\n'])
    extend_([u'        name="Username" id="Username" value="" placeholder="Username"/>\n'])
    extend_([u'        <span class="input-group-btn">\n'])
    extend_([u'            <button class="btn btn-primary btn-lg" type="button">Go!</button>\n'])
    extend_([u'        </span>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<script type="text/javascript" charset="utf-8" src=\'/static/js/page.index.js\'></script>\n'])

    return self

index = CompiledTemplate(index, 'templates/index.html')
join_ = index._join; escape_ = index._escape

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
    extend_([u'        <script type="text/javascript" charset="utf-8" src="https://code.jquery.com/jquery-1.10.2.min.js"></script>\n'])
    extend_([u'        <script type="text/javascript" charset="utf-8" src="//netdna.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>\n'])
    extend_([u'        <script type="text/javascript" charset="utf-8" src="http://cdn.bootcss.com/jquery-timeago/1.1.0/jquery.timeago.min.js"></script>\n'])
    extend_([u'        <script type="text/javascript" charset="utf-8" src="/static/js/jquery.cookie.js"></script>\n'])
    extend_([u'        <script type="text/javascript" charset="utf-8" src="/static/js/base.js"></script>\n'])
    extend_([u'    </head>\n'])
    extend_([u'    <body>\n'])
    extend_([u'        ', escape_(content, False), u'\n'])
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
    extend_([u'<div class= "message">\n'])
    extend_([u'    <div class="avatar"></div>\n'])
    extend_([u'    <div class="text">\n'])
    extend_([u'        <div class="info">\n'])
    extend_([u'            <span class="name">', escape_(message.User, True), u'</span>\n'])
    extend_([u'            <time class="timeago" datetime=\'', escape_(message.Timestamp, True), u"'></time>\n"])
    extend_([u'        </div>\n'])
    extend_([u'        <div class="content">\n'])
    extend_([u'            <span>', escape_(message.Content, True), u'</span>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

message = CompiledTemplate(message, 'templates/message.html')
join_ = message._join; escape_ = message._escape

# coding: utf-8
def room (room):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    self['title'] = join_(u'Talk here! - Homepage')
    extend_([u'<script type="text/javascript" charset="utf-8" src="/static/js/page.room.js"></script>\n'])
    extend_([u'<link rel="stylesheet" href="/static/css/room.css" title="" type="text/css" />\n'])
    extend_([u'<input type="hidden" name="" id="roomId" value="', escape_(room.UUID, True), u'" />\n'])
    extend_([u'\n'])
    extend_([u'    <div class="modal-dialog">\n'])
    extend_([u'        <div class="modal-content">\n'])
    extend_([u'            <div class="topic modal-header">\n'])
    extend_([u'                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n'])
    extend_([u'                <h4>', escape_(room.Topic, True), u'</h4>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="message-container modal-body">\n'])
    for message in loop.setup(room.messages):
        extend_(['                ', escape_(plainRender.message(message), False), u'\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="editor modal-footer">\n'])
    extend_([u'                <div class="chatbox">\n'])
    extend_([u'                    <textarea class="form-control" rows="3" autofocus=\'autofocus\'></textarea>\n'])
    extend_([u'                </div>\n'])
    extend_([u'                <div>\n'])
    extend_([u'                    <button type="button" class="btn btn-default clear action">Clear</button>\n'])
    extend_([u'                    <button type="button" class="btn btn-primary send action">Send</button>\n'])
    extend_([u'                </div>\n'])
    extend_([u'            </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])

    return self

room = CompiledTemplate(room, 'templates/room.html')
join_ = room._join; escape_ = room._escape

# coding: utf-8
def rooms(rooms):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    self['title'] = 'Talk here! - Rooms'
    extend_([u'<script type="text/javascript" charset="utf-8" src=\'/static/js/page.rooms.js\'></script>\n'])
    extend_([u'<link rel="stylesheet" href="/static/css/rooms.css" title="" type="text/css" />\n'])
    extend_([u'<div class="nav utils">\n'])
    extend_([u'    <button class="btn btn-default action changeUser"><span class="glyphicon glyphicon-user"></span></button>\n'])
    extend_([u'</div>\n'])
    extend_([u'<div class="modal fade" id="modal-room" tabindex="-1" role="dialog" aria-hidden="true" data-backdrop=\'static\'></div>\n'])
    extend_([u'<div id="rooms" class="center-block">\n'])
    extend_([u'    <div>\n'])
    extend_([u'        <div id="rooms-slide-carousel" class="carousel slide" data-ride="carousel">\n'])
    extend_([u'            <ol class="carousel-indicators">\n'])
    for i in loop.setup(range(0,len(rooms))):
        extend_(['                ', u'<li data-target="#rooms-slide-carousel" data-slide-to="', escape_(i, True), u'"></li>\n'])
    extend_([u'            </ol>\n'])
    extend_([u'            <div class="carousel-inner">\n'])
    for room in loop.setup(rooms):
        extend_(['                ', u'<div class="item\n'])
        if loop.first:
            extend_(['                    ', u'active\n'])
        extend_(['                ', u'    ">\n'])
        extend_(['                ', u'        <img src="/static/images/room-background-default.jpg">\n'])
        extend_(['                ', u'        <div class="carousel-caption">\n'])
        extend_(['                ', u'            <h3>', escape_(room.Topic, True), u'</h3>\n'])
        extend_(['                ', u'            <a class="btn btn-primary" data-toggle="modal" href="/room/', escape_(room.UUID, True), u'" data-target="#modal-room">Join this room!</a>\n'])
        extend_(['                ', u'        </div>\n'])
        extend_(['                ', u'    </div>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <a class="left carousel-control" href="#rooms-slide-carousel" data-slide="prev">\n'])
    extend_([u'                <span class="glyphicon glyphicon-chevron-left"></span>\n'])
    extend_([u'            </a>\n'])
    extend_([u'\n'])
    extend_([u'            <a class="right carousel-control" href="#rooms-slide-carousel" data-slide="prev">\n'])
    extend_([u'                <span class="glyphicon glyphicon-chevron-right"></span>\n'])
    extend_([u'            </a>\n'])
    extend_([u'\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

rooms = CompiledTemplate(rooms, 'templates/rooms.html')
join_ = rooms._join; escape_ = rooms._escape

