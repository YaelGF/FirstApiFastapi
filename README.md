# FirstApiFastapi

The first api rest with the framework fastapi and uvicorn

# How to Install


``` shell
git clone https://github.com/YaelGF/FirstApiFastapi.git
```

``` shell
cd docker
docker built -t fastapi:v1 .
```

``` shell
cd ..
docker run -it -v $(pwd)/PaginaFastapi:/PaginaFastApi -p8080:8080 --name fastapi -h python fastapi:v1
```

``` shell
docker start -i fastapi
cd PaginaFastApi
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

# Run the project

## Endpoints
![endpoints](/assets/endpoints.png)

## Clientes
![clientes](/assets/Pruebas.png)
![Result](/assets/resultClientes.png)

## Cliente
![cliente](/assets/cliente.png)
![result](/assets/resultCliente.png)


# License
[Apache License 2.0](https://github.com/YaelGF/FirstApiFastapi/blob/main/LICENSE)
