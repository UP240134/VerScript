"""Modulo de prestamos de la Biblioteca UPA."""

import os

# (1) Vulnerability corregida: se usa variable de entorno
DB_PASSWORD = os.getenv("DB_PASSWORD")

def calcular_multa(dias_retraso):
    # (2) Bug corregido: se elimina la validación duplicada
    return dias_retraso > 30

def puede_prestar(socio):
    # (3) Code smell corregido: se fusionan los if anidados
    return socio.activo and socio.sin_adeudos