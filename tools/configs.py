class LocalConfig(object):
    DB_HOST= "127.0.0.1"
    DB_PORT: 3306
    DB_USER='root'
    DB_PASSWORD= 'db_pw'   # 数据库的密码
    DB_DB = "xinan_bank_test"
    # 数据变化的自动警告关闭
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 数据改变后自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USER + ":" + DB_PASSWORD + "@" + DB_HOST + "/" + DB_DB
    base_api="http://191.168.0.1:port"  # 接口host地址
    mobile_login = '18616300004'
    pw_login = 'd7w4bvzDod7PUt9OS7zOkA=='

# l = LocalConfig()
# print(l.mobile_login)



# read_database.py文件里面，add_register_info（）方法需要根据不同的环境，插不入不同的环境test，uat
