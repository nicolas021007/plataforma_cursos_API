TORTOISE_ORM = {

    "connections":{
        "default": "sqlite://db.sqlite3"
    },
    "apps":{
        "models":{
            "models": [
                "infraestructure.tortoise.models",
                "aerich.models",
            ],
            "default_connection":"default"
        }
        
    },
}