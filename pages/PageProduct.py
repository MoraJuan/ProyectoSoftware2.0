import flet as ft
from sqlalchemy.orm import Session
from services.productService import ProductService

class PageProduct:
    def __init__(self, page: ft.Page, session: Session):
        self.page = page
        self.session = session
        self.page.title = "Lista de Productos"
        self.product_service = ProductService(session)
        self.build_ui()

    def build_ui(self):
        self.product_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Nombre")),
                ft.DataColumn(ft.Text("Precio")),
                ft.DataColumn(ft.Text("Stock")),
            ],
            rows=[]
        )
        
        self.name_input = ft.TextField(
            label="Nombre del Producto",
            width=300,
            bgcolor=ft.colors.BLACK87,  # Changed to dark background
            border_color=ft.colors.BLUE_400
        )
        self.price_input = ft.TextField(
            label="Precio",
            width=300,
            keyboard_type=ft.KeyboardType.NUMBER,
            bgcolor=ft.colors.BLACK87,  # Changed to dark background
            border_color=ft.colors.BLUE_400
        )
        self.stock_input = ft.TextField(
            label="Stock",
            width=300,
            keyboard_type=ft.KeyboardType.NUMBER,
            bgcolor=ft.colors.BLACK87,  # Changed to dark background
            border_color=ft.colors.BLUE_400
        )

        self.back_button = ft.IconButton(
            icon=ft.icons.ARROW_BACK,
            icon_color=ft.colors.BLUE_400,
            tooltip="Volver al inicio",
            on_click=lambda _: self.page.go("/")
        )

        self.add_button = ft.ElevatedButton(
            text="Agregar Producto",
            on_click=self.add_product,
            bgcolor=ft.colors.BLUE_400,
            color=ft.colors.WHITE
        )

        self.clear_button = ft.ElevatedButton(
            text="Limpiar Productos",
            on_click=self.clear_products,
            bgcolor=ft.colors.RED_400,
            color=ft.colors.WHITE
        )

        self.page.add(
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        self.back_button,
                        ft.Text("Gestión de Productos", 
                            size=20, 
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.BLUE_900)
                    ], alignment=ft.MainAxisAlignment.START),
                    ft.Container(
                        content=ft.Column([
                            self.name_input,
                            self.price_input,
                            self.stock_input,
                            ft.Row([
                                self.add_button,
                                self.clear_button
                            ])
                        ]),
                        padding=20,
                        bgcolor=ft.colors.BLACK87,  # Changed to dark background
                        border_radius=10
                    ),
                    self.product_table
                ])
            )
        )
        self.load_products()

    def load_products(self):
        try:
            self.product_table.rows.clear()
            products = self.product_service.get_all_products()
            for product in products:
                self.product_table.rows.append(
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text(str(product.id))),
                        ft.DataCell(ft.Text(product.name)),
                        ft.DataCell(ft.Text(f"${product.price:.2f}")),
                        ft.DataCell(ft.Text(str(product.stock))),
                    ])
                )
            self.page.update()
        except Exception as ex:
            self.page.show_snack_bar(
                ft.SnackBar(content=ft.Text(f"Error al cargar productos: {str(ex)}"))
            )

    def add_product(self, e=None):
        try:
            product_data = {
                "name": self.name_input.value,
                "price": float(self.price_input.value),
                "stock": int(self.stock_input.value)
            }
            self.product_service.create_product(product_data)
            self.clear_inputs()
            self.load_products()
            self.page.show_snack_bar(
                ft.SnackBar(content=ft.Text("Producto agregado correctamente"))
            )
        except ValueError:
            self.page.show_snack_bar(
                ft.SnackBar(content=ft.Text("Por favor, ingrese valores válidos"))
            )
        except Exception as ex:
            self.page.show_snack_bar(
                ft.SnackBar(content=ft.Text(f"Error: {str(ex)}"))
            )

    def clear_products(self, e=None):
        try:
            if self.product_service.delete_all_products():
                self.load_products()
                self.page.show_snack_bar(
                    ft.SnackBar(content=ft.Text("Productos eliminados correctamente"))
                )
            else:
                self.page.show_snack_bar(
                    ft.SnackBar(content=ft.Text("Error al eliminar productos"))
                )
        except Exception as ex:
            self.page.show_snack_bar(
                ft.SnackBar(content=ft.Text(f"Error: {str(ex)}"))
            )

    def clear_inputs(self):
        self.name_input.value = ""
        self.price_input.value = ""
        self.stock_input.value = ""
        self.page.update()