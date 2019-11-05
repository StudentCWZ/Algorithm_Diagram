# 散列表用于缓存
'''
cache = {}
def get_page(url):
	if cache.get(url):
		return cache['url']
	else:
		data = get_data_from_server(url)
		cache[url] = data
		return data
'''

