from flet import (Column, Container, CrossAxisAlignment, ElevatedButton,
                  MainAxisAlignment, Page, Row, Text, alignment)


def PageHome(page: Page):
    page.title = "Gestión de Negocios"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.scroll = "adaptive"
    page.padding = 20

    #!Crear botones del menú
    botones_menu = Column(
        [
            ElevatedButton("Realizar Venta",
                           on_click=lambda e: page.go("/realizar_venta")),
            ElevatedButton("Ver Productos",
                           on_click=lambda e: page.go("/ver_productos")),
            ElevatedButton("Ver Proveedores",
                           on_click=lambda e: page.go("/ver_proveedores")),
            ElevatedButton("Ver Compradores",
                           on_click=lambda e: page.go("/ver_compradores")),
            ElevatedButton(
                "Ver Ventas", on_click=lambda e: page.go("/ver_ventas")),
        ],
        alignment="center",
        spacing=20,
    )

    #!Vista de la pestaña principal
    page.add(
        Container(
            content=Column([
                Column([Text("inicio")]),
                Row(
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
            ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=40,
            ),
            alignment=alignment.center,
        )
    )
