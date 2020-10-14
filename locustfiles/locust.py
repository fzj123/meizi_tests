
from configparser import ConfigParser
import os

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
print(userId)