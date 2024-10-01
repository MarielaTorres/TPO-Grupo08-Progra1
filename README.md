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

