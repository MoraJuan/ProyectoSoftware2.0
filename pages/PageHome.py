from flet import Column, Container, ElevatedButton, Page, Row, Text, alignment


def PageHome(page: Page):
    page.title = "Gestión de Negocios"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.add(Text("Inicio"))

    # Crear botones del menú
    botones_menu = Column(
        [
            ElevatedButton("Realizar Venta", on_click=lambda e: page.go("/realizar_venta")),
            ElevatedButton("Ver Productos", on_click=lambda e: page.go("/ver_productos")),
            ElevatedButton("Ver Proveedores", on_click=lambda e: page.go("/ver_proveedores")),
            ElevatedButton("Ver Compradores", on_click=lambda e: page.go("/ver_compradores")),
            ElevatedButton("Ver Ventas", on_click=lambda e: page.go("/ver_ventas")),
        ],
        alignment="center",
        spacing=20,
    )

    # Estructura del layout
    layout_principal = Row(
        controls=[
            Container(
                content=botones_menu,
                width=300,
                alignment=alignment.center,
                padding=20,
            ),
        ],
        alignment="center",
    )

    # Agregar el layout a la página
    page.add(layout_principal)