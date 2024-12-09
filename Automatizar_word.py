import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate

doc = DocxTemplate('plantilla.docx')

fecha = datetime.today().strftime("%d/%m/%Y")
sede = 'augas'
# estado = 'mich'
# fase = '22'
# monto = '10000'
# monto_en_letra = 'diez mil'
# concepto = 'test'

constantes = {'fecha': fecha}

df = pd.read_excel('datos.xlsx')
for i, fila in df.iterrows():
    contenido = {
        'sede': fila["sede"],
        'estado': fila["estado"],
        'fase': fila["fase"],
        'monto': fila["monto"],
        'monto_en_letra': fila['monto_en_letra'],
        'concepto': fila["concepto"]
    }
    contenido.update(constantes)
    doc.render(contenido)
    doc.save(f"Formato_{fila['sede']}_{fila['estado']}.docx")

doc.render(constantes)
doc.save(f'prueba.docx')