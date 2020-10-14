from locust import TaskSet, task
import logging
from configparser import ConfigParser
import os


class TestNewsCommand(TaskSet):
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    print(parent_dir)
    rp = ConfigParser()
    rp.read(parent_dir + '/locust.ini', encoding='utf-8')
    userId = rp.get("request_variable", "userId")
    userName = rp.get("request_variable", "userName")
    tenantId = rp.get("request_variable", "tenantId")
    fileSize = rp.get("request_variable", "fileSize")
    folderId = rp.get("request_variable", "folderId")
    fileNameLightcut = rp.get("request_variable", "fileNameLightcut")
    fileNameNewsCommand = rp.get("request_variable", "fileNameNewsCommand")

    @task(1)
    def newsCommand_upload(self):
        url = "/resourceconfigservice/api/resource/add"
        data = {
            'userId': self.userId,
            'userName': self.userName,
            'tenantId': self.tenantId,
            'ccId': '视音频',
            'source': 'newsCommand',
            'fileSize': self.fileSize,
            'name': 'test',
            'tags': '{"tagPerson":[],"tagTime":[],"tagOther":[],"tagLocation":[]}',
            'oriName': 'test.mp4',
            'folderId': self.folderId,
        }
        print(data)
        files = {
            'file': (self.fileNameLightcut, open(self.fileNameNewsCommand, 'rb'), 'application/x-unknown-content-type')
        }

        with self.client.post(url, data=data, files=files) as response:
            if response.status_code == 200:
                logging.info("%s请求返回状态： %d" % (url, response.status_code))
                logging.info("%s请求返回结果：%s" % (url, response.text))
