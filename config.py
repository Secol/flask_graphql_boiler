class DevConfig():

    DEBUG=True
    DEFAULT_SERVICE_URI='0.0.0.0'
    DEFAULT_SERVICE_PORT=8666

    SECRET_KEY='secret'

    ERROR_HTTP_VERB={
        'message' : 'Ooooops...'
    }


class ProdConfig():

    DEBUG=False
    DEFAULT_SERVICE_URI='0.0.0.0'
    DEFAULT_SERVICE_PORT=8666

    SECRET_KEY='secret'

    ERROR_HTTP_VERB={
        'message' : 'Ooooops...'
    }