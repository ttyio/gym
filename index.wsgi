# coding: UTF-8

import sae
import os
import web
from id_verify import Id_verify
from gym_tutorial import Gym_tutorial
from view_page import View_page

urls = (
    '/', 'Hello',
    '/auth','Id_verify',
    '/gym','Gym_tutorial',
    '/page','View_page'
)
 
class Hello:
    def GET(self):
        return ("Hello, vincenth!")

app = web.application(urls, globals()).wsgifunc()
application = sae.create_wsgi_app(app)

