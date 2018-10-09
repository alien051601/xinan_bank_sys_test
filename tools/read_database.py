from flask_sqlalchemy import SQLAlchemy
from models import UserBasicInfo
from flask_api import creat_app
from BaseCase import env
from jiami import *

db = SQLAlchemy()

app = creat_app()
app.config.from_object(env)
db.init_app(app)

app_context = app.app_context()
app_context.push()
db.create_all()


def config_prepare(func):
    app = creat_app()
    app.config.from_object(env)
    db.init_app(app)
    def wrapper(id):
        app_context = app.app_context()
        app_context.push()
        db.create_all()
        r = func(id)
        return r
    return wrapper


@config_prepare
def read_register_info(id):
    r = db.session.query(UserBasicInfo).filter_by(id=id).first()
    dict_new = r.to_register_dict()
    return dict_new


def add_register_info():
    # r = db.session.query(UserBasicInfo.id).filter_by().order_by(UserBasicInfo.id.desc()).first()
    r = db.session.query(UserBasicInfo).filter_by().order_by(UserBasicInfo.id.desc()).first()
    id_new = r.id+1
    mobile_new = int(r.register_mobile) + 1
    pw_1 = "a123456"

    # 对密码加密
    p = Prpcrypt()
    pw_16 = p.pad(pw_1)
    pw_2 = p.jiami(pw_16)

    u = UserBasicInfo(id = id_new,register_env="Test",register_mobile=mobile_new,register_pw1=pw_1,register_pw2=pw_2)
    db.session.add(u)
    db.session.commit()

# 读取数据库中ID最大的一个数据，并返回此行的id，mobile，加密的密码
def read_last_info():
    r = db.session.query(UserBasicInfo).filter_by().order_by(UserBasicInfo.id.desc()).first()
    id_new = r.id
    mobile_new = r.register_mobile
    pw_1 = r.register_pw1
    pw_2 = r.register_pw2
    return id_new,mobile_new,pw_1,pw_2

# 更新数据加密之后的密码
def updata_jiamiPW_info(row_num,pw_yuanshi):
    r = db.session.query(UserBasicInfo).get(row_num)

    # 对密码加密
    p = Prpcrypt()
    pw_16 = p.pad(pw_yuanshi)
    pw_jiami = p.jiami(pw_16)

    r.register_pw2 = pw_jiami
    r.register_pw1 = pw_yuanshi
    db.session.commit()



if __name__ == '__main__':
#     # r = read_register_info(1)
#     # print("r的值:", r)
#
#     app_context = app.app_context()
#     app_context.push()
#     db.create_all()
#     r = add_register_info()

    r = read_last_info()[0]
    print(r)

    # pw_new = "A123456"
    # updata_jiamiPW_info(10,pw_new)



    pass