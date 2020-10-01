from bottle import route, post, delete, put, run, response, request

from dto.userDto import UserUpdateDto, UserDto
from service.userService import UserService

service = UserService()


@route('/users')
def users():
    response.content_type = 'application/json'
    return UserDto.schema().dumps(service.find_all(), many=True)


@route('/users/<user_id>')
def user(user_id):
    response.content_type = 'application/json'
    return service.find_by_id(user_id).to_json()


@post('/users/add')
def create_user():
    # parse input data
    try:
        data = request.json
        p_user = UserUpdateDto.from_dict(data)
    except:
        raise ValueError
    if data is None:
        raise ValueError
    response.content_type = 'application/json'
    return service.add(p_user).to_json()


@put('/users/<user_id>')
def update_user(user_id):
    # parse input data
    try:
        data = request.json
        p_user = UserUpdateDto.from_dict(data)
    except:
        raise ValueError
    if data is None:
        raise ValueError
    response.content_type = 'application/json'
    return service.update(user_id, p_user).to_json()


@delete('/users/<user_id>')
def delete_user(user_id):
    service.delete(user_id)


run(host='0.0.0.0', port=5000, debug=True)
