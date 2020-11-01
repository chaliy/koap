# KOAP - OpenAPI Dev Portal (Kubernetes)

![Docker](https://github.com/chaliy/koap/workflows/Docker%20image/badge.svg)![Koap UI](https://github.com/chaliy/koap/workflows/Koap%20UI/badge.svg)


Simple idea of having a web app that will show SwaggerUI for list of configured specs. API specifications could come from different places: [manifest file](./examples/manifest.yaml), or [Kubernetes ConfigMaps](./examples/configmaps/), or Kubernetes Koap CRDs.

## Featureus

- [x] UI to navigate through different OpenAPI and Swagger Specs
- [x] Backend service to host UI and gather configured API Specs
- [x] Kubernetes operator to listen for ConfigMaps with API Manifiests
- [ ] Support Kubernetes Koap CRDs
- [ ] Support Service/Deployment/POD annotations with API Specs
- [ ] Support to limit Koap to the single Kubernetes namespace

![UI](./docs/ui.png)

## How to use

### Kubernetes

1. Install KOAP to your Kuberntes cluster. KOAP will use in-cluster auth to Kubernetes API.
2. Create few ConfigMaps with API Manifests ([example](./examples/configmaps/))
3. Enjoy

### Docker

1. Run
```sh
docker run -it -p 8080:8080 \
    -v $PWD/examples/manifest.yaml:/etc/koap/manifest.yaml \
    ghcr.io/chaliy/koap:latest service --api-manifest /etc/koap/manifest.yaml
```

2. Enjoy
```sh
open http://localhost:8080
```

## Contribute

### How to run locally

Ensure you have `make`, `node`, `python`, `pipenv` on your machine.

```sh
make build # Install dependecies and build UI
make local-run # Run server
```

```sh
open http://localhost:8080
```

## API Manifests

### Manifest file

Koap accepts `--api-manifest` with path to JSON or YAML representation of [API Manifest](./examples/manifest.yaml).


### Kubernetes ConfigMap 

ConfigMaps with annotation `koap.tv/apimanifests` will be treated as set of [API Manifests](./examples/configmaps/). Each key is API Manifest.