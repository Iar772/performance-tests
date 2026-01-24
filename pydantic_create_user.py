from pydantic import BaseModel, EmailStr, Field, ConfigDict

class UserBaseSchema(BaseModel):
    """
    Базовая pydantic схема пользователя.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class UserSchema(UserBaseSchema):
    """
    Полная pydantic схема пользователя.
    """
    id: str


class CreateUserRequestSchema(UserBaseSchema):
    """
    Pydantic схема запроса на создание пользователя через /api/v1/users, без поля id.
    """
    pass

class CreateUserResponseSchema(BaseModel):
    """
    Pydantic схема ответа на запрос по созданию пользователя через /api/v1/users.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    user: UserSchema