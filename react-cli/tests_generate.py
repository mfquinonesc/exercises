from src.scaffold import *

# Testing scaffold

# Testing components

file_path = 'tests/components/Button'

generate_component(file_path, '.js', True, True, True)

generate_component(file_path, '.jsx', True)

generate_component(file_path, '.tsx')

# Testing pages

file_path = 'tests/pages/Home'

generate_page(file_path, '.js', True, True, True)

generate_page(file_path, '.jsx', True)

generate_page(file_path, '.tsx')

# Testing stores

file_path = 'tests/stores/AppStore'

generate_store(file_path, '.js')

generate_store(file_path, '.jsx')

generate_store(file_path, '.tsx')

# Testing routes 

file_path = 'tests/routers/AppRouter'

generate_router(file_path, '.js')

generate_router(file_path, '.jsx')

generate_router(file_path, '.tsx')

# Testing classes

file_path = 'tests/classes/user'

generate_class(file_path, True)

generate_class(file_path)

# Testing interfaces

file_path = 'tests/interfaces/login'

generate_interface(file_path)

# Testing services

file_path = 'tests/services/auth'

generate_service(file_path, False, True)

generate_service(file_path, True)

# Testing hooks

file_path = 'tests/hooks/width'

generate_hook(file_path)

generate_hook(file_path, True)

# Testing stylesheet

file_path = 'tests/files/Button'

generate_component(file_path,'jsx',True)
generate_stylesheet(file_path)

file_path = 'tests/files/Selector'

generate_component(file_path,'jsx',True,True)
generate_stylesheet(file_path,True)

file_path = 'tests/apps/index'

generate_stylesheet(file_path, True)
generate_stylesheet(file_path, True,True)

# Testing folders 

file_path =  'tests/modules/'

generate_folders(file_path)