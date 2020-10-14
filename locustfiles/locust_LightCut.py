import os
from configparser import ConfigParser
from locust import TaskSet, task
import logging


class TestLightCut(TaskSet):
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
    def view_thread(self):
        url = "/resourcemanagerservice/api/task/import"
        data = {
            "taskList": [
                {
                    "keyFrameInfo": "",
                    "resourceId": "a25b9dee-d226-4cd2-a905-92a840f216c7",
                    "sourceSystem": "LightCut",
                    "creatorId": "admin",
                    "creatorName": "admin",
                    "memo": "",
                    "inpoint": 0,
                    "relationResourceIds": "-",
                    "metadataInfo": "",
                    "duration": 0,
                    "hdFlag": 1,
                    "ccid": "",
                    "isTempResource": 0,
                    "callbackUrl": "",
                    "id": "60d429b2-8d66-414f-a40a-edbbf473f64c",
                    "afd": 8,
                    "programType": 1,
                    "programCode": "",
                    "priority": 0,
                    "folderId": "",
                    "outpoint": 0,
                    "segmentInfo": 4,
                    "sourceType": 4,
                    "tenantId": "63e8f91121eb495dba4a56604cae5f16",
                    "name": "0805入库.mp4",
                    "files": [
                        {
                            "includeVideo": 1,
                            "includeAudio": 1,
                            "id": "fb513198-71f1-4186-a748-c50adc88dd0e",
                            "source": "<?xml version=\"1.0\" encoding=\"UTF-16\"?>\n<SourceInfo>\n    <SourceFile FileType=\"5\" IncludeAudio=\"1\" IncludeVideo=\"1\" Channel=\"0\" FileName=\"0805入库.mp4\" PathID=\"\" Path=\"http://10.0.41.170:80/lightcut/private/admin/\" TrimIn=\"0\" TrimOut=\"275\" RelativePath=\"\" MD5Code=\"\" StreamMediaInfoID=\"\" UseDetailStreamMediaInfo=\"1\">\n        <sStreamMediaInfo enumStreamMediaType=\"128\" dwStreamMediaSubType=\"0\" bIsIncludeVideo=\"1\" bIsIncludeAudio=\"1\" llFileSize=\"67636103\" dwVideoFrame=\"3842\" dwAudioSamples=\"6794240\" dwTotalAverDataRateInBitsPerSec=\"0\" dwTotalMaxDataRateInBitsPerSec=\"0\" dwTotalMinDataRateInBitsPerSec=\"0\">\n            <sVideoMediaInfo wWidth=\"856\" wHeight=\"480\" dwStandardRate=\"25000\" dwStandardScale=\"1000\" enumScanMode=\"2\" enumColorFormat=\"1024\" enumVideoType=\"8388608\" dwVideoSubType=\"2\" dwDataRateInBitsPerSec=\"3404368\" bConstantRate=\"0\" dwGOPSize=\"118\" dwReferencePeriod=\"1\" bIsY16_235=\"1\" dwDisplayWidth=\"4\" dwDisplayHeight=\"3\" enumColorPrimaries=\"1\" enumColorTransfer=\"1\" enumColorMatrix=\"1\" enumAFD=\"-1\"/>\n            <sAudioMediaInfo enumAudioType=\"32\" dwAudioSubType=\"0\" dwChannels=\"2\" dwBitsPerSample=\"16\" dwSamplesPerSec=\"44100\" dwAvgBitsPerSec=\"8957\" dwBlockAlign=\"4\" enumAudioCFG=\"1\" enumChannelSamplesFormat=\"1\"/>\n        </sStreamMediaInfo>\n    </SourceFile>\n</SourceInfo>",
                            "md5Code": "",
                            "fileType": 5,
                            "status": 0
                        }
                    ],
                    "resourceType": 14
                }
            ]
        }
        with self.client.get(url, catch_response=True) as response:
            if response.status_code == 200:
                logging.info("%s请求返回状态： %d" % (url, response.status_code))
                logging.info("%s请求返回结果：%s" % (url, response.text))
