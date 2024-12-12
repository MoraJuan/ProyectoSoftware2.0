"""
Componentes de alerta reutilizables
"""
import flet as ft

def create_alert_dialog(title: str, content: str, actions=None):
    """Crea un diálogo de alerta personalizado"""
    return ft.AlertDialog(
        title=ft.Text(title),
        content=ft.Text(content),
        actions=actions or [
            ft.TextButton("OK", on_click=lambda _: True),
        ],
    )

def show_success_message(page: ft.Page, message: str):
    """Muestra un mensaje de éxito"""
    page.show_snack_bar(
        ft.SnackBar(
            content=ft.Text(message),
            bgcolor=ft.colors.GREEN,
        )
    )

def show_error_message(page: ft.Page, message: str):
    """Muestra un mensaje de error"""
    page.show_snack_bar(
        ft.SnackBar(
            content=ft.Text(message),
            bgcolor=ft.colors.RED,
        )
    )