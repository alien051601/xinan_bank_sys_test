from flask_restful import Api,reqparse,Resource
from flask import jsonify
# from models import UserBasicInfo,db, app
from user_controller import register_new
from flask_api import creat_app

# app = creat_app()
# api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('row_num')
parser.add_argument('sex')


class Register(Resource):
    def post(self):
        args = parser.parse_args()

        row_num = args['row_num']
        # sex_p = args['sex']
        # print('register接口传递的值为：',id_p,sex_p)
        # r = db.session.query(UserBasicInfo).filter_by(id=1).first()
        # result = r.to_register_dict()

        result = register_new(row_num)
        return jsonify({"code":123,"msg":"success","date":result})



# if __name__ == '__main__':
#     api.add_resource(Register, '/register_new')
#     app.run(debug=True)