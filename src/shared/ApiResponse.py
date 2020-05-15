from flask import Response, json


class ApiResponse:

    @staticmethod
    def custom_response(res, status_code):
        """
        Custom reponse function
        """
        return Response(
            mimetype="application/json",
            response=json.dumps(res),
            status=status_code
        )
