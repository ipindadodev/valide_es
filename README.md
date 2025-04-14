# Valide.es

**Valide.es** es un microservicio open source para validar identificadores estructurados usados en España, como:

- DNI / NIE / NIF
- CIF (personas jurídicas)
- IBAN (cuentas bancarias)
- Teléfonos nacionales
- Códigos postales

Su objetivo es proporcionar una API sencilla, fiable y portable para validar datos normativos sin depender de servicios externos como RED SARA o formularios de terceros.

---

## 🚀 ¿Para qué sirve?

- Evita lógica duplicada en formularios y procesos internos
- Mejora la calidad de los datos desde el primer momento
- Centraliza la validación normativa española en un solo servicio

---

## ⚙️ Tecnologías

- [FastAPI](https://fastapi.tiangolo.com/) como framework de API
- Validación con [Pydantic](https://docs.pydantic.dev/)
- Pensado para ejecutarse en tu VPS o infraestructura local

---

## 📦 Instalación rápida

## Clona el repositorio
```bash
git clone https://github.com/ipindadodev/valide_es.git
cd valide_es
```

## Crea y activa entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate
```

## Instala dependencias
```bash
pip install -r requirements.txt

# Lanza el microservicio en local
uvicorn valide_es.main:app --reload
```