# coding=utf-8
import sys
from flask import Flask
from imp import reload
from flask import request,render_template
from KuGou_Spid import Music_download

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def search():
    if request.method == 'GET':
        return render_template('search.html')

    elif request.method == 'POST':
        keyword = request.form.get('keyword')
        items = Music_download.HighSearch(keyword)
        if items != None:
            return render_template('list.html', list=items)
        else:
            return '找不到！！！不支持英文'

    else:
        return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)