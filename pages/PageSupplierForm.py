import flet as ft
from services.supplierService import SupplierService
from ui.components.alerts import show_success_message, show_error_message

def PageSupplierForm(page: ft.Page, session, edit_mode=False):
    page.title = "Agregar Proveedor" if not edit_mode else "Editar Proveedor"
    supplier_service = SupplierService(session)
    
    # Campos del formulario
    name_field = ft.TextField(
        label="Nombre",
        width=300,
        autofocus=True,
        required=True
    )
    email_field = ft.TextField(
        label="Email",
        width=300,
        required=True
    )
    phone_field = ft.TextField(
        label="Teléfono",
        width=300,
        required=True
    )
    address_field = ft.TextField(
        label="Dirección",
        width=300,
        required=True
    )

    def load_supplier_data():
        """Carga los datos del proveedor si estamos en modo edición"""
        if edit_mode:
            supplier_id = page.client_storage.get("edit_supplier_id")
            if supplier_id:
                supplier = supplier_service.get_supplier_by_id(supplier_id)
                if supplier:
                    name_field.value = supplier.name
                    email_field.value = supplier.email
                    phone_field.value = supplier.phone
                    address_field.value = supplier.address
                    page.update()

    def save_supplier(e):
        """Guarda o actualiza el proveedor"""
        try:
            if not all([
                name_field.value,
                email_field.value,
                phone_field.value,
                address_field.value
            ]):
                show_error_message(page, "Por favor complete todos los campos")
                return

            supplier_data = {
                "name": name_field.value,
                "email": email_field.value,
                "phone": phone_field.value,
                "address": address_field.value
            }

            if edit_mode:
                supplier_id = page.client_storage.get("edit_supplier_id")
                supplier_service.update_supplier(supplier_id, supplier_data)
                message = "Proveedor actualizado exitosamente"
            else:
                supplier_service.create_supplier(supplier_data)
                message = "Proveedor creado exitosamente"

            show_success_message(page, message)
            go_back(None)  # Volver a la lista después de guardar

        except Exception as ex:
            show_error_message(page, f"Error al guardar el proveedor: {str(ex)}")

    def go_back(e):
        """Vuelve a la lista de proveedores"""
        if edit_mode:
            page.client_storage.remove("edit_supplier_id")
        page.go("/ver_proveedores")

    # Construir la interfaz
    page.controls = [
        ft.Column([
            ft.Container(
                content=ft.Row([
                    ft.Text(
                        "Editar Proveedor" if edit_mode else "Nuevo Proveedor",
                        size=20,
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        tooltip="Volver",
                        on_click=go_back
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                padding=10
            ),
            ft.Container(
                content=ft.Column([
                    name_field,
                    email_field,
                    phone_field,
                    address_field,
                    ft.Row([
                        ft.ElevatedButton(
                            text="Cancelar",
                            icon=ft.icons.CANCEL,
                            on_click=go_back
                        ),
                        ft.ElevatedButton(
                            text="Guardar",
                            icon=ft.icons.SAVE,
                            on_click=save_supplier
                        ),
                    ], spacing=10)
                ]),
                padding=10
            )
        ])
    ]

    # Si estamos en modo edición, cargar los datos del proveedor
    if edit_mode:
        load_supplier_data()

    page.update()