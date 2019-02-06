import os
from multi_tedency import settings
from tenants.models import Tenant
from multi_tedency.settings import BASE_DIR
def write_file(file_to_store_settings, newDbString):
  fh = open(file_to_store_settings, "w")
  try:
      return fh.write(newDbString)
  finally:
      fh.close()


def save_db_settings_to_file(db_settings):
    path_to_store_settings = os.path.join(BASE_DIR, 'multi_tedency/database_settings')
    newDbString = """
from multi_tedency.settings import DATABASES
DATABASES['%(id)s'] = {
'ENGINE': '%(ENGINE)s', 
'NAME': '%(NAME)s',                      
'USER': 'root',                      
'PASSWORD': 'ranosys',                  
'HOST': '127.0.0.1',                      
'PORT': '3306',                      
}
    """ % db_settings
    file_to_store_settings = os.path.join(path_to_store_settings, db_settings['id'] + ".py")
    write_file(file_to_store_settings, newDbString)
    return write_file(file_to_store_settings, newDbString)  # psuedocode for compactness


def db_create(db_name):
    database_id = db_name
    newDatabase = {}
    newDatabase["id"] = database_id
    newDatabase['ENGINE'] = 'django.db.backends.mysql'
    newDatabase['NAME'] = '%s' % database_id
    newDatabase['USER'] = ''
    newDatabase['PASSWORD'] = ''
    newDatabase['HOST'] = ''
    newDatabase['PORT'] = ''
    settings.DATABASES[database_id] = newDatabase

    return save_db_settings_to_file(newDatabase)  # this is for step 2)


# def create_migrate_db():
#     create_database_path = os.path.join(BASE_DIR, 'create_database.sh')
#     queryset =Tenant.objects.all()
#     db_name = queryset[0].db_name
#     print(db_name)
#     db_create(db_name)
#     db_create_migrate = os.system('echo ranosys|sudo -S bash {0} {1} {2} {3}'.format(create_database_path, db_name, 'root', 'ranosys'))
#     return db_create_migrate