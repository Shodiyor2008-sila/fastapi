from .. import models,schemas,utils,oauth2,database
from fastapi import FastAPI,Response,HTTPException,status,Depends,APIRouter
from sqlalchemy.orm import Session,joinedload
from typing import List,Optional
import mysql.connector
from sqlalchemy import func
my_posts = [{'title':'favorite device','content':'phones','id':1},{'title':'favorite sport','content':'football','id':2}]
router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)
# con = mysql.connector.connect(user='root', host='localhost', database='test', passwd = '12341234', port = 3306)
my_posts = [{'title':'favorite device','content':'phones','id':1},{'title':'favorite sport','content':'football','id':2}]


# @app.get('/sqlalchemy')
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return posts



@router.get('/',response_model=List[schemas.PostResponse])
def get_posts(db: Session = Depends(database.get_db)):
    posts = db.query(models.Post).join(models.Users).all()
    return posts
    # post = db.query(models.Post).filter(models.Post.user_id == current_user.id).all() # getting a post for a specific user who is logged in
    # conn = con.cursor()
    # conn.execute('select * from posts')
    # posts = conn.fetchall()
    # # # # print(posts)
    # return posts
    # return {'data':'This is your posts'}
    # result = db.query(models.Post,func.count(models.Vote.post_id)).join(models.Vote,models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).all()
    # return result


@router.get('/latest',response_model=schemas.PostResponse)
def latest_post():
    post = my_posts[len(my_posts) - 1]
    return post


@router.get('/{id}',response_model = schemas.PostResponse)
def get_post(id:int,db: Session = Depends(database.get_db),current_user:int = Depends(oauth2.get_current_user)):
    # conn = con.cursor()
    # conn.execute('''select * from posts where id = %s''',(id,))
    # post = conn.fetchone()
    # con.close()
    # return {'data':post}
    # print(id)
    # post = find_post(id)
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail={'message':f'post with id:{id} not found'})
        # response.status_code = 404
        # return {'message':f'post with id:{id} not found'}
    return post
    


@router.post('/',status_code=status.HTTP_201_CREATED,response_model = schemas.PostResponse)
def create_posts(post:schemas.PostBase,db: Session = Depends(database.get_db),current_user:int = Depends(oauth2.get_current_user)):
    # conn = con.cursor()
    # conn.execute('''insert into posts (title,content,published) values (%s,%s,%s) ''',
    #              (post.title,post.content,post.published))
    # new_post_id = conn.lastrowid
    # conn.execute('''select * from posts where id = %s''',(new_post_id,))
    # new_post = conn.fetchone()
    # con.commit()
    # conn.close()
    # con.commit()
    # print(current_user.email)
    new_post = models.Post(
        title = post.title,content = post.content,published = post.published,user_id = current_user.id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
    # print(f'This is {post.rating}!!!')
    # print(post.published)
    # print(post.model_dump)
    # print(post.model_dump())
    # post_dict = post.model_dump()
    # post_dict['id'] = randrange(0,1000000)
    # my_posts.append(post_dict)
    # return {'data':post_dict}

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(database.get_db),current_user:int = Depends(oauth2.get_current_user)):
    # conn = con.cursor()
    # Check if the post exists before attempting to delete
    # conn.execute('''SELECT * FROM posts WHERE id = %s''', (id,))
    # post = conn.fetchone()
    post_query = db.query(models.Post).filter(models.Post.id == int(id))
    post = post_query.first()
    if post_query.first() == None:
        # conn.close()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} was not found')
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Boshqalarni nomidan delete qila olmaysan')
    # Delete the post
    # conn.execute('''DELETE FROM posts WHERE id = %s''', (id,))
    # con.commit()
    # conn.close()
    post_query.delete(synchronize_session=False)
    db.commit()

    # index = find_index_post(id)
    # if index == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id {id} was not found')
    # my_posts.pop(index)
    # return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/{id}',response_model=schemas.PostResponse)
def update_post(id:int,updated_post:schemas.PostBase,db: Session = Depends(database.get_db),current_user:int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    # conn = con.cursor()
    # conn.execute('''select * from posts where id = %s''',(id,))
    # bormikan_ozi = conn.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} was not found')
    # conn.execute('''update posts set title = %s,content = %s,published = %s where id = %s''',(post.title,post.content,post.published,id,))
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Boshqalarni nomidan delete qila olmaysan')
    # con.commit()
    # conn.execute('''select * from posts where id = %s''',(id,))
    # updated_post = conn.fetchone()
    # con.close()
    # return {'data': updated_post}
    post_query.update(updated_post.model_dump(),synchronize_session=False)
    db.commit()
    return post_query.first()
#     post_dict = post.model_dump()
#     post_dict['id'] = id
#     my_posts[index] = post_dict
#     return {'data':post_dict}
    # print(post)
    # return {'message':'succesfully updated'}