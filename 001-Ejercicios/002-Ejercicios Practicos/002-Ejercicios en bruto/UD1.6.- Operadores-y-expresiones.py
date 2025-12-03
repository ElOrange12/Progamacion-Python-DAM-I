'''
  Calculadora
  v1.0 Daniel Oliveira Vidal
  Calcula el impuesto de la venta de camisetas de una tienda.
'''

print("Programa calculadora de impuestos")
print("(c) 2025 Jose Vicente Carratalá")
print("Introduce una base y te calculo el IVA y el total")

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

base_imponible = input("Introduce la base imponible de la factura: ")

# Calculamos el IVA (asumiendo un 21%)
total_iva = float(base_imponible) * 0.21

# Calculamos el total general
total_factura = float(base_imponible) + total_iva

print(f'Base Imponible: {base_imponible}')
print(f'Impuesto a Valor Agregado (IVA): {total_iva:.2f}')
print(f'Total Factura: {total_factura:.2f}')
