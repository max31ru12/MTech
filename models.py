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


log_entry_data = {"ip": "127.0.0.1", "method": "GET", "uri": "http://example.com", "status_code": 200}
print(GetLog(**log_entry_data))


# Валидация такая вот
valid_data = {"log": "{127.0.0.1} {str} {URI} {int}"}

# Если успех, то будет выведено log='{127.0.0.1} {str} {URI} {int}'
print(PostLog(**valid_data))

