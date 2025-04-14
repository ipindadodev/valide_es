# app/wsgi.py

from app.main import app  # Este es tu FastAPI app

def application(scope, receive, send):
    """
    Adaptador ASGI a WSGI básico para FastAPI usando mod_wsgi.
    """
    if scope['type'] == 'http':
        from mangum import Mangum
        handler = Mangum(app)
        return handler(scope, receive, send)
    raise NotImplementedError(f"Scope type {scope['type']} not supported.")
# Este adaptador permite que tu aplicación FastAPI funcione con servidores WSGI.