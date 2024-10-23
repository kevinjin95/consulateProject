def connection_redis():
    from redis import Redis as connect
    from os import getenv
    from dotenv import load_dotenv

    load_dotenv()

    r = connect(
        host=getenv("REDIS_HOST"), 
        password=getenv("REDIS_PASSWORD"),
        port=getenv("REDIS_PORT"), 
        decode_responses=True
    )
    return r

def connection_mongo():
    pass