from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import config

auth = HTTPBasicAuth()
users = config.users

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


# This is example API Resource

class Weather(Resource):
    @auth.login_required
    def get(self):
        """
        Route get method
        type something :)
        happy coding
        """

        return {'message': 'hello'}


    def post(self):
        """
        Route post method
        type something :)
        happy coding
        """

        pass


    def delete(self):
        """
        Route delete method
        type something :)
        happy coding
        """

        pass