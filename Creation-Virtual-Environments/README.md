# 🇪🇸 Crear un Entorno Virtual (venv) para Python en Terminal | 🇬🇧 Creating a Virtual Environment (venv) for Python in Terminal

## 🇪🇸 Crear un Entorno Virtual (venv) en la Terminal para Python

Este tutorial te guiará a través de los pasos necesarios para crear un entorno virtual (`venv`) en la terminal para poder trabajar con Python e instalar librerías necesarias para machine learning (ML), como PyTorch, TensorFlow y Keras. También aprenderás cómo gestionar versiones específicas de las librerías.

### 1. ¿Qué es un entorno virtual?

Un entorno virtual en Python permite aislar las dependencias de cada proyecto, evitando conflictos entre diferentes versiones de paquetes que puedan estar instalados globalmente. Esto es especialmente útil para proyectos de machine learning, donde las versiones de las librerías son cruciales.

### 2. Crear un entorno virtual

Sigue estos pasos para crear un entorno virtual usando `venv` en tu terminal:

1. Abre una terminal.
2. Navega a la carpeta donde quieras crear tu entorno virtual.
3. Ejecuta el siguiente comando para crear el entorno virtual:

```bash
python3 -m venv nombre_del_entorno
```
  - Reemplaza nombre_del_entorno con el nombre que quieras darle a tu entorno.

4. Activa el entorno virtual:

  - En macOS/Linux:
    
  ```bash
  source nombre_del_entorno/bin/activate
  ```
  - En Windows:
    
  ```bash
  .\nombre_del_entorno\Scripts\activate
  ```
Una vez activado, verás el nombre del entorno en la línea de comandos. Ahora, todas las librerías que instales se guardarán en este entorno.

### 3. Instalar las librerías necesarias para ML

Con el entorno activado, puedes instalar las librerías necesarias. A continuación te mostramos cómo instalar PyTorch, TensorFlow y Keras:

  - Para instalar PyTorch, consulta la página oficial de instalación de PyTorch para encontrar el comando adecuado según tu sistema operativo y configuración.

    Por ejemplo, para instalar PyTorch con CUDA 11.7:

```bash
pip install torch torchvision torchaudio
```
   - Para instalar Tensorflow:

```bash
pip install tensorflow
```
  - Para instalar Keras
```bash
pip install keras
```
### 4. Instalar versiones específicas de las librerías

Si necesitas instalar versiones específicas de las librerías, puedes hacerlo agregando la versión deseada al comando de instalación.

Por ejemplo:

  - Para instalar una versión específica de PyTorch:
```bash
pip install torch==1.10.0
```

  - Para instalar TensorFlow en una versión particular:

```bash
pip install tensorflow==2.6.0
```

Puedes buscar todas las versiones disponibles de las librerías en [PyPI](https://pypi.org/).

### 5. Desactivar el entorno virtual

Cuando termines de trabajar en el proyecto, puedes desactivar el entorno virtual con el siguiente comando:

```bash
deactivate
```

### 6. Recomendaciones adicionales

Mantén tu entorno limpio y asegúrate de gestionar las dependencias correctamente utilizando un archivo requirements.txt. Para generar este archivo, usa:

```bash
pip freeze > requirements.txt
```

### 7. Consulta de versiones

Para explorar las diferentes versiones de las librerías disponibles, visita [PyPI](https://pypi.org/).


## 🇬🇧 Creating a Virtual Environment (venv) in Terminal for Python

This tutorial will guide you through the steps required to create a virtual environment (`venv`) in the terminal to be able to work with Python and install libraries necessary for machine learning (ML), such as PyTorch, TensorFlow, and Keras. You will also learn how to manage specific versions of the libraries.

### 1. What is a virtual environment?

A virtual environment in Python allows you to isolate the dependencies of each project, avoiding conflicts between different versions of packages that may be installed globally. This is especially useful for machine learning projects, where library versions are crucial.

### 2. Create a virtual environment

Follow these steps to create a virtual environment using `venv` in your terminal:

1. Open a terminal.
2. Navigate to the folder where you want to create your virtual environment.
3. Run the following command to create the virtual environment:

```bash
python3 -m venv environment_name
```
- Replace environment_name with the name you want to give to your environment.

4. Activate the virtual environment:

- On macOS/Linux:

```bash
source environment_name/bin/activate
```
- On Windows:

```bash
.\environment_name\Scripts\activate
```
Once activated, you will see the name of the environment on the command line. Now, all the libraries you install will be saved in this environment.

### 3. Installing libraries needed for ML

With the environment enabled, you can install the necessary libraries. Here's how to install PyTorch, TensorFlow, and Keras:

- To install PyTorch, check the official PyTorch installation page to find the appropriate command for your operating system and setup.

For example, to install PyTorch with CUDA 11.7:

```bash
pip install torch torchvision torchaudio
```
- To install Tensorflow:

```bash
pip install tensorflow
```
- To install Keras
```bash
pip install keras
```
### 4. Installing specific versions of libraries

If you need to install specific versions of libraries, you can do so by adding the desired version to the installation command.

For example:

- To install a specific version of PyTorch:
```bash
pip install torch==1.10.0
```

- To install TensorFlow on a particular version:

```bash
pip install tensorflow==2.6.0
```

You can find all available versions of the libraries on [PyPI](https://pypi.org/).

### 5. Deactivate the virtual environment

When you finish working on the project, you can deactivate the virtual environment with the following command:

```bash
deactivate
```

### 6. Additional recommendations

Keep your environment clean and make sure to manage dependencies properly using a requirements.txt file. To generate this file, use:

```bash
pip freeze > requirements.txt
```

### 7. Checking versions

To explore the different versions of the available libraries, visit [PyPI](https://pypi.org/).


  
