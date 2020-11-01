## Kaop API Manifest

Manifest describes set of APIs.

```yaml
apis:
  weatherbit: # Key of the API
    title: Weatherbit.io # Title will render on UI
    apiSpec: https://www.weatherbit.io/static/swagger.json # Spec URL that will be fetched by Swagger UI
  petstore:
    title: PET Store
    apiSpec: https://petstore.swagger.io/v2/swagger.json
```

### Speicification

- [JSON Specification](./specs/manifest.yaml)