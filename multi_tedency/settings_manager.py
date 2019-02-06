from multi_tedency.settings import DATABASES,BASE_DIR
import os

# current_dir_path = os.getcwd() + '/' + 'multi_tedency'
path_to_store_settings = os.path.join(BASE_DIR, 'multi_tedency/database_settings')
print(path_to_store_settings)
# path_to_store_settings = current_dir_path + '/' + 'database_settings'
for fname in os.listdir(path_to_store_settings):
    full_path = os.path.join(path_to_store_settings, fname)
    f = open(full_path)
    content = f.read()
    f.close()
    exec(content) #you'd better be sure that the file doesn't contain anything malicious