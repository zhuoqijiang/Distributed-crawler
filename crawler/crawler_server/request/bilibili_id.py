import requests

_request_timeout = 1


class GetFollowerFollowing:
    _url = 'https://api.bilibili.com/x/relation/stat'

    def __init__(self, uid):
        self._uid = uid

    def _get_url_params(self):
        url_params = {'vmid': str(self._uid), 'jsonp': 'jsonp'}
        return url_params

    def get_follower_following(self):
        url_params = self._get_url_params()
        r = requests.get(self._url, params=url_params, timeout=_request_timeout)
        try:
            data = r.json()['data']
            follower = data['follower']
            following = data['following']
        except:
            return 0, 0
        else:
            return follower, following


class GetVedios:
    _url = 'https://api.bilibili.com/x/space/arc/search'

    def __init__(self, uid):
        self._uid = uid

    def _get_url_params(self):
        url_params = {'mid': str(self._uid), 'pn': '1', 'ps': '25', 'index': '1', 'jsonp': 'jsonp'}
        return url_params

    def get_vedios(self):
        vedio_addrs = []
        url_params = self._get_url_params()
        r = requests.get(self._url, params=url_params, timeout=_request_timeout)
        try:
            vlist = r.json()['data']['list']['vlist']
        except:
            return vedio_addrs
        else:
            for v in vlist:
                vedio_addrs.append('https://www.bilibili.com/video/{}'.format(v['bvid']))
            return vedio_addrs


class GetArchiveLike:
    _url = 'https://api.bilibili.com/x/space/upstat'
    _cookie = ''

    def __init__(self, uid):
        self._uid = uid

    def _get_url_params(self):
        url_params = {'mid': str(self._uid), 'jsonp': 'jsonp'}
        return url_params

    def _get_header(self):
        header = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/533.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Mobile Safari/533.36 Edg/98.0.1108.41',
            'cookie': self._cookie
        }
        return header

    def get_archive_like(self):
        url_params = self._get_url_params()
        header = self._get_header()
        r = requests.get(self._url, params=url_params, headers=header, timeout=_request_timeout)
        try:
            data = r.json()['data']
            archive = data['archive']['view']
            like = data['likes']
        except:
            return 0, 0
        else:
            return archive, like

