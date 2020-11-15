## Kubernetes Deployment

This folder serves as an exmple of deployment. In most cases it is recommended take it modify and then apply to the target cluster.

- Uses kustomized, use `kubectl apply -k ./deploy` to provision
- Used `koap-dev` as target namespace
- Does not include Ingress. This is up to implementator


### Instructions

0. Ensure you have Kubernetes Cluster; kubectl in you path; `koap-dev` namespace
1. Apply deployment

```sh
kubectl apply -k .
```

2. Port forward Koap UI

```sh
kubectl port-forward svc/koap 8080:http
```

```sh
open http://localhost:8080
```

3. Apply few examples

```sh
kubectl apply -f ../examples/configmaps/example1.yaml
kubectl apply -f ../examples/configmaps/example2.yaml
```

### Cleanup

```sh
kubectl delete -k .
```