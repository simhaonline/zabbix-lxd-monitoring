#!/usr/bin/python3
from pylxd import Client
import sys

container_id = sys.argv[1]
operation = sys.argv[2]

api = Client().api
response = api.get()
if operation == 'up':
    if (api.containers[container_id].state.get().json()['metadata']['status']) == 'Running':
        print (1)
    else:
        print (0)

if operation == 'cpu_usage':
    print (int((api.containers[container_id].state.get().json()['metadata']['cpu']['usage'])/(1e+9)))

if operation == 'used_memory':
    print ((api.containers[container_id].state.get().json()['metadata']['memory']['usage']))

if operation == 'used_swap':
    print ((api.containers[container_id].state.get().json()['metadata']['memory']['swap_usage']))
