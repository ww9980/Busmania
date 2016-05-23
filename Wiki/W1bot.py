import pywikibot
from pywikibot import pagegenerators
site = pywikibot.Site()
f = open('../W1list.txt','r')
for lin in f:
	print('processing with', lin)
	lin = lin.rstrip()
	page = pywikibot.Page(site, lin)
	text = page.text
	new=''
	for line in text.splitlines():
		s = line.find('notability')
		if s>=0:
			continue;
		s = line.find('unreferenced')
		if s>=0:
			continue;
		new= new + line +'\n'
	lin = '../w1/' + lin
	W1write = open(lin,'w')
	W1write.write(new)
print('done')

#此系根据文件中条目名称生成多个以页面名为名的文件脚本

#cat = pywikibot.Category(site,'Category:Living people')
#gen = pagegenerators.CategorizedPageGenerator(cat)
#for page in gen:
  #Do something with the page object, for example:
#  text = page.text