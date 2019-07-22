from app import app, cfg

if __name__ == '__main__':
    app.run(debug=cfg.DEBUG, host=cfg.DEFAULT_SERVICE_URI, port=cfg.DEFAULT_SERVICE_PORT)