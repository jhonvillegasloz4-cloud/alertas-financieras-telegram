#!/usr/bin/env python3
"""
🔔 SISTEMA DE ALERTAS WHATSAPP - GITHUB ACTIONS
Notificaciones automáticas en tiempo real vía Telegram
Ejecutado automáticamente cada día a las 9 AM
"""

import os
from datetime import datetime, timedelta
from typing import Dict, List

# ============================================================================
# CONFIGURACIÓN - DESDE GITHUB SECRETS
# ============================================================================

class ConfiguracionAlertas:
    """Configuración de Telegram desde GitHub Secrets"""

    # 🔑 CREDENCIALES TELEGRAM (Variables de GitHub Secrets)
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    CHAT_ID_JHONATAN = os.getenv("CHAT_ID_JHONATAN", "")
    CHAT_ID_ESPOSA = os.getenv("CHAT_ID_ESPOSA", "")

    # 📱 NÚMEROS DE DESTINO
    JHONATAN = "+573205550947"
    ESPOSA = "+573022615445"
    USUARIOS = [JHONATAN, ESPOSA]

    # ⏰ CONFIGURACIÓN DE HORARIOS
    ZONA_HORARIA = "America/Bogota"
    HORA_ALERTAS = "09:00"

    # 💰 OBLIGACIONES Y FECHAS DE PAGO
    OBLIGACIONES = {
        "Arriendo": {
            "valor": 700000,
            "fecha": "01",
            "tipo": "fijo"
        },
        "Mercado": {
            "valor": 800000,
            "fecha": "05",
            "tipo": "fijo"
        },
        "Jose": {
            "valor": 200000,
            "fecha": "10",
            "tipo": "deuda",
            "prioridad": "⚡ ACELERAR"
        },
        "Tata": {
            "valor": 300000,
            "fecha": "15",
            "tipo": "deuda",
            "prioridad": "⚡ ACELERAR"
        },
        "Pl Wom": {
            "valor": 44000,
            "fecha": "20",
            "tipo": "deuda",
            "prioridad": "⚡ ACELERAR"
        },
    }

    # RECORDATORIOS: Alertar 1, 2, 3 días antes
    DIAS_RECORDATORIO = [1, 2, 3]


# ============================================================================
# GESTOR DE ALERTAS TELEGRAM
# ============================================================================

class GestorAlertasTelegram:
    """Envía alertas a ambos números por Telegram"""

    def __init__(self):
        self.bot_token = ConfiguracionAlertas.BOT_TOKEN
        self.chat_ids = {
            "Jhonatan": ConfiguracionAlertas.CHAT_ID_JHONATAN,
            "Esposa": ConfiguracionAlertas.CHAT_ID_ESPOSA
        }
        self.historial = []

        # Intentar importar Telegram
        try:
            from telegram import Bot
            self.bot = Bot(token=self.bot_token)
            self.telegram_ok = True
            print("✅ Telegram conectado correctamente\n")
        except Exception as e:
            print(f"⚠️  Error de Telegram: {str(e)}")
            self.telegram_ok = False

    def enviar_a_ambos(self, mensaje: str, asunto: str = "Alerta Financiera") -> bool:
        """Envía el mismo mensaje a Jhonatan y su esposa"""

        print(f"\n📤 Enviando: {asunto}")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(mensaje)
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        for usuario, chat_id in self.chat_ids.items():
            if self.telegram_ok and chat_id:
                try:
                    self.bot.send_message(
                        chat_id=int(chat_id),
                        text=mensaje,
                        parse_mode='Markdown'
                    )
                    print(f"✅ {usuario} ({chat_id})")

                    self.historial.append({
                        "timestamp": datetime.now().isoformat(),
                        "usuario": usuario,
                        "estado": "enviado",
                        "asunto": asunto
                    })

                except Exception as e:
                    print(f"❌ Error en {usuario}: {str(e)}")
                    self.historial.append({
                        "timestamp": datetime.now().isoformat(),
                        "usuario": usuario,
                        "estado": "error",
                        "error": str(e),
                        "asunto": asunto
                    })
            else:
                print(f"⚠️  {usuario} - Sin Chat ID configurado")
                self.historial.append({
                    "timestamp": datetime.now().isoformat(),
                    "usuario": usuario,
                    "estado": "sin_configurar",
                    "asunto": asunto
                })

        return True

    def alerta_pago_proximo(self, concepto: str, valor: float,
                            fecha: str, dias_faltantes: int):
        """Alerta de pago próximo"""

        prioridad = ""
        if concepto in ["Jose", "Tata", "Pl Wom"]:
            prioridad = "\n⚡ PRIORIDAD: ACELERAR"

        mensaje = f"""🔔 *RECORDATORIO DE PAGO*

Concepto: {concepto}
Valor: ${valor:,.0f}
Fecha pago: {fecha}
Vencimiento: En {dias_faltantes} días{prioridad}

✅ Abre el sheet para detalles:
https://docs.google.com/spreadsheets/d/1AGw15nUa3O5nNRc9ckMcvVxlvLf0Sxf507Wqa59tqSg/"""

        self.enviar_a_ambos(mensaje, f"Recordatorio: {concepto}")

    def resumen_semanal(self, resumen: Dict):
        """Resumen financiero semanal"""

        mensaje = f"""📊 *RESUMEN FINANCIERO SEMANAL*
{datetime.now().strftime('%A, %d de %B de %Y')}

💰 *Comprometido esta semana:*
• Gastos Fijos: ${resumen.get('fijos', 0):,.0f}
• Gastos Variables: ${resumen.get('variables', 0):,.0f}
• Deudas a Cuotas: ${resumen.get('deudas', 0):,.0f}

📍 *Disponible:* ${resumen.get('disponible', 0):,.0f}

⚡ *DEUDAS PRIORITARIAS:*
• Jose - $200,000
• Tata - $300,000
• Pl Wom - $44,000

👉 Ver detalles en sheet"""

        self.enviar_a_ambos(mensaje, "Resumen Semanal")

    def confirmacion_aceleracion(self, deuda: str, monto_extra: float):
        """Confirma aceleración de deuda"""

        nueva_fecha = (datetime.now() + timedelta(days=30)).strftime("%d/%m/%Y")

        mensaje = f"""⚡ *DEUDA ACELERADA - CONFIRMADO*

Concepto: {deuda}
Monto adicional: ${monto_extra:,.0f}
Nueva fecha: {nueva_fecha}

✅ Pago acelerado registrado
💡 Ahorras intereses por cancelación anticipada

Ambos han sido notificados ✓"""

        self.enviar_a_ambos(mensaje, f"Aceleración: {deuda}")

    def alertas_hoy(self):
        """Verifica y envía alertas programadas para hoy"""

        hoy = datetime.now()
        dia_hoy = hoy.day

        for concepto, datos in ConfiguracionAlertas.OBLIGACIONES.items():
            dia_pago = int(datos["fecha"])

            # Calcular días faltantes
            if dia_pago >= dia_hoy:
                dias_faltantes = dia_pago - dia_hoy
            else:
                # Próximo mes
                dias_en_mes = (datetime(hoy.year, hoy.month + 1 if hoy.month < 12 else 1, 1)
                              - timedelta(days=1)).day
                dias_faltantes = (dias_en_mes - dia_hoy) + dia_pago

            # Enviar alerta si es uno de los días configurados
            if dias_faltantes in ConfiguracionAlertas.DIAS_RECORDATORIO:
                fecha_pago = f"{datos['fecha']:0>2}/{hoy.month:0>2}/{hoy.year}"
                self.alerta_pago_proximo(concepto, datos['valor'],
                                        fecha_pago, dias_faltantes)


