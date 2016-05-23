import pywikibot
import os
from pywikibot import pagegenerators
site = pywikibot.Site()
os.system("pwb.py pagefromfile.py -titlestart:{t} -titleend:{e} -notitle -file:../w1/file.txt")
print('done')


#cat = pywikibot.Category(site,'Category:Living people')
#gen = pagegenerators.CategorizedPageGenerator(cat)
#for page in gen:
  #Do something with the page object, for example:
#  text = page.text