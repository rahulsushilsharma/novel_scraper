import requests
from requests_html import HTML

flag = True
n_url = input('enter the url :')

def get_p(url):
	return requests.get(url)


def w_chap(ch):
	with open('chapter.text',"a",encoding="utf-8") as chap:
		chap.write(ch)


while flag:
	x = get_p(n_url)
	h = HTML(html = x.text)
	try:
		match = h.find('#next_chap')
		atr = match[0].attrs
		n_url = 'https://readnovelfull.com' + atr['href']
		print('there is a new chapter, parsing...')
		
	except Exception as e:
		print("no new chapter")
		flag = False
	chap_content = h.find('#chr-content',first = True).text
	w_chap('\n\n' + n_url[40:52] + '\n')
	w_chap(chap_content)



