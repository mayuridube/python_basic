import json


def json_write(coordinates, camera_id, camera_path, module_name, expiry):
    cameralist = {}
    print(coordinates[0])
    cameralist['cameraId'] = camera_id
    cameralist['camerapath'] = camera_path
    cameralist['moduleConfig'] = {
        'moduleName': module_name,
        'expiry': expiry,
        'sp-module_Config': {
            'co-ordinates': {
                'start':
                    {

                        'x1': coordinates[0],
                        'x2': coordinates[1]
                    },
                'end':
                    {
                        'x1': coordinates[2],
                        'x2': coordinates[3]
                    },
            }
        }
    }

    with open('data.json', 'w') as outfile:
        json.dump(cameralist, outfile)


def json_read():

    with open('data.json') as json_file:
        data = json.load(json_file)
        # print(data)
        module_data = data['moduleConfig']
        print(module_data)
        module_name = module_data['moduleName']
        print(module_name)


if __name__ == '__main__':
    coordinate_list = [10, 20, 14, 30]
    json_write(coordinate_list, '123', 'abc', 'fr', '02-10-19')
    # read same json file
    json_read()

