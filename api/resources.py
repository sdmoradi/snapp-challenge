from flask_restful import Resource


# This is example API Resource
class Weather(Resource):
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