from bs4 import BeautifulSoup as Soup
import requests
import webbrowser

def run():
	headers = {'User-Agent':'Shashwat Test Bot'}
	r = requests.get("https://en.wikipedia.org/wiki/Special:Random", headers = headers)

	if r.status_code == 200:
		url = r.url
		soup = Soup(r.text)
		print soup.find(id="firstHeading").string.encode("ascii","replace")
		print 
		ans = raw_input("Open article? ")
		if ans[0] in 'yY':
			webbrowser.open(url)
			return 0
		else:
			return 1

if __name__ == "__main__":
	run()
