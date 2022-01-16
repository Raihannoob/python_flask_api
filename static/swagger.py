template = {
    "swagger": "2.0",
    "info": {
        "title": "Hotel API",
        "description": "API for searching  hotels",
        "contact": {
            "responsibleOrganization": "",
            "responsibleDeveloper": "Raihan",
            "email": "tanvir@w3engineers.com",
        },
        "version": "1.0"
    },
    "basePath": "/resources/v1",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ],
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}