# ============================================================================
# MAIN - EJECUTAR SISTEMA
# ============================================================================

def main():
    """Ejecuta el sistema de alertas"""

    print("\n" + "="*70)
    print("   🔔 ALERTAS TELEGRAM - EJECUCIÓN AUTOMÁTICA")
    print(f"   {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("="*70)

    # Validar que están configuradas las variables
    if not ConfiguracionAlertas.BOT_TOKEN:
        print("\n❌ ERROR: BOT_TOKEN no está configurado en GitHub Secrets")
        print("   Ve a Settings → Secrets and variables → Actions")
        print("   Agrega: BOT_TOKEN = tu_token")
        return

    if not ConfiguracionAlertas.CHAT_ID_JHONATAN:
        print("\n❌ ERROR: CHAT_ID_JHONATAN no está configurado en GitHub Secrets")
        return

    if not ConfiguracionAlertas.CHAT_ID_ESPOSA:
        print("\n❌ ERROR: CHAT_ID_ESPOSA no está configurado en GitHub Secrets")
        return

    # Inicializar gestor
    gestor = GestorAlertasTelegram()

    print(f"\n📱 USUARIOS CONFIGURADOS:")
    print(f"   • Jhonatan: {ConfiguracionAlertas.JHONATAN}")
    print(f"   • Esposa:   {ConfiguracionAlertas.ESPOSA}")

    # 1. Resumen semanal (solo lunes)
    if datetime.now().weekday() == 0:  # 0 = Lunes
        print("\n" + "─"*70)
        print("📊 ENVIANDO RESUMEN SEMANAL")
        print("─"*70)

        resumen = {
            "fijos": 2100917,
            "variables": 290000,
            "deudas": 1290694,
            "disponible": 961731
        }
        gestor.resumen_semanal(resumen)

    # 2. Alertas de pago próximo
    print("\n" + "─"*70)
    print("🔔 VERIFICANDO ALERTAS DE PAGO")
    print("─"*70)
    gestor.alertas_hoy()

    # 3. Historial
    print("\n" + "─"*70)
    print("📋 RESUMEN DE EJECUCIÓN")
    print("─"*70)

    for idx, msg in enumerate(gestor.historial, 1):
        print(f"\n{idx}. [{msg['timestamp']}]")
        print(f"   Usuario: {msg['usuario']}")
        print(f"   Asunto: {msg['asunto']}")
        print(f"   Estado: {msg['estado']}")

    # Resumen final
    print("\n" + "="*70)
    print(f"   ✅ EJECUCIÓN COMPLETADA")
    print(f"   Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"   Próxima ejecución: Mañana a las 9:00 AM")
    print("="*70 + "\n")

    return gestor


if __name__ == "__main__":
    main()
