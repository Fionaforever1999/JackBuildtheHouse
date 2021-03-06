# coding=utf-8
# import redis
import hashlib
import os
class Config:
    DEBUG=False
    SQLALCHEMY_DATABASE_URI='mysql://root:88899210@127.0.0.1:3306/test1'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DROPZONE_MAX_FILE_SIZE = 3
    DROP_MAX_FILES = 30
    DROPZONE_ALLOWED_FILE_TYPE = 'image/*,.pdf,.txt'
    DROPZONE_ENABLE_CSRF = True
    MAX_CONTENT_LENGTH = 3 * 1024 * 1024
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    JBH_PROFILE_PATH = os.path.join(basedir,'profile')
#PIL pillow
    # #redis配置
    # REDIS_HOST = "127.0.0.1"
    # REDIS_PORT = 6379
    #
    # #session配置
    # SECRET_KEY = "iHome"
    # #将session存储到redis中
    # SESSION_TYPE = "redis"
    # SESSION_USE_SIGNER = True
    # # SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # PERMANENT_SESSION_LIFETIME = 60*60*24*14#秒
    #
    #七牛云的访问服务器
    # QINIU_URL='http://oyvzbpqij.bkt.clouddn.com/'

    #权限信息
    # TOKEN=hashlib.md5('ihome_bj14').hexdigest()
    #

class DevelopConfig(Config):
    DEBUG = True
class ProductConfig(Config):
    pass
