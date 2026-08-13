# 🐧 Rocky Linux CLI Setup & Filosofía CLI-First

> [!IMPORTANT]
> **Fuente de Verdad de Infraestructura Personal:** Guía de aprovisionamiento, arquitectura mental y runbook técnico para la laptop dedicada con Rocky Linux CLI (RHEL Family).

---

## 📑 Tabla de Contenidos
- [1. La Filosofía CLI-First: Ventaja Competitiva Real](#1-la-filosofía-cli-first-ventaja-competitiva-real)
- [2. La Arquitectura de 5 Capas del Bioinformático Senior](#2-la-arquitectura-de-5-capas-del-bioinformático-senior)
- [3. Runbook de Aprovisionamiento (Rocky Linux CLI)](#3-runbook-de-aprovisionamiento-rocky-linux-cli)
- [4. El Estándar de $2,500 USD/mes: De Starter a Senior](#4-el-estándar-de-2500-usdmes-de-starter-a-senior)

---

## 🧠 1. La Filosofía CLI-First: Ventaja Competitiva Real

Trabajar en la terminal (CLI) no es una moda ni estética "hacker"; es una **necesidad estructural y de rendimiento**:

1. **Procesamiento por Streams (Memory-Efficient):**
   Un archivo `.fastq` o `.vcf` de 80 GB no cabe en la memoria RAM de una laptop convencional para abrirse en una GUI. Con la CLI, usando **pipes (`|`)** y herramientas orientadas a flujos (`zcat`, `grep`, `awk`, `seqkit`), procesas el archivo en tiempo real sin cargar gigabytes a la memoria.
2. **Reproducibilidad & Automatización:**
   Los clics en una interfaz gráfica (GUI) no se pueden guardar en un repositorio de Git ni se pueden programar para ejecutarse a las 3:00 AM. Un pipeline en CLI es 100% auditable, versionable y automatizable.
3. **Entornos Remotos e Infraestructura HPC:**
   Los servidores de supercómputo (HPC, AWS Batch, clusters universitarios) **no tienen interfaz gráfica**. Dominar la CLI elimina la fricción de operar nodos remotos vía SSH.

> **Regla de Equilibrio:** Usa la GUI solo para visualizaciones finales complejas (ej. PyMOL para estructuras 3D o IGV para exploración visual). El 90% del trabajo duro (procesamiento, pipelines y análisis) ocurre en la CLI.

---

## 🏛️ 2. La Arquitectura de 5 Capas del Bioinformático Senior

```
+-----------------------------------------------------------------------+
|  CAPA 5: Agentes de IA en CLI (`agy`, `claude-code`, LLMs en stdout)  |
+-----------------------------------------------------------------------+
|  CAPA 4: Gestor de Sesiones & Multiplexor (`tmux` + `bash`)           |
+-----------------------------------------------------------------------+
|  CAPA 3: Procesamiento de Flujos de Texto (`grep`, `awk`, `sed`, `jq`) |
+-----------------------------------------------------------------------+
|  CAPA 2: Diagnóstico y Monitoreo (`htop`, `journalctl`, `systemctl`)  |
+-----------------------------------------------------------------------+
|  CAPA 1: Kernel & Sistema de Archivos (`ext4`, `XFS`, Permisos, POSIX)|
+-----------------------------------------------------------------------+
```

- **Capa 1 (Sistema & POSIX):** Entender estructura de directorios, usuarios, permisos (`chmod`, `chown`) y variables de entorno (`PATH`).
- **Capa 2 (Diagnóstico):** Identificar cuellos de botella de procesador o memoria con `htop`, e inspeccionar logs del sistema con `journalctl -f`.
- **Capa 3 (Streams):** Manipular datos tabulares y genómicos sin abrirlos por completo (`awk '{print $1}'`, `grep -c "^@"`).
- **Capa 4 (Multiplexor):** Mantener paneles independientes en la misma terminal y sesiones inmunes a desconexiones usando `tmux`.
- **Capa 5 (IA en CLI):** Integrar agentes como `agy` directamente en la consola para diagnosticar scripts y automatizar flujos sin salir de la terminal.

---

## 🛠️ 3. Runbook de Aprovisionamiento (Rocky Linux CLI)

### Paso 1: Actualizar el Sistema e Instalar Paquetes Esenciales
```bash
sudo dnf update -y
sudo dnf install -y curl wget git htop tmux tree fastfetch
```

### Paso 2: Instalar Node.js 20 LTS (Vía NodeSource)
```bash
curl -fsSL https://rpm.nodesource.com/setup_20.x | sudo bash -
sudo dnf install -y nodejs
node -v  # Verificar v20.x
npm -v   # Verificar v10.x
```

### Paso 3: Instalar e Iniciar Antigravity CLI (`agy`) Nativamente
```bash
# 1. Ejecutar script oficial de instalación (binario nativo)
curl -fsSL https://antigravity.google/cli/install.sh | bash

# 2. Agregar ~/.local/bin al PATH en bashrc
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# 3. Autenticarte con tu cuenta/suscripción
agy auth login
```
*(Sigue la URL mostrada y autoriza el código de 8 caracteres desde tu navegador).*

### Paso 4: Configuración Básica de `tmux`
```bash
# Crear sesión multiplexada
tmux new -s lab

# Comandos clave de tmux:
# Ctrl+b luego %  -> Dividir pantalla verticalmente
# Ctrl+b luego "  -> Dividir pantalla horizontalmente
# Ctrl+b luego d  -> Desconectarse manteniendo procesos vivos
# tmux attach -t lab -> Reconectarse a la sesión
```

---

## 💎 4. El Estándar de $2,500 USD/mes: De Starter a Senior

| Nivel | Habilidades Demostrables | Valor Comercial |
| :--- | :--- | :--- |
| **Nivel 1 (Starter Setup)** | `htop`, `tmux`, `git`, `systemctl`, comandos básicos de terminal. | $500 - $800 USD |
| **Nivel 2 (Bio-CLI Mastery)** | Streams (`awk`, `grep`), manipulación VCF/BAM con `samtools`/`bcftools`, `Conda`/`Mamba`. | $1,200 - $1,500 USD |
| **Nivel 3 (Junior de Élite)** | Pipelines en `Nextflow` + `Docker`/`Apptainer` + TDD en Python (`pytest`) + Contribución Open Source (`nf-core`). | **$2,500 - $3,500+ USD** |

---

*Documento creado para la persisitencia del setup y la maestría en la terminal de Rocky Linux.*
