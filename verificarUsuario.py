from fasthtml.common import *
def login_requerido(f):
    """Decorador para verificar login antes de acessar rotas protegidas."""
    def wrapper(req: Request):
        if not req.session.get('usuario'):  
            return Redirect("/login")  # 🔄 Redireciona para login se não autenticado
        return f(req)
    return wrapper
