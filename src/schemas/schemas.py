from pydantic import BaseModel, ConfigDict


class Link(BaseModel):
    original_link: str

    model_config = ConfigDict(from_attributes = True)


class Short(BaseModel):
    short_link: str

    model_config = ConfigDict(from_attributes = True)


class LinkComplete(BaseModel):
    original_link: str
    short_link: str
    counter: int
    
    model_config = ConfigDict(from_attributes = True)