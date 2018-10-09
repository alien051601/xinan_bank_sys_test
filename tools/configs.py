# # env config
# ENV = 'test'
# APP_VERSION = '2.3.7'
# HEADERS = {"Accept": "*/*",
#            "User-Agent": 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
#
# db_config = {
#     "local_test": {
#         "DB_HOST": "127.0.0.1",
#         "DB_PORT": 3306,
#         "DB_USER": 'root',
#         "DB_PASSWORD": 'alien007'
#     },
# }
#
# class LocalConfig(object):
# DB_HOST= "192.168.7.214"
# DB_PORT: 60214
# DB_USER='testd_api_java'
# DB_PASSWORD= 'usb6af85KKFdjZhZBCZw0twOp4Fha1Fv'
# DB_DB = "xinan_bank_test"

class LocalConfig(object):
    DB_HOST= "127.0.0.1"
    DB_PORT: 3306
    DB_USER='root'
    DB_PASSWORD= 'alien007'
    DB_DB = "xinan_bank_test"
    # 数据变化的自动警告关闭
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 数据改变后自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USER + ":" + DB_PASSWORD + "@" + DB_HOST + "/" + DB_DB
    # base_api="http://192.168.7.101:8098"
    base_api="http://192.168.7.228:8098"
    mobile_login = '18616300004'
    # pw_login = 'C3pwf3Cz/0Ofk/QV7CHWvA=='
    pw_login = 'd7w4bvzDod7PUt9OS7zOkA=='

# l = LocalConfig()
# print(l.mobile_login)



# read_database.py文件里面，add_register_info（）方法需要根据不同的环境，插不入不同的环境test，uat
