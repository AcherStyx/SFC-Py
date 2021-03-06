from control_layer.config.send_config import SFC


def get_sfp_id():
    sfc_instance = SFC("ubuntu.local", "8181")
    sfp_id_list = []
    for path in sfc_instance.get_rendered_sfp()["rendered-service-paths"]["rendered-service-path"]:
        sfp_id_list.append(int(path["path-id"]))
    sfp_id_list.sort()
    return sfp_id_list[0]


# SERVER_IP = "192.168.225.1"
SERVER_IP = "127.0.0.1"
SERVER_PORT = 1234

# SFF_IP = "192.168.225.131"
SFF_IP = "127.0.0.1"
SFF_PORT = 4789
SFP_ID = get_sfp_id
