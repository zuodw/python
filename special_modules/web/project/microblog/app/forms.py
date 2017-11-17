from flask_wtf import FlaskForm # 导入Form类
from wtforms import StringField, BooleanField # 导入2个需要的字段类： TextField和BooleanField
from wtforms.validators import DataRequired # 验证器，简单的检查相应域提交的数据是否为空

class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)