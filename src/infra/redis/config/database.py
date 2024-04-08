from redis import Redis
import os


if os.getenv('REDIS_URL'):
    REDIS_URL = os.getenv('REDIS_URL')
else:
    REDIS_URL = "redis://localhost:6379/0"

redis_client = Redis.from_url(REDIS_URL)

def get_redis():
    return redis_client