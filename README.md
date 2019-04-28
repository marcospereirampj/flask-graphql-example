# Flaks GraphQL Example

API:
https://dadosabertos.camara.leg.br/swagger/api.html


Example:

http://localhost:5000/graphql

{
  deputies (perPage: 20, page: 2) {
    id
    nome
  }
}