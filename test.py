from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

nex_page = urlopen(url)

html_bytes = nex_page.read()
html = html_bytes.decode("utf-8")

print(html)