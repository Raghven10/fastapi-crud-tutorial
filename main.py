import uvicorn
from fastapi import FastAPI, Path, Body, Depends
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT 
from app.auth.jwt_bearer import jwtBearer


posts = [
    {
        "id": 1,
        "title": "Open AI",
        "content":"Open AI Models and Features"
    },
    {
        "id": 2,
        "title": "Replicate AI",
        "content":"Replicate AI Models and Features"
    },
    {
        "id": 3,
        "title": "HuggingFace AI",
        "content":"HuggingFace AI Models and Features"
    }
]

users = []

app = FastAPI()

################################ Get for testing purposes #################################
@app.get("/", tags=["test"])
def read_root():
    return {"Hello": "World"}


################################ Get for Posts #################################
 
@app.get("/posts", tags=["posts"])
def read_posts():
    return {"data": posts}

################################ Get Single Post #################################

@app.get("/posts/{post_id}", tags=["posts"])
def read_post(post_id: int = Path(...,ge=1)):
    if id > len(posts):
        return {
            "Error": "Post does not exist"
        }
    return {"data": [post for post in posts if post["id"] == post_id]}

################################ Add New Post #################################

@app.post("/posts",dependencies=[Depends(jwtBearer())], tags=["posts"])
def create_post(post: PostSchema):
    post.id = len(posts)+1
    posts.append(post)
    return {"data": post.model_dump()}

## User SIgnup #################################

@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

## Check User Login #################################

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {"Error": "Invalid Credentials"}