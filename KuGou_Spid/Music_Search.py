import copy
from KuGou_Spid import web_request

def search(keyword):
    search_url = 'http://songsearch.kugou.com/song_search_v2?keyword={}&page=1&platform=WebFilter'.format(keyword)
    # 这里需要判断一下，ip与搜索字段可能会限制搜索，total进行判断
    total = web_request.parse(search_url)['data']['total']
    if total != 0:
        search_total_url = search_url + '&pagesize=%d' % total
        music_list = web_request.parse(search_total_url)['data']['lists']
        item, items = {}, []
        for music in music_list:
            if music['SQFileHash'] != '0'*32:
                item['Song'] = music['SongName']  # 歌名
                item['Singer'] = music['SingerName']  # 歌手
                item['Hash'] = music['SQFileHash'] # 歌曲无损hash
                item['Size'] = str(round((music['SQFileSize']/1024)/1024,2))+'M'
                item['minute'] = str(int(music['SQDuration']/60))
                if(music['SQDuration']%60<10):
                    item['second'] = '0'+str(music['SQDuration'] % 60)
                else:
                    item['second'] = str(music['SQDuration'] % 60)
                items.append(copy.deepcopy(item))
        return items
    else:
        return None

if __name__ == '__main__':
    search()

