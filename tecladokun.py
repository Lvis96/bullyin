import keyboard
import openpyxl
from datetime import datetime

# Lista de señales de bullying
bullying_keywords = ["insulto1", "insulto2", "insulto3"]

# Archivo Excel para el reporte
report_filename = "reporte_bullying.xlsx"
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Reporte Bullying"
sheet.append(["Fecha y Hora", "Palabra Detectada"])

def check_for_bullying_words(event):
    if event.event_type == keyboard.KEY_DOWN:
        if hasattr(event, "name") and event.name is not None:
            typed_word = event.name.lower()
            print("Palabra capturada:", typed_word)
            for keyword in bullying_keywords:
                if keyword in typed_word:
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    sheet.append([current_time, keyword])
                    workbook.save(report_filename)
                    print("¡Alerta de bullying! Palabra detectada:", keyword)

keyboard.hook(check_for_bullying_words)

print("Comenzando a monitorear el teclado para señales de bullying. Presiona Ctrl + C para detener.")
keyboard.wait("ctrl+c")
