"""A python module for writing RSS."""
import time
class PageRSS:
	"""A helper class for creating a page's RSS."""
	def __init__(self, title, description, link, date):
		self.items = []
		self.title = title
		self.description = description
		self.link = link
		self.pubDate = time.strftime("%a, %d %b %Y %H:%M:%S %z",date)

	"""Add items to RSS feed."""
	def addItem(self, title, link, desc):
		item = {}
		item['title'] = title
		item['link'] = link
		item['desc'] = desc
		self.items.append(item)

	"""Generates RSS feed."""
	def make(self):
		contents = "<?xml version='1.0' ?><rss version='2.0'><channel><title>{}</title><link>{}</link><description>{}</description><pubDate>{}</pubDate>".format(self.title,self.link,self.description,self.pubDate)
		for i in self.items:
			contents += "<item><title>{}</title><link>{}</link><description>{}</description></item>".format(i['title'],i['link'],i['desc'])
		contents += "</channel></rss>"
		return contents
