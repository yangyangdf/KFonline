import os

SECRET_KEY = os.urandom(24)
# SECRET_KEY = 'asdasdasdasd'
DEBUG =True

DB_USERNAME = 'root'
DB_PASSWORD = 'yy0424..'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'kefu'

# PERMANENT_SESSION_LIFETIME =



DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset-utf-8'%(
    DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME
)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

CMS_USER_ID = 'KEFUZAIXIANCHAXUNXITONG'
FRONT_USER_ID = 'FRONTKEFUZAIXIANCHAXUNXITONG'

# 发送邮箱的服务器地址
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = '587'
MAIL_USE_TLS = True
# MAIL_USE_SSL : default False
MAIL_USERNAME = '412880433@qq.com'
MAIL_PASSWORD = 'csiymukhceztcbbc'
MAIL_DEFAULT_SENDER = '412880433@qq.com'

# #阿里大于相关配置
# ALIDAYU_APP_KEY = '23709557'
# ALIDAYU_APP_SECRET = 'd9e430e0a96e21c92adacb522a905c4b'
# ALIDAYU_SIGN_NAME = '小饭桌应用'
# ALIDAYU_TEMPLATE_CODE = 'SMS_68465012'


UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'images')

UEDITOR_UPLOAD_TO_QINIU = True
UEDITOR_QINIU_ACCESS_KEY = 'X7a1DCsqPQ8M0TWXGjxahPaLMi3AVxWdLaKHYztR'
UEDITOR_QINIU_SECRET_KEY = '-PFBtC0MxEW_gDKwLFBaUrhQBgDw7TBohgtxQifM'
UEDITOR_QINIU_BUCKET_NAME = 'kfonline'
UEDITOR_QINIU_DOMAIN = 'http://q15h6dlt0.bkt.clouddn.com/'

PER_PAGE = 10


CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
