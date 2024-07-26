import requests
from app.core.config import Config

def get_address_by_coordinates(lat, lng):
    """
    Get a human-readable address from latitude and longitude using Google's reverse geocoding API.
    
    :param lat: Latitude of the location
    :param lng: Longitude of the location
    :return: Address as a string or None if the request fails
    """
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={Config.GOOGLE_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            # Extract the formatted address
            address = data['results'][0]['formatted_address']
            return address
        else:
            # Handle different status codes from the API
            print(f"Error: {data['status']}")
            return None
    else:
        print(f"Error: HTTP {response.status_code}")
        return None
    
def get_coordinates_by_address(address):
    """
    Get latitude and longitude from an address using Google's geocoding API.
    
    :param address: The address to convert into coordinates
    :return: Dictionary with latitude and longitude or None if the request fails
    """
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={Config.GOOGLE_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            # Extract the latitude and longitude
            location = data['results'][0]['geometry']['location']
            return {
                'lat': location['lat'],
                'lng': location['lng']
            }
        else:
            # Handle different status codes from the API
            print(f"Error: {data['status']}")
            return None
    else:
        print(f"Error: HTTP {response.status_code}")
        return None