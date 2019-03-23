# -*- coding: utf-8 -*-
import  urllib2
import json
import config_heros
# from sklearn.svm import SVR
import time
import csv

def get_item_ordersn(platform=1,num_of_pages=1):

    ordersn_list=[]
    url_head='https://stzb.cbg.163.com/cgi/api/query?platform_type='+str(platform)+'&order_by=selling_time%20DESC&page='
    if platform==0:
        url_head='https://stzb.cbg.163.com/cgi/api/query?view_loc=all_list&order_by=selling_time%20DESC&page='


    for i in range(1,num_of_pages+1):
        fails=0
        s={}
        while True:
            try:
                if fails>=5:
                    print 'get ordersn page'+str(i)+'failed!'
                    return None
                page_source= urllib2.urlopen(url_head+str(i),timeout=3).read()
                s = json.loads(page_source)

            except:
                fails+=1
            else:
                break
        for item in s['result']:
            # print item['game_ordersn']
            ordersn_list.append(item['game_ordersn'])
        print 'page:',i,len(ordersn_list)
        print s['paging']['is_last_page']
        if s['paging']['is_last_page']:
            print 'last page reached!'
            break
    # print ordersn_list
    return ordersn_list



def get_item_details(ordersn):

    url='https://stzb.cbg.163.com/cgi/api/get_equip_detail?serverid=1&ordersn='+ordersn+'&view_loc=all_list'

    fails=0

    while True:
        try:
            if fails>=5:
                print 'final failure!'
                return None
            page=urllib2.urlopen(url,timeout=2)
            page_source=page.read()
        except:
            fails+=1
            print 'connecting error, retrying:',fails
        else:
            break

    hjson=json.loads(page_source)
    equip_desc=hjson['equip']['equip_desc']
    equip=json.loads(equip_desc)

    price=hjson['equip']['price']
    equip.update({u"price":price})
    # print equip['price']

    return equip
'''
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

    heros=equip['card']


    for hero in heros:
        if hero['quality']==5:
            print hero['name'],hero['awake_state'],hero['advance_num'],hero['season'],hero['country']
    for skill in skills:
        print skill['name']

'''
def details2vector(item_details):
    cbg_cfg=config_heros.get_config()

    v_dian_cang=[0 for i in range(0,len(cbg_cfg['dian_cang']))]
    v_dian_ji=[0 for i in range(0,len(cbg_cfg['dian_ji']))]
    v_hero=[0 for i in range(0,len(cbg_cfg['hero']))]

    v_skill=[0 for i in range(0,len(cbg_cfg['skill']))]
    n_awake=0
    n_type_advance=0

    #价格为负数，样本有误
    if item_details==None:
        return {'n_type_advance':n_type_advance,'n_awake':n_awake,'dian_cang':v_dian_cang,'dian_ji':v_dian_ji,'hero':v_hero,'skill':v_skill,'price':-100}
    #典藏卡，只要查看商品数据是否有该key

    for item in item_details['card_dian_cang']:
        for i in range(len(v_dian_cang)):
            if item['hero_id']==cbg_cfg['dian_cang'][i]['hero_id']:
                v_dian_cang[i]=1

    #
    # print v_dian_cang
    # for i in cbg_cfg['dian_cang']:
    #     print i['name']
    # print '\n'
    # for i in item_details['card_dian_cang']:
    #     print i['name']
    #
    #典籍卡
    for item in item_details['card_dian_ji']:
        for i in range(len(v_dian_ji)):
            if item['hero_id']==cbg_cfg['dian_ji'][i]['hero_id']:
                v_dian_ji[i]=1
    #
    # print v_dian_ji
    # for i in cbg_cfg['dian_ji']:
    #     print i['name']
    # print '\n'
    # for i in item_details['card_dian_ji']:
    #     print i['name']


    # return {'dian_cang':v_dian_cang,'dian_ji':v_dian_ji,'hero':v_hero,'skill':v_skill}
    #技能卡
    for item in item_details['skill']:
        for i in range(len(v_skill)):
            if item['skill_id']==cbg_cfg['skill'][i]['skill_id']:
                v_skill[i]=1

    # print v_skill
    # for i in item_details['skill']:
    #     print i['name']

    # format:{"hit_range": 4, "dynamic_icon": 0, "hero_features": 0, "name": "\u5468\u745c", "hero_type_advance": 0, "awake_state": 1, "country": 4, "is_season_card": 0, "card_border": "", "hero_type_availible": [21], "hero_type": 1, "cost": 3, "season": "N", "icon_hero_id": 100031, "cfg_hero_type_availible": [11, 21], "quality": 5, "advance_num": 0, "hero_id": 100031}

    for item in item_details['card']:
        for i in range(len(v_hero)):
            if item['hero_id']==cbg_cfg['hero'][i]['hero_id']:
                v_hero[i]=v_hero[i]+item['advance_num']+1

    # for item in item_details['card']:
    #     if item['quality']==5:
    #         print item['name'],item['advance_num'],'红，觉醒: ',item['awake_state'],'进阶:',item['hero_type_advance']

    for item in item_details['card']:
        if item['quality']==5 and item['awake_state']==1:
            n_awake=n_awake+1
        if item['quality']==5 and item['hero_type_advance']==1:
            n_type_advance=n_type_advance+1

    # print item_details['price']
    return {'n_type_advance':n_type_advance,'n_awake':n_awake,'dian_cang':v_dian_cang,'dian_ji':v_dian_ji,'hero':v_hero,'skill':v_skill,'price':item_details['price']}


if __name__=="__main__":


    platform=1
    sample_page=1
    ordersn_list=get_item_ordersn(platform,sample_page)
    print 'crawling ordersn: page '+str(sample_page)+'_'+'sample_page'
    heros=[]
    price=[]

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    fname = "result/data_platform_" + str(platform) + "_"+str(len(ordersn_list))+'_samples_' + now + ".csv"

    data_file=open(fname,'wb')
    csv_write = csv.writer(data_file, dialect='excel')


    print len(ordersn_list)
    n=0
    t1 = time.time()
    for sn in ordersn_list:
        n+=1
        item_detail=get_item_details(sn)
        print 'total_time:',time.time()-t1,'processing:',n,'/',len(ordersn_list)
        heros.append(details2vector(item_detail)['hero'])
        price.append(details2vector(item_detail)['price'])
        csv_write.writerow([details2vector(item_detail)['price']]+details2vector(item_detail)['hero'])

    data_file.close()
