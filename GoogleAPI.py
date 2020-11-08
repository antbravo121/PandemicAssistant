from serpapi import GoogleSearch
from ItemData import ItemData


def get_results(item, location):
	params = {
		"q": item,
		"tbm": "shop",
		"location": location,
		"hl": "en",
		"gl": "us",
		"api_key": "286dc1ea151c8c789b1babc2c6e89694919c91e5edb1908278d4c771c5fdcf68",
		"num":5
	}

	client = GoogleSearch(params)
	results = client.get_dict()
	results = results["shopping_results"]

	item_list = []

	for result in results:
		item_list.append(ItemData(
			result.get("title"),
			result.get("link"),
			result.get("price"),
			result.get("snippet"),
			result.get("source")
			)
		)

	return item_list



