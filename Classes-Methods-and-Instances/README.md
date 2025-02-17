¡Por supuesto! Aquí tienes un archivo `README.md` que funciona como un **tutorial** sobre clases, métodos, instancias y funciones en Python, basado en lo que hemos visto. Puedes copiar y pegar este contenido directamente en tu repositorio.

---

# 🇪🇸 Tutorial de Clases, Métodos e Instancias en Python

¡Bienvenido/a a este tutorial sobre clases, métodos e instancias en Python! Aquí aprenderás los conceptos básicos de la programación orientada a objetos (POO) en Python, incluyendo cómo crear clases, definir métodos, trabajar con instancias y entender la diferencia entre funciones y métodos.

---

## 📚 Contenido

1. [¿Qué es una clase?](#qué-es-una-clase)
2. [¿Qué es un método?](#qué-es-un-método)
3. [¿Qué es una instancia?](#qué-es-una-instancia)
4. [Diferencia entre funciones y métodos](#diferencia-entre-funciones-y-métodos)
5. [Ejemplo práctico: Clase Calculadora](#ejemplo-práctico-clase-calculadora)
6. [¿Cómo usar este tutorial?](#cómo-usar-este-tutorial)

---

## ¿Qué es una clase?

Una **clase** es una plantilla o un "molde" que define cómo serán los objetos de un tipo particular. Contiene atributos (datos) y métodos (funciones) que operan sobre esos datos.

### Ejemplo:
```python
class Calculadora:
    def __init__(self, marca):
        self.marca = marca  # Atributo de la clase
```

---

## ¿Qué es un método?

Un **método** es una función que está asociada a una clase. Los métodos definen el comportamiento de los objetos creados a partir de la clase.

### Ejemplo:
```python
class Calculadora:
    def suma(self, a, b):  # Método de la clase
        return a + b
```

---

## ¿Qué es una instancia?

Una **instancia** es un objeto creado a partir de una clase. Cada instancia tiene sus propios atributos y puede usar los métodos definidos en la clase.

### Ejemplo:
```python
calc = Calculadora("Casio")  # 'calc' es una instancia de la clase Calculadora
print(calc.marca)  # Salida: "Casio"
```

---

## Diferencia entre funciones y métodos

- **Función**: Es un bloque de código independiente que no está asociado a una clase.
- **Método**: Es una función que está asociada a una clase y opera sobre una instancia de esa clase.

### Ejemplo de función:
```python
def suma(a, b):
    return a + b
```

### Ejemplo de método:
```python
class Calculadora:
    def suma(self, a, b):
        return a + b
```

---

## Ejemplo práctico: Clase Calculadora

A continuación, te muestro un ejemplo completo de una clase `Calculadora` que incluye métodos para sumar, restar, multiplicar y dividir, además de un historial de operaciones.

### Código:
```python
class Calculadora:
    def __init__(self, marca):
        self.marca = marca  # Atributo de instancia
        self.historial = []  # Historial de operaciones

    def suma(self, a, b):
        resultado = a + b
        self.historial.append(f"Suma: {a} + {b} = {resultado}")
        return resultado

    def resta(self, a, b):
        resultado = a - b
        self.historial.append(f"Resta: {a} - {b} = {resultado}")
        return resultado

    def multiplicacion(self, a, b):
        resultado = a * b
        self.historial.append(f"Multiplicación: {a} * {b} = {resultado}")
        return resultado

    def division(self, a, b):
        if b == 0:
            return "Error: No se puede dividir por cero"
        resultado = a / b
        self.historial.append(f"División: {a} / {b} = {resultado}")
        return resultado

    def mostrar_historial(self):
        return self.historial

# Crear una instancia de la clase Calculadora
calc = Calculadora("Casio")

# Usar los métodos
print(calc.suma(10, 5))          # Salida: 15
print(calc.resta(10, 5))         # Salida: 5
print(calc.multiplicacion(10, 5)) # Salida: 50
print(calc.division(10, 5))       # Salida: 2.0
print(calc.mostrar_historial())   # Salida: ['Suma: 10 + 5 = 15', 'Resta: 10 - 5 = 5', ...]
```

---

## ¿Cómo usar este tutorial?

1. Clona este repositorio en tu máquina local.
2. Abre el archivo `README.md` para seguir las explicaciones.
3. Prueba el código en tu entorno de Python.
4. ¡Experimenta y modifica el código para aprender más!

---

## 📝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes sugerencias, mejoras o nuevos ejemplos, no dudes en hacer un fork del repositorio y enviar un pull request.

---

## 📄 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE). Siéntete libre de usar, modificar y distribuir el contenido.

---

## 📧 Contacto

Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue en este repositorio o contactarme directamente.

---

# 🇺🇸 Tutorial on Classes, Methods, and Instances in Python

Welcome to this tutorial on classes, methods, and instances in Python! Here you'll learn the basics of object-oriented programming (OOP) in Python, including how to create classes, define methods, work with instances, and understand the difference between functions and methods.

---

## 📚 Content

1. [What is a class?](#what-is-a-class)
2. [What is a method?](#what-is-a-method)
3. [What is an instance?](#what-is-an-instance)
4. [Difference between functions and methods](#difference-between-functions-and-methods)
5. [Practical example: Calculator Class](#practical-example-calculator-class)
6. [How to use this tutorial?](#how-to-use-this-tutorial)

---

## What is a class?

A **class** is a template or "blueprint" that defines how objects of a particular type will look. It contains attributes (data) and methods (functions) that operate on that data.

### Example:
```python
class Calculator:
    def __init__(self, brand):
        self.brand = brand  # Class attribute
```

---

## What is a method?

A **method** is a function that is associated with a class. Methods define the behavior of objects created from the class.

### Example:
```python
class Calculator:
    def add(self, a, b):  # Class method
        return a + b
```

---

## What is an instance?

An **instance** is an object created from a class. Each instance has its own attributes and can use the methods defined in the class.

### Example:
```python
calc = Calculator("Casio")  # 'calc' is an instance of the Calculator class
print(calc.brand)  # Output: "Casio"
```

---

## Difference between functions and methods

- **Function**: An independent block of code not associated with a class.
- **Method**: A function associated with a class that operates on an instance of that class.

### Function example:
```python
def add(a, b):
    return a + b
```

### Method example:
```python
class Calculator:
    def add(self, a, b):
        return a + b
```

---

## Practical example: Calculator Class

Below is a complete example of a `Calculator` class that includes methods for addition, subtraction, multiplication, and division, as well as an operation history.

### Code:
```python
class Calculator:
    def __init__(self, brand):
        self.brand = brand  # Instance attribute
        self.history = []  # Operation history

    def add(self, a, b):
        result = a + b
        self.history.append(f"Add: {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"Subtract: {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"Multiply: {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        result = a / b
        self.history.append(f"Divide: {a} / {b} = {result}")
        return result

    def show_history(self):
        return self.history

# Create an instance of the Calculator class
calc = Calculator("Casio")

# Use the methods
print(calc.add(10, 5))          # Output: 15
print(calc.subtract(10, 5))     # Output: 5
print(calc.multiply(10, 5))     # Output: 50
print(calc.divide(10, 5))       # Output: 2.0
print(calc.show_history())      # Output: ['Add: 10 + 5 = 15', 'Subtract: 10 - 5 = 5', ...]
```

---

## How to use this tutorial?

1. Clone this repository to your local machine.
2. Open the `README.md` file to follow the explanations.
3. Test the code in your Python environment.
4. Experiment and modify the code to learn more!

---

## 📝 Contributions

Contributions are welcome! If you have suggestions, improvements, or new examples, feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the [MIT](LICENSE) license. Feel free to use, modify, and distribute the content.

---

## 📧 Contact

If you have any questions or suggestions, please open an issue in this repository or contact me directly.

---

¡Espero que este tutorial te sea útil! 😊
