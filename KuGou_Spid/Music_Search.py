import copy
import web_request

def search(keyword):
    search_url = 'http://songsearch.kugou.com/song_search_v2?keyword={}page=1'.format(keyword)
    # 这里需要判断一下，ip与搜索字段可能会限制搜索，total进行判断
    total = web_request.parse(search_url)['data']['total']

