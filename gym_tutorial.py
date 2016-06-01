#coding:UTF-8
import hashlib
import web
import lxml
import time
import os
import urllib2,json
from lxml import etree

class Gym_tutorial:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        data = web.input()
        group = data.group
        name = data.name
        return self.render.reply_img_desc(u"title",group,name,u"http://7xqdbr.com1.z0.glb.clouddn.com/chest_bench_press.gif")

    def POST(self):        
        str_xml = web.data() 
        xml = etree.fromstring(str_xml)
        content=xml.find("Content").text
        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text
        
        return self.render.reply_text(fromUser,toUser,int(time.time()),content+u"?")


