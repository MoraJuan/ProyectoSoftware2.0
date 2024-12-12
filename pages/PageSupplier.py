from flet import (Column, Container, ElevatedButton, FontWeight, IconButton,
                  MainAxisAlignment, Page, Row, Text, TextButton, icons)

from services.supplierService import SupplierService
from ui.components.alerts import (create_alert_dialog, show_error_message,
                                  show_success_message)
from ui.components.data_table import DataTable


def PageSupplier(page: Page, session):
    page.title = "Lista de Proveedores"
    supplier_service = SupplierService(session)

    def deleteSupplier(id):
        print(id)

    #!Carga los proveedores y los muestra en columnas
    def loadSuppliersTable():
        suppliers = supplier_service.get_all_suppliers()
        suppliers_data = [
            {
                "ID": supplier.id,
                "Nombre": supplier.name,
                "Email": supplier.email,
                "Teléfono": supplier.phone,
                "Dirección": supplier.address,
                "Elimar": IconButton(
                    icon=icons.DELETE,
                    tooltip=f"Eliminar {supplier.name}",
                    on_click=lambda e, supplier_id=supplier.id: deleteSupplier(
                        supplier_id),
                    icon_size=30,
                    icon_color="red"
                )
            }
            for supplier in suppliers
        ]

        return DataTable(
            columns=["ID", "Nombre", "Email",
                     "Teléfono", "Dirección", "Eliminar"],
            data=suppliers_data
        )

    #!Vista de la pestaña principal
    suppliersTable = loadSuppliersTable()
    page.add(
        Container(
            content=Column([
                Column([Text("Proveedores")]),
                IconButton(
                    icon=icons.HOME,
                    tooltip="Volver al inicio",
                    on_click=lambda e: page.go("/")
                ),
                suppliersTable
            ])
        )
    )
