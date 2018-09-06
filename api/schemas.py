import coreapi
import coreschema
from rest_framework.schemas import ManualSchema

LoginSchema = ManualSchema(fields=[
    coreapi.Field(
        'username',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'password',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
])