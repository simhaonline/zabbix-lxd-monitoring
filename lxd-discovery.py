#!/usr/bin/python3

from pylxd import Client
import json

client = Client()

#HCONTAINERID
containers=[]
for container in client.containers.all():
    containers.append({"{#HCONTAINERID}":container.name})

output={"data":containers}
print (json.dumps(output))