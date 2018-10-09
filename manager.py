from models import  db,app
from register_api import Register
from flask_restful import Api



db.init_app(app)
api = Api(app)
api.add_resource(Register,'/register_new')

# 运行localhost的服务器（网页+接口）
if __name__ == '__main__':
    app.run(debug=True)

