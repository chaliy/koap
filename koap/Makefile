local-run:
	KOAP_API_GROUPS_JSON='\
	{"groups": [{ \
			"key": "weatherbit",  \
			"title": "Weatherbit.io",  \
			"apiSpec": "https://www.weatherbit.io/static/swagger.json" \
		},{ \
			"key": "petstore", \
			"title": "PET Store", \
			"apiSpec": "https://petstore.swagger.io/v2/swagger.json" \
		}] \
	}' \
	pipenv run python ./main.py