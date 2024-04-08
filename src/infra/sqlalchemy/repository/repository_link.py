from sqlalchemy.orm import Session
from sqlalchemy import select, update
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from src.infra.providers.create_short import create_code


class RepositoryLink():
    def __init__(self, session: Session):
        self.db = session

    def create(self, link: schemas.Link) -> schemas.LinkComplete:
        create_short = RepositoryLink(self.db).check_short()
        if create_short:
            db_link = models.Link(original_link=link.original_link,
                                  short_link=create_short)
            self.db.add(db_link)
            self.db.commit()
            self.db.refresh(db_link)
            return db_link
        else:
            return None

    def get(self, short: schemas.Short) -> schemas.LinkComplete:
        query = select(models.Link).where(models.Link.short_link == short.short_link)
        link_complete = self.db.execute(query).scalars().first()
        return link_complete

    def counter(self, link: schemas.LinkComplete) -> None:
        link_complete = RepositoryLink(self.db).get(link)
        update_stmt = update(models.Link).where(models.Link.short_link == link.short_link).values(counter=link_complete.counter+1)
        self.db.execute(update_stmt)
        self.db.commit()
    
    def check_short(self):
        check = True
        i = 0
        while check:
            i += 1
            code = create_code()
            short_model = schemas.Short(**{'short_link': code})
            short = RepositoryLink(self.db).get(short_model)
            if not short or i == 10000:
                check = False
            if i == 10000:
                code = None
        return code