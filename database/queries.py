# database/queries.py

# ====================================================
# QUERIES DE INICIALIZACIÓN (TABLAS Y DATOS POR DEFECTO)
# ====================================================

CREATE_USUARIOS_TABLE = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
"""

COUNT_USUARIOS = """
SELECT COUNT(*) FROM usuarios
"""

INSERT_USUARIO = """
INSERT INTO usuarios (usuario, password) VALUES (?, ?)
"""

# ====================================================
# QUERIES DE AUTENTICACIÓN / LOGIN
# ====================================================

VERIFY_CREDENTIALS = """
SELECT * FROM profiles WHERE user_email = ? AND password = ?
"""