
from ..forms import BaseForm
from wtforms import StringField,IntegerField
from wtforms.validators import Regexp, EqualTo, ValidationError,InputRequired
from utils import kfcache

class SignupForm(BaseForm):
    telephone = StringField(validators=[Regexp(r'1[345789]\d{9}',message='请输入正确格式的手机号码')])
    # cms_captcha = StringField(validators=[Regexp(r"\w{4}",message='请输入正确格式的短信验证码')])
    username=StringField(validators=[Regexp(r'.{2,20}',message="请输入正确格式用户名")])
    password=StringField(validators=[Regexp(r'[0-9a-zA-Z_\.]{6,20}',message="请输入正确格式密码")])
    password2=StringField(validators=[EqualTo("password",message="两次输入密码不一致")])
    graph_captcha=StringField(validators=[Regexp(r"\w{4}",message="请输入正确格式的图片验证码")])


    def validate_graph_captcha(self, field):
        graph_captcha = field.data
        graph_captcha_mem = kfcache.get(graph_captcha.lower())
        if not graph_captcha_mem:
            raise ValidationError(message='图形验证码错误！')


class SigninForm(BaseForm):
    telephone = StringField(validators=[Regexp(r'1[345789]\d{9}',message='请输入正确格式的手机号码')])
    password=StringField(validators=[Regexp(r'[0-9a-zA-Z_\.]{6,20}',message="请输入正确格式密码")])
    remeber = StringField()


class AddPostForm(BaseForm):
    title = StringField(validators=[InputRequired(message='请输入标题！')])
    content = StringField(validators=[InputRequired(message='请输入内容！')])
    board_id = IntegerField(validators=[InputRequired(message='请输入板块id！')])

class AddcommentForm(BaseForm):
    content = StringField(validators=[InputRequired(message='请输入评论内容')])
    post_id = IntegerField(validators=[InputRequired(message='请输入帖子id')])