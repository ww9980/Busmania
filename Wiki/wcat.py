import pywikibot
import os
from pywikibot import pagegenerators
site = pywikibot.Site()
#os.system(u"pwb.py listpages.py -cat:香港")
f = open('../W1list.txt','r')
fs = open('../w1/file.txt','w', encoding="utf-8")
for lin in f:
	l1 = lin.find('#')
	if l1 >=0:
		continue;
	print('processing with category named', lin)
	lin = lin.rstrip()
	cat = pywikibot.Category(site,'Category:' + lin)
	gen = pagegenerators.CategorizedPageGenerator(cat, recurse=True)
	for page in gen:
		text = page.text
		title = page.title()
		s1 = title.find('File:')
		s2 = title.find('User:')
		if s1>=0:
			continue;
		if s2>=0:
			continue;
		#print(title)
		new=''
		for line in text.splitlines():
			s = line.find('notability')
			if s>=0:
				continue;
			s = line.find('unreferenced')
			if s>=0:
				continue;
			new= new + line +'\n'
		fs.write('{{-start-}}\n')
		fs.write('{t}' + title + '{e}\n')
		fs.write(new)
		fs.write('{{-stop-}}\n')
print('done')

#此系读取文件中的类别们读取该类别下面所有的页面并生成单一文档之脚本
#文件中可以使用井字号#来跳过部分行



#cat = pywikibot.Category(site,'Category:Living people')
#gen = pagegenerators.CategorizedPageGenerator(cat)
#for page in gen:
  #Do something with the page object, for example:
#  text = page.text