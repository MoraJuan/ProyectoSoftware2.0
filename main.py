# main.py
import sys
import os
import flet
from flet import Page, Text, ElevatedButton
from sqlalchemy.orm import sessionmaker
from database.connection import Base, engine, SessionLocal
from models import Customer, CommercialInvoice, User, Administrator, Employee, Product, Stock, Supplier

# Crear todas las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión
session = SessionLocal()

def main(page: Page):
    # Agregar un Cliente de muestra si no existe
    cliente = session.query(Customer).first()
    if not cliente:
        nuevo_cliente = Customer(name='Juan Perez', email='juan.perez@example.com')
        session.add(nuevo_cliente)
        session.commit()
        cliente = nuevo_cliente
    
    # Mostrar el Cliente
    page.add(Text(f"Cliente: {cliente.name}, Email: {cliente.email}"))
    
    # Botón para refrescar datos
    def refresh(e):
        cliente = session.query(Customer).first()
        page.controls.clear()
        page.add(Text(f"Cliente: {cliente.name}, Email: {cliente.email}"))
        page.add(ElevatedButton("Refresh", on_click=refresh))
        page.update()
    
    page.add(ElevatedButton("Refresh", on_click=refresh))

if __name__ == "__main__":
    flet.app(target=main)