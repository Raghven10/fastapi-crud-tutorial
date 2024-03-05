from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)
    class Config:
        schema_extra = {
            "post_demo": {
                "title": "Some Title",
                "content": "Some Content"
            }
        }

class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo": {
                "name": "Some Name",
                "email": "email@example.com",
                "password": "Some Password"

            }
        }

class UserLoginSchema(BaseModel):
    
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo": {
                
                "email": "email@example.com",
                "password": "Some Password"

            }
        }