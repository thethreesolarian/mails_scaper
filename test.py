import requests
from lxml import html
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

page = requests.get("https://www.business.bg/o-347/s-200/avtomivki.html", verify=False)
root = html.fromstring(page.text)
tree = root.getroottree()
result = root.xpath('//*[@id="terem-ead"]')
for r in result:
    print(tree.getpath(r))