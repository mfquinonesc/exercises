import textwrap
import re
import os

##
# private functions
##

def __check_folder_path(file_path: str):

    pattern = r'^[a-zA-Z0-9/_]+$'

    if not bool(re.match(pattern, file_path)):
        print('Error -> the file path contains invalid characters')
        return False

    if file_path.startswith('/'):
        print('Error -> the file path starts with /')
        return False

    if  file_path.endswith('/'):
        print('Error -> the file path ends with /')
        return False

    folders = file_path.split('/')
    folders.pop()

    if not len(folders) > 0:
        return True

    folder_path = "/".join(folders)
    os.makedirs(folder_path, exist_ok=True)
    return True


def __create_file(file_path: str, extension: str, template: str):

    clean_template = textwrap.dedent(template).lstrip()

    with open(f"{file_path}.{extension.replace('.', '')}", 'w') as file:
        file.write(clean_template)


def __create_template(name:str, keyword:str):

    template = f"""\
    /**
    * {name} {keyword.capitalize()}    
    */
    export default {keyword} {name} {{    
    }}
    """
    return template


def __get_file_name(file_path: str):
    return file_path.split('/').pop()


def __get_path(file_path: str):
    path = file_path.split('/')
    path.pop()
    return '/'.join(path)


def __uppercase_first(text:str):
    return text[0].upper() + text[1:]

##
# public functions
##

def generate_component(file_path: str, extension: str, include_stylesheet: bool = False, use_module: bool = False, use_scss: bool = False):

    if not __check_folder_path(file_path):
        return

    name = __get_file_name(file_path)

    stylesheet_import = ''

    if include_stylesheet:
        stylesheet_import = f"import './{name}{'.module' if use_module else ''}.{'scss' if use_scss else 'css'}';"

    template = f"""
    import React from 'react';
    {stylesheet_import}

    /**
    * {name} Component
    *
    * @component
    * @param {{children}} props - Component children.
    * @returns {{JSX.Element}} The rendered {name} component.
    */
    export default function {name}({{children}}) {{
        return (
            <div>
                {{children}}
            </div>
        );  
    }}
    """
    __create_file(file_path, extension, template)


def generate_page(file_path: str, extension: str, include_stylesheet: bool = False, use_module: bool = False, use_scss: bool = False):

    if not __check_folder_path(file_path):
        return

    name = __get_file_name(file_path)

    stylesheet_import = ''

    if include_stylesheet:
        stylesheet_import = f"import './{name}{'.module' if use_module else ''}.{'scss' if use_scss else 'css'}';"

    template = f"""
    import React from 'react';
    {stylesheet_import}

    /**
    * {name} Page Component
    *
    * @component
    * @returns {{JSX.Element}} The rendered {name} page.
    */
    export default function {name}() {{
        return <h1>{name} Page</h1>;
    }}
    """
    __create_file(file_path, extension, template)


def generate_service(file_path: str, use_typescript: bool = False, include_axios: bool = False):

    if not __check_folder_path(file_path):
        return

    name = __get_file_name(file_path)

    full_name = f"{name}Service"

    axios_template = f"""
    import axios from 'axios';

    /**
    * Base URL for the API.
    * Update this to point to your backend.
    * @constant {{string}}
    */
    const API_BASE_URL = 'https://localhost:3000/.../{str.lower(name)}';
    """

    template = f"""
    { axios_template if include_axios else ''}
    /**
    * {full_name} Service
    *
    * @namespace {full_name}
    */
    const {full_name} = {{       
    }};

    export default {full_name};
    """
    path = f"{__get_path(file_path)}/{full_name}"

    __create_file(path, 'ts' if use_typescript else 'js', template)


def generate_router(file_path: str, extension: str):

    if not __check_folder_path(file_path):
        return

    name = __get_file_name(file_path)

    template = f"""
    import React from 'react';
    import {{BrowserRouter as Router, Routes, Route }} from 'react-router-dom';      

    /**
    * {name} Component
    *
    * @component
    * @returns {{JSX.Element}} The rendered route structure for the application.
    */
    export default function AppRoutes() {{
        return (
            <Router>
                <Routes>
                    {{/* Add routes here */}}
                </Routes>
            </Router>
        );
    }}
    """
    __create_file(file_path, extension, template)


def generate_store(file_path: str, extension: str):

    if not __check_folder_path(file_path):
        return

    name = __get_file_name(file_path)

    template = f"""
    import {{ configureStore }} from '@reduxjs/toolkit';
    // import reducers here

    /**
    * Redux Store Configuration
    *
    * @module {name}
    */
    export const {name} = configureStore({{
        reducer: {{
            // your reducers
        }},
    }});
    """
    __create_file(file_path, extension, template)


def generate_stylesheet(file_path: str, use_module: bool = False, use_scss: bool = False):

    if not __check_folder_path(file_path):
        return

    component_name = __get_file_name(file_path)

    file_name = f"{component_name}{'.module' if use_module else ''}"

    path = f"{__get_path(file_path)}/{file_name}"

    extension = f".{'scss' if use_scss else 'css'}"

    __create_file(path, extension,'')


def generate_hook(file_path: str, use_typescript: bool = False):

    if not __check_folder_path(file_path):
        return

    name = __uppercase_first(__get_file_name(file_path))

    full_name = f"use{name}"
    
    template = f"""  
    /**
    * {full_name}      
    */    
    function {full_name}() {{       
    }}

    export default {full_name};
    """
    path = f"{__get_path(file_path)}/{full_name}"

    __create_file(path, 'ts' if use_typescript else 'js', template)


def generate_interface(file_path: str):

    if not __check_folder_path(file_path):
        return

    name = __get_file_name(file_path)

    template = __create_template(name, 'interface')
    __create_file(file_path, 'ts', template)


def generate_class(file_path: str, use_typescript: bool = False):

    if not __check_folder_path(file_path):
        return

    name = __get_file_name(file_path)

    template = __create_template(name, 'class')
    __create_file(file_path, 'ts' if use_typescript else 'js', template)


def get_encapsulated_path(file_path:str):
    
    path = __get_path(file_path)
    name = __get_file_name(file_path)
    return '/'.join([path, name, name])


def generate_folders(file_path:str):

    folders = ["components", "features", "pages", "routes",
               "services", "store", "hooks", "context", "utils", "types"]    
    
    for f in folders:
        __check_folder_path('/'.join([file_path, f, f]))


def generate_context(file_path:str, extension:str):

    if not __check_folder_path(file_path):
        return
    
    name = __get_file_name(file_path)

    template = f"""

    """
    __create_file(file_path, extension, template)