<h1>Instalaciones basicas para instalar el proyecto</h1>

- Lo promero de todo debde tener instalado Python

Instalaciones basicas para instalar el proyecto

- Clonar el repositorio Link
  Con el comando: git clone [Repositorio ZIP](https://github.com/topgambajrjdeveloper/sergio/archive/refs/heads/main.zip)

Dejo una guia de Virtualenvs
 [Virtualenvs](https://python-guide-es.readthedocs.io/es/guide-es/dev/virtualenvs.html)

- Crea el entorno virtual con: python -m venv venv ,
  Esto sirve para cualquiera de los siatemas operativos:
  Inicia la palabra y ahorrate el escribir tanto con el Tabulador
- Si estas en MAC o Linux usa este comando:
  source venv/bin/activate o . venv/bin/activate
        - Si estas en Windows este otro comando: .\venv\Scripts\activate
- Desactivar el entorno virtual usar: deactivate

- Instalar las importacines del archivo requirements.txt
  Comando para instalar en windows: pip install -r requirements.txt , pero si estas en linux o MAC, debes hacerlo asi: pip3 install -r requirements.txt