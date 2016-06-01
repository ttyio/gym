#coding:UTF-8
import hashlib
import web
import lxml
import time
import os
import urllib2,json
import httplib
from lxml import etree

class View_page:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        data = web.input()
        group=data.group
        name=data.name
        if group == "chest":
            if name == "bench_press":
                return self.render.reply_page(u"杠铃仰卧推举(Bench Press)","http://7xqdbr.com1.z0.glb.clouddn.com/chest_bench_press.gif",
                                              u"A.重点锻炼部位：胸大肌，辅助肌将会用到三角肌和肱三头肌。仰卧推举为锻炼胸部肌肉的最佳动作。",
                                              u"B.开始位置：躺在水平卧推板上，两脚平贴于地。伸直手臂，正握住横杠，两手间距比肩稍宽；两臂伸直支撑住杠铃于胸部上方。",
                                              u"C.动作过程：将杠推起离开固定架，手肘慢慢弯屈，杠铃垂直落下，直至横杠贴近胸部至大约接近乳头上方的位置，不需完全接触到胸部；然后向上推起至开始位置，重复动作。",
                                              u"D.训练要点：",
                                              u"1.不要把背和臀部拱起或憋气，容易产生危险。",
                                              u"2.手臂上推至顶端时，不要把手肘打直锁死。",
                                              u"3.两手间距切勿太窄，否则会练到别的地方。")
            if name == "flat_dumbbell_press":
                return self.render.reply_page(u"哑铃仰卧推举(Flat Dumbbell Press) ","http://7xqdbr.com1.z0.glb.clouddn.com/chest_flat_dumbbell_press.gif",
                                              u"A.重点锻炼部位：胸大肌，辅助肌为三角肌和肱三头肌。",
                                              u"B.开始位置：仰躺在平卧推板上，两脚平贴于地。双手持哑铃，伸直。",
                                              u"C.动作过程：两臂慢慢弯屈，哑铃垂直落下，下降至手肘约低于身体水平时，稍停，再做上推动作，上推时吐气，直至开始位置，重复动作。",
                                              u"D.训练要点：",
                                              u"1.不要把背和臀部拱起或憋气，容易产生危险。",
                                              u"2.手臂上推至顶端时，不要把手肘打直锁死。",
                                              u"")
            if name == "parallel_dips":
                return self.render.reply_page(u"双杠撑体(Parallel dips)","http://7xqdbr.com1.z0.glb.clouddn.com/chest_parallel_dips.gif",
                                              u"A、重点锻炼部位：胸大肌下半（下胸），其次辅助肌为肱三头肌和三角肌。",
                                              u"B、开始位置：双杠间距最好比肩宽。双手握杠，以手臂将身体向上支撑住，挺胸、收腹；两腿伸直并拢，放松并自然下垂。",
                                              u"C、动作过程：吐气，手肘慢慢弯曲，身体下降，在最低位置时，头部向前引，两肘稍向外展，以使胸大肌充分拉长伸展。接下来，吸气，用胸大肌的力量，收缩胸大肌撑起两臂，使身体上升直至两臂伸直；当上臂超过双杠的水平位置时，臀部稍向后缩，上身呈低头含胸的样子。在两臂伸直的时候，胸大肌处于收缩紧绷的状态。重复练习以上步骤。",
                                              u"D.训练要点：",
                                              u"1.动作要缓慢进行，不要借身体的摆荡或惯性助力完成动作。",
                                              u"2.撑起时的速度可稍快，并注意是要用你的胸肌施力。",
                                              u"3.挺胸、抬头、收腹、不耸肩, 为加大训练强度可在腰间负重练习。")
            if name == "incline_dumbbell_press":
                return self.render.reply_page(u"上斜哑铃卧推(Incline Dumbbell Press)","http://7xqdbr.com1.z0.glb.clouddn.com/chest_incline_dumbbell_press.gif",
                                              u"A.重点锻炼部位：胸大肌上胸，其次是前三角肌和肱三头肌。",
                                              u"B.开始位置：躺在上斜的卧推板上。",
                                              u"C.动作过程：双手持哑铃，当两臂伸直时是位在肩部的上方。放下至胸部上方时吸气。当下降至最低处时（即接近锁骨处），稍停，即做上推动作，上推时吐气。",
                                              u"D.训练要点：",
                                              u"1.练习过程将主要力量集中在胸大肌上，使胸肌保持紧张状态。",
                                              u"",
                                              u"")
            if name == "incline_bench_press":
                return self.render.reply_page(u"上斜杠铃卧推(Incline Bench Press)","http://7xqdbr.com1.z0.glb.clouddn.com/chest_incline_bench_press.gif",
                                              u"A.重点锻炼部位：胸大肌上部（上胸），其次是前三角肌和肱三头肌。",
                                              u"B.开始位置：仰卧在上斜的卧推板上。两手握住横杠，间距比肩宽；两臂伸直支撑住杠铃位于肩部的上方。",
                                              u"C.动作过程：缓缓将杠放下至胸部之上，位于约胸部乳头以上接近锁骨的位置。将杠放下时吸气；当杠接近胸部高度约一两公分时，稍停，即做上推动作，上推时吐气。",
                                              u"D.训练要点：",
                                              u"1.一般都采用较宽的握距，横杠放下在锁骨处，使胸部肌肉更用得上力。",
                                              u"",
                                              u"")
            if name == "dumbbell_bench_fly":
                return self.render.reply_page(u"平卧哑铃飞鸟(Dumbbell bench fly)","http://7xqdbr.com1.z0.glb.clouddn.com/chest_dumbbell_bench_fly.gif",
                                              u"A.重点锻炼部位：胸大肌和三角肌。",
                                              u"B.开始位置：仰卧在水的卧推板上，双手持哑铃，掌心相对，推起至两臂伸直，支撑在胸部上方。",
                                              u"C.动作过程：两手持哑铃向两侧扩展落下，手肘保持稍微弯屈，持哑铃落下至手肘略低于身体水平线；在此过程中手肘始终要保持弯曲，并感到胸部两侧肌肉有充分的拉伸感。当哑铃落下时吸气。持铃依原路径上举，回到原位时吐气。 D.训练要点：哑铃向两侧落下时，手肘与上臂需保持弯曲，如果将手肘伸直，则胸部肌肉便很难得到伸展和收缩的感觉。",
                                              u"D.训练要点：",
                                              u"无",
                                              u"",
                                              u"")
            if name == "dumbbell_incline_fly":
                return self.render.reply_page(u"上斜哑铃飞鸟(Dumbbell Incline Fly)","http://7xqdbr.com1.z0.glb.clouddn.com/chest_dumbbell_incline_fly.gif",
                                              u"A.重点锻炼部位：胸大肌上胸部，其次为三角肌。",
                                              u"B.开始位置：仰卧在上斜的卧推板上，双手持哑铃，掌心相对，推起至两臂伸直，支撑在胸部上方。",
                                              u"C.动作过程：两手持哑铃向两侧扩展落下，手肘稍微弯屈，哑铃落下至手肘略低于水平；过程中手肘始终保持弯曲，并感到胸部两侧肌肉有充分的拉伸感。当哑铃落下时吸气。持铃依原路径上举，回到原位时吐气",
                                              u"D.训练要点：",
                                              u"1.哑铃向两侧落下时，手肘与上臂需保持微弯，如果将手肘伸直，则胸部肌肉便很难得到伸展和收缩的感觉。",
                                              u"",
                                              u"")
            if name == "cable_chest_cross_over":
                return self.render.reply_page(u"滑轮机械扩胸(Cable chest cross Over(滑轮飞鸟))","http://7xqdbr.com1.z0.glb.clouddn.com/chest_cable_chest_cross_over.gif",
                                              u"A.重点锻炼部位：主要锻练胸大肌，其次为三角肌。当握把相触的位置高时，所训练的部位偏向上胸部； 当握把的相触位置在中部或下部，训练的部位则偏于中胸或下胸。 ",
                                              u"B、开始位置：站在拉力器的下方，两脚张开约与肩同宽，两臂向侧上举，肘关节稍微弯曲，两手心向下分别握住拉力器的一端握把。重心方向应该由上向下成45度角。 （不小于30度角）。 ",
                                              u"C、动作过程：身体稍向前倾，吸气，两臂由上往下用力夹至胸前呈交叉状，直至两拉力器握把相触。稍停，吐气，缓缓放松还原。 ",
                                              u"D.训练要点：",
                                              u"1.身体保持稍前倾，不可利用前后摆动的力量。",
                                              u"2.要充分伸展胸肌，动作需缓慢而有节奏地进行。",
                                              u"3.完成动作时两臂均衡用力，防止猛拉或突然性还原动作。")
            if name == "predec_machine_flyes":
                return self.render.reply_page(u"坐式机械飞鸟(Pec-Dec machine flyes)","http://7xqdbr.com1.z0.glb.clouddn.com/chest_predec_machine_flyes.gif",
                                              u"A、重点锻炼部位：胸大肌和肩部三角肌群 ",
                                              u"B、开始位置：坐在蝴蝶机椅上，收腹、挺胸、紧腰，上半身挺直，前臂放在阻力板护垫上，前臂并与地面保持垂直，上臂则与地面平行。",
                                              u"C、动作过程：吸气，两臂同时用力向中间夹胸，使两个阻力板尽可能相触，稍停，然后吐气，缓慢还原。 ",
                                              u"D.训练要点：",
                                              u"1.注意动作完成要圆滑、从容，防止突然性猛夹动",
                                              u"",
                                              u"")
        if group == "biceps":
            if name == "one_arm_concentration_curls":
                return self.render.reply_page(u"集中弯举(One Arm Concentration Curls)","http://7xqdbr.com1.z0.glb.clouddn.com/biceps_one_arm_concentration_curls.gif",
                                              u"A.重点锻练部位：肱二头肌 ",
                                              u"B.开始位置：坐于凳上，身体稍向前倾，单手持哑铃，前臂自然下垂，手臂紧贴大腿内侧。 ",
                                              u"C.动作过程：上臂固定住，贴紧大腿内侧，弯屈手肘将哑铃慢慢举起至胸前；稍停，慢慢放回原位，重复动作，两手交替训练。",
                                              u"D.训练要点：",
                                              u"1.当手臂弯起时，腰背部不要放松；弯起至胸前时，使肱二头肌尽量收紧，并保持静止，再慢慢放下",
                                              u"",
                                              u"")
            if name == "straight_bar_arm_curl":
                return self.render.reply_page(u"杠铃弯举(Straight Bar Arm Curl)","http://7xqdbr.com1.z0.glb.clouddn.com/biceps_straight_bar_arm_curl.gif",
                                              u"A.重点锻练部位：肱二头肌，其次是前臂肌。",
                                              u"B.开始位置：双手反握杠铃，两手间距约同比肩宽，将杠铃下放垂于腿前。上臂内侧紧贴身体。",
                                              u"C.动作过程：以肘关节为支点，用二头肌的力量，将杠铃向上举起至肩前。稍停，再慢慢地循原路放下至腿前。",
                                              u"D.训练要点：",
                                              u"1.当杠铃弯起时，上臂贴于体侧不动。",
                                              u"2.在举起杠铃的同时，使躯干稍微向后仰会较易于施力（但过度后仰将对二头肌的训练效果大打折扣）。",
                                              u"3.弯起将二头肌完全收缩后，杠铃再循原路放下。放下时的速度要慢些。每次必须做到充分的伸展和收缩。")
            if name == "barbell_preacher_curls":
                return self.render.reply_page(u"杠铃斜板弯举(Barbell preacher curls) ","http://7xqdbr.com1.z0.glb.clouddn.com/biceps_barbell_preacher_curls.gif",
                                              u"A.重点锻练部位：肱二头肌，其次为屈肘肌群 ",
                                              u"B.开始位置：坐在弯举椅上，身体前倾，两臂伸直，将上臂搁在斜板上，使腋窝卡在斜板的上沿，手心向上，反握杠铃，两手宽度约与肩同宽。 ",
                                              u"C.动作过程：吸气，两臂以肘关节为轴用力将杠铃举起靠近锁骨，稍停，吐气，将两臂放松还原，重复练习。 ",
                                              u"D.训练要点：",
                                              u"1.将杠铃举起时，上臂保持不动，下放时要缓慢且充分伸展。 ",
                                              u"2.做此动作时因受斜板的限制，较难借用身体其它部位的力量，所以对肱二头肌的训练效果显著。",
                                              u"")
            if name == "dumbbells_alternate_hammer_curls":
                return self.render.reply_page(u"站姿哑铃锤式弯举(Dumbbells alternate hammer curls)","http://7xqdbr.com1.z0.glb.clouddn.com/biceps_dumbbells_alternate_hammer_curls.gif",
                                              u"A.重点锻练部位：肱二头肌。",
                                              u"B.开始位置：可采直立或坐姿，两手各持哑铃，手臂伸直自然下垂，虎口朝向前方。",
                                              u"C.动作过程：上臂用力收缩，以手肘为轴经体侧将哑铃举起，稍停2-3秒，然后吐气，将哑铃缓慢放下还原至体侧，两手交替动作，重复动作。",
                                              u"D.训练要点：",
                                              u"1.上臂固定不动，手腕伸直持哑铃，动作时不可借助身体摆动的惯性力。",
                                              u"",
                                              u"")
            if name == "cable_standing_onearm_curls":
                return self.render.reply_page(u"滑轮二头肌弯举(Cable standing one-arm curls) ","http://7xqdbr.com1.z0.glb.clouddn.com/biceps_cable_standing_onearm_curls.gif",
                                              u"A.重点锻练部位：肱二头肌。",
                                              u"B.开始位置：反手握住把柄，掌心向前，将拉柄下拉至体侧，两脚站立约与肩同宽，挺胸收腹紧腰。",
                                              u"C.动作过程：吸气，上臂保持不动，屈肘慢慢将把柄向上拉，直到接近肩部，稍停，吐气，再慢慢放下还原，重复动作。",
                                              u"D.训练要点：",
                                              u"1.上拉时，身体要保持平直，肘部不要前后摇动。",
                                              u"",
                                              u"")
            if name == "dumbbels_seatedl_curls":
                return self.render.reply_page(u"坐姿哑铃交替弯举(Dumbbels seatedl curls) ","http://7xqdbr.com1.z0.glb.clouddn.com/biceps_dumbbels_seatedl_curls.gif",
                                              u"A.重点锻练部位：肱二头肌。",
                                              u"B.开始位置：正坐在凳的一端，两手各持哑铃，垂于身体两侧。",
                                              u"C.动作过程：先以一手将哑铃举起至肩前，稍停，然后慢慢放下，在下放的同时，另一手举起，如此两手交替着做。",
                                              u"D.训练要点：",
                                              u"1.这个动作与站姿哑铃锤式弯举雷同，可以参考其要点。",
                                              u"",
                                              u"")
        if group == "triceps":
            if name == "barbell_narrow_grip_bench_presses":
                return self.render.reply_page(u"杠铃窄握推举(Barbell narrow-grip bench presses)","http://7xqdbr.com1.z0.glb.clouddn.com/triceps_barbell_narrow_grip_bench_presses.gif",
                                              u"A.重点锻炼部位：肱三头肌，其次动用到的是胸大肌内侧、前三角肌。",
                                              u"B.开始位置：仰躺在板上，两脚平贴于地，以维持身体平衡；两手间距约与肩同宽或稍窄，握住横杠中间，两臂伸直将杠铃举起固定在两肩上方。",
                                              u"C.动作过程：让杠铃随着手臂慢慢的弯屈下降，直至横杠将触及胸部为止，稍停之后，再向上推起至开始位置，重复动作。",
                                              u"D.训练要点：",
                                              u"1.需感到三头肌受力紧绷。",
                                              u"2.两手手肘应靠近身体两侧，如果向外开展的话，训练的部位会变成以胸大肌内侧为主，三头肌反而受力不足。",
                                              u"3.宽握卧推主要是锻炼胸大肌。")
            if name == "bench_dip_behind_back":
                return self.render.reply_page(u"架桥式板凳撑体(Bench dip behind back)","http://7xqdbr.com1.z0.glb.clouddn.com/triceps_bench_dip_behind_back.gif",
                                              u"A.重点锻炼部位：肱三头肌，其次胸大肌、肱二头肌、三角肌和大圆肌。",
                                              u"B.开始位置：此动作以两个凳子为辅。先坐在一个凳上，两手撑在所坐着的凳子上，将两脚放在另一个凳子上。",
                                              u"C.动作过程：，将身体悬空（请将尊臀离开凳子），两手撑住，吐气，两肩放松，两臂慢慢弯屈，身体尽量下沉（尤其要沉臀），稍停2- 3秒，然后吸气，将两臂伸直撑起身体还原。重复动作。",
                                              u"D.训练要点：",
                                              u"1.臂屈伸时速度适中而平稳，身体挺直，两肘要向内夹臂。",
                                              u"2.将脚的高度抬高或身体负重可提高训练难度，加大负荷刺激。",
                                              u"")
            if name == "lying_triceps_extension":
                return self.render.reply_page(u"仰卧三头肌伸展(Lying triceps extension)","http://7xqdbr.com1.z0.glb.clouddn.com/triceps_lying_triceps_extension.gif",
                                              u"A.重点锻炼部位：肱三头肌，其次胸大肌、前锯肌和背阔肌。",
                                              u"B.开始位置 ：仰卧在长凳上。双手正握杠铃，间距比肩稍窄，上臂挺直不动，手臂伸直将杠铃固定于上方。",
                                              u"C.动作过程：上臂不动，弯屈手肘，慢慢将杠铃放下至额头上方，稍停，再用力上拉提起至原位。重复动作。",
                                              u"D.训练要点：",
                                              u"1.这个动作使用W杠会较利于练习。",
                                              u"2.这个动作是固定你上臂，以肘部为轴以训练三头肌的屈臂上拉。为了了解差异，你可以将手臂伸直，用较轻的重量做手肘固定的直臂上拉，来比较一下曲臂与直臂用力的部位效果与差异，有助于你对这个动作的了解，对训练会收到较大的效果。",
                                              u"")
            if name == "ezbar_standing_extensions":
                return self.render.reply_page(u"Ｗ杠立式伸展举(EZbar standing extensions)","http://7xqdbr.com1.z0.glb.clouddn.com/triceps_ezbar_standing_extensions.gif",
                                              u"A.重点锻炼部位：肱三头肌。",
                                              u"B.开始位置：两手正握杠铃，上臂弯屈将杠置于脑后。",
                                              u"C.动作过程：吸气，以肘关节为轴，伸直前臂把杠铃上举，稍停2-3秒。然后吸气，屈臂慢慢落下至脑后，重复动作。",
                                              u"D.训练要点：",
                                              u"1.这个动作也可以如左图般双手合抱杠片或一个哑铃训练,上臂必须尽量靠紧耳侧，两肘夹紧，上臂保持与地面呈垂直，两肘尖垂直向上。",
                                              u"2.落下时不要放到底，也不要将力量完全放松，保持一定的肌肉紧张度，以免受伤。",
                                              u"3.速度不要太快，不可突然加速或用惯性弹性的力量，不要向前后移动借力。")
            if name == "seated_dumbbell_extension":
                return self.render.reply_page(u"坐姿哑铃三头肌伸展(Seated dumbbell extension) ","http://7xqdbr.com1.z0.glb.clouddn.com/triceps_seated_dumbbell_extension.gif",
                                              u"A.重点锻炼部位：肱三头肌。",
                                              u"B.开始位置：坐在凳上，两脚平贴于地，右手持哑铃，伸直于头顶上方。",
                                              u"C.动作过程：右上臂紧贴耳侧不动。右手肘向后弯屈，落下至右肩上方，落下时的位置尽量放低，但不要放到底。然后，以肱三头肌的力量，将哑铃向上举起至开始位置。重复动作。完成一组后，再换左手。两手交替做。",
                                              u"D.训练要点：",
                                              u"1.也可以采用立姿，但建议采坐姿训练。",
                                              u"2.上臂紧贴耳侧不动；落下时的位置尽量放低，但不要放到底或将力量完全放松。",
                                              u"3.手臂持铃向头后对角线落下，要比直接向后方落下的训练的效果要好。")
            if name == "dumbbell_kickbacks":
                return self.render.reply_page(u"哑铃单手后屈伸(Dumbbell kickbacks) ","http://7xqdbr.com1.z0.glb.clouddn.com/triceps_dumbbell_kickbacks.gif",
                                              u"A.重点锻炼部位：肱三头肌。",
                                              u"B.开始位置：双手持哑铃自然直立，曲膝，弯腰约高于水平，手肘弯曲前臂自然垂于胸前。",
                                              u"C.动作过程：上臂紧贴体侧，上臂与手肘固定，手臂将哑铃向后上方举起，直至手臂伸直，再慢慢放下还原。动作过程中，只有前臂上下活动。重复动作。一组完成后再换另一手训练。",
                                              u"D.训练要点：",
                                              u"1.当手臂伸直时，使肱三头肌彻底收缩，保持静止并默数1、2、3，然后再放下还原。",
                                              u"2.上臂要紧贴于体侧并且不动，动作中切记以三头肌施力，不要靠晃动或惯性的力量。",
                                              u"3.训练的动作也可以采用跪姿，进行单手训练。以一张长凳为辅。假设训练右手三头肌，则左脚跪于凳上，左手紧抓凳缘，右手持哑铃，身体向前倾或与地面平行。其余动作同上。")
        if group == "thighs":
            if name == "smithmachine_squats":
                return self.render.reply_page(u"史密斯架蹲举(Smith-machine squats)","http://7xqdbr.com1.z0.glb.clouddn.com/thighs_smithmachine_squats.gif",
                                              u"A.重点锻练部位：股四头肌。",
                                              u"B.开始位置：立于蹲举架（或Smith Machine）下方，将杠铃置于颈后肩上，两手握住横杠的两端，使杠铃重心两边平衡。两脚分开约与肩同宽，脚尖稍向外分开，膝盖稍微弯曲，两腿可稍向前移。",
                                              u"C.动作过程：两眼平视正前方。两膝慢慢弯屈，下蹲直到大腿的位置约同水平。当大腿下蹲至水平位置时，稍停后即慢慢伸直至回原位置。",
                                              u"D.训练要点：",
                                              u"1.在整个下蹲和起立的过程中，保持身体腰背挺直，头部稍微抬起，两眼平视正前方。",
                                              u"2.两腿稍向前移，可加强对股二头肌的刺激。",
                                              u"3.脚掌始终平贴于地。")
            if name == "leg_press":
                return self.render.reply_page(u"仰卧腿蹲举(Leg Press) ","http://7xqdbr.com1.z0.glb.clouddn.com/thighs_leg_press.gif",
                                              u"A.重点锻练部位：股四头肌和臀大肌群；强化臀腿曲线。",
                                              u"B.开始位置：斜躺在蹲举机的靠背椅上，将两腿斜上举起并屈膝，两脚掌蹬在阻力板上。",
                                              u"C.动作过程：吸气，用股四头肌之力用力向上蹬阻力板，直到将两腿伸直，并尽力收缩你的股四头肌。稍停一会。吐气，慢慢屈膝，并保持股四头肌的紧张度，让阻力板下降到原先的高度。重复动作。",
                                              u"D.训练要点：",
                                              u"1.出力向上蹬板时要让整个脚底平贴住阻力板，不要只用钱脚掌或脚根的力量。 ",
                                              u"2.两腿伸直时，并不要将膝盖完全打直，这样让你把力量放在打直的膝盖上喘息。保持适当的屈度以及股四头肌的紧张，然后再慢慢的放下来。",
                                              u"3.下降时应保持股四头肌的紧张度，慢慢地，控制阻力板的下降速度。")
            if name == "leg_curls":
                return self.render.reply_page(u"腿后勾(Leg curls)","http://7xqdbr.com1.z0.glb.clouddn.com/thighs_leg_curls.gif",
                                              u"A.重点锻练部位：主要训练部位为股二头肌。",
                                              u"B.开始位置：俯卧在训练机的卧凳上，让膝盖正好抵住凳缘，两腿伸直使脚跟紧勾在托垫棍的下缘。两手握住凳前端两侧固定。",
                                              u"C.动作过程：以股二头肌的力量将小腿向上弯起，至股二头肌收紧，稍停，默数l、2。然后再循原路慢慢回到起点。重复做。",
                                              u"D.训练要点：",
                                              u"1.将腹部与臀部贴紧凳面，不要悬空或突起借力。",
                                              u"2.下降时应保持股二头肌的紧张度，慢慢地，控制还原的速度。动作过程中不要快速、依靠惯性或猛冲的力量。",
                                              u"")
            if name == "hack_squats":
                return self.render.reply_page(u"斜板机械蹲举(Hack Squats) ","http://7xqdbr.com1.z0.glb.clouddn.com/thighs_hack_squats.gif",
                                              u"A.重点锻练部位：股四头肌。",
                                              u"B.开始位置：背靠在斜板蹲举训练机上，两腿并拢，屈膝下蹲，尽可能蹲得深些。收腹紧腰挺胸，紧贴靠背板，将重力架负于肩上。",
                                              u"C.动作过程：吸气，以股四头肌之力将两腿用力伸直立起，把重力架扛起，并尽力收缩股四头肌群，直到两腿伸直，稍停1～3秒钟。然后吐气并缓慢还原，重复动作。",
                                              u"D.训练要点：",
                                              u"1.两腿伸直时，并不要将膝盖完全打直，这样让你把力量放在打直的膝盖上喘息。保持适当的屈度以及股四头肌的紧张，然后再慢慢的放下来。 ",
                                              u"2.在完成动作过程中，身体必须保持挺胸收腹紧腰的姿势，不要松腰弓背。 下蹲时动作要稍慢，使股四头肌在紧张的状态中逐渐伸张，直到大腿约与水平相同。起立时，腰臀部自然的向前顶。",
                                              u"3.不要利用屈膝反弹、惯性或猛冲的力量；当立起把腿伸直时，保持大腿股四头肌群的紧张感并彻底紧缩。")
            if name == "leg_extension":
                return self.render.reply_page(u"前抬腿(Leg extension)","http://7xqdbr.com1.z0.glb.clouddn.com/thighs_leg_extension.gif",
                                              u"A.重点锻练部位：大腿股四头肌。",
                                              u"B.开始位置：两脚背面分别紧勾住伸腿机的下托垫棍。两手握住凳的两边稳住。 ",
                                              u"C.动作过程：以股四头肌的收缩力，使两腿伸直，并维持这个静止收缩状态约一至两秒后，慢慢的放回原位，还原过程中亦要保持股四头肌的紧张，不要放松。 ",
                                              u"D.训练要点：",
                                              u"1.脚抬起（伸直）时速度不要猛冲，切记是使用四头肌的力量举起。放下时也不要将四头肌完全放松，保持四头肌的力量慢慢放回原位。",
                                              u"",
                                              u"")                                                                                       
            if name == "dumbbell_lunges":
                return self.render.reply_page(u"哑铃跨步蹲举(Dumbbell lunges) ","http://7xqdbr.com1.z0.glb.clouddn.com/thighs_dumbbell_lunges.gif",
                                              u"A.重点锻练部位：臀大肌、股二头肌（腿筋）和股四头肌。 ",
                                              u"B.开始位置：两脚并拢，双手持哑铃（或可持杠铃置于颈后肩上）。",
                                              u"C.动作过程：将右脚向前跨出一大步，并慢慢向前蹲下，当下蹲至最低位置时，两腿同时伸起，右脚向后收回恢复站立姿。重复上述动作，左、右脚交替训练。 ",
                                              u"D.训练要点：",
                                              u"1.在下蹲和起立过程中，当腿即将伸直或快将要弯曲到尽头时，股四头肌的施力会特别多。",
                                              u"",
                                              u"")
            if name == "stifleg_deadlifts":
                return self.render.reply_page(u"直膝硬拉(Stif-leg Deadlifts；Barbell Straight-back Straight-leg Deadlift) ","http://7xqdbr.com1.z0.glb.clouddn.com/thighs_stifleg_deadlifts.gif",
                                              u"A.重点锻练部位：股二头肌。",
                                              u"B.开始位置：两脚张开与肩同宽，握住横杠，两手间距略比肩宽。两手悬垂握住横杠贴近身体，置于股四头肌前方，挺胸收腹，挺直腰背，平视前方。",
                                              u"C.动作过程：膝盖保持伸直，弯曲腰背将杠往下放，直到股二头肌有紧绷感；然后缓缓将腰挺直，把杠拿起，当动作完成杠举起至最高处时，将肩往后拉。重复动作。",
                                              u"D.训练要点：",
                                              u"1.杠铃移动的路线保持在与水平垂直的一直线上，也就是，沿着身体直线上下移动便是。",
                                              u"2.不要举得太重，这个动作需保持膝盖伸直，对下背的负担较大。 ",
                                              u"3.抓握杠铃时，两手各采一正一反握的方式可加强抓力。保持手臂、背部、膝盖挺直。")
            if name == "smithmachine_squats":
                return self.render.reply_page(u"史密斯架蹲举(Smith-machine squats) ","http://7xqdbr.com1.z0.glb.clouddn.com/thighs_smithmachine_squats.gif",
                                              u"A.重点锻练部位：股四头肌。 ",
                                              u"B.开始位置：立于蹲举架（或Smith Machine）下方，将杠铃置于颈后肩上，两手握住横杠的两端，使杠铃重心两边平衡。两脚分开约与肩同宽，脚尖稍向外分开，膝盖稍微弯曲，两腿可稍向前移。",
                                              u"C.动作过程：两眼平视正前方。两膝慢慢弯屈，下蹲直到大腿的位置约同水平。当大腿下蹲至水平位置时，稍停后即慢慢伸直至回原位置。 ",
                                              u"D.训练要点：",
                                              u"1.在整个下蹲和起立的过程中，保持身体腰背挺直，头部稍微抬起，两眼平视正前方。 ",
                                              u"2.两腿稍向前移，可加强对股二头肌的刺激。 ",
                                              u"3.脚掌始终平贴于地。")
        if group == "abs":
            if name == "crunchs":
                return self.render.reply_page(u"仰卧起坐(Crunchs) ","http://7xqdbr.com1.z0.glb.clouddn.com/abs_crunchs.gif",
                                              u"A.重点锻炼部位：上腹部。",
                                              u"B.开始位置：身体平躺在地上，将小腿搁置于凳上，并使大腿垂直于地面，两手可以交叉在胸前或以手掌平贴于耳际。",
                                              u"C.动作过程：收缩腹肌，弯腰，肩膀尽量向膝盖靠近；稍停，再慢慢回复到开始位置",
                                              u"D.训练要点：",
                                              u"1.将下背紧贴地面，能使腹部肌群在弯曲收缩时，得到更佳的收缩效果。",
                                              u"2.采用负重训练可加强训练效果。可以用双手抱杠片加重进行此动作训练。",
                                              u"3.动作中避免使用瞬间反弹的冲力。 4.不要将双手紧抱于头颈后，会有拉伤颈椎的可能。")
            if name == "lying_leg_raises":
                return self.render.reply_page(u"仰卧腿上举(Lying leg raises) ","http://7xqdbr.com1.z0.glb.clouddn.com/abs_lying_leg_raises.gif",
                                              u"A.重点锻炼部位：下腹部，辅助肌群为大腿上部弯屈肌群。 ",
                                              u"B.开始位置：平躺在凳上，将下背紧贴凳面，两腿弯曲并拢放松。",
                                              u"C.动作过程：身体和下背部贴紧凳面，把腿向上抬起至大腿与身体呈垂直，稍停，慢慢放下。重覆动作。 ",
                                              u"D.训练要点：",
                                              u"1.将背部紧贴凳面，能使下腹肌群能得到较强的收缩。如果下背弯屈或离开凳面，会影响下腹肌群的收缩效果。 ",
                                              u"2.为了加强训练强度，也可以仰卧在上斜板（头上脚下）上来练。",
                                              u"")
            if name == "side_crunchs":
                return self.render.reply_page(u"侧身仰卧起坐(Side Crunchs)","http://7xqdbr.com1.z0.glb.clouddn.com/abs_side_crunchs.gif",
                                              u"A.重点锻炼部位：侧腹肌。",
                                              u"B.开始位置：以身体右侧，侧躺在垫子上，以训练左侧腹肌；靠地面的一手使身体平衡，另一手可置于头部。 ",
                                              u"C.动作过程：动作时，身体向左侧上方弯曲，注意侧腹肌的使力，稍停后慢慢回到起使位置，再重复动作。左右侧轮替。",
                                              u"D.训练要点：",
                                              u"无",
                                              u"",
                                              u"")
            if name == "bottom_forearm_wrist_curls":
                return self.render.reply_page(u"正提腕弯举(Bottom Forearm Wrist Curls)","http://7xqdbr.com1.z0.glb.clouddn.com/abs_bottom_forearm_wrist_curls.gif",
                                              u"A.重点锻炼部位：前臂肌群(前臂内侧的屈指肌)",
                                              u"B.开始位置：坐在凳的一端，两手掌心向上握住杠铃，间距约一个或二个拳头宽，使两前臂贴放在凳上，手腕放松，掌根部位置于凳的边缘以便手腕运动。",
                                              u"C.动作过程：手腕慢慢垂下，稍停之后用力将杠铃弯举起直至不能再高时为止。然后慢慢再放回原位。重覆动作。",
                                              u"D.训练要点：",
                                              u"1.手掌心向上的腕弯举（正提腕弯举），主要是练前臂内侧的屈指肌。",
                                              u"2.手掌心向下的腕弯举（反手提腕弯举），主要是练前臂外侧的伸指肌。",
                                              u"3.用力时以腕为轴，用前臂的肌肉力量，尽力将杠铃提起。也可以做反手提腕弯举，用同样间距，掌心向下，握住杠铃，手腕下垂，掌根部位紧靠凳缘。动作方法相同。")
            if name == "top_forearm_wrist_curls":
                return self.render.reply_page(u"反手提腕弯举(Top Forearm Wrist Curls) ","http://7xqdbr.com1.z0.glb.clouddn.com/abs_top_forearm_wrist_curls.gif",
                                              u"A.重点锻炼部位：前臂肌群(前臂外侧的伸指肌) ",
                                              u"B.开始位置：这个动作利用到弯举椅；坐在凳上，掌心朝下握住杠铃，间距约一至二个拳头宽，将前臂置放于斜板上缘，提杠前臂悬于斜板上，腕部放松。 ",
                                              u"C.动作过程：以前臂施力，手腕为轴，将杠铃提起至手腕能弯起的最高处，稍停，再慢慢将杠铃放下。重覆动作。",
                                              u"D.训练要点：",
                                              u"1.用力时以腕为轴，用前臂的肌肉力量，尽力将杠铃提起。",
                                              u"2.此动作亦可使用平板凳，动作大致与前述的正提腕弯举相同。即，用同样间距，掌心向下，握住杠铃，手腕下垂，掌根部位紧靠凳缘。动作方法同上。 ",
                                              u"3.杠铃下放的过程中，前臂保持施力，不要全然的放松力量让杠铃自由落下。")
            if name == "seated_calfraise":
                return self.render.reply_page(u"坐姿提踵(Seated calfraise) ","http://7xqdbr.com1.z0.glb.clouddn.com/abs_seated_calfraise.gif",
                                              u"A.重点锻炼部位：小腿肌群。 ",
                                              u"B.开始位置：坐在凳上，将前脚掌置于踏板上，在两膝盖上负重物或杠铃，以两手托住不使其滑动。 ",
                                              u"C.动作过程：吸气，以小腿三头肌（腓肠肌）的力量，将脚跟提起到最高位置，使小腿肌肉完全收紧，稍停之后，吐气，慢慢还原。重覆动作。",
                                              u"D.训练要点：",
                                              u"1.将两脚前掌置于踏板上，脚跟露于踏垫外；需特别注意，在运动时，是以前脚掌为支点来运动，不要用到脚趾。",
                                              u"",
                                              u"")
        if group == "back":
            if name == "front_chinups":
                return self.render.reply_page(u"颈后引体向上(Chin-up behind neck)/胸前引体向上(Front chin-ups)","http://7xqdbr.com1.z0.glb.clouddn.com/back_front_chinups.gif",
                                              u"A.重点锻练部位：背阔肌，肩部肌群。",
                                              u"B.开始位置：以正手宽握横杆，先将两臂放松身体悬垂在单杠下方。腰背放松，尽量将背阔肌伸展。",
                                              u"C.动作过程：吸气，集中以背阔肌施力，弯曲手臂引体上拉至颈后（胸前），尽量使单杠接近颈后（胸前），稍停2-3秒。然后吐气，以背阔肌的力量控制住，使身体慢慢下降还原，不要将背阔肌力量突然的放松下降。重复动作。",
                                              u"D.训练要点：",
                                              u"1. 身体不要前后摆动利用惯性。",
                                              u"2. 全身下放时，肩胛部要放松，使背阔肌充分伸张。",
                                              u"")
            if name == "barbell_bent_rows":
                return self.render.reply_page(u"杠铃曲体划船(Barbell bent rows)","http://7xqdbr.com1.z0.glb.clouddn.com/back_barbell_bent_rows.gif",
                                              u"A.重点锻练部位：背阔肌，辅助肌斜方肌、脊下肌、后三角肌、肱二头肌和前臂。",
                                              u"B.开始位置：两脚张开约与肩同宽，上体前曲至与地面平行，两膝微弯，下背肌群勿过度紧绷。两手间距比肩宽，握住杠铃。",
                                              u"C.动作过程：将杠铃沿身体提起，使杠铃接近上腹部，再慢慢放下还原，重复动作。",
                                              u"D.训练要点：",
                                              u"1.如果两手间距较窄的话，会使不同部位的肌群受到刺激。",
                                              u"2.在提起杠铃时，应感到背部肌群的施力，而不是只是把重量向上提而已。",
                                              u"")
            if name == "hyperextensions":
                return self.render.reply_page(u"俯身挺背(Hyperextensions)","http://7xqdbr.com1.z0.glb.clouddn.com/back_hyperextensions.gif",
                                              u"A.重点锻练部位：下背部肌群。",
                                              u"B.开始位置：俯卧垫上，将两脚固定好，两手抱头或置于背后或双手抱胸。",
                                              u"C.动作过程：身体向前弯下，然后再以腰背肌力量，挺身还原。重复动作。",
                                              u"D.训练要点：",
                                              u"1.在动作过程中，腰背部保持挺直，不要松腰含胸弓背。",
                                              u"2.身体向前弯曲时，尽量把速度放慢，切忌突然快速，以防腰背部肌肉拉伤。",
                                              u"")
            if name == "standing":
                return self.render.reply_page(u"站姿负重俯身挺背","http://7xqdbr.com1.z0.glb.clouddn.com/back_standing.gif",
                                              u"A.重点锻练部位：下背部肌群。",
                                              u"B.开始位置：两手持杠铃抓稳置于颈后肩上，挺胸收腹紧腰。",
                                              u"C.动作过程：吸气，身体向前弯下，至腰背部与地面平行，臀部自然地向后移，使身体重心处于脚跟后方，稍停3-4秒。再以腰背肌肉的力量，挺身还原，还原后自然呼吸。重复动作。",
                                              u"D.训练要点：",
                                              u"1.在动作过程中，腰背部保持挺直，不要松腰含胸弓背。",
                                              u"2.身体向前弯曲时，尽量把速度放慢，切忌突然快速，以防腰背部肌肉拉伤。",
                                              u"")
            if name == "front_pulldown":
                return self.render.reply_page(u"坐姿滑轮颈前下拉(Front pull-down)","http://7xqdbr.com1.z0.glb.clouddn.com/back_front_pulldown.gif",
                                              u"A.重点锻练部位：主要训练部位为上背肌、背阔肌；其次辅助肌为前三角肌、斜方肌、和上臂肌。",
                                              u"B.开始位置：坐在拉背机的固定座上，两手分别握住上方横杠两端的把柄，两手间距比肩宽。",
                                              u"C.动作过程：吸气，自上方位置将横杆垂直下拉至胸前，稍停2-3秒钟。然后吐气，沿原路缓慢还原。重复做。",
                                              u"D.训练要点：",
                                              u"1.完成动作时两臂要平均用力，避免猛拉或无控制地放松还原。",
                                              u"",
                                              u"")
            if name == "pulley_rowing":
                return self.render.reply_page(u"滑轮坐姿划船(Pulley Rowing)","http://7xqdbr.com1.z0.glb.clouddn.com/back_pulley_rowing.gif",
                                              u"A.重点锻练部位：背阔肌和上背肌群。",
                                              u"B.开始位置：坐在拉力机座上，屈膝，两手握住拉力机把手，身体向前倾。",
                                              u"C.动作过程：吸气，以背阔肌用力，两臂向后方拉动牵引绳​​，身体自然向后仰，挺胸，至把手触及胸腹。稍停2-3秒。然后吐气，缓慢还原。重复动作。",
                                              u"D.训练要点：",
                                              u"1.动作做得要完整，肌肉收缩要充分，防止猛拉或猛放动作。",
                                              u"",
                                              u"")
            if name == "dumbbell_onearm_rows":
                return self.render.reply_page(u"哑铃单臂划船(Dumbbell One-arm Rows)","http://7xqdbr.com1.z0.glb.clouddn.com/back_dumbbell_onearm_rows.gif",
                                              u"A.重点锻练部位：背阔肌，其次为肱二头肌。",
                                              u"B.开始位置：立姿训练，采弓箭步。左脚前跨，身体前曲约与地面平行。右手持哑铃，拳眼向前，垂于体侧。",
                                              u"C.动作过程：将哑铃向上提起至肩膀接近肩膀，当哑铃上拉时，集中用背阔肌肉的力量。然后循原路慢慢放下还原。",
                                              u"D.训练要点：",
                                              u"1.当哑铃提起至最高点时，同时使身体稍微向另一侧转体，更利于背部肌群的彻底收缩。",
                                              u"2.若以长凳为辅，则可将右腿屈膝跪在长凳上，左手扶在凳面，其余动作相同。",
                                              u"")
            if name == "tbar_rows":
                return self.render.reply_page(u"T-bar划船(T-bar rows)","http://7xqdbr.com1.z0.glb.clouddn.com/back_tbar_rows.gif",
                                              u"A.重点锻练部位：背阔肌中上部肌群。",
                                              u"B.开始位置：跨立在T-bar划船机上，两腿自然伸直，挺胸弓腰体前屈，两手伸直握住把柄。",
                                              u"C.动作过程：吐气，用背阔肌的收缩力量，将T杠提起至胸腹间，稍停2-3秒。然后吐气，将杠缓慢放下还原。",
                                              u"D.训练要点：",
                                              u"1.将杠拉起时两臂要贴近体侧，身体要保持挺胸，利于背阔肌的收缩。放下时，两肩胛骨应放松，使背阔肌充分伸展，不要使T-bar触地。",
                                              u"",
                                              u"")
            if name == "deadlifts":
                return self.render.reply_page(u"硬拉(Deadlifts)","http://7xqdbr.com1.z0.glb.clouddn.com/back_deadlifts.gif",
                                              u"A.重点锻练部位：下背肌、臀部。",
                                              u"B.开始位置：两脚张开与肩同宽，半蹲姿握住横杠，两手间距比肩宽，挺胸收腹，腰背挺直，平视前方。",
                                              u"C.动作过程：意识集中于腿和腰背肌的力量，依次将腰、膝盖挺直，将杠铃提起直至全身直立，当动作完成杠举起至最高处时，将肩往后拉；再弯屈膝腰将杠下放，不要触地。重复动作。",
                                              u"D.训练要点：",
                                              u"1.杠铃尽量靠近身体，移动的路线，保持在与水平垂直的一直线上，也就是，沿着身体直线上下移动便是。",
                                              u"2.保持手臂、背部伸直。",
                                              u"")
        if group == "shoulders":
            if name == "smith_machine_press":
                return self.render.reply_page(u"杠铃胸前推举(Smith Machine press)","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_smith_machine_press.gif",
                                              u"A.重点锻炼部位：三角肌，辅助肌群肱三头肌、胸大肌、斜方肌和背部。",
                                              u"B.开始位置：双手上举，正握住杠铃，两手间距比肩宽。掌心向上，托住杠铃。",
                                              u"C.动作过程：撑住杠铃，把杠铃缓缓放下，直到杠铃下放至接近锁骨的上方；稍停，再以三角肌之力将杠垂直向上推，直到启始位置。",
                                              u"D.训练要点：",
                                              u"1.上推时，身体不要后仰。不要在推举时憋住气。",
                                              u"2.将意识集中在三角肌上，运用三角肌的力量进行训练。别把施力的重点放在前臂或三头肌。",
                                              u"")
            if name == "dumbbell_shoulder_press":
                return self.render.reply_page(u"坐姿哑铃推举(Dumbbell Shoulder Press)","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_dumbbell_shoulder_press.gif",
                                              u"A.重点锻炼部位：三角肌。这个动作能锻炼上半身的大肌肉群。其他会牵动到的肌群有斜方肌、上胸肌、肱三头肌、和上背肌群。",
                                              u"B.开始位置：双手持哑铃，弯曲手臂将哑铃举起至头部耳侧。",
                                              u"C.动作过程：将哑铃向上垂直推起，至手臂伸直（手肘不锁死），稍停，再慢慢放下至起点。",
                                              u"D.训练要点：",
                                              u"1.使用哑铃训练，比之杠铃有较大的自由度。",
                                              u"2.上推时，身体不要后仰。系上重训腰带可以给予辅助。",
                                              u"3.训练中将意识集中在三角肌，运用三角肌之力。注意别把施力的重点放在前臂或三头肌。")
            if name == "barbell_press_behind_neck":
                return self.render.reply_page(u"杠铃颈后推举(Barbell Press Behind Neck)","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_barbell_press_behind_neck.gif",
                                              u"A.重点锻炼部位：三角肌。这个动作能锻炼身体上部的大肌肉群。辅助肌群为斜方肌、上胸肌、肱三头肌、和上背肌群。",
                                              u"B.开始位置：双手正抓杠铃，把横杠置于颈后肩上。",
                                              u"C.动作过程：两手握距比肩宽，将杠铃推起至两臂伸直。再慢慢放下至颈后肩上方。",
                                              u"D.训练要点：",
                                              u"1.如果定期改变两手间的握距，可锻炼到不同的部位的肌肉获得不同的训练成果。",
                                              u"2.宽握对锻炼三角肌较有利，窄握则偏重于锻炼肱三头肌。",
                                              u"")
            if name == "bent_over_lateral_raise":
                return self.render.reply_page(u"俯立侧平举(Bent Over Lateral Raise)","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_bent_over_lateral_raise.gif",
                                              u"A.重点锻炼部位：后三角肌，其次为上背肌群。",
                                              u"B.开始位置：两脚张开与肩同宽，两膝稍微弯屈，上半身向下弯曲至大约与地面平行。两手持哑铃，掌心相对，悬垂于膝前。下背部放松。",
                                              u"C.动作过程：两手持铃向两侧平举起，直至上臂与背部平行，稍停，再放下哑铃还原。重覆动作。",
                                              u"D.训练要点：",
                                              u"1.手肘保持微弯，不要打直。",
                                              u"2.向两侧举起时，使手肘和腕部保持稍微弯屈，可以使三角肌群得到更好的刺激。同时也更能专注于三角肌的训练，避免关节受伤。",
                                              u"3.在整个动作过程中，意识要集中在要训练的肌群（三角肌）上。")
            if name == "side_laterals_raises":
                return self.render.reply_page(u"立姿侧平举(Side Laterals Raises)","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_side_laterals_raises.gif",
                                              u"A.重点锻炼部位：三角肌外侧中束部位。",
                                              u"B.开始位置：两手各持哑铃垂于体侧，两肘稍弯屈，拳眼向前。",
                                              u"C.动作过程：两手同时向两侧举起，直到与头部齐高位置。然后慢慢地循原路落下回原位，重复动作。",
                                              u"D.训练要点：",
                                              u"1.在提起和放下过程中，保持手肘和手腕稍微弯屈，更能加强对三角肌的刺激。",
                                              u"2.动作过程中加上腕部的转动，能加强对三角肌的刺激。当哑铃向两侧提起时，转动手腕使哑铃与地面呈垂直， 直到手臂举起至最高位置。当哑铃落下时，手腕回复原状态。",
                                              u"")
            if name == "upright_rows":
                return self.render.reply_page(u"立正划船(Upright Rows)","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_upright_rows.gif",
                                              u"A.重点锻炼部位：前三角肌，辅助肌群是斜方肌，肱二头肌和前臂。",
                                              u"B.开始位置：采正手抓举，手掌背向前，握住横杠，两手间距约与肩同宽，两臂提杠垂于腿前。",
                                              u"C.动作过程：将杠铃沿身体慢慢提起，两肘保持在杠铃上方，上拉至接近锁骨前，稍停。再慢慢沿身体放下至腿前。重覆动作。",
                                              u"D.训练要点：",
                                              u"1.训练过程将意识集中在三角肌，提起或放下时都不要将三角肌放松。",
                                              u"2.以三角肌控制速度，放下杠铃的速度要慢，上提时的速度可以稍快。",
                                              u"3.身体不要前后晃动，也不要借惯性或猛冲的力量。")
            if name == "dumbbell_front_raises":
                return self.render.reply_page(u"立姿哑铃前抬举(Dumbbell Front Raises)","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_dumbbell_front_raises.gif",
                                              u"A.重点锻炼部位：主要训练部位是前三角肌，次为上胸肌外侧。",
                                              u"B.开始位置：两手各持哑铃，下垂于腿前，手掌心向后。",
                                              u"C.动作过程：肘部稍屈，把哑铃向前上方举起，直至视线平行的高度。然后，慢慢放下还原，重覆动作。",
                                              u"D.训练要点：",
                                              u"1.注意运用的肌群，施力不正确时容易在训练以后感到颈部（斜方肌一带）酸痛。",
                                              u"",
                                              u"")
            if name == "cable_onearm_front_laterals":
                return self.render.reply_page(u"滑轮单手前胸侧平举(Cable one-arm front laterals)","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_cable_onearm_front_laterals.gif",
                                              u"A.重点锻炼部位：三角肌外侧中束部位。",
                                              u"B.开始位置：利用Smith Machine，单手持把柄垂于体前，两肘保持稍弯屈，拳眼向前；闲置的另一手可以抓住Smith杆以便平衡。",
                                              u"C.动作过程：单手持拉柄向侧边举起，至约与肩部齐高位置。再慢慢地循原路落下回原位，再重覆动作。左右手交替。",
                                              u"D.训练要点：",
                                              u"",
                                              u"",
                                              u"")
            if name == "cable_cross_bent_laterals":
                return self.render.reply_page(u"绳索交错俯立侧平举(Cable cross bent laterals)","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_cable_cross_bent_laterals.gif",
                                              u"A.重点锻炼部位：后三角肌，其次为上背肌群。",
                                              u"B.开始位置：两脚分开约与肩同宽，两手掌心相对握住拉力器把柄，身体向前屈至约与地面平行，两腿稍屈，下背放松。",
                                              u"C.动作过程：两手将拉柄交错向两侧举起，直至上臂与背部平行，稍停，将把柄慢慢放下还原。重复动作。",
                                              u"D.训练要点：",
                                              u"",
                                              u"",
                                              u"")
            if name == "barbel":
                return self.render.reply_page(u"杠/哑铃耸肩(Barbel / Dumbell Shrug)","http://7xqdbr.com1.z0.glb.clouddn.com/shoulders_barbel.gif",
                                              u"A.重点锻炼部位：主要训练部位在肩侧斜方肌，其次为颈部肌和上背肌群。",
                                              u"B.开始位置：采正手抓举，手肘伸直，持杠铃或哑铃，两手掌背向前，垂于腿前。",
                                              u"C.动作过程：两肩向上耸起，使肩尽量触及耳朵，然后在这个顶点位置上慢慢地使两肩向后转，再慢慢由后向下前转至两臂下垂的原位。重覆动作。",
                                              u"D.训练要点：",
                                              u"1.在耸肩过程中，手肘伸直，不要弯屈。",
                                              u"2.这个动作也可以采用哑铃来进行，方法相同。",
                                              u"")
        return self.render.reply_text(u"Unknown cmd, contact @vincenth")
