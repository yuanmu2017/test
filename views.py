from . import test
import requests
import json
from bs4 import BeautifulSoup
import re

@test.route('/ig')
def test():
	headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			   'Accept-Encoding': 'gzip, deflate, br',
			   'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
			   'Cache-Control': 'max-age=0',
			   'Connection': 'keep-alive',
			   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}
	body = requests.get(url='https://www.instagram.com/nasa/', headers=headers)
	body.encoding = 'utf-8'
	bs = BeautifulSoup(body.text, 'html.parser')
	s = bs.find_all('script')[1].string[:-1]
	dict_string = '{' + s.split('= {')[1]
	return dict_string
 