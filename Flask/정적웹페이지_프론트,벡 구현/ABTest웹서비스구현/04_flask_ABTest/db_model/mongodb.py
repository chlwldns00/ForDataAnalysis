import pymongo

MONGO_HOST = 'localhost:27017' #전역변수 처리
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))


def conn_mongodb(): #접속 예외처리
    try:
        MONGO_CONN.admin.command('ismaster')
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    except:
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
        blog_ab = MONGO_CONN.blog_session_db.blog_ab

    return blog_ab
