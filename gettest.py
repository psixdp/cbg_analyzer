# -*- coding: utf-8 -*-
import urllib2
import json
import re

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
# def parse_dict():




if __name__ == "__main__":
    html = urllib2.urlopen(
        r'https://stzb.cbg.163.com/cgi/api/get_equip_detail?serverid=1&ordersn=201902182002116-1-3KD137FBWRRJN7&view_loc=all_list')
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
    f=open('result/json.txt','w+')
    f.write(source.decode("unicode_escape"))
    f.close()
    print source.decode("unicode_escape")