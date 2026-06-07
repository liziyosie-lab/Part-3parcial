# Flask Login App - Entrega Participación

Aplicación Flask con autenticación usando **flask-login**, **flask-migrate** y **flask-bcrypt**.

## Requisitos previos
- Python 3.8 o superior instalado

## Instalación y ejecución

### Windows
1. Doble clic en `setup_windows.bat`
2. Cuando termine, ejecuta:
   ```
   venv\Scripts\activate
   python run.py
   ```

### Mac / Linux
1. Abre terminal en esta carpeta
2. Ejecuta:
   ```bash
   chmod +x setup_mac_linux.sh
   ./setup_mac_linux.sh
   source venv/bin/activate
   python run.py
   ```

3. Abre el navegador en: **http://127.0.0.1:5000**

## Funcionalidades
- ✅ Registro de usuarios (contraseña cifrada con flask-bcrypt)
- ✅ Login / Logout con flask-login
- ✅ Sesión persistente (opción "Recordarme")
- ✅ Rutas protegidas con `@login_required`
- ✅ Base de datos con migraciones (flask-migrate)
- ✅ Dashboard con información del usuario
