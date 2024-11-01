# Trabajo Práctico Obligatorio
## Proyecto: Sistema de Gestión de Cámaras de Seguridad
[Link al Informe del Proyecto](https://uadeeduar.sharepoint.com/:w:/r/sites/Section_485647-Equipo08/Documentos%20compartidos/Equipo%2008/Equipo%2008%20-%20Informe%20de%20Proyecto.docx?d=w05161529d7724e51b4b158416e6f25ff&csf=1&web=1&e=EF7C84)
## DETALLE

### Explicación del sistema propuesto

El sistema propuesto se basa en la gestión de cámaras de seguridad, donde cada una está calificada por un número, por ejemplo: `CAM01`, `CAM02`, entre otras. Con un sensor, se reconocerá a la persona que pasó, incluyendo su nombre completo, DNI y otros datos que estén en la base central. Esta información luego se almacena en una lista.

El sistema es una simulación donde las cámaras serán el protagonista principal del programa y las personas tendrán un rol secundario para cumplir la función. Su objetivo principal es realizar el **reconocimiento facial** de cada persona, indicando por dónde pasó y quién es, para mantener la organización y el control.

### Funcionalidades previstas del sistema

1. **ABM de cámaras**: Alta, Baja y Modificación de cámaras.
2. **ABM de personas**: Alta, Baja y Modificación de personas.
3. **Log de eventos registrados por las cámaras**.
4. **Generación de informes** a través de eventos que reporten cantidad de asistencia, porcentaje, mínima y máxima.
5. **Contador de veces que una persona pasó por un lugar**: El sistema debe ser capaz de mostrar cuántas veces pasó una persona por un lugar, qué cámara lo detectó y cuándo, utilizando contadores, condicionales e iterativas.

### Descripción técnica

- **Simulación**: Este sistema es una simulación de un espacio geográfico sin cámaras de verdad. El programa realizará su objetivo basándose en los conceptos aprendidos en las clases y con código que irá afinándose mediante prueba y error, buscando una solución dinámica y organizada.
- **Almacenamiento de cámaras**: Las cámaras serán almacenadas en una lista que podrá ser gestionada por el cliente.
- **Matriz de usuarios**: Los usuarios generados, junto con sus respectivos datos (ID, Nombre de Usuario, Área y Rol), se almacenarán en una matriz.
- **Distribución de cámaras**: Todas las cámaras se irán guardando en una lista que, posteriormente, se volcará en una matriz para visualizar la distribución de las cámaras en el lugar.
- **Lugar específico**: El sistema simulará un lugar específico, elegido por el cliente, con una cantidad de personas que habitan en ese espacio.


![image](https://github.com/user-attachments/assets/168dba7f-25b2-45d7-9bde-cfaf1bc3d069)

### Tareas de Desarrollo

### RECOMENDACIÓN DEL PROFE PARA CRUD, al construir la función que "elimina" un elemento, recomendó mejor cambiarlo de estado "activo" a "inactivo".

A continuación se detallan las tareas de desarrollo propuestas para el sistema, incluyendo su estado actual y responsabilidades:

1. **ABM de Cámaras (Alta, Baja, Modificación)**
   - **Descripción**: Crear funciones que permitan agregar, eliminar y modificar cámaras en la lista.
   - **Responsable**: Kevin
   - **Estado**: Funciones iniciales ya creadas, se necesita organizarlas de la mejor manera, crear un punto de entrada al módulo (similar a un menú principal) y conectar el menú principal al menú de Cámaras.
   - WIP

2. **ABM de Personas (Alta, Baja, Modificación)**
   - **Descripción**: Implementar funciones para gestionar personas, con almacenamiento en la matriz de usuarios.
   - **Responsable**: Caro
   - **Estado**: Funciones iniciales ya creadas, se necesita organizarlas de la mejor manera, crear un punto de entrada al módulo (similar a un menú principal) y conectar el menú principal al menú de Personas.
   - WIP

3. **Log de Eventos**
   - **Descripción**: Desarrollar la funcionalidad de registro de eventos capturados por las cámaras, guardando el número de cámara, nombre de la persona, fecha y hora.
   - **Responsable**: Mariela Torres
   - **Estado**: Se desarrolló el log de eventos y se agregó al main con el menú correspondiente.

4. **Contador de Asistencias**
   - **Descripción**: Implementar un contador que muestre cuántas veces una persona pasó por cada cámara y cuándo.
   - **Responsable**: Mariela Torres
   - **Estado**: *(Pendiente)*

5. **Generación de Informes**
   - **Descripción**: Crear funciones que generen informes basados en los eventos registrados: asistencia, porcentaje, mínima y máxima.
   - **Responsable**: *(Asignar responsable)*
   - **Estado**: *(Pendiente)*

6. **Simulación y Pruebas**
   - **Descripción**: Crear un script de simulación para probar todas las funcionalidades del sistema.
   - **Responsable**: Mariela Torres
   - **Estado**: Se agregaron los 30 items para la precarga de datos para personas, camaras y log_eventos. *Actualizar teniendo en cuenta la segunda entrega*

7. **Revisión y Ajustes del Informe**
   - **Descripción**: Revisar el informe y asegurarse de que esté alineado con el desarrollo del código.
   - **Responsable**: *(Asignar responsable)*
   - **Estado**: *(Pendiente)*

8. **Documentación del Código**
   - **Descripción**: Documentar todas las funciones y su uso en el código.
   - **Responsable**: *(Asignar responsable)*
   - **Estado**: *(Pendiente)*
  
9. **Menu de inicio y validaciones**
   - **Descripción**: Crear un menu de inicio que de acceso a las diferentes funcionalidades del sistema
   - **Responsable**: Agustin
   - **Estado**: WIP
     
10.**Validación de datos ingresados**
   - **Descripción**: Crear funciones de validación del ingreso de datos, por ejemplo, verificar que el usuario ingrese el nombre y apellido cómo tipo de dato texto y no haya ningún carácter especial y/o números, etc.
   - **Responsable**:  *(Asignar responsable)*
   - **Estado**:  *(Asignar responsable)*

11.**Excepciones en el sistema**
   - **Descripción**: Crear y definir excepciones específicas para manejar errores dentro del sistema de gestión de cámaras:
        - InvalidInputError: Excepción para datos ingresados incorrectamente (formato de nombre, DNI, etc.).
        - CameraNotFoundError: Excepción para cuando se intenta acceder a una cámara inexistente.
        - PersonNotRegisteredError: Excepción para cuando una persona detectada no está registrada en el sistema.
        - EventNotLoggedError: Excepción para cuando no hay eventos registrados para una cámara o persona específica.
        - DuplicateEntryError: Excepción para evitar duplicados al agregar cámaras o personas.
        - DataTypeError: Excepción para manejar el ingreso de tipos de datos incorrectos (por ejemplo, caracteres especiales en un nombre). *(Relacionado con el punto anterior)*
   - **Responsable**:  *(Asignar responsable)*
   - **Estado**:  *(Asignar responsable)*
     
12.**Importar y exportar en Json los datos**
   - **Descripción**: Crear funciones para importar y exportar los datos del sistema en formato JSON, permitiendo almacenar los datos ingresados a modo de base de datos. Esto facilitará la persistencia de la información, permitiendo guardar y cargar el estado del sistema.
   - **Responsable**:  *(Asignar responsable)*
   - **Estado**:  *(Asignar responsable)*
