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

    def build_ui(self):
        self.supplier_table = ft.Container()
        self.load_suppliers()

        self.home_button = ft.IconButton(
            icon=ft.icons.HOME,
            tooltip="Volver al inicio",
            on_click=lambda e: self.page.go("/")
        )

        self.page.add(
            ft.Container(
                content=ft.Column([
                    ft.Text("Proveedores", weight=ft.FontWeight.BOLD, size=20),
                    self.home_button,
                    self.supplier_table
                ])
            )
        )

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
                    # "Eliminar": ft.IconButton(
                    #     icon=ft.icons.DELETE,
                    #     tooltip=f"Eliminar {supplier.name}",
                    #     on_click=lambda e, supplier_id=supplier.id: self.delete_supplier(supplier_id),
                    #     icon_size=30,
                    #     icon_color="red"
                    # )
                }
                for supplier in suppliers
            ]

            self.supplier_table.content = DataTable(
                columns=["ID", "Nombre", "Email", "Teléfono", "Dirección"],
                data=suppliers_data
            )
            self.page.update()

        except Exception as e:
            show_error_message(self.page, f"Error al cargar los proveedores: {str(e)}")