# app/wsgi.py

from app.main import app
from fastapi.middleware.wsgi import WSGIMiddleware

application = WSGIMiddleware(app)

# This is a WSGI application that can be used with any WSGI server.