# Data Scientist Challenge - LATAM Airlines 

Autor: Mario Guzmán Briones
email: mario.guzman@globant.com

### Desarrollo del desafío para postular a un cargo de Data Scientist en LATAM Airlines

# Estructuración del repositorio
challenge_ds_latam
│   README.md
│   setup.sh
│   requirements.in
│   requirements.txt
│   config.py
│   utilities.py
│   .gitignore    
└──/data
└──/metrics 
└──/models
└──/notebooks
└──/venv

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

### Correr la notebook **solution.ipynb** que contiene el EDA, la construcción del modelo y las conclusiones.