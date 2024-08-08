import urllib3

def lambda_handler(event, context):
    url = "http://api.ipify.org"
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    
    if response.status == 200:
        ip_address = response.data.decode('utf-8')
        print(f"Public IP Address: {ip_address}")
        return {
            'statusCode': 200,
            'body': f"Public IP Address: {ip_address}"
        }
    else:
        print(f"Failed to fetch IP address. Status code: {response.status}")
        return {
            'statusCode': response.status,
            'body': "Failed to fetch IP address."
        }
