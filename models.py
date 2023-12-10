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


# log_entry_data = {"ip": "127.0.0.1", "method": "GET", "uri": "http://example.com", "status_code": 200}
valid_data = {
    "uuid4": "550e8400-e29b-41d4-a716-446655440000",
    "created": "2023-12-01T12:34:56",
    "log": {
        "ip": "192.168.1.1",
        "method": "GET",
        "uri": "http://example.com",
        "status_code": 200
    }
}


# aaaa = {
#     "ip": "192.168.1.1",
#     "method": "GET",
#     "uri": "https://example.com/path/to/resource",
#     "status_code": 200
# }

try:
    print(GetLogData(**{
                        "ip": "192.16",
                        "method": "str",
                        "uri": "URI",
                        "status_code": "int"
                    }))
except:
    print("hello")



# Валидация такая вот
valid_data = {"log": "{127.0.0.1} {str} {URI} {int}"}

# Если успех, то будет выведено log='{127.0.0.1} {str} {URI} {int}'
print(PostLog(**valid_data))

