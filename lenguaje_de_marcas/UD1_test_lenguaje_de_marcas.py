import random

# Lista de preguntas y respuestas
preguntas = preguntas = [
    ("¿Cuál es la etiqueta utilizada para crear un salto de línea?", [
        "a) <hr>",
        "b) <newline>",
        "c) <linebreak>",
        "d) <br>"
    ], "d"),
    ("¿Cuál es el atributo que se utiliza en una lista ordenada para indicar el número del primer elemento?", [
        "a) start",
        "b) reversed",
        "c) initial",
        "d) index"
    ], "a"),
    ("¿Qué etiqueta se utiliza para mostrar un bloque de cita con márgenes y espaciado?", [
        "a) <quote>",
        "b) <cite>",
        "c) <blocktext>",
        "d) <blockquote>"
    ], "d"),
    ("¿Cuál es el elemento utilizado para crear un salto de línea en un formulario?", [
        "a) <formline>",
        "b) <break>",
        "c) <br>",
        "d) <linebreak>"
    ], "c"),
    ("¿Cuál es la etiqueta para mostrar texto preformateado?", [
        "a) <text>",
        "b) <pre>",
        "c) <formatted>",
        "d) <code>"
    ], "b"),
    ("¿Qué atributo se usa para definir el nombre de una sección de enlace interno?", [
        "a) href",
        "b) id",
        "c) link",
        "d) target"
    ], "b"),
    ("¿Cuál es el tipo de ruta que se toma como referencia la carpeta actual?", [
        "a) Rutas relativas",
        "b) Rutas absolutas",
        "c) Rutas externas",
        "d) Rutas internas"
    ], "a"),
    ("¿Cuál es la etiqueta para mostrar información de contacto en cursiva?", [
        "a) <info>",
        "b) <contact>",
        "c) <address>",
        "d) <italic>"
    ], "c"),
    ("¿Cuál es la etiqueta para crear un enlace en una página web?", [
        "a) <a>",
        "b) <link>",
        "c) <href>",
        "d) <url>"
    ], "a"),
    ("¿Qué etiqueta se utiliza para mostrar una línea horizontal en la página?", [
        "a) <line>",
        "b) <divider>",
        "c) <hr>",
        "d) <horizontal>"
    ], "c"),
    ("¿Cuál es el atributo que se utiliza para especificar el número de columnas que ocupa un elemento de tabla?", [
        "a) span",
        "b) colspan",
        "c) rows",
        "d) columnspan"
    ], "b"),
    ("¿Qué atributo se utiliza para indicar el idioma principal de un documento HTML?", [
        "a) <language>",
        "b) <lang>",
        "c) <mainLang>",
        "d) <htmlLang>"
    ], "b"),
    ("¿Cuál es el elemento utilizado para definir una lista no ordenada?", [
        "a) <ul>",
        "b) <ol>",
        "c) <li>",
        "d) <list>"
    ], "a"),
    ("¿Cuál es el atributo utilizado en una lista ordenada para indicar un número negativo como primer elemento?", [
        "a) <start>",
        "b) <initial>",
        "c) <negnum>",
        "d) <number>"
    ], "a"),
    ("¿Qué etiqueta se utiliza para crear un salto de línea en un párrafo?", [
        "a) <br>",
        "b) <newline>",
        "c) <hr>",
        "d) <line>"
    ], "a"),
    ("¿Cuál es la etiqueta utilizada para insertar imágenes en una página web?", [
        "a) <image>",
        "b) <picture>",
        "c) <img>",
        "d) <photo>"
    ], "c"),
    ("¿Qué significa HTML?", [
        "a) Hyper Text Markup Language",
        "b) High Technical Modern Language",
        "c) Hyperlink and Text Markup Language",
        "d) Home Tool Markup Language"
    ], "a"),
    ("¿Cuál es la etiqueta utilizada para definir un encabezado de primer nivel en HTML?", [
        "a) <h1>",
        "b) <header>",
        "c) <head1>",
        "d) <primary>"
    ], "a"),
    ("¿Qué etiqueta se utiliza para crear un elemento de una lista en HTML?", [
        "a) <ul>",
        "b) <li>",
        "c) <ol>",
        "d) <dl>"
    ], "b"),
    ("¿Qué elemento se utiliza para agrupar elementos en un formulario HTML?", [
        "a) <fieldset>",
        "b) <group>",
        "c) <formgroup>",
        "d) <container>"
    ], "a"),
    ("¿Cuál es la etiqueta para crear un enlace de correo electrónico en HTML?", [
        "a) <mail>",
        "b) <email>",
        "c) <a>",
        "d) <mailto>"
    ], "c"),
    ("¿Qué etiqueta se utiliza para resaltar texto en cursiva en HTML?", [
        "a) <italic>",
        "b) <em>",
        "c) <k>",
        "d) <cursive>"
    ], "b"),
    ("¿Cuál es el atributo que se utiliza para definir un texto de imagen de reemplazo en HTML?", [
        "a) src",
        "b) alt",
        "c) image",
        "d) placeholder"
    ], "b"),
    ("¿Qué elemento se utiliza para mostrar una línea de separación temática en HTML?", [
        "a) <line>",
        "b) <separator>",
        "c) <rule>",
        "d) <hr>"
    ], "d"),
    ("¿Cuál es la etiqueta que define el encabezado de una tabla HTML?", [
        "a) <header>",
        "b) <th>",
        "c) <top>",
        "d) <head>"
    ], "b"),
    ("¿Qué atributo se usa para establecer el ancho de una celda en una tabla HTML?", [
        "a) width",
        "b) size",
        "c) cell-width",
        "d) colspan"
    ], "a"),
    ("¿Cuál es la etiqueta utilizada para definir una lista desordenada en HTML?", [
        "a) <ul>",
        "b) <ol>",
        "c) <li>",
        "d) <list>"
    ], "a"),
    ("¿Qué atributo se utiliza para definir el idioma principal de un documento HTML?", [
        "a) <language>",
        "b) <lang>",
        "c) <mainLang>",
        "d) <htmlLang>"
    ], "b"),
    ("¿Qué elemento se utiliza para definir un comentario en HTML?", [
        "a) <comment>",
        "b) #",
        "c) <!-- -->",
        "d) <c>"
    ], "c"),
    ("¿Cuál es el atributo que se usa para abrir un enlace en una nueva pestaña en HTML?", [
        "a) target='blank'",
        "b) target='new'",
        "c) target='newwindow'",
        "d) target='out'"
    ], "a"),
    ("¿Cuál es el atributo que se usa para indicar la dirección de destino de un enlace en HTML?", [
        "a) src",
        "b) link",
        "c) destination",
        "d) href"
    ], "d"),
    ("¿Qué elemento se utiliza para mostrar texto en negrita sin significado semántico en HTML?", [
        "a) <bold>",
        "b) <strong>",
        "c) <b>",
        "d) <em>"
    ], "c"),
     ("¿Cuál es la etiqueta que engloba al resto de etiquetas HTML?", [
        "a) <html>",
        "b) <head>",
        "c) <body>",
        "d) <DOCTYPE html>"
    ], "a"),

    ("¿Qué etiqueta se utiliza para crear una lista ordenada en HTML?", [
        "a) <ul>",
        "b) <li>",
        "c) <ol>",
        "d) <dl>"
    ], "c"),

    ("¿Qué se recomienda para agilizar la creación de páginas web?", [
        "a) Usar únicamente la etiqueta <body>",
        "b) Crear una plantilla base con la estructura principal",
        "c) Incluir muchas imágenes desde el principio",
        "d) Ignorar las etiquetas HTML"
    ], "b"),

    ("¿Por qué es importante cambiar la etiqueta <html> para incluir un atributo lang en una página HTML?", [
        "a) Para mejorar la estructura de la página",
        "b) Para definir el idioma de la página",
        "c) Para cambiar el fondo de la página",
        "d) Para añadir imágenes"
    ], "b"),

    ("¿Qué se necesita para que un enlace en HTML tenga utilidad?", [
        "a) Agregar muchos atributos",
        "b) Incluir elementos <div>",
        "c) Estipular el atributo href",
        "d) No es posible crear enlaces útiles en HTML"
    ], "c"),

    ("¿Cuál es el propósito de los atributos en las etiquetas HTML?", [
        "a) Cambiar el idioma de la página",
        "b) Dar estilo a la página",
        "c) Agregar información adicional",
        "d) Ocultar el contenido de la página"
    ], "c"),

    ("¿Qué elemento se utiliza para agrupar elementos en un formulario HTML?", [
        "a) <fieldset>",
        "b) <group>",
        "c) <formgroup>",
        "d) <container>"
    ], "a"),

    ("¿Cuál es la etiqueta para crear un enlace de correo electrónico en HTML?", [
        "a) <mail>",
        "b) <email>",
        "c) <a>",
        "d) <mailto>"
    ], "c"),
    
    ("¿En HTML, cuál es la diferencia entre elementos de tipo 'Block' e 'Inline'?", [
        "a) Los elementos 'Block' siempre se muestran en una nueva línea, mientras que los elementos 'Inline' se muestran en la misma línea que el contenido circundante.",
        "b) Los elementos 'Block' siempre están en negrita, mientras que los elementos 'Inline' están en cursiva.",
        "c) Los elementos 'Block' solo se pueden usar en formularios, mientras que los elementos 'Inline' se utilizan para crear listas.",
        "d) No hay diferencia entre los elementos 'Block' e 'Inline' en HTML."
    ], "a"),
    ("En HTML, ¿qué representa el número que sigue a la etiqueta 'h' en las cabeceras?", [
    "a) El tamaño de la fuente del texto en la cabecera.",
    "b) El color del fondo de la cabecera.",
    "c) El nivel de la cabecera, donde 1 es el nivel más alto y 6 el nivel más bajo.",
    "d) El espacio entre el texto de la cabecera y el borde."
    ], "c"),
    ("En HTML, ¿cómo se define un párrafo y qué representa?", 
    ["a) Se define con la etiqueta <paragraph> y representa un bloque de texto con sangría.",
    "b) Se define con la etiqueta <p> y representa un bloque de texto tras el que deja un pequeño espacio en blanco hasta el siguiente.",
    "c) Se define con la etiqueta <line> y representa un salto de línea.",
    "d) Se define con la etiqueta <block> y representa un bloque de texto terminado por un punto y aparte."
    ], "b"),
    ("En HTML, ¿cuál es el propósito principal del elemento <a>?", [
    "a) Crear un nuevo párrafo en el documento.",
    "b) Mostrar una imagen en la página web.",
    "c) Enlazar un archivo con otro para permitir la navegación entre páginas o dentro de la misma página.",
    "d) Definir un encabezado de nivel 1 en el documento."
    ], "c"),
    ("En HTML, ¿cómo se definen las rutas absolutas para enlazar recursos como archivos o imágenes?", [
    "a) Se utilizan rutas relativas indicando ./ seguido del nombre del archivo o imagen.",
    "b) Las rutas absolutas siempre comienzan con un punto (.).",
    "c) Las rutas absolutas se estipulan desde la base del sistema de archivos o servidor.",
    "d) Las rutas absolutas no son compatibles en HTML."
    ], "c"),
    ("En HTML, ¿cómo se diferencia un enlace externo de un enlace interno con ancla?", [
    "a) Los enlaces externos tienen una extensión de archivo diferente a los enlaces internos.",
    "b) Los enlaces externos siempre comienzan con un punto (.).",
    "c) Los enlaces externos apuntan a otras páginas externas, mientras que los enlaces internos con ancla se refieren a segmentos de la página actual.",
    "d) Los enlaces externos tienen un atributo href, mientras que los enlaces internos con ancla no lo requieren."
    ], "c"),
    ("En HTML, ¿qué tipo de enlace se utiliza para establecer una sección en la que se pueda enlazar sin tener un atributo href?", [
    "a) Enlace interno",
    "b) Enlace con ancla",
    "c) Enlace externo",
    "d) Enlace relativo"
    ], "b"),
    ("En una lista ordenada de HTML, ¿qué hace el atributo 'reversed'?", [
    "a) Invierte el orden de la lista.",
    "b) Cuenta el número de elementos en sentido contrario.",
    "c) Reorganiza los elementos en orden alfabético.",
    "d) No tiene ningún efecto en la lista ordenada."
    ], "b"),
    ("¿Cuál de los siguientes elementos se utiliza para definir una tabla en HTML?", [
    "a) <table>",
    "b) <tr>",
    "c) <td>",
    "d) <ul>"
    ], "a"),
    ("¿Qué elemento se utiliza en HTML como un contenedor para la división de la página en secciones y se usa para aplicar estilos a esas secciones?", [
    "a) <block>",
    "b) <container>",
    "c) <section>",
    "d) <div>"
    ], "d"),
    ("¿Cuál es el propósito principal del elemento <span> en HTML?", [
    "a) Establecer títulos para secciones de la página.",
    "b) Crear divisiones de página para aplicar estilos.",
    "c) Dar formato a fragmentos de texto sin cambiar el contenido.",
    "d) Agregar imágenes a la página web."
    ], "c"),
        ("¿Cuál es el propósito principal de las etiquetas semánticas en HTML?", [
        "a) Añadir funcionalidades adicionales a una página web.",
        "b) Cambiar la presentación de una página.",
        "c) Facilitar la lectura del código y la división de la página en secciones lógicas.",
        "d) Mejorar la velocidad de carga de la página."
    ], "c"),
    ("¿Por qué son importantes las etiquetas semánticas en HTML?", [
        "a) Para añadir efectos visuales a la página.",
        "b) Para dificultar la lectura del código.",
        "c) Para favorecer el posicionamiento en los motores de búsqueda y mejorar la accesibilidad.",
        "d) Para reducir el tiempo de desarrollo de una página."
    ], "c"),
    ("¿Qué promueve el HTML semántico además de facilitar la lectura del código?", [
        "a) El uso de más etiquetas de estilo en HTML.",
        "b) El abandono de etiquetas que aplican estilos y el uso de CSS para ese propósito.",
        "c) El uso de etiquetas genéricas como <div> en lugar de etiquetas semánticas.",
        "d) La creación de páginas web con elementos visuales más complejos."
    ], "b"),
    ("¿Cuál es la función principal de la etiqueta <header> en HTML?", [
        "a) Representa la sección de cabecera de una página, que generalmente contiene elementos como el banner de la página.",
        "b) Es un elemento utilizado para crear encabezados con tamaños variados.",
        "c) Define una sección grande de la página que engloba el contenido principal.",
        "d) Representa una sección lateral o un panel de información adicional."
    ], "a"),
    ("¿Cuál es el propósito principal de la etiqueta <nav> en HTML?", [
        "a) Representa la sección de cabecera de una página, que generalmente contiene elementos como el banner de la página.",
        "b) Define una sección grande de la página que engloba el contenido principal.",
        "c) Representa el menú de la página, independientemente de su posición.",
        "d) Define un artículo dentro de la página, como un segmento de información."
    ], "c"),
    ("¿Cuál es el papel de la etiqueta <section> en HTML?", [
        "a) Define una sección lateral o un panel de información adicional.",
        "b) Representa una sección de cabecera que generalmente contiene elementos como el banner de la página.",
        "c) Agrupa una sección grande de la página, como un apartado de texto.",
        "d) Define un artículo dentro de la página, como una noticia."
    ], "c"),
    ("¿Cuál es la función principal de la etiqueta <article> en HTML?", [
        "a) Define una sección lateral o un panel de información adicional.",
        "b) Representa la sección de cabecera de una página, que generalmente contiene elementos como el banner de la página.",
        "c) Agrupa un artículo dentro de la página, como un segmento de información independiente.",
        "d) Define una sección grande de la página, como un apartado de texto."
    ], "c"),
    ("¿Qué representa principalmente la etiqueta <aside> en HTML?", [
        "a) Define una sección lateral o un panel de información adicional.",
        "b) Es la sección de cabecera de una página que generalmente contiene elementos como el banner de la página.",
        "c) Agrupa una sección grande de la página, como un apartado de texto.",
        "d) Define un artículo dentro de la página, como una noticia."
    ], "a"),
    ("¿Cuál es la función principal de la etiqueta <footer> en HTML?", [
        "a) Define una sección lateral o un panel de información adicional.",
        "b) Representa una sección de cabecera que generalmente contiene elementos como el banner de la página.",
        "c) Agrupa una sección grande de la página, como un apartado de texto.",
        "d) Representa el pie de la página, que suele contener datos de la página y enlaces de interés."
    ], "d"),
    ("¿Cuál es el propósito principal del elemento <form> en HTML?", [
        "a) Representar la sección de cabecera de una página.",
        "b) Definir una estructura de tabla.",
        "c) Contener los campos del formulario, botones y la información a enviar al servidor.",
        "d) Establecer el estilo y diseño de la página web."
    ], "c"),

    ("¿Cuál es el propósito de los atributos 'action' y 'method' en un elemento <form>?", [
        "a) 'action' define el estilo de la página y 'method' la estructura de la tabla.",
        "b) 'action' determina la ubicación del banner de la página, 'method' establece el tipo de menú.",
        "c) 'action' especifica la página que gestionará el formulario, y 'method' define la forma en que se envían los datos.",
        "d) 'action' estipula el título de la página y 'method' el número de secciones."
    ], "c"),

    ("¿Qué atributo modificador permite bloquear un campo de formulario, impidiendo que el usuario interactúe con él?", [
        "a) 'value'",
        "b) 'placeholder'",
        "c) 'required'",
        "d) 'disabled'"
    ], "d"),

    ("¿Cuál de los siguientes tipos de campo se utiliza para introducir contraseñas?", [
        "a) Text",
        "b) Radio",
        "c) Password",
        "d) Submit"
    ], "c"),

    ("En un campo de tipo 'radio', ¿qué atributo se utiliza para especificar el elemento seleccionado por defecto?", [
        "a) 'checked'",
        "b) 'value'",
        "c) 'required'",
        "d) 'placeholder'"
    ], "a"),

    ("¿Cuál es el propósito del elemento <label> en un formulario HTML?", [
        "a) Definir el tipo de entrada para un campo del formulario.",
        "b) Establecer un nombre único para el formulario.",
        "c) Asociar una descripción al campo del formulario y activar el campo al hacer clic en la etiqueta.",
        "d) Ocultar el campo de entrada al usuario."
    ], "c"),

    ("¿Qué tipo de campo se utiliza para obtener textos largos de varias líneas por parte del usuario?", [
        "a) Number",
        "b) Checkbox",
        "c) Range",
        "d) Textarea"
    ], "d"),

    ("¿Cuál de los siguientes tipos de campo se utiliza para introducir una fecha con un calendario emergente para facilitar la selección?", [
        "a) Date",
        "b) Email",
        "c) Color",
        "d) Text"
    ], "a"),

    ("¿Qué atributo se utiliza para establecer el valor mínimo y máximo permitidos en un campo de tipo 'number'?", [
        "a) 'value'",
        "b) 'placeholder'",
        "c) 'min' y 'max'",
        "d) 'required'"
    ], "c"),

    ("En un campo de tipo 'select', ¿qué atributo se utiliza para permitir al usuario seleccionar varias opciones a la vez?", [
        "a) 'checked'",
        "b) 'multiple'",
        "c) 'required'",
        "d) 'selected'"
    ], "b"),

    ("¿Cuál es la función principal del elemento <fieldset> en un formulario?", [
        "a) Establecer el nombre de un campo.",
        "b) Crear un botón sin funcionalidad.",
        "c) Agrupar un conjunto de elementos del formulario con una caja.",
        "d) Representar una sección lateral o un panel de información adicional."
    ], "c"),

    ("¿Cuál es la función principal del elemento <legend> dentro de un <fieldset> en un formulario?", [
        "a) Definir el estilo y diseño de una página web.",
        "b) Establecer el valor mínimo y máximo en un campo de tipo 'number'.",
        "c) Especificar el nombre del bloque formado por el conjunto de elementos.",
        "d) Crear un botón de envío del formulario."
    ], "c"),
    ("¿Cuál es el propósito del elemento <datalist> en un formulario HTML?", [
        "a) Proporcionar una lista de opciones en un campo de búsqueda.",
        "b) Establecer un campo de contraseña.",
        "c) Crear una casilla de verificación para el formulario.",
        "d) Definir el rango de números permitidos en un campo 'number'."
    ], "a"),

    ("En un campo de tipo 'range', ¿cuáles son los atributos que estipulan el valor mínimo y máximo permitidos?", [
        "a) 'min' y 'max'",
        "b) 'value' y 'required'",
        "c) 'placeholder' y 'disabled'",
        "d) 'selected' y 'multiple'"
    ], "a"),

    ("¿Cuál de los siguientes tipos de campo se utiliza para introducir una URL y asegurarse de que se haya ingresado una URL válida?", [
        "a) Text",
        "b) Email",
        "c) Url",
        "d) Tel"
    ], "c"),

    ("¿Para qué se utiliza el atributo 'multiple' en un campo de tipo 'file' en un formulario HTML?", [
        "a) Para permitir múltiples envíos de formularios simultáneos.",
        "b) Para especificar múltiples valores por defecto en el campo.",
        "c) Para adjuntar varios archivos en un solo campo de entrada.",
        "d) No tiene ningún efecto en un campo de tipo 'file'."
    ], "c"),

    ("¿Cuál de los siguientes elementos se utiliza para crear un botón sin funcionalidad por sí mismo en un formulario HTML?", [
        "a) <button>",
        "b) <label>",
        "c) <fieldset>",
        "d) <legend>"
    ], "a"),

    ("¿Cuál es el propósito de la etiqueta <label> en un formulario HTML?", [
        "a) Definir el nombre del formulario.",
        "b) Establecer el valor por defecto de un campo.",
        "c) Asociar una etiqueta descriptiva a un campo y activar el campo al hacer clic en la etiqueta.",
        "d) Definir el tamaño del área de texto en un campo <textarea>."
    ], "c"),

    ("En un campo de tipo 'color', ¿qué atributo se utiliza para especificar el color que aparece por defecto en el recuadro?", [
        "a) 'value'",
        "b) 'min'",
        "c) 'placeholder'",
        "d) 'required'"
    ], "a"),

    ("¿Qué tipo de campo se utiliza para introducir números de teléfono?", [
        "a) Text",
        "b) Tel",
        "c) Number",
        "d) Email"
    ], "b"),

    ("En un campo de tipo 'select', ¿qué atributo se utiliza para estipular el valor o valores seleccionados por defecto?", [
        "a) 'checked'",
        "b) 'value'",
        "c) 'required'",
        "d) 'selected'"
    ], "d"),

    ("¿Cuál es la función principal del elemento <textarea> en un formulario HTML?", [
        "a) Definir el estilo de la página web.",
        "b) Establecer un campo de búsqueda.",
        "c) Obtener textos largos de varias líneas del usuario.",
        "d) Crear un desplegable de opciones."
    ], "c"),

    ("¿Cuál es la función principal del elemento <button> en un formulario HTML?", [
        "a) Definir el estilo de la página web.",
        "b) Crea un botón sin funcionalidad propia, es decir, que no hace nada",
        "c) Crear un campo de contraseña.",
        "d) Añadir una lista de opciones a un campo de búsqueda."
    ], "b"),
    ("¿Cuál es el propósito del atributo 'required' en un campo de un formulario HTML?", [
        "a) Hace que el campo sea invisible para el usuario.",
        "b) Bloquea la interacción del usuario con el campo.",
        "c) Impide que el formulario se envíe a menos que el campo esté rellenado.",
        "d) Define un valor por defecto en el campo."
    ], "c"),

    ("¿Qué atributo se utiliza en un campo de tipo 'number' para estipular el paso, es decir, el valor que aumenta o disminuye cada vez que el usuario interactúa con el campo?", [
        "a) 'min'",
        "b) 'max'",
        "c) 'step'",
        "d) 'value'"
    ], "c"),

    ("¿Cuál es la función principal del elemento <fieldset> en un formulario HTML?", [
        "a) Crear un botón sin funcionalidad.",
        "b) Agrupar varios elementos en un bloque.",
        "c) Establecer un nombre al formulario.",
        "d) Definir el valor por defecto de un campo."
    ], "b"),

    ("¿Para qué se utiliza el atributo 'multiple' en un campo de tipo 'select' en un formulario HTML?", [
        "a) Para permitir la selección de varias opciones a la vez.",
        "b) Para especificar múltiples valores por defecto.",
        "c) Para ocultar el campo al usuario.",
        "d) No tiene ningún efecto en un campo de tipo 'select'."
    ], "a"),

    ("¿Cuál de los siguientes elementos se utiliza para definir el valor por defecto en un campo de formulario HTML?", [
        "a) <label>",
        "b) <fieldset>",
        "c) <legend>",
        "d) <value>"
    ], "d"),

    ("¿Cuál es el tipo de campo utilizado para introducir una fecha en formato dd/mm/aaaa con la posibilidad de seleccionarla a través de un calendario?", [
        "a) Text",
        "b) Password",
        "c) Date",
        "d) Number"
    ], "c"),

    ("¿Cuál de los siguientes elementos se utiliza para crear un campo de búsqueda en un formulario HTML?", [
        "a) <form>",
        "b) <input>",
        "c) <textarea>",
        "d) <fieldset>"
    ], "b"),

    ("¿Qué atributo se utiliza en un campo de tipo 'date' para especificar el valor por defecto en formato internacional (aaaa-mm-dd)?", [
        "a) 'value'",
        "b) 'min'",
        "c) 'step'",
        "d) 'selected'"
    ], "a"),

    ("¿Cuál es el propósito principal del atributo 'placeholder' en un campo de formulario HTML?", [
        "a) Ocultar el campo al usuario.",
        "b) Establecer el valor por defecto del campo.",
        "c) Proporcionar un texto descriptivo o ilustrativo cuando el campo está vacío.",
        "d) Bloquear la interacción del usuario con el campo."
    ], "c"),

    ("¿Qué tipo de campo se utiliza para introducir una dirección de correo en un formulario HTML?", [
        "a) Text",
        "b) Email",
        "c) Url",
        "d) Tel"
    ], "b"),
    ("¿Cuál es el atributo utilizado en la etiqueta <form> para especificar la URL a la que se enviarán los datos del formulario?", [
        "a) 'method'",
        "b) 'action'",
        "c) 'name'",
        "d) 'id'"
    ], "b"),

    ("¿Cuál es el propósito principal del atributo 'method' en la etiqueta <form> en HTML?", [
        "a) Establecer el título del formulario.",
        "b) Especificar la página que gestionará el formulario.",
        "c) Definir el estilo del formulario.",
        "d) Determinar la forma en que se envían los datos del formulario."
    ], "d"),

    ("¿Qué tipo de campo se utiliza para recoger texto corto de cualquier tipo, como un nombre o una frase?", [
        "a) Password",
        "b) Radio",
        "c) Text",
        "d) File"
    ], "c"),

    ("¿Cuál es el atributo utilizado para estipular un valor por defecto en un campo de formulario HTML?", [
        "a) 'min'",
        "b) 'value'",
        "c) 'step'",
        "d) 'placeholder'"
    ], "b"),

    ("¿Qué tipo de campo se utiliza para introducir una contraseña en un formulario HTML?", [
        "a) Text",
        "b) Password",
        "c) Checkbox",
        "d) Keyword"
    ], "b"),

    ("¿Qué tipo de campo se utiliza para permitir al usuario seleccionar una y solo una de entre varias opciones?", [
        "a) Radio",
        "b) Checkbox",
        "c) Submit",
        "d) Button"
    ], "a"),

    ("¿Cuál es la función principal del tipo de campo 'submit' en un formulario HTML?", [
        "a) Bloquear la interacción del usuario con el campo.",
        "b) Recoger texto corto de cualquier tipo.",
        "c) Representar el botón de envío del formulario.",
        "d) Crear un botón sin funcionalidad."
    ], "c"),

    ("¿Qué atributo se utiliza en un campo de tipo 'checkbox' para estipular que está seleccionado por defecto?", [
        "a) 'value'",
        "b) 'checked'",
        "c) 'name'",
        "d) 'placeholder'"
    ], "b"),

    ("¿Cuál de los siguientes elementos se utiliza para introducir un número dentro de un rango con valores mínimo y máximo permitidos?", [
        "a) <button>",
        "b) <input>",
        "c) <select>",
        "d) <textarea>"
    ], "b")

]




