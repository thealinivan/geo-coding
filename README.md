# geo-coding
Geo-coding and reverse geo-coding API interface using Google Maps API



## Running locally

#### 1. Prerequisites: Docker / Docker desktop (recommended) 
- Mac: https://docs.docker.com/desktop/install/mac-install/
- Windows: https://docs.docker.com/desktop/install/windows-install/
- Linux: https://docs.docker.com/desktop/install/linux-install/

#### 2. Populate the .env file: 
Ask repository owners for env variables

#### 3. Build & run docker from root directory
```
docker compose up --build
```


## Access

You may find Postman useful to test the endpoints: https://www.postman.com/downloads/

#### Authorization 
API Key Authorization required in header (exception: test endpoint)
- X-API-KEY: your-api-key

#### Endpoints

- http://localhost:5000/api (test endpoint)
- http://localhost:5000/api/geocode
- http://localhost:5000/api/reverse-geocode

#### Examples
-   eg. http://localhost:5000/api/geocode?address=Strada+Costache+Racovita+16,+Tecuci
-   eg: http://localhost:5000/api/reverse-geocode?lat=45.8463007&lng=27.4280217
