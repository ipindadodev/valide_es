# Valide.es
![Made in Spain](https://img.shields.io/badge/Made%20in-Spain-red?style=flat-square)
![Powered by FastAPI](https://img.shields.io/badge/Powered%20by-FastAPI-009688?style=flat-square&logo=fastapi)
![License MIT](https://img.shields.io/github/license/ipindadodev/valide_es?style=flat-square)
![Valide.es](https://img.shields.io/badge/Validaci%C3%B3n-espa%C3%B1ola-blue?style=flat-square)

![Valide.es logo](https://github.com/user-attachments/assets/782cf45c-a2f9-4316-933f-251fae002ba5)


**Valide.es** es un microservicio open source para validar identificadores estructurados usados en España, como:

- DNI / NIE / NIF (Personas físicas y jurídicas)
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
- Pensado para ejecutarse en tu servidor o infraestructura local

---

## 📦 Instalación rápida

```bash
# Clona el repositorio
git clone https://github.com/ipindadodev/valide_es.git
cd valide_es

# Crea y activa entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instala dependencias
pip install -r requirements.txt

# Lanza el microservicio en local
uvicorn valide_es.main:app --reload
```

---

## 📡 Endpoints disponibles

| Método | Endpoint      | Descripción                    |
|--------|---------------|--------------------------------|
| POST   | `/nif`        | Valida DNI/NIE/NIF             |
| POST   | `/iban`       | Valida IBAN español            |
| POST   | `/phone`      | Valida número nacional         |

---

## 🧾 Licencia

Este proyecto se publica bajo licencia [MIT](LICENSE).

---

## 💡 Roadmap

- Aún no decidido ¿quieres añadir algo? haz una PR

---

## ✨ Créditos

Creado con ❤️ por [@ipindadodev](https://github.com/ipindadodev) como herramienta libre, modular y robusta para validar datos estructurados en el ecosistema español.
