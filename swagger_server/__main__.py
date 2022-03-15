#!/usr/bin/env python3

import connexion
from swagger_server.controllers import poll
from swagger_server import encoder


def main():
    poll.start_polling(25)
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.app.url_map.strict_slashes = False
    app.add_api('swagger.yaml', arguments={
                'title': 'Swagger Parser Microservice'})
    app.run(port=8081, debug=True)


if __name__ == '__main__':
    main()
