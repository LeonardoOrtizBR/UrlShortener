from fastapi import APIRouter, status, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.redis.config.database import get_redis
from src.schemas import schemas
from src.infra.sqlalchemy.repository.repository_link import RepositoryLink
from src.infra.redis.repository.repository_redis import RedisRepository
from src.jobs.verify_url import verify_url
from src.jobs.verify_short import verify_short

router = APIRouter()

@router.post('/link', status_code=status.HTTP_201_CREATED, response_model=schemas.LinkComplete)
def create_link(link: schemas.Link, redis = Depends(get_redis), db: Session = Depends(get_db)):
    if not verify_url(link.original_link):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='O link que você enviou não está correto')
    create_link = RepositoryLink(db).create(link)
    if create_link:
        RedisRepository(redis).insert_hash_ex(create_link)
        return create_link
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Número máximo de tentativas de criar um encurtador de link exedidas')
    

@router.get('/{short_link}', status_code=status.HTTP_200_OK, response_model=schemas.LinkComplete)
def get_link(short_link: str, background: BackgroundTasks, redis = Depends(get_redis), db: Session = Depends(get_db)):
    if verify_short(short_link):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='O link enviado não está correto no padrão correto')
    short = schemas.Short(**{'short_link': short_link})
    get_short = RedisRepository(redis).get_hash(db, short)
    if get_short:
        background.add_task(RepositoryLink(db).counter, get_short)
        return get_short
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Nenhum link encontrado com esse encurtador')
    

@router.get('/{short_link}/counter', status_code=status.HTTP_200_OK, response_model=schemas.LinkComplete)
def get_counter(short_link: str, redis = Depends(get_redis), db: Session = Depends(get_db)):
    if verify_short(short_link):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='O encurtador enviado não está no padrão aceito')
    short = schemas.Short(**{'short_link': short_link})
    get_short = RedisRepository(redis).get_hash(db, short, False)
    if get_short:
        return get_short
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Nenhum link encontrado com esse encurtador')