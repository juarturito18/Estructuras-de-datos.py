def newsapi_client( api_key, query, timeout = 30, retries = 3):
    return f"NewsAPI: {query}, con timeout {timeout}"

def guardian_client( api_key, section, from_date, timeout = 30, retries = 3):
    return f"Guardian: {section} desde {from_date}, con timeout {timeout}"

#EL args se usa pra poder recibir mas de un valor en una funcion, y este va a crear una tupla
def example_args (*args):
    print(f"Todos {args}")
    print(f"{type(args )}")

example_args("Los posibles", "parametros", "que", "puedo", "agregar")
example_args("Los posibles", "parametros")
example_args()

#con kargs se usar para poder ingresar los valores que queramos pero estos de forma de dict, y ademas de ello se tiene que nombrar los valores
def example_kargs(**kargs):
    print(f"Kargs: {kargs}")
    print(f"Kargs: {type(kargs)}")

example_kargs(key = "value", llave = "valor")

def fetch_news(api_name, *args, **kargs):
    """
    Función flexible para recibir api
    """

    base_config = {
        "timeout" : 30,
        "retries": 3
    }

    #De esta forma se traen los valores de base_config y kargs a nuestro dictionario de forma dinamica
    config = {
        **base_config
        **kargs
    }


    api_client = {
        "newapi": newsapi_client,
        "Guardianapi": guardian_client
    }

    client = api_client[api_name]
    return client(*args, **config)



