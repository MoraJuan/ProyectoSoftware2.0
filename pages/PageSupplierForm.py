
#? Importaciones
import flet as ft
from sqlalchemy.orm import Session
from services.supplierService import SupplierService
from ui.components.alerts import show_success_message, show_error_message


class PageSupplierForm:
    def __init__(self, page: ft.Page, session: Session, edit_mode=False):
        self.page = page
        self.session = session
        self.edit_mode = edit_mode
        self.supplier_service = SupplierService(session)
        self.page.title = "Agregar Proveedor" if not edit_mode else "Editar Proveedor"
        self.build_ui()
    
    #! Crea la vista de PageSupplier
    def build_ui(self):
        self.name_field = ft.TextField(
            label="Nombre", width=300, autofocus=True)
        self.email_field = ft.TextField(
            label="Email", width=300)
        self.phone_field = ft.TextField(
            label="Teléfono", width=300)
        self.address_field = ft.TextField(
            label="Dirección", width=300)

        self.cancel_button = ft.ElevatedButton(
            text="Cancelar",
            icon=ft.icons.CANCEL,
            on_click=self.go_back
        )
        self.save_button = ft.ElevatedButton(
            text="Guardar",
            icon=ft.icons.SAVE,
            on_click=self.save_supplier
        )

        self.page.add(
            ft.Column([
                ft.Container(
                    content=ft.Row([
                        ft.Text(
                            "Editar Proveedor" if self.edit_mode else "Nuevo Proveedor",
                            size=20,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            tooltip="Volver",
                            on_click=self.go_back
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    padding=10
                ),
                ft.Container(
                    content=ft.Column([
                        self.name_field,
                        self.email_field,
                        self.phone_field,
                        self.address_field,
                        ft.Row([
                            self.cancel_button,
                            self.save_button
                        ], spacing=10)
                    ]),
                    padding=10
                )
            ])
        )

        if self.edit_mode:
            self.load_supplier_data()

    #! Carga la informacion del proveedor para editar
    def load_supplier_data(self):
        try:
            supplier_id = self.page.client_storage.get("edit_supplier_id")
            if supplier_id:
                supplier = self.supplier_service.get_supplier_by_id(
                    supplier_id)
                if supplier:
                    self.name_field.value = supplier.name
                    self.email_field.value = supplier.email
                    self.phone_field.value = supplier.phone
                    self.address_field.value = supplier.address
                    self.page.update()
        except Exception as e:
            show_error_message(
                self.page, f"Error al cargar los datos del proveedor: {str(e)}")

    #! Guarda la informacion
    def save_supplier(self, e):
        try:
            if not all([
                self.name_field.value,
                self.email_field.value,
                self.phone_field.value,
                self.address_field.value
            ]):
                show_error_message(
                    self.page, "Por favor complete todos los campos")
                return

            supplier_data = {
                "name": self.name_field.value,
                "email": self.email_field.value,
                "phone": self.phone_field.value,
                "address": self.address_field.value
            }

            if self.edit_mode:
                supplier_id = self.page.client_storage.get("edit_supplier_id")
                self.supplier_service.update_supplier(
                    supplier_id, supplier_data)
                message = "Proveedor actualizado exitosamente"
            else:
                self.supplier_service.create_supplier(supplier_data)
                message = "Proveedor creado exitosamente"

            show_success_message(self.page, message)
            self.go_back(None)

        except Exception as e:
            show_error_message(
                self.page, f"Error al guardar el proveedor: {str(e)}")

    #! Ir al inicio
    def go_back(self, e):
        if self.edit_mode:
            self.page.client_storage.remove("edit_supplier_id")
        self.page.go("/ver_proveedores")
