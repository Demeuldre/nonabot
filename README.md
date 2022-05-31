# Tabla de contenidos
  * [¿Qué es?](#que-es)
  * [Requerimientos](#requerimientos)
  * [Como utilizar](#como-utilizar)
  * [Descripción del Robot](#descripción-del-robot)
  * [Componentes Electrónicos](#componentes-electrónicos)
  * [Diseño](#diseño)
  * [Esquema Hardware](#esquema-hardware)
  * [Arquitectura del Software](#arquitectura-del-software)
  * [Fotos](#video)
  * [Bibliografia](#bibliografia)
  * [Autores](#autores)
  
# Requerimientos

For running each sample code:
- [Python 3.10.x](https://www.python.org/)
- [NumPy](https://numpy.org/)
- [Opencv](https://opencv.org/)
- [Keras](https://keras.io/)

For development:
  
- pytest (for unit tests)

# Como utilizar 
1. Clonar este repositiorio 
 > https://github.com/VerticalFarming/nonabot.git
2. Instalar el siguiente txt.
 usando pip: 
  pip install -r src/requirements.txt
3. Ejecutar el script de python en cada directorio.

# ¿Qué es?
El Nonabot es un robot capaz de resolver nonogramas.

# Descripción del Robot
Un nonograma es un rompecabezas que consiste en colorear las celdas según los números para revelar una imágen oculta. 

Hemos diseñao un H-Bot con el objetivo de resolver el puzle de forma autónoma mediante el uso de visión por computador, steppers y un manipulador para marcar las casillas.

# Componentes Electrónicos
  - Raspberry Pi 2 Modelo B
  - Raspberry Pi Camera v2
  - Arduino Uno
  - 2x NEMA22
  - Servomotor 8.5G
  - Fuente de alimentación ATX

# Diseño
<img src="/capturas/3d-general.PNG" width="500" height="344" >

Las piezas 3D se encuentran [aqui](https://github.com/VerticalFarming/nonabot/tree/master/piezas).

 - 4x Varillas de 12mm de diámetro
 - 4x Rodamientos de 12mm de diámetro
 - 2x Correas
 - Soporte de madera de 1x1 metros

# Esquema Hardware
<img src="/capturas/esquema-hardware.PNG" width="500" height="324" >

# Arquitectura del Software
<img src="/capturas/esquema-software.png" width="500" height="542" >

# Fotos
<img src="/capturas/imagen_1.jpeg" width="500" height="342" >
<img src="/capturas/imagen_2.jpeg" width="500" height="342" >
<img src="/capturas/imagen_3.jpeg" width="500" height="342" >

# Bibliografia
 - <a href="https://www.instructables.com/4xiDraw/">4xiDraw</a>

# Autores
 - <a href="https://github.com/oscar-sanchez27">Oscar Sanchez Lima</a>
 - <a href="https://github.com/VerticalFarming">Eric Demeuldre Val</a>
 - <a href="https://github.com/JoelFerrando">Joel Ferrando</a>
