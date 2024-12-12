import flet as ft
from sqlalchemy.orm import Session

from models import Product


class PageProduct:
    def __init__(self, page: ft.Page, session: Session):
        self.page = page
        self.session = session
        self.page.title = "Lista de Productos"
        self.build_ui()

    def build_ui(self):
        self.product_list = ft.ListView(expand=True)
        self.load_products()

        self.name_input = ft.TextField(label="Nombre del Producto")
        self.price_input = ft.TextField(label="Precio", keyboard_type=ft.KeyboardType.NUMBER)
        self.stock_input = ft.TextField(label="Stock", keyboard_type=ft.KeyboardType.NUMBER)
        self.add_button = ft.ElevatedButton(text="Agregar Producto", on_click=self.add_product)
        self.clear_button = ft.ElevatedButton(text="Limpiar Productos", on_click=self.clear_products)
        self.back_button = ft.ElevatedButton(text="Regresar", on_click=lambda e: self.page.go("/"))

        self.page.add(
            self.product_list,
            self.name_input,
            self.price_input,
            self.stock_input,
            self.add_button,
            self.clear_button,
            self.back_button
        )

    def load_products(self):
        self.product_list.controls.clear()
        products = self.session.query(Product).all()
        for product in products:
            self.product_list.controls.append(ft.Text(f"{product.name} - {product.price} - {product.stock}"))
        self.page.update()

    def add_product(self, e):
        new_product = Product(
            name=self.name_input.value,
            price=float(self.price_input.value),
            stock=int(self.stock_input.value)
        )
        self.session.add(new_product)
        self.session.commit()
        self.load_products()
        self.clear_inputs()

    def clear_inputs(self):
        self.name_input.value = ""
        self.price_input.value = ""
        self.stock_input.value = ""
        self.page.update()

    def clear_products(self, e):
        self.session.query(Product).delete()
        self.session.commit()
        self.load_products()