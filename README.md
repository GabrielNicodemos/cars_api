# CARS-API
CARS-API é uma API desenvolvida com Django REST Framework para gerenciar proprietários de carros e seus veículos em uma cidade fictícia chamada Nork-Town. A API permite criar e gerenciar proprietários e carros, com restrições de quantidade e tipos de veículos permitidos.

## Pré-requisitos

- Docker e Docker Compose instalados.
- Python 3.10 ou superior.

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/cars-api.git
cd cars-api
```

### 2. Construir a Imagem Docker
```bash
docker-compose build
```

### 3. Aplicar Migrações do Banco de Dados
```bash
docker-compose run web python manage.py migrate
```

### 4. Rodar aplicação
```bash
docker-compose up
```
### 5. Para executar os testes automatizados:
```bash
docker-compose run web python manage.py test
```

Autor: Gabriel Eduardo




