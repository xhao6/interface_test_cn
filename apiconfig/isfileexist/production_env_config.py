# -*- coding: utf-8 -*-
from api_class import *


App_a = {"app_id": "203228",
         "app_secret": "fbe54068c5eafd5262ff169a1682cca2",
         "grant_type": "client_credentials",
         "file": "v5vcloud_api_main_tests.py",
         "region_code": "0086",
         "app_id": "203228",
         "md5": "014CAF6FF12D0E3E0CA2E43AD498AD9A",
         "md5_1": "",
         "accounts":
             {"account_01": { "id": "TEST_testAccount111",
                                "nickName": "Iam_login_05",
                                "user_avatar": "http://cn.file.chatgame.me/api/file/download/2016/7/26/2/b999baff-45b4-4147-957e-8c05d2c55b16.jpg"
                              },

             },
        "miss_error_code":4001,
        }

CoreServer_url  = "https://cloudcn.v5.cn"
File_url = "http://cn.api.chatgame.me"
##########判断上传的文件是否已经存在-----缺少参数####
##########这个地方，将file这个请求参数去掉了##
###########TESTCASE####################
CoreServer_IsFileExistTest_01 = IsFileExistTest()
#input
CoreServer_IsFileExistTest_01.url = File_url+"/api/file/exist?"
CoreServer_IsFileExistTest_01.md5 = App_a["md5_1"]
CoreServer_IsFileExistTest_01.app_id = App_a["app_id"]
CoreServer_IsFileExistTest_01.region_code = App_a["region_code"]
#expect
CoreServer_IsFileExistTest_01.miss_error_code = App_a["miss_error_code"]
