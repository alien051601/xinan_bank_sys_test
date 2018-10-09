from flask import Blueprint,render_template



test_view = Blueprint('test',__name__,template_folder='../templates')

@test_view.route('/register')
def register():
    pass


