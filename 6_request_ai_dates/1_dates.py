
from datetime import datetime, timedelta


# 1. Obtener la hora y fecha alcual 
now = datetime.now()
print(f"Fecha y hora actual: {now}")

# 2. Crear fecha y hora especifica
specific_date = datetime(2025, 10, 1, 12, 0, 0) # 1 de octubre de 2025 a las 12:00:00
print(f"Fecha y hora especifica: {specific_date}")

# 3. Formatear fechas y horas. strftime(). Pasarle el objeto datetime y el formate especificado.
# Formato: %Y (año) %m (mes) %d (dia) %H (hora) %M (minuto) %S (segundo)
formatted_date = now.strftime("%d-%m-%Y")
print(f"Fecha formateada: {formatted_date}")

# 4. Operaciones con fechas y horas. timedelta(). Sumar o restar tiempo a una fecha.
yerterday = datetime.now - timedelta(days=1) # Restar un dia
print(f"Ayer: {yerterday}")

tomorrow = datetime.now + timedelta(days=1) # Sumar un dia
print(f"Tomorrow: {tomorrow}")

one_hour_later = datetime.now + timedelta(hours=1) # Sumar una hora
print(f"Una hora mas tarde: {one_hour_later}")

# 5. Obtener componentes individuales de una fecha y hora.
year = now.year
month = now.month
day = now.day
print(f"Año: {year}, Mes: {month}, Dia: {day}")

# 6. Calcular diferencia entre dos fechas.
date1 = datetime.now()
date2 = datetime(2025, 10, 1, 12, 0, 0) 
diference = date2 - date1 # Diferencia entre las dos fechas
print(f"Diferencia entre las dos fechas: {diference}")

# 7. Convertir una cadena a fecha
#import locale 
# locale.setlocale("es_ES.UTF-8") # Cambiar la localizacion a español