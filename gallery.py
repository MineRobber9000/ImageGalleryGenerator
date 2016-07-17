import os,config,string,time,cPickle,prss;

pic_html_template = "<h3>{0}</h3><img src='{1}'><p>Added on {3}<br>Comments:<br><em>{2}</em></p>"

print("picture gallery: made by MineRobber9000")
print("---------------------------------------")
if os.path.exists("gallery.pickled"):
	pics = cPickle.load(open("gallery.pickled","rb"))
else:
	pics = []
print("'n' to add a new picture, 'g' to generate the page, and 'q' to quit.")
choice = raw_input("> ")
while choice != '' and choice != "q":
	if choice == "n":
		title = raw_input("Title: ")
		url = raw_input("URL: ")
		comments = raw_input("Comments:\n")
		pics.append({'title':title,'url':url,'comments':comments,'timetuple':time.localtime()})
	elif choice == "g":
		html = "<html><head><title>{0}</title><link rel='stylesheet' href='{2}'></head><body><h1>{0}</h1><h2>curated by {1}</h2>".format(config.TITLE,config.AUTHOR,config.CSS_LOCATION)
		rss = prss.PageRSS(config.TITLE+" by "+config.AUTHOR,config.URL,"A gallery made using MineRobber9000's ImageGalleryGenerator.",time.localtime())
		pics.reverse()
		for pic in pics:
			html += pic_html_template.format(pic['title'],pic['url'],pic['comments'],time.strftime(config.DATE_FORMAT,pic['timetuple']))
			rss.addItem(pic['title'],pic['url'],pic['comments'].replace("<","&lt;").replace(">","&gt;"))
		pics.reverse()
		html += "<hr><p>Generated using MineRobber9000's <a href='https://github.com/MineRobber9000/ImageGalleryGenerator'>ImageGalleryGenerator</a></p>"
		with open(config.LOCATION,'wb') as p:
			p.write(html)
		with open(config.RSS_LOCATION, 'wb') as r:
			r.write(rss.make())
	else:
		print("Invalid choice.")
	cPickle.dump(pics,open("gallery.pickled","wb"))
	choice = raw_input("> ")
