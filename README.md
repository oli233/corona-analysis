# corona-analysis
corona-analysis is a Python library for maintain and visualise covid-19 cases data.
all data from www.worldometers.info

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependences.

```bash
pip install -r requirements.txt
```

## Usage
Deploy with docker and api container will expose the data endpoints.

An example with the endpoint '/api/corona/v1.0/all':
<img width="1251" alt="cdata" src="https://user-images.githubusercontent.com/34482354/172177595-bc47d92b-5671-4fa9-94d5-f474b9546f65.png">

## Endpoints
The API has 3 endpoints now:
```python
/
```
the root endpoint gives endpoints status in general, including health and reachability.

```python
/api/corona/v1.0/all
```
gives all data in a json format

```python
/api/corona/v1.0/date=<string:date>&id=<string:country_name>
```
gives data for a specific region

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This project is licensed under the Apache-2.0 license.
