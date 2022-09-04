import httpx

with open("proxy.txt", 'w') as file:
	file.write(httpx.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all").text)