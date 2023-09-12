from rasa_sdk import Tracker
from datetime import datetime
import re

class utilities:
    def get_action_before_action_listen(tracker: Tracker):
        latest_actions = []
        for e in tracker.events:
            if e['event'] == 'action':
                latest_actions.append(e)

        if len(latest_actions) > 1:
            return latest_actions[-3]['name']
        else:
            return None
        
    def decode_day(day):
        if day.islower():
            decode = {
                'lunes': 'Lunes',
                'martes': 'Martes',
                'miercoles': 'Miercoles',
                'jueves': 'Jueves',
                'viernes': 'Viernes',
                'sabado': 'Sabado',
                'domingo': 'Domingo'
            }
        else:
            decode = {
                'Monday': 'Lunes',
                'Tuesday': 'Martes',
                'Wednesday': 'Miercoles',
                'Thursday': 'Jueves',
                'Friday': 'Viernes',
                'Saturday': 'Sabado',
                'Sunday': 'Domingo'
            }

        for value in list(decode.values()):
            if value == day:
                return value

        return decode.get(day, None)
    
    def decode_aula(aula):
        decode = {
            'laboratorio 104': 'Lab. 104',
            'aula 101': 'Aula 101',
            'laboratorio 102': 'Lab. 102',
            'aula 102': 'Aula 102',
            'aula 302': 'Aula 302',
            'laboratorio 205': 'Lab. 205',
            'laboratorio 101': 'Lab. 101', 
            'aula 306': 'Aula 306',
            'laboratorio 103': 'Lab. 103',
            'aula 303': 'Aula 303',
            'aula 304': 'Aula 304',
            'laboratorio 204': 'Lab. 204',
            'aula 305': 'Aula 305', 
            'laboratorio 203': 'Lab. 203'
        }

        for value in list(decode.values()):
            if value == aula:
                return value

        return decode.get(aula, None)
    
    def obtener_hora(texto):
        print(texto, type(texto))
        if texto is None:
            return None
        regex = r"\b(\d{1,2})\b\s(?:d[eu]\sla)?\s(?:m[au]ñana|tarde)?\s(\d{1,2})?"
        matches = re.findall(regex, texto, re.IGNORECASE)
        print(matches)
        if matches:
            print(texto)
            match = matches[0]
            hora = match[0]
            if match[1]:
                minutos = match[1]
            else:
                minutos = '00'
            # Convertir la hora de la tarde a formato de 24 horas
            if "tarde" in texto.lower():
                hora = str(int(hora) + 12)
            segundos = "00"
            return f"{hora.zfill(2)}:{minutos}:{segundos}"
        
        return texto 
    
    def obtener_aula_numero(texto):
        list_aulas_json = [
            "Lab. 104",            
            "Aula 101",            
            "Lab. 102",            
            "Aula 102",            
            "Aula 302",            
            "Lab. 205",            
            "Lab. 101",            
            "Aula 306",            
            "Lab. 103",            
            "Aula 303",            
            "Aula 304",            
            "Lab. 204",            
            "Aula 305",            
            "Lab. 203"
        ]
        for aula in list_aulas_json:
            if aula == texto:
                return texto
        regex = r"(?i)(aula|laboratorio)(\s+(\d{3})|\s?(\d{1,3}))"
        matches = re.findall(regex, texto)

        for match in matches:
            opcion = match[0].lower().strip()
            numero = match[2] if match[2] else match[3]
            resultado = " ".join([opcion, numero])
            return resultado

        
    def obtener_dia_semana(texto):
        regex = r"(?i)(lunes|martes|miércoles|miercoles|jueves|viernes|sábado|sabado|domingo)"
        matches = re.findall(regex, texto)
        if matches:
            dia = matches[0].lower()
            return dia
        else:
            return texto
        


    def validar_entidades(tracker):
        entities = tracker.latest_message.get("entities")
        dia_values = set()
        tiempo_values = set()
        habitacion_values = set()

        for entity in entities:
            if entity["entity"] == "dia":
                dia_values.add(entity["value"])
            elif entity["entity"] == "tiempo":
                tiempo_values.add(entity["value"])
            elif entity["entity"] == "habitacion":
                habitacion_values.add(entity["value"])

        if len(dia_values) > 1 or len(tiempo_values) > 1 or len(habitacion_values) > 1:
            return 1
        else:
            print("Éxito")
            pass

            


