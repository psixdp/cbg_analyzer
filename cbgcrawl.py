#coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from time import sleep
import re

def write_html(str,text):
	f=open(str,'r+')
	for i in text:
		# f.write(i[0]+' '+i[1]+' '+i[2])
		# f.write(i[0]+' '+i[1])
		# f.write(i[0]+' '+i[1]+' '+i[2]+' '+i[3])
		# f.write(i[0]+' '+i[1]+' '+i[2]+' '+i[3])
		f.write(i[0]+'\t'+i[1]+'\t'+i[2]+'\t'+i[3])

		f.write('\n')
	f.close()

def load_html(str):
	f=open(str,'r')
	text=f.read()
	f.close()
	return text





if __name__ == "__main__":
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')
	driver = webdriver.Chrome(chrome_options=chrome_options)


	url="https://stzb.cbg.163.com/cgi/mweb/equip/1/201903070702116-1-WY1FUIPCXUX5XI?view_loc=search"
	driver.get(url)
#-------等待加载武将页面完成
	sleep(3)
	html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
	# pageSource=driver.page_source
	# #print pageSource
	# reg=r'<div class=\"state-wrap state[0-9]\"><i class="ico\">(.*?)</i></div><div class=\"best-wrap\"><i class=\"ico\">(.*?)</i></div>[\s\S]*?<div class=\"name tC\">\s*?(\S*?)\s*?</div>'
	# reg=r'<div class=\"name tC\">\s*?(\S*?)\s*?</div>'

#-------这一段是武将页面
	# reg=r'<div class=\"state-wrap state[0-9]\"><i class="ico\">(.*?)</i></div><div class=\"best-wrap\"><i class=\"ico\">(.*?)</i></div>[\s\S]*?<div class=\"stars-wrap\">((?:\+|\-)*)[\s\S]*?<div class=\"name tC\">\s*?(\S*?)\s*?</div>'

	# re_ques=re.compile(reg)
	# html=load_html("webhtml.txt")
	
	# html_text=html.replace('<!---->','<div class="best-wrap"><i class="ico">None</i></div>')
	# html_text=html_text.replace('<span class="star up"><i class="ico">⭐</i></span>','+')
	# html_text=html_text.replace('<span class="star"><i class="ico">⭐</i></span>','-')

	# card=re_ques.findall(html_text)
	# # #print [i.decode('unicode_escape') for i in card]
	# print card
	# for i in card:
	# 	print i[0],i[1],i[2],i[3]
	# write_html("reg_result.txt",card)	

	
	# tab=driver.find_elements_by_class_name("战法")
	# tab=driver.find_element_by_xpath("//a[contains(@href, 'javascript:;')]")
#-------武将页面结束
	#跳转到战法标签页
	driver.find_element_by_xpath("//a[text()='战法']").click()
	sleep(3)
	html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")

