from django.shortcuts import render

# Create your views here.
from test.models import BilibiliUsers
from django.http import HttpResponse
from django.shortcuts import render


class Bilibili:
    @staticmethod
    def get_data(request):
        datas = BilibiliUsers.objects.all()
        dicts = []
        for data in datas:
            d = data.__dict__
            d.pop('_state')
            Bilibili.data_key_map(d)
            dicts.append(d)
        return render(request, "bilibili_users.html", {"test": dicts})

    @staticmethod
    def data_key_map(data):
        data['用户id'] = data.pop('uid')
        data['关注数'] = data.pop('follower')
        data['粉丝数'] = data.pop('following')
        data['获赞数'] = data.pop('likes')
        data['播放数'] = data.pop('archive')
        data['视频地址'] = data.pop('vedios')
