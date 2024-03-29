from flask import Flask, jsonify
from flask_graphql import GraphQLView
from werkzeug.utils import redirect

from models import db_session
from graphql_query import schema  # , introspection_dict

app = Flask(__name__)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    )
)


@app.route('/', methods=['GET'])
def export_graphql_json():
    return redirect('/graphql')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()
