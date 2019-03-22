#coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from time import sleep
import time
import re





def get_items_list(num_of_items,type,file_name):
	#iOS platform
	if type==1:
		url='https://stzb.cbg.163.com/cgi/mweb/pl/role?platform_type=1' 
	else:
		url='https://stzb.cbg.163.com/cgi/mweb/pl/role?platform_type=2'

	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')
	driver = webdriver.Chrome(chrome_options=chrome_options)
	scroll_num=num_of_items/15

	driver.get(url)
	sleep(2)
	js = "window.scrollTo(0,document.body.scrollHeight)" 
	for i in range(0,scroll_num):
		driver.execute_script(js)
		sleep(2)
		print 'scrolling...'+str(i+1)


	pageSource=driver.page_source
	print 'source code got\n'
	# print pageSource
	# driver.find_elements_by_xpath("//div[@class='product-item list-item list-item-link']")[0].click()
	# sleep(3)
	# print driver.page_source



	links=driver.find_elements_by_xpath("//div[@class='product-item list-item list-item-link']")
	length=len(links)           #列表的长度，一共有多少个a标签
	print length,'  items detected\n'
	f=open(file_name,'w')
	if num_of_items>length:
		num_of_items=length
	for i in range(0,num_of_items):   #遍历列表的循环，使程序可以逐一点击
		try:
			# print "locating href......................."
			links=driver.find_elements_by_xpath("//div[@class='product-item list-item list-item-link']")    #在每次循环内都重新获取a标签，组成列表
			# print "href located"
			links[i].click()
			sleep(3)           #留出加载时间
			# print "href clicked"
			# print driver.find_element_by_xpath("//*").get_attribute("outerHTML")
			server_tag=driver.find_element_by_xpath("//span[@class='area-server icon-text']").text
			# print "area server located"
			title=driver.find_element_by_xpath("//span[@class='price icon-text']").text   #.text的意思是指输出这里的纯文本内容
			# print "price located"

			f.write(server_tag+"\t"+title+"\t"+driver.current_url+'\n')
			print 'item '+str(i+1)+'  marked'
			driver.back()           #后退，返回原始页面目录页
			# print "returned to lists.......................\n--------------------------------------------------------------------"
			sleep(1)           #留出加载时间
		except:
			print 'timeout exception.......................'
			driver.quit()
			print 'restart driver................'
			driver = webdriver.Chrome(chrome_options=chrome_options)
			print 'driver restarted'
			driver.get(url)
			sleep(2)
			js = "window.scrollTo(0,document.body.scrollHeight)" 
			for j in range(0,scroll_num):
				driver.execute_script(js)
				sleep(2)
				print 'scrolling...'+str(j+1)
			print "reload page succeeded!"
			continue 
		      
		
	f.close()
	driver.quit()
	print 'Finished!'

if __name__ == '__main__':
	now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
	item_type=2
	item_num=500

	fname="itemlists_type_"+str(item_type)+"_"+str(item_num)+"_"+now+".txt"

	get_items_list(500,item_type,fname)