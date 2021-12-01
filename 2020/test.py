import requests

_saved_data = {}

def get_all_tabs(accountName, ssid):
	#keys: 'numTabs', 'tabs', 'quadLayout', 'items'
	# 	tabs: 'n', 'i', 'id', 'type', 'selected', 'colour', 'srcL', 'srcC', 'srcR'
	#  items: 'verified', 'w', 'h', 'icon', 'league', 'id', 'sockets', 'name', 'typeLine', 'identified', 'ilvl', 'properties', 'explicitMods', 'flavourText', 'frameType', 'x', 'y', 'inventoryId', 'socketedItems'
	if not _saved_data:
		tabIndex = 0
		url = 'https://www.pathofexile.com/character-window/get-stash-items'
		payload = {'league': 'Heist', 'accountName':accountName, 'tabs': 1, 'tabIndex':tabIndex, 'realm':'pc'}

		my_cookies = {'POESESSID' : ssid} #poesessid finns i dina cookies när du loggar in på sidan
		stash_tab = requests.get(url , params = payload, cookies = my_cookies)

		data = stash_tab.json()
		numTabs = data["numTabs"]
		
		while True:
			tabIndex += 1
			if tabIndex >= numTabs:
				break
			payload["tabIndex"] = tabIndex
			data["items"] += requests.get(url, params=payload, cookies=my_cookies).json()["items"]
		_saved_data.update(data)
	return _saved_data


def get_all_images(data):
	for item in data["items"]:
		print(item["icon"])



for x in range(10):
	print(get_all_tabs("consumed", "dd59dd12def77d6035ff8fa943ef43b7")["items"][x]["icon"])


get_all_images(_saved_data)