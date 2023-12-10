from pydantic import BaseModel, AnyUrl, IPvAnyAddress, UUID4
from datetime import datetime

IPvAnyAddress


class PostLog(BaseModel):

    log: str


class GetLogData(BaseModel):

    ip: IPvAnyAddress
    method: str
    uri: AnyUrl
    status_code: int


class GetLog(BaseModel):

    uuid4: UUID4
    created: datetime
    log: GetLogData
