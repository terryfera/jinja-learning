from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('.'))

template = ENV.get_template("interface_loop.j2")

class NetworkInterface(object):

    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink

intlist = [
    "GigabitEthernet0/1",
    "GigabitEthernet0/2",
    "GigabitEthernet0/3"
]

print(template.render(interface_list=intlist))
