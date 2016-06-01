#coding:UTF-8
import hashlib
import web
import lxml
import time
import os
import urllib2,json
import httplib
from lxml import etree

class Id_verify:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        self.appID = "wx9f1520015f7ba29f"
        self.security = "39d45a0185602d527496c98ee22f57dc "
        self.access_token = ""

    def get_token(self):
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (self.appID, self.security)
        result = urllib2.urlopen(url).read()
        self.access_token = json.loads(result).get('access_token')
        return httplib.HttpResponse(result)

    def create_menu(self):
        url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % (self.access_token)
        data = {
           "button":[
           {
              "name":"1",
              "sub_button":[
              {
                "type":"click",
                "name":"2",
                "key":"meitu"
              },
              {
                "type":"view",
                "name":"3",
                "url":"http://m.jb51.net/photos"
              }]
           }]
        }
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')
        req.add_header('encoding', 'utf-8')
        response = urllib2.urlopen(req, json.dumps(data,ensure_ascii=False))
        result = response.read()
        return httplib.HttpResponse(result)

    def get_material(self, mid):
        url = "https://api.weixin.qq.com/cgi-bin/material/get_material?access_token=%s" % (self.access_token)
        data = {
            "media_id":mid
        }
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')
        req.add_header('encoding', 'utf-8')
        response = urllib2.urlopen(req, json.dumps(data,ensure_ascii=False))
        result = response.read()
        return httplib.HttpResponse(result)

    def check_signature(self):
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        
        token="jesus_is_a_man"
        
        list=[token,timestamp,nonce]
        list.sort()
        
        sha1=hashlib.sha1()     
        map(sha1.update, list)
        hashcode=sha1.hexdigest()
        
        if hashcode == signature:
            return echostr      
        return 'access verification fail'


    def chat(self, ask):
        ask = ask.encode('UTF-8')
        enask = urllib2.quote(ask)
        baseurl = r'http://api.qingyunke.com/api.php?key=free&appid=0&msg='
        url = baseurl+enask
        resp = urllib2.urlopen(url)
        reson = json.loads(resp.read())
        return reson

    def GET(self):
        return self.check_signature()

    def POST(self):        
        str_xml = web.data() 
        xml = etree.fromstring(str_xml)
        content=xml.find("Content").text
        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text

        if msgType == "event":
            mscontent = xml.find("Event").text
            if mscontent == "subscribe":
                reply = u"谢谢你关注健身大百科,输入h试试吧!\n"
                return self.render.reply_text(fromUser,toUser,int(time.time()),reply)

        if (content == "h") or (content == "H") or (content == "Help") or (content == "help"):
            reply = u"h(elp): 主菜单\n"
            reply += u"0: 胸肌(Chest)\n"
            reply += u"1: 二头肌(Biceps)\n"
            reply += u"2: 三头肌(Triceps)\n"
            reply += u"3: 大腿肌群/肱二头肌/肱四头肌(Thighs)\n"
            reply += u"4: 腹部(Abs)\n"
            reply += u"5: 前臂(Forarms)\n"
            reply += u"6: 小腿(Calfs)\n"
            reply += u"7: 背部肌群(Back)\n"
            reply += u"8: 三角肌(shoulders)\n"
            reply += u"9: 斜方肌(Trapz)\n"
            reply += u"输入其它我们支持聊天功能哦~\n"
            return self.render.reply_text(fromUser,toUser,int(time.time()),reply)
        if content == "0":
            reply = str(self.render.article(u"杠铃仰卧推举(Bench Press)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/chest_bench_press.gif","http://gymguru.applinzi.com/page?group=chest&name=bench_press"))
            reply += str(self.render.article(u"哑铃仰卧推举(Flat Dumbbell Press) ","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/chest_flat_dumbbell_press.gif","http://gymguru.applinzi.com/page?group=chest&name=flat_dumbbell_press"))
            reply += str(self.render.article(u"双杠撑体(Parallel dips)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/chest_parallel_dips.gif","http://gymguru.applinzi.com/page?group=chest&name=parallel_dips"))
            reply += str(self.render.article(u"上斜哑铃卧推(Incline Dumbbell Press)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/chest_incline_dumbbell_press.gif","http://gymguru.applinzi.com/page?group=chest&name=incline_dumbbell_press"))
            reply += str(self.render.article(u"上斜杠铃卧推(Incline Bench Press)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/chest_incline_bench_press.gif","http://gymguru.applinzi.com/page?group=chest&name=incline_bench_press"))
            reply += str(self.render.article(u"平卧哑铃飞鸟(Dumbbell bench fly)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/chest_dumbbell_bench_fly.gif","http://gymguru.applinzi.com/page?group=chest&name=dumbbell_bench_fly"))
            reply += str(self.render.article(u"上斜哑铃飞鸟(Dumbbell Incline Fly)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/chest_dumbbell_incline_fly.gif","http://gymguru.applinzi.com/page?group=chest&name=dumbbell_incline_fly"))
            reply += str(self.render.article(u"滑轮机械扩胸(Cable chest cross Over(滑轮飞鸟))","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/chest_cable_chest_cross_over.gif","http://gymguru.applinzi.com/page?group=chest&name=cable_chest_cross_over"))
            reply += str(self.render.article(u"坐式机械飞鸟(Pec-Dec machine flyes)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/chest_predec_machine_flyes.gif","http://gymguru.applinzi.com/page?group=chest&name=predec_machine_flyes"))
            return self.render.reply_img_text(fromUser,toUser,int(time.time()),9,reply)
        if content == "1":      
            reply = str(self.render.article(u"集中弯举(One Arm Concentration Curls)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/biceps_one_arm_concentration_curls.gif","http://gymguru.applinzi.com/page?group=biceps&name=one_arm_concentration_curls"))
            reply += str(self.render.article(u"杠铃弯举(Straight Bar Arm Curl)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/biceps_straight_bar_arm_curl.gif","http://gymguru.applinzi.com/page?group=biceps&name=straight_bar_arm_curl"))
            reply += str(self.render.article(u"杠铃斜板弯举(Barbell preacher curls)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/biceps_barbell_preacher_curls.gif","http://gymguru.applinzi.com/page?group=biceps&name=barbell_preacher_curls"))              
            reply += str(self.render.article(u"站姿哑铃锤式弯举(Dumbbells alternate hammer curls)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/biceps_dumbbells_alternate_hammer_curls.gif","http://gymguru.applinzi.com/page?group=biceps&name=dumbbells_alternate_hammer_curls"))            
            reply += str(self.render.article(u"滑轮二头肌弯举(Cable standing one-arm curls) ","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/biceps_cable_standing_onearm_curls.gif","http://gymguru.applinzi.com/page?group=biceps&name=cable_standing_onearm_curls"))           
            reply += str(self.render.article(u"坐姿哑铃交替弯举(Dumbbels seatedl curls)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/biceps_dumbbels_seatedl_curls.gif","http://gymguru.applinzi.com/page?group=biceps&name=dumbbels_seatedl_curls"))         
            return self.render.reply_img_text(fromUser,toUser,int(time.time()),6,reply)
        if content == "2":      
            reply = str(self.render.article(u"杠铃窄握推举(Barbell narrow-grip bench presses)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/triceps_barbell_narrow_grip_bench_presses.gif","http://gymguru.applinzi.com/page?group=triceps&name=barbell_narrow_grip_bench_presses"))
            reply += str(self.render.article(u"架桥式板凳撑体(Bench dip behind back)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/triceps_bench_dip_behind_back.gif","http://gymguru.applinzi.com/page?group=triceps&name=bench_dip_behind_back"))
            reply += str(self.render.article(u"仰卧三头肌伸展(Lying triceps extension)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/triceps_lying_triceps_extension.gif","http://gymguru.applinzi.com/page?group=triceps&name=lying_triceps_extension"))           
            reply += str(self.render.article(u"Ｗ杠立式伸展举(EZbar standing extensions)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/triceps_ezbar_standing_extensions.gif","http://gymguru.applinzi.com/page?group=triceps&name=ezbar_standing_extensions"))               
            reply += str(self.render.article(u"坐姿哑铃三头肌伸展(Seated dumbbell extension) ","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/triceps_seated_dumbbell_extension.gif","http://gymguru.applinzi.com/page?group=triceps&name=seated_dumbbell_extension"))          
            reply += str(self.render.article(u"哑铃单手后屈伸(Dumbbell kickbacks)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/triceps_dumbbell_kickbacks.gif","http://gymguru.applinzi.com/page?group=triceps&name=dumbbell_kickbacks"))             
            return self.render.reply_img_text(fromUser,toUser,int(time.time()),6,reply)
        if content == "3":
            reply = str(self.render.article(u"史密斯架蹲举(Smith-machine squats)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/thighs_smithmachine_squats.gif","http://gymguru.applinzi.com/page?group=thighs&name=smithmachine_squats"))
            reply += str(self.render.article(u"仰卧腿蹲举(Leg Press)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/thighs_leg_press.gif","http://gymguru.applinzi.com/page?group=thighs&name=leg_press"))
            reply += str(self.render.article(u"腿后勾(Leg curls)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/thighs_leg_curls.gif","http://gymguru.applinzi.com/page?group=thighs&name=leg_curls"))
            reply += str(self.render.article(u"斜板机械蹲举(Hack Squats) ","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/thighs_hack_squats.gif","http://gymguru.applinzi.com/page?group=thighs&name=hack_squats"))
            reply += str(self.render.article(u"前抬腿(Leg extension)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/thighs_leg_extension.gif","http://gymguru.applinzi.com/page?group=thighs&name=leg_extension"))
            reply += str(self.render.article(u"哑铃跨步蹲举(Dumbbell lunges)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/thighs_dumbbell_lunges.gif","http://gymguru.applinzi.com/page?group=thighs&name=dumbbell_lunges"))
            reply += str(self.render.article(u"直膝硬拉(Stif-leg Deadlifts；Barbell Straight-back Straight-leg Deadlift)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/thighs_stifleg_deadlifts.gif","http://gymguru.applinzi.com/page?group=thighs&name=stifleg_deadlifts"))
            reply += str(self.render.article(u"史密斯架蹲举(Smith-machine squats) ","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/thighs_smithmachine_squats.gif","http://gymguru.applinzi.com/page?group=thighs&name=smithmachine_squats"))
            return self.render.reply_img_text(fromUser,toUser,int(time.time()),8,reply)
        if content == "4":
            reply = str(self.render.article(u"仰卧起坐(Crunchs)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/abs_crunchs.gif","http://gymguru.applinzi.com/page?group=abs&name=crunchs"))
            reply += str(self.render.article(u"仰卧腿上举(Lying leg raises)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/abs_lying_leg_raises.gif","http://gymguru.applinzi.com/page?group=abs&name=lying_leg_raises"))
            reply += str(self.render.article(u"侧身仰卧起坐(Side Crunchs)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/abs_side_crunchs.gif","http://gymguru.applinzi.com/page?group=abs&name=side_crunchs"))
            return self.render.reply_img_text(fromUser,toUser,int(time.time()),3,reply)
        if content == "5":
            reply = str(self.render.article(u"正提腕弯举(Bottom Forearm Wrist Curls)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/abs_bottom_forearm_wrist_curls.gif","http://gymguru.applinzi.com/page?group=abs&name=bottom_forearm_wrist_curls"))
            reply += str(self.render.article(u"反手提腕弯举(Top Forearm Wrist Curls)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/abs_top_forearm_wrist_curls.gif","http://gymguru.applinzi.com/page?group=abs&name=top_forearm_wrist_curls"))
            return self.render.reply_img_text(fromUser,toUser,int(time.time()),2,reply)
        if content == "6":
            reply = str(self.render.article(u"坐姿提踵(Seated calfraise) ","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/abs_seated_calfraise.gif","http://gymguru.applinzi.com/page?group=abs&name=seated_calfraise"))
            return self.render.reply_img_text(fromUser,toUser,int(time.time()),1,reply)
        if content == "7":
            reply = str(self.render.article(u"颈后引体向上(Chin-up behind neck)/胸前引体向上(Front chin-ups)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/back_front_chinups.gif","http://gymguru.applinzi.com/page?group=back&name=front_chinups"))
            reply += str(self.render.article(u"杠铃曲体划船(Barbell bent rows)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/back_barbell_bent_rows.gif","http://gymguru.applinzi.com/page?group=back&name=barbell_bent_rows"))
            reply += str(self.render.article(u"俯身挺背(Hyperextensions)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/back_hyperextensions.gif","http://gymguru.applinzi.com/page?group=back&name=hyperextensions"))
            reply += str(self.render.article(u"站姿负重俯身挺背","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/back_standing.gif","http://gymguru.applinzi.com/page?group=back&name=standing"))
            reply += str(self.render.article(u"坐姿滑轮颈前下拉(Front pull-down)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/back_front_pulldown.gif","http://gymguru.applinzi.com/page?group=back&name=front_pulldown"))
            reply += str(self.render.article(u"滑轮坐姿划船(Pulley Rowing)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/back_pulley_rowing.gif","http://gymguru.applinzi.com/page?group=back&name=pulley_rowing"))
            reply += str(self.render.article(u"哑铃单臂划船(Dumbbell One-arm Rows)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/back_dumbbell_onearm_rows.gif","http://gymguru.applinzi.com/page?group=back&name=dumbbell_onearm_rows"))
            reply += str(self.render.article(u"T-bar划船(T-bar rows)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/back_tbar_rows.gif","http://gymguru.applinzi.com/page?group=back&name=tbar_rows"))
            reply += str(self.render.article(u"硬拉(Deadlifts)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/back_deadlifts.gif","http://gymguru.applinzi.com/page?group=back&name=deadlifts"))
            return self.render.reply_img_text(fromUser,toUser,int(time.time()),9,reply)
        if content == "8":
            reply = str(self.render.article(u"杠铃胸前推举(Smith Machine press)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_smith_machine_press.gif","http://gymguru.applinzi.com/page?group=shoulders&name=smith_machine_press"))
            reply += str(self.render.article(u"坐姿哑铃推举(Dumbbell Shoulder Press)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_dumbbell_shoulder_press.gif","http://gymguru.applinzi.com/page?group=shoulders&name=dumbbell_shoulder_press"))
            reply += str(self.render.article(u"杠铃颈后推举(Barbell Press Behind Neck)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_barbell_press_behind_neck.gif","http://gymguru.applinzi.com/page?group=shoulders&name=barbell_press_behind_neck"))
            reply += str(self.render.article(u"俯立侧平举(Bent Over Lateral Raise)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_bent_over_lateral_raise.gif","http://gymguru.applinzi.com/page?group=shoulders&name=bent_over_lateral_raise"))
            reply += str(self.render.article(u"立姿侧平举(Side Laterals Raises)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_side_laterals_raises.gif","http://gymguru.applinzi.com/page?group=shoulders&name=side_laterals_raises"))
            reply += str(self.render.article(u"立正划船(Upright Rows)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_upright_rows.gif","http://gymguru.applinzi.com/page?group=shoulders&name=upright_rows"))
            reply += str(self.render.article(u"立姿哑铃前抬举(Dumbbell Front Raises)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_dumbbell_front_raises.gif","http://gymguru.applinzi.com/page?group=shoulders&name=dumbbell_front_raises"))
            reply += str(self.render.article(u"滑轮单手前胸侧平举(Cable one-arm front laterals)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_cable_onearm_front_laterals.gif","http://gymguru.applinzi.com/page?group=shoulders&name=cable_onearm_front_laterals"))
            reply += str(self.render.article(u"绳索交错俯立侧平举(Cable cross bent laterals)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_cable_cross_bent_laterals.gif","http://gymguru.applinzi.com/page?group=shoulders&name=cable_cross_bent_laterals"))
            return self.render.reply_img_text(fromUser,toUser,int(time.time()),9,reply)
        if content == "9":
            reply = str(self.render.article(u"杠/哑铃耸肩(Barbel / Dumbell Shrug)","welcome","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_barbel.gif","http://gymguru.applinzi.com/page?group=shoulders&name=barbel"))
            return self.render.reply_img_text(fromUser,toUser,int(time.time()),1,reply)
        res = self.chat(content)
        return self.render.reply_text(fromUser,toUser,int(time.time()),res["content"])
