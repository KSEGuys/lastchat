#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import web
from datetime import datetime

# config

# 30 days
_cookie_expire_time = 3600 * 24 * 30

# host info
urls = (
        "/",'index',
        "/rooms","rooms",
        '/identity','identity',
        '/room/(.+)','room',
        '/message','message',
        '/messagestyle','messageStyle'
        )

templateGlobals = {
        "strftime": datetime.strftime,
        "str": str
        }

templateDir = 'templates'

plainRender = web.template.render(templateDir, globals=templateGlobals)
templateGlobals["plainRender"] = plainRender
render = web.template.render(templateDir,base='layout',globals=templateGlobals)
templateGlobals["render"] = render
