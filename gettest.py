# -*- coding: utf-8 -*-
import urllib2
import json
import re

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
# def parse_dict():
import json
import config_heros






if __name__ == "__main__":
    html = urllib2.urlopen(
        r'https://stzb.cbg.163.com/cgi/api/get_equip_detail?serverid=1&ordersn=201902131602116-1-RKHFMIPQBH1YYO&view_loc=all_list')
    source = html.read()
    hjson = json.loads(source)
    # print
    # print source

    game_config_js_url = 'https://cbg-stzb.res.netease.com/js/game_auto_config.js'

    config = urllib2.urlopen(game_config_js_url).read()


    reg_skill=r'{"skill_type": (\d), "skill_id": (\d*?), "name": "(.*?)"}'
    reg_hero=r'{"name": "(.*?)", "country": "(\d)", "hero_type": (\d), "season": "(.*?)", "icon_hero_id": (\d*?), "quality": (\d), "pinyin": "([a-z]*?)", "hero_id": (\d*?)}'
    reg_dian_cang= r'{"name": "(.*?)", "country": "(\d)", "hero_type": (\d), "season": "(.*?)", "icon_hero_id": ([0-9]*?), "quality": (\d), "hero_id": ([0-9]*?)}'
    # reg_dian_ji=r'{"name": "六韬·文韬", "country": "5", "hero_type": 1, "season": "N", "icon_hero_id": 100403, "quality": 4, "hero_id": 100403}'
    re_ques = re.compile(reg_skill)
    skills=re_ques.findall(config)

    # for skill in skills:
    #     print skill[2].decode("unicode_escape")
    # re_ques=re.compile(reg_hero)
    # heros=re_ques.findall(config)
    # for hero in heros:
    #     print hero[0].decode("unicode_escape"),hero[1],hero[2],hero[3],hero[4],hero[5]

    # re_ques = re.compile(reg_dian_cang)
    # dian_cang = re_ques.findall(config)
    # for hero in dian_cang:
    #     print hero[0].decode("unicode_escape"), hero[1], hero[2], hero[3], hero[4], hero[5]

    # print source.decode("unicode_escape")
    # f=open('result/json.txt','w+')
    # f.write(source.decode("unicode_escape"))
    # f.close()
    #
    equip_desc=hjson['equip']['equip_desc']
    equip=json.loads(equip_desc)

    #format:{"hit_range": 4, "dynamic_icon": 0, "hero_features": 0, "name": "\u5468\u745c", "hero_type_advance": 0, "awake_state": 1, "country": 4, "is_season_card": 0, "card_border": "", "hero_type_availible": [21], "hero_type": 1, "cost": 3, "season": "N", "icon_hero_id": 100031, "cfg_hero_type_availible": [11, 21], "quality": 5, "advance_num": 0, "hero_id": 100031}
    heros=equip['card']

    #format:   {"icon_hero_id": 110502, "hero_id": 110502, "state": 2, "name": "\u51e4\u4eea\u4ead"}
    dian_cangs=equip['card_dian_cang']

    #format:{"icon_hero_id": 100548, "hero_id": 100548, "state": 2, "name": "\u516d\u97ec\u00b7\u864e\u97ec"}
    dian_jis=equip['card_dian_ji']
    #format: {"skill_type": 2, "season": 0, "research_progress": 100, "name": "\u5148\u9a71\u7a81\u51fb", "skill_id": 200233}
    skills = equip['skill']



    features=equip['card_feature']
    dynamic_icons=equip['dynamic_icon']
    platform=equip['platform']
    season_info=equip['season_info']
    server_id=equip['server_id']

    assets=equip['tenure']

    heros=json.loads(hjson['equip']['equip_desc'])['card']
    # for hero in heros:
    #     if hero['quality']==5:
    #         print hero['name'],hero['awake_state'],hero['advance_num'],hero['season'],hero['country']
    # for skill in skills:
    #     print skill['name']



    # parse config:
    f=open('result/config_js_modified.txt','r')
    config_jsobj=f.read()
    f.close()


    cfg=config_heros.get_config()
    print cfg
    cfg = config_heros.get_config()


    #dian_cang{"name": "桃园结义", "country": "5", "hero_type": 1, "season": "N", "icon_hero_id": 110500, "quality": 5, "hero_id": 110500}
    for dian_cang in cfg['dian_cang']:
        print dian_cang['name']
    #hero:{"name": "吕布", "country": "5", "hero_type": 1, "season": "S2", "icon_hero_id": 100479, "quality": 5, "hero_id": 100479}
    for hero in cfg['hero']:
        print hero['name']
    #dian_ji {"name": "六韬·文韬", "country": "5", "hero_type": 1, "season": "N", "icon_hero_id": 100403, "quality": 4, "hero_id": 100403}
    #skill:{"skill_type": 3, "skill_id": 200003, "name": "金吾飞将"}
    #special_hero:{"name": "十常侍", "country": "1", "hero_type": 1, "season": "N", "icon_hero_id": 100002, "quality": 5, "hero_id": 100002}