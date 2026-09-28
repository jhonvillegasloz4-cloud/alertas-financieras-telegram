# 🚀 SISTEMA DE ALERTAS TELEGRAM - GITHUB ACTIONS

Alertas financieras automáticas ejecutadas por GitHub cada día a las 9:00 AM.

**Costo:** $0 USD/mes ✅ (Completamente gratis)

---

## 📋 REQUISITOS

- Cuenta en GitHub (gratis)
- Bot de Telegram creado
- Token del bot
- Chat IDs de ambos usuarios

---

## ⚡ SETUP EN 5 PASOS

### PASO 1: Crear repositorio en GitHub

1. Ve a **https://github.com/new**
2. Nombre: `alertas-financieras-telegram`
3. Descripción: `Sistema de alertas financieras automáticas`
4. **Crear repositorio**

### PASO 2: Clonar repositorio en tu PC

```bash
git clone https://github.com/TU_USUARIO/alertas-financieras-telegram.git
cd alertas-financieras-telegram
```

Reemplaza `TU_USUARIO` con tu usuario de GitHub.

### PASO 3: Copiar archivos

Copia estos archivos a la carpeta:

```
alertas-financieras-telegram/
├── .github/
│   └── workflows/
│       └── alertas.yml
├── alertas_telegram.py
├── README.md
└── .gitignore
```

**Importante:** La carpeta `.github/workflows/` debe crearse exactamente así.

### PASO 4: Configurar GitHub Secrets

1. Ve a tu repositorio en GitHub
2. **Settings** → **Secrets and variables** → **Actions**
3. Haz clic en **"New repository secret"**
4. Agrega 3 secretos:

#### Secret 1:
- **Name:** `BOT_TOKEN`
- **Value:** `8710261366:AAETUjYc65JMNyF4m-jdnuKH6bY1Oq3UzPM`
- Click **"Add secret"**

#### Secret 2:
- **Name:** `CHAT_ID_JHONATAN`
- **Value:** Tu Chat ID (el número que obtuviste)
- Click **"Add secret"**

#### Secret 3:
- **Name:** `CHAT_ID_ESPOSA`
- **Value:** Chat ID de tu esposa (el número que obtuviste)
- Click **"Add secret"**

**Ejemplo:** Si tu Chat ID es `123456789`:
```
CHAT_ID_JHONATAN = 123456789
CHAT_ID_ESPOSA = 987654321
```

### PASO 5: Subir archivos a GitHub

```bash
# Agregar todos los archivos
git add .

# Crear commit
git commit -m "Setup inicial: alertas telegram automáticas"

# Subir a GitHub
git push origin main
```

---

## ✅ VERIFICAR QUE FUNCIONA

### Opción A: Esperar a las 9:00 AM

Los mensajes deberían llegar automáticamente a Telegram.

### Opción B: Ejecutar manualmente

1. Ve a tu repositorio en GitHub
2. **Actions** (pestaña)
3. **Alertas Financieras Telegram** (en la lista)
4. Haz clic en **"Run workflow"** → **"Run workflow"**
5. Espera 2-3 minutos

Verás los logs de la ejecución.

---

## 📊 ¿QUÉ RECIBIRÁN?

Cada día a las 9:00 AM:

### 🔔 Recordatorios de Pago
- 1 día antes
- 2 días antes
- 3 días antes

### 📊 Resumen Financiero
- Solo los lunes a las 9:00 AM
- Disponibilidad de efectivo
- Deudas prioritarias
- Comprometido del mes

### ⚡ Confirmación de Aceleración
- Cuando aceleres una deuda
- Monto pagado
- Nueva fecha de vencimiento

---

## 🔄 ACTUALIZAR VALORES

Si necesitas cambiar algo:

### Cambiar hora de ejecución

**Archivo:** `.github/workflows/alertas.yml`

Línea:
```yaml
- cron: '0 14 * * *'  # Cambiar '14' por la hora deseada
```

Ejemplo: Para 10 AM (15:00 UTC):
```yaml
- cron: '0 15 * * *'
```

### Cambiar valores de obligaciones

**Archivo:** `alertas_telegram.py`

```python
"Jose": {
    "valor": 200000,  # ← Cambiar aquí
    "fecha": "10",    # ← O aquí
    "tipo": "deuda",
}
```

### Agregar nueva obligación

```python
"Nueva": {
    "valor": 50000,
    "fecha": "25",
    "tipo": "deuda",
}
```

---

## 📝 DESPUÉS DE CAMBIOS

```bash
# Agregar cambios
git add .

# Crear commit
git commit -m "Actualizar: Jose a 250000"

# Subir
git push origin main
```

La próxima ejecución automática usará los cambios.

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### Los mensajes no llegan

**Verificar:**
1. Los Chat IDs están correctos en GitHub Secrets
2. El Bot Token es correcto
3. Ve a **Actions** y revisa los logs

### Error: "Authentication failed"

Verifica que:
- BOT_TOKEN sea exacto (sin espacios)
- CHAT_ID_JHONATAN sea solo números
- CHAT_ID_ESPOSA sea solo números

### No veo los logs

1. Ve a tu repositorio en GitHub
2. **Actions** (pestaña)
3. Haz clic en la última ejecución
4. Haz clic en **"alertas"**
5. Expande los pasos para ver detalles

---

## 📋 CHECKLIST FINAL

- [ ] Repositorio creado en GitHub
- [ ] Archivos copiados a la carpeta
- [ ] Carpeta `.github/workflows/` creada
- [ ] 3 Secrets configurados en GitHub
- [ ] Primer `git push` hecho
- [ ] Ejecuté manualmente desde Actions (opcional)
- [ ] Recibí mensajes de prueba en Telegram

---

## 🎯 PRÓXIMOS PASOS

- **Hoy:** Setup completado ✅
- **Mañana:** Verificar que se ejecute a las 9 AM
- **Próximas semanas:** Recibir alertas automáticas

---

## 📞 INFORMACIÓN DE REFERENCIA

| Item | Valor |
|------|-------|
| Hora ejecución | 9:00 AM (Bogotá) = 14:00 UTC |
| Frecuencia | Diariamente |
| Costo | $0 USD/mes |
| Bot Token | En GitHub Secrets (seguro) |
| Chat IDs | En GitHub Secrets (seguro) |

---

## 🔐 SEGURIDAD

Los datos sensibles (Bot Token, Chat IDs) están en **GitHub Secrets** que:
- ✅ No se muestran en los logs
- ✅ No se suben al repositorio
- ✅ Solo GitHub Actions puede accederlos
- ✅ Están encriptados

---

**¿Listo?** Sigue los 5 pasos arriba para completar el setup. 🚀

Última actualización: 28/09/2026
