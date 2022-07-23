from flask_restx.reqparse import RequestParser

page_parser: RequestParser = RequestParser()
page_parser.add_argument('page', type=int, location='args', required=False)
page_parser.add_argument('status', type=str, location='args', required=False)
