create_user_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'mobile': {'type': 'string', "pattern": "^[1-9]{1}[0-9]{9}$"},
        'email': {'type': 'string', "pattern": "[^@]+@[^@]+\.[^@]"},
        'password': {'type': 'string'}
    },
    'required': ['name', 'mobile', 'email', 'password']
}

edit_user_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'mobile': {'type': 'string', "pattern": "^[1-9]{1}[0-9]{9}$"},
        'password': {'type': 'string'}
    }
}
