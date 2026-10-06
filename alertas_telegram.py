import asyncio
import os
from datetime import datetime, timedelta
from telegram import Bot
from telegram.error import TelegramError

class ConfiguracionAlertas:
    def __init__(self):
        self.bot_token = os.getenv('BOT_TOKEN')
        self.chat_id_jhonatan = os.getenv('CHAT_ID_JHONATAN')
        self.chat_id_esposa = os.getenv('CHAT_ID_ESPOSA')
        
        if not all([self.bot_token, self.chat_id_jhonatan, self.chat_id_esposa]):
            raise ValueError("Faltan variables de entorno: BOT_TOKEN, CHAT_ID_JHONATAN, CHAT_ID_ESPOSA")

class GestorAlertasTelegram:
    def __init__(self, config):
        self.config = config
        self.bot = None
    
    async def inicializar_bot(self):
        """Inicializa el bot de Telegram en contexto async"""
        self.bot = Bot(token=self.config.bot_token)
    
    async def enviar_a_ambos(self, mensaje):
        """Envía mensaje a ambos usuarios"""
        try:
            if not self.bot:
                await self.inicializar_bot()
            
            # Enviar a Jhonatan
            await self.bot.send_message(
                chat_id=self.config.chat_id_jhonatan,
                text=mensaje
            )
            print(f"[{datetime.now()}] Mensaje enviado a Jhonatan: OK")
            
            # Enviar a Esposa
            await self.bot.send_message(
                chat_id=self.config.chat_id_esposa,
                text=mensaje
            )
            print(f"[{datetime.now()}] Mensaje enviado a Esposa: OK")
            
        except TelegramError as e:
            print(f"Error enviando mensaje: {e}")
        finally:
            await self.bot.close()
    
    async def alerta_pago_proximo(self):
        """Alerta de pago próximo a vencer"""
        mensaje = (
            "💰 *ALERTA DE PAGO PRÓXIMO*\n\n"
            "Tienes pagos próximos a vencer en los próximos días.\n"
            f"Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            "Revisa tu estado de cuentas."
        )
        await self.enviar_a_ambos(mensaje)
    
    async def alertas_hoy(self):
        """Alerta de pagos hoy"""
        mensaje = (
            "📅 *PAGOS HOY*\n\n"
            "Tienes pagos vencidos hoy. Por favor, realiza los pagos pendientes.\n"
            f"Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            "Acción requerida ahora."
        )
        await self.enviar_a_ambos(mensaje)
    
    async def resumen_diario(self):
        """Resumen financiero diario"""
        mensaje = (
            "📊 *RESUMEN FINANCIERO DIARIO*\n\n"
            f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            "Estado de cuentas actualizado.\n"
            "Revisa tus pendientes."
        )
        await self.enviar_a_ambos(mensaje)

async def main():
    """Función principal async"""
    try:
        config = ConfiguracionAlertas()
        gestor = GestorAlertasTelegram(config)
        
        print("Iniciando alertas de Telegram...")
        
        # Ejecutar alertas
        await gestor.alerta_pago_proximo()
        await asyncio.sleep(1)
        await gestor.alertas_hoy()
        await asyncio.sleep(1)
        await gestor.resumen_diario()
        
        print("Alertas completadas exitosamente")
        
    except Exception as e:
        print(f"Error en main: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())