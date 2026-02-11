# 🚀 FastAPI Authentication API

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Uvicorn-ASGI-purple" />
  <img src="https://img.shields.io/badge/Passlib-1.7.4-orange" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
</p>

---

## 📖 Descripción

API REST desarrollada con **FastAPI** que incluye:

- ✅ Registro de usuarios
- ✅ Login con **email** y contraseña
- ✅ Hash seguro de contraseñas con **Passlib (bcrypt)**
- ✅ Sistema de roles (`admin`, `standard`)
- ✅ Manejo de sesiones
- ✅ Validaciones con Pydantic
- ✅ Documentación automática con Swagger

---

## 🏗️ Estructura del Proyecto
app/
│── main.py
│── database.py
│
├── models/
│ └── user.py
│
├── schemas/
│ └── auth.py
│
├── routers/
│ └── auth.py
│
└── core/
└── security.py

---

## 📌 Ejemplo de Schema (Login)

```python
# app/schemas/auth.py
from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


## Clonar repo
git clone https://github.com/tuusuario/tu-repo.git
cd tu-repo

Crear entorno virtual
python -m venv env

Linux / 🍎 Mac
source env/bin/activate

Instalar dependencias
pip install -r requirements.txt


pip install fastapi uvicorn passlib[bcrypt] python-jose python-multipart sqlalchemy


▶️ Ejecutar el Proyecto
uvicorn app.main:app --reload


http://127.0.0.1:8000




