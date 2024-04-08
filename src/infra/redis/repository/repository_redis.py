from redis import Redis
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repository.repository_link import RepositoryLink
from src.schemas import schemas


class RedisRepository:
    def __init__(self, redis_conn: Redis) -> None:
        self.__redis_conn = redis_conn

    def insert_hash_ex(self, link: schemas.LinkComplete, ex: int = 86400) -> None:
        self.__redis_conn.hset(link.short_link, mapping={
                                                         'short_link': link.short_link,
                                                         'original_link': link.original_link,
                                                         'counter': link.counter
                                                         })
        self.__redis_conn.expire(link.short_link, ex)

    def get_hash(self, db: Session, short: schemas.Short, counter: bool = True) -> schemas.LinkComplete:
        original_link = self.__redis_conn.hgetall(short.short_link)
        if not original_link:
            mysql = RepositoryLink(db).get(short)
            if mysql:
                RedisRepository(self.__redis_conn).insert_hash_ex(mysql)
                if counter:
                    original_link = RedisRepository(self.__redis_conn).counter(short)
                    return original_link
                return mysql
        if original_link and counter:
            original_link = RedisRepository(self.__redis_conn).counter(short)
        if original_link and not counter:
            link_complete = {}
            for key, value in original_link.items():
                link_complete[key.decode('utf-8')] = value.decode('utf-8')
            return schemas.LinkComplete(**link_complete)
        return original_link
    
    def counter(self, short: schemas.Short):
        value = self.__redis_conn.hget(short.short_link, 'counter').decode('utf-8')
        self.__redis_conn.hset(short.short_link, 'counter', int(value)+1)
        original_link = self.__redis_conn.hgetall(short.short_link)
        link_complete = {}
        for key, value in original_link.items():
            link_complete[key.decode('utf-8')] = value.decode('utf-8')
        return schemas.LinkComplete(**link_complete)