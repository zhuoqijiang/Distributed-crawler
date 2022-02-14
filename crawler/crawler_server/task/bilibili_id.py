import json
import logging

import request.bilibili_id
from public.mysql_operator import MysqlOperator

class BilibiliIdTask:

    def __init__(self, uid):
        self._uid = uid

    def run(self):
        follower_following = request.bilibili_id.GetFollowerFollowing(self._uid)
        vedio = request.bilibili_id.GetVedios(self._uid)
        archive_like = request.bilibili_id.GetArchiveLike(self._uid)
        follower, following = follower_following.get_follower_following()
        vedio_list = vedio.get_vedios()
        vedio_dict = {"list": vedio_list}
        vedios = str(json.dumps(vedio_dict))
        archive, like = archive_like.get_archive_like()
        task_dict = {
            'uid': self._uid,
            'follower': follower,
            'following': following,
            'vedios': vedios,
            'archive': archive,
            'likes': like
        }
        MysqlOperator.repace_into("bilibili_users", task_dict)
        logging.info("get uid:{} data".format(self._uid))
        return task_dict



