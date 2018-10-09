from flask_sqlalchemy import SQLAlchemy
from BaseCase import env
from flask_api import creat_app

app = creat_app()
app.config.from_object(env)
db = SQLAlchemy()
db.init_app(app)

class UserBasicInfo(db.Model):
    __tablename__ = "user_basic_info"
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    register_env = db.Column(db.String(10), nullable=False)
    register_mobile = db.Column(db.String(15), nullable=False)
    register_pw1 = db.Column(db.String(15), nullable=False)
    register_pw2 = db.Column(db.String(15))
    user_code = db.Column(db.String(32))
    register_code = db.Column(db.String(15))
    realname = db.Column(db.String(64))
    mobile_bank = db.Column(db.String(15))
    idno = db.Column(db.String(18))
    bank_no = db.Column(db.String(3))
    bank_card_no = db.Column(db.String(32))
    account_org_id = db.Column(db.String(64))
    account_id = db.Column(db.String(64))
    third_account_id = db.Column(db.String(64))
    buy_pw = db.Column(db.String(15))
    status = db.Column(db.Integer())
    remark = db.Column(db.String(256))
    user_type = db.Column(db.Integer())
    client = db.Column(db.Integer())
    platform = db.Column(db.String(3))
    create_time = db.Column(db.Date)
    update_time = db.Column(db.Date)

    def __str__(self):
        return "Userbasicinfo{userid=%s,realname=%s}" % (self.id,self.realname)

    def to_register_dict(self):
        """将对象转化为字典"""
        user_dict = {
            "id":self.id,
            "register_env":self.register_env,
            "register_mobile":self.register_mobile,
            "register_pw1":self.register_pw1
        }
        return user_dict

class Books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    pub_date = db.Column(db.Date)




# if __name__ == '__main__':
#     app_context = app.app_context()
#     app_context.push()
#     db.create_all()

    # 直接执行sql方法查询
    # sql = "select * from user_basic_info where id <10;"
    # r = db.session.execute(sql).fetchone()
    # print(r)

    # 使用flask-sqlalchemy查询
    # id_or = 2
    # r = db.session.query(UserBasicInfo).from_statement("select * from user_basic_info where id=:id_new").params(id_new=id_or).all()

    # id_new = 2
    # r = db.session.execute("select * from user_basic_info where id=:id", params={"id":id_new}).fetchall()
    # print(r.to_register_dict())
    # print(r)
