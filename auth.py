from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from security import OAuth2PasswordBearerWithCookie
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


# Clave secreta para firmar tokens (usá una más segura en producción)
SECRET_KEY = "mi_clave_super_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hashear_password(password):
    return pwd_context.hash(password)

def crear_token_acceso(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


#oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#from main import OAuth2PasswordBearerWithCookie
#oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="login")
oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="login")


security = HTTPBearer()

def obtener_usuario_actual(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
        return email
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
