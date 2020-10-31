# OpenAPI Dev Portal (Kubernetes)

Simple idea of having a web app that will show SwaggerUI for list of configured specs. Specifications could come from different places: configured using env variables, or config file, or Kubernetes Koap CRDs, or Kubernetes ConfigMaps.

## Featureus

- [x] UI to navigate though different OpenAPI and Swagger Specs
- [x] Backend service to host UI and gather configured API Specs
- [ ] Kubernetes operator to listen for Kubernetes Koap CRDs and ConfigMaps

## How to run

```sh
make build # Install dependecies and build UI
make local-run # Run server
```

```sh
open http://localhost:8080
```