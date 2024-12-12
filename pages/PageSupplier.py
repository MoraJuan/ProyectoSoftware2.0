
#? Importaciones
import flet as ft
from sqlalchemy.orm import Session
from services.supplierService import SupplierService
from ui.components.data_table import DataTable
from ui.components.alerts import show_success_message, show_error_message


class PageSupplier:
    def __init__(self, page: ft.Page, session: Session):
        self.page = page
        self.session = session
        self.page.title = "Lista de Proveedores"
        self.supplier_service = SupplierService(session)
        self.build_ui()

    #! Crea la vista de PageSupplier
    def build_ui(self):
        self.supplier_table = ft.Container()
        self.load_suppliers()

        self.home_button = ft.IconButton(
            icon=ft.icons.HOME,
            tooltip="Volver al inicio",
            on_click=lambda e: self.page.go("/")
        )

        self.add_button = ft.ElevatedButton(
            "Agregar Proveedor",
            on_click=lambda e: self.page.go("/agregar_proveedor")
        )

        self.page.add(
            ft.Container(
                content=ft.Column([
                    ft.Text("Proveedores", weight=ft.FontWeight.BOLD, size=20),
                    self.home_button,
                    self.add_button,
                    self.supplier_table
                ])
            )
        )

    #! Carga los proveedores de la base de datos y crea la tabla
    def load_suppliers(self):
        try:
            suppliers = self.supplier_service.get_all_suppliers()
            suppliers_data = [
                {
                    "ID": supplier.id,
                    "Nombre": supplier.name,
                    "Email": supplier.email,
                    "Teléfono": supplier.phone,
                    "Dirección": supplier.address,
                }
                for supplier in suppliers
            ]

            self.supplier_table.content = DataTable(
                columns=["ID", "Nombre", "Email", "Teléfono", "Dirección"],
                data=suppliers_data,
                on_select=self.on_edit_supplier,
                on_delete=self.on_delete_supplier
            )
            self.page.update()

        except Exception as e:
            show_error_message(
                self.page, f"Error al cargar los proveedores: {str(e)}")

    #! Permite editar los proveedores
    def on_edit_supplier(self, supplier):
        try:
            self.page.client_storage.set("edit_supplier_id", supplier["ID"])
            self.page.go("/editar_proveedor")
        except Exception as e:
            show_error_message(
                self.page, f"Error al editar el proveedor: {str(e)}")

    #! Permite eliminar los proveedores
    def on_delete_supplier(self, supplier):
        try:
            supplier_id = supplier["ID"]
            self.supplier_service.delete_supplier(supplier_id)
            show_success_message(self.page, "Proveedor eliminado exitosamente")
            self.load_suppliers()
        except Exception as e:
            show_error_message(
                self.page, f"Error al eliminar el proveedor: {str(e)}")
