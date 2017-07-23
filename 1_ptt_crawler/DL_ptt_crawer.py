#-*- coding: utf-8 -*-　

# use: python 2.7

# reference:
# https://github.com/zake7749/PTT-Crawler
# https://github.com/wy36101299/PTTcrawler/blob/master/pttcrawler.py

import json
import requests
import time, os, re

from bs4 import BeautifulSoup
from bs4.element import NavigableString


# setting
save_dir_path = '/crawler_save'
crawler_board = 'Gossiping' # 'WomenTalk'
crawler_from = 0
crawler_to = 1000 

def main():
	if not os.path.exists(save_dir_path):
		os.makedirs(save_dir_path)
	crawler = PttCrawler()
	crawler.crawl(board=crawler_board, start=crawler_from, end=crawler_to)

class PttCrawler(object):

	root = "https://www.ptt.cc/bbs/"
	main = "https://www.ptt.cc"
	gossip_data = {
		"from":"bbs/Gossiping/index.html",
		"yes": "yes"
	}

	def __init__(self):
		self.session = requests.session()
		requests.packages.urllib3.disable_warnings()
		self.session.post("https://www.ptt.cc/ask/over18",
						   verify=False,
						   data=self.gossip_data)

	def articles(self, page):
		res  = self.session.get(page,verify=False)
		soup = BeautifulSoup(res.text, "lxml")
		for article in soup.select(".r-ent"):
			try:
				yield self.main + article.select(".title")[0].select("a")[0].get("href")
			except:
				pass 

	def pages(self, board=None, index_range=None, output_dir="result/"):
		target_page = self.root + board + "/index"
		if range is None:
			yield target_page + ".html"
		else:
			for index in index_range:
				yield target_page + str(index) + ".html"

	def parse_article(self, url):
		raw  = self.session.get(url, verify=False)
		soup = BeautifulSoup(raw.text, "lxml")
		try:
			article = {}
			article["Author"] = soup.select(".article-meta-value")[0].contents[0].split(" ")[0]
			article["Board"]  = soup.select(".article-meta-value")[1].contents[0]
			article["Title"]  = soup.select(".article-meta-value")[2].contents[0]
			article["Date"]  = soup.select(".article-meta-value")[3].contents[0]
			content = ""
			for tag in soup.select("#main-content")[0]:
				if type(tag) is NavigableString and tag !='\n':
					content += tag
					break
			article["Content"] = content
			findIPtag = u'※ 發信站:'

            # deal different ip type
			try:	
				ip_temp = soup.find(string = re.compile(findIPtag))
				ip_temp = re.search(r"[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*", ip_temp).group()
			except:
				try:
					ip_temp = 'NA'
					f2_content = soup.select('.f2')
					for content in f2_content:
						if findIPtag in content.contents[0]:
							ip_temp = content.next_sibling.split()[-1]
							break
				except:
					ip_temp = 'NA'
			article["IP"] = ip_temp 

			upvote = 0
			downvote = 0
			novote = 0
			response_list = []

			for response_struct in soup.select(".push"):
				if "warning-box" not in response_struct['class']:
					response_dic = {}
					response_dic["Content"] = response_struct.select(".push-content")[0].contents[0][1:]
					response_dic["Vote"]  = response_struct.select(".push-tag")[0].contents[0][0]
					response_dic["User"]  = response_struct.select(".push-userid")[0].contents[0]
					response_list.append(response_dic)
					if response_dic["Vote"] == u"推":
						upvote += 1
					elif response_dic["Vote"] == u"噓":
						downvote += 1
					else:
						novote += 1

			article["Responses"] = response_list
			article["UpVote"] = upvote
			article["DownVote"] = downvote
			article["NoVote"] = novote
		except Exception as e:
			print(e)
			print(u"error in: %s " % url)

		return article

	def output(self, filename, data):
		save_path = save_dir_path + filename
		with open(save_path + ".json", 'w') as op:
			op.write(json.dumps(data, indent=4, ensure_ascii=False).encode('utf-8'))

	def crawl(self, board="Gossiping", start=1, end=2, sleep_time=0.5):
		crawl_range = range(start, end)
		for page in self.pages(board, crawl_range):
			print(u"now in %s board, page: %d ..." %(board,start))
			res = []
			for article in self.articles(page):
				res.append(self.parse_article(article))
				time.sleep(sleep_time)
			self.output(board + '_' + str(start), res)

			print(u"finish %s board, page: %d " %(board,start))
			start += 1
		print 'save dir: ', save_dir_path

if __name__ == '__main__':
	main()










