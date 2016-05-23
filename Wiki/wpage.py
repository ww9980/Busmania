import pywikibot
from pywikibot import pagegenerators
site = pywikibot.Site()
f = open('../W1list.txt','r')
fs = open('../w1/file.txt','w', encoding="utf-8")
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
	fs.write('{{-start-}}\n')
	fs.write('{t}' + lin + '{e}\n')
	fs.write(new)
	fs.write('{{-stop-}}\n')
print('done')

#此系根据文件中条目名称生成单个文件并用于V1bot阅读之脚本

#cat = pywikibot.Category(site,'Category:Living people')
#gen = pagegenerators.CategorizedPageGenerator(cat)
#for page in gen:
  #Do something with the page object, for example:
#  text = page.text