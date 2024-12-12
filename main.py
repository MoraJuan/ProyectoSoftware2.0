# Import
import flet
from flet import Container, Page, Text, alignment

from database.connection import Base, SessionLocal, engine
from pages import PageHome, PageProduct, PageSupplier, PageSupplierForm

# Crear todas las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión
session = SessionLocal()

def main(page: Page):
    # Definir las rutas
    def route_change(route):
        page.clean()
        if page.route == "/":
            PageHome.PageHome(page)
        elif page.route == "/realizar_venta":
            page.add(Container(content=Text("Pantalla para realizar ventas"), alignment=alignment.center))
        elif page.route == "/ver_productos":
            PageProduct.PageProduct(page, session)
        elif page.route == "/ver_proveedores":
            PageSupplier.PageSupplier(page, session)
        elif page.route == "/agregar_proveedor":
            PageSupplierForm.PageSupplierForm(page, session, edit_mode=False)
        elif page.route == "/editar_proveedor":
            PageSupplierForm.PageSupplierForm(page, session, edit_mode=True)
        elif page.route == "/ver_compradores":
            page.add(Container(content=Text("Pantalla para ver compradores"), alignment=alignment.center))
        elif page.route == "/ver_ventas":
            page.add(Container(content=Text("Pantalla para ver ventas"), alignment=alignment.center))
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

if __name__ == "__main__":
    flet.app(target=main)