# Mezclar las preguntas en orden aleatorio
random.shuffle(preguntas)

# Función para realizar el test
def realizar_test():
    puntaje = 0
    for i, (pregunta, opciones, respuesta) in enumerate(preguntas, 1):
        print(f"\nPregunta {i}: {pregunta}")
        random.shuffle(opciones)
        for opcion in opciones:
            print(opcion)
        respuesta_usuario = input("\nTu respuesta: ").strip().lower()
        if respuesta_usuario == respuesta:
            print("-------------------------")
            print("¡Respuesta correcta! ✔✔✔✔✔✔✔✔✔")
            print("-------------------------\n")
            puntaje += 1
        else:
            print("-------------------------")
            print(f"✖✖✖✖✖✖✖ Respuesta incorrecta. La opción correcta es: {respuesta}\n")
            print("-------------------------\n")
    
    print(f"Has completado el test, {nombre_usuario}. Puntaje final: {puntaje}/{len(preguntas)}")

# Solicitar el nombre del usuario
nombre_usuario = input("Bienvenido al test HTML. Por favor, introduce tu nombre: ")

# Solicitar el número de preguntas
num_preguntas = int(input("¿Cuántas preguntas deseas en el test? "))
while num_preguntas > len(preguntas):
    print(f"Lo siento, solo hay {len(preguntas)} preguntas disponibles.")
    num_preguntas = int(input("Por favor, elige un número igual o menor: "))

# Mezclar las preguntas en orden aleatorio
random.shuffle(preguntas)
preguntas = preguntas[:num_preguntas]

# Ejecutar el test
print(f"Muy bien, {nombre_usuario}! Comencemos con tu test de HTML con {num_preguntas} preguntas.")
realizar_test()