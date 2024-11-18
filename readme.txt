CUE: CLAVES PRIMARIAS Y CRUD 
DRILLING: LISTADO DE PRODUCTOS 


evaluacion 
m7_s4

Para clonar:
https://github.com/ThDelgado/app_supermercado.git


Thelma Delgado








		
pasos para instalar DEPENDENCIAS
------------------------------------------

    1-instalar entorno virtual:
        py.exe -m venv venv
    2- activar entorno virtual
        .\venv\scripts\activate
    3- restaurar DEPENDENCIAS
        pip install -r .\requirements.txt



superuser

nombre: admin
email: admin@admin.com
clave: 123456



(venv) PS C:\workspace_m7\app_db> python  manage.py startapp inventario
(venv) PS C:\workspace_m7\app_db> python manage.py makemigrations
Migrations for 'inventario':
  inventario\migrations\0001_initial.py
    - Create model Productos
(venv) PS C:\workspace_m7\app_db> python manage.py migrate       
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, inventario, sessions
Running migrations:
  Applying inventario.0001_initial... OK
(venv) PS C:\workspace_m7\app_db>



Type "help" for help.

app_db=# \l
                                                          List of databases
             Name             |  Owner   | Encoding |          Collate           |           Ctype            |   Access privileges
------------------------------+----------+----------+----------------------------+----------------------------+-----------------------
 BoutiqueW                    | postgres | UTF8     | English_United States.1252 | English_United States.1252 |
 BoutiqueWii_d                | postgres | UTF8     | English_United States.1252 | English_United States.1252 |
 api2                         | postgres | UTF8     | English_United States.1252 | English_United States.1252 |
 app_db                       | postgres | UTF8     | English_United States.1252 | English_United States.1252 |