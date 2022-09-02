# Data Scientist Challenge - LATAM Airlines 

- Autor: Mario Guzmán Briones 
- email: mario.guzman@globant.com

### Desarrollo del desafío para postular a un cargo de Data Scientist en LATAM Airlines

# Estructuración del repositorio

```
challenge_ds_latam
│   README.md
│   setup.sh              # Configuraciones del ambiente
│   requirements.in       # Requerimientos
│   requirements.txt
│   config.py             # Configuraciones necesarias para la notebook
│   utilities.py          # Funciones requeridas para la notebook
│   .gitignore        
└──/data                  # Almacenamiento de las métricas, y dataset
    └──/metrics_models    # Dataset con las métricas de los modelos  
└──/models                # Modelos entrenados
    └──/atraso_completo
    └──/atraso_lunes
    └──/atraso_martes
    └──/atraso_miercoles
    └──/atraso_jueves
    └──/atraso_viernes
    └──/atraso_sabado
    └──/atraso_domingo
    └──/atraso_manana
    └──/atraso_tarde
    └──/atraso_noche
└──/notebooks             # Notebook desarrollada
    └──/solution.ipynb        
└──/venv                  # virtual environmet
```

# Environment:
    - Python 3.8.2

### Para ejecutar nuevamente este script se debe crear un virtual environment

```
# Crear carpeta del virtual environment
mkdir venv
# Crear virtual environment
python3 -m venv venv/
```

### Cambiar al virtual environment

```
source venv/bin/activate
```

### Configurar virual environment con las dependencias necesarias

```
sh setup.sh
```

### Trabajar desde jupyter lab

```
jupyter lab
```

### Correr la notebook **solution.ipynb** que contiene el EDA, la construcción del modelo y las conclusiones.