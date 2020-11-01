## Kuberntes Integration

KOAP can listen to resources in Kuberntes Cluster and based on that register specs in Swagger UI.

### Tech details

- Koap uses in-cluster authentication, Koap will gather API Manifests only from resources it have at least read access
- Koap will react on `create`, `modifled` and `delete` events from K8s resource. Delete event will remove APIs from Koap

### ConfigMaps

Koap will listen to changes in ConfiMaps annotated with `koap.tv/apimanifests`.

```yaml
kind: ConfigMap
metadata:
  name: myhelsinki-koapapispecs
  annotations:
    koap.tv/apimanifests: "true"
data:
  manifest1: |- 
    apis:
      myhelsinki:
        title: MyHelsinki
        apiSpec: http://open-api.myhelsinki.fi/swagger.json
```

Each key of the ConfigMap will be treated as single API Manifest. Koap will merge all minifests by key. So for example if two manifests have `myhelsinki` API, then only one of them will win.

### Annotations on Services/Deployments/Pods

__NOTE:__ This is not implmented. Just an idea.

Koap will listen to changes to all Service/Deployments/Pods and based annotations, Koap will proxy Open API specs to Koap UI