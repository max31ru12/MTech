from pydantic import BaseModel


class PostLog(BaseModel):

    log: str


# Валидация такая вот
valid_data = {"log": "{127.0.0.1} {str} {URI} {int}"}

# Если успех, то будет выведено log='{127.0.0.1} {str} {URI} {int}'
print(PostLog(**valid_data))

