import requests
import json

error_code_dict = {
    200: "‘OK’",
    400: "‘Bad request’ is sent when the server cannot understand the request sent by the client.",
    401: "‘Unauthorized’ is sent whenever fulfilling the requests requires supplying valid credentials.",
    403: "‘Forbidden’ means that the server understood the request but will not fulfill it.",
    404: "‘Not found’ means that the server found no content matching the Request-URI.",
    422: "Server understands request, but can't process it.",
    429: "client has exceeded the rate limit",
}


def add_print_spacer():
    print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


if __name__ == "__main__":
    response_API = requests.get('https://dataset.api.hub.geosphere.at/v1/station/current/tawes-v1-10min?parameters=TL&station_ids=11035')
    if response_API.status_code in error_code_dict.keys():
        if response_API.status_code != 200:
            print('!!!!!!! Error processing request !!!!!!!!')
        add_print_spacer()
        print(f'Request status {response_API.status_code}: {error_code_dict[response_API.status_code]}')
    else:
        print('!!!!!!! Error processing request !!!!!!!!')
        print(f'unknown statust code: {response_API.status_code}')

    add_print_spacer()
    print("Received data from Host\n")

    api_data = response_API.text
    print(api_data)
