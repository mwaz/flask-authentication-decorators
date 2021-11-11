from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import uuid
from datetime import datetime, timedelta
from library.main import db, app
from library.models import BookModel, User, token_required


# register route
@app.route('/signup', methods=['POST'])
def signup_user(): 
    data = request.get_json() 
    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    user = User.query.filter_by(username=data['username']).first()
    if not user:
        new_user = User(public_id=str(uuid.uuid4()), username=data['username'], password=hashed_password, admin=False)
        db.session.add(new_user) 
        db.session.commit() 

        return jsonify({'message': 'registered successfully'}), 201
    else:
        return make_response(jsonify({"message": "User already exists!"}), 409)

# user login route
@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    if not auth or not auth.get('username') or not auth.get('password'):
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic-realm= "Login required!"'})

    user = User.query.filter_by(username=auth['username']).first()
    if not user:
        return make_response('Could not verify user!', 401, {'WWW-Authenticate': 'Basic-realm= "No user found!"'})

    if check_password_hash(user.password, auth.get('password')):
        token = jwt.encode({'public_id': user.public_id}, app.config['SECRET_KEY'], 'HS256')
        return make_response(jsonify({'token': token}), 201)

    return make_response('Could not verify password!', 403, {'WWW-Authenticate': 'Basic-realm= "Wrong Password!"'})


#  add a book
@app.route('/bookapi/addbook', methods=['POST'])
@token_required
def create_book(current_user):
    '''adds a new book to collection!'''
    data = request.get_json()
    book = BookModel.query.filter_by(title=data['title']).first()
    if book:
        return make_response(jsonify({"message": "Book with same title already exists!"}), 409)
    else:
        new_books = BookModel(title=data['title'], author=data['author'], owner=current_user) 
        db.session.add(new_books)  
        db.session.commit() 
        return jsonify({'message' : 'new book created'})

# get all books
@app.route('/bookapi/books', methods=['GET'])
@token_required
def get_books(current_user):
 
   books = BookModel.query.all()
   output = []
   for book in books:
       book_data = {}
       book_data['id'] = book.id
       book_data['title'] = book.title
       book_data['author'] = book.author
    #    book_data['owner'] = book.user_id
       output.append(book_data)
 
   return jsonify({'Books' : output})


# deleting a book
@app.route('/bookapi/books/<book_id>', methods=['DELETE'])
@token_required
def delete_book(book_id): 
 
   book = BookModel.query.filter_by(id=book_id).first()  
   if not book:  
       return jsonify({'message': 'book does not exist'})  
 
   db.session.delete(book) 
   db.session.commit()  
   return jsonify({'message': 'Book deleted'})
