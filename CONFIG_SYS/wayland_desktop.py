import hashlib
import os
import pathlib
import sys


def _file_hash(filepath) -> str:
    """Calcula un hash MD5 para comparar si dos archivos son idénticos."""
    hasher = hashlib.md5()
    with open(filepath, "rb") as file:
        hasher.update(file.read())
    return hasher.hexdigest()


def es_wayland() -> bool:
    if not sys.platform.startswith("linux"):
        return False

    # CORREGIDO: agregados los paréntesis () a .lower()
    xdg_session = os.environ.get("XDG_SESSION_TYPE", "").lower()
    wayland_display = os.environ.get("WAYLAND_DISPLAY", "")

    return xdg_session == "wayland" or bool(wayland_display)


def Existe_desktop(
    app_id: str = "app-python",
    app_name: str = "Mi Aplicacion",
    exec_cmd: str = "",
    icono_source_path: str = None,
    categoria: str = "Utility;",
):
    # Si no es Wayland (Windows, macOS o Linux X11), no hace nada
    if not es_wayland():
        return

    # 1. Definir rutas estándar de usuario
    datos_home = os.environ.get("XDG_DATA_HOME", os.path.expanduser("~/.local/share"))
    dir_apps = pathlib.Path(datos_home) / "applications"
    dir_apps.mkdir(parents=True, exist_ok=True)

    desktop_file_path = dir_apps / f"{app_id}.desktop"
    nombre_icono = app_id

    # 2. Copiar icono solo si existe la ruta proporcionada
    if icono_source_path and os.path.exists(icono_source_path):
        # CORREGIDO: la extensión se extrae de icono_source_path
        ext = pathlib.Path(icono_source_path).suffix.lower()

        if ext == ".png":
            icons_dir = (
                pathlib.Path(datos_home)
                / "icons"
                / "hicolor"
                / "512x512"
                / "apps"
            )
        else:
            icons_dir = (
                pathlib.Path(datos_home)
                / "icons"
                / "hicolor"
                / "scalable"
                / "apps"
            )

        icons_dir.mkdir(parents=True, exist_ok=True)
        target_icon_path = icons_dir / f"{app_id}{ext}"

        if not target_icon_path.exists() or _file_hash(
            icono_source_path
        ) != _file_hash(target_icon_path):
            with (
                open(icono_source_path, "rb") as src,
                open(target_icon_path, "wb") as dst,
            ):
                dst.write(src.read())

    # 3. Generar contenido del .desktop (sin espacios en '=' y con [Desktop Entry])
    desktop_content = f"""[Desktop Entry]
Type=Application
Name={app_name}
Exec={exec_cmd}
Icon={nombre_icono}
StartupWMClass={app_id}
Terminal=false
Categories={categoria}
"""

    # 4. Verificar si el archivo .desktop ya existe y si es idéntico
    if desktop_file_path.exists():
        try:
            contenido_existente = desktop_file_path.read_text(encoding="utf-8")
            if contenido_existente == desktop_content:
                # El archivo existente es exactamente igual: no se reescribe
                return
        except Exception:
            pass  # Si falla la lectura, reescribir por seguridad

    # 5. Escribir archivo
    desktop_file_path.write_text(desktop_content, encoding="utf-8")
    desktop_file_path.chmod(0o755)