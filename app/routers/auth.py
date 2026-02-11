from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import User
from app.schemas.auth import LoginRequest
from app.core.security import verify_password, hash_password, create_access_token
from app.schemas.user import UserCreate, UserOut
from app.dependencies import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])


# =========================
# REGISTER
# =========================
@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):

    # Verificar si el email ya existe
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email ya registrado")

    db_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),  # ✅ CORRECTO
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# =========================
# LOGIN (email + password)
# =========================

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == data.email).first()

    if not db_user or not verify_password(data.password, db_user.password):
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    token = create_access_token({"user_id": db_user.id})

    return {
        "access_token": token,
        "token_type": "bearer"
    }