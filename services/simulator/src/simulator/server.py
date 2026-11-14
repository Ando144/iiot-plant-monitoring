import asyncio
import logging
import random
import time

from asyncua import Server

from simulator import production

async def main():
    _logger = logging.getLogger(__name__)
    # setup our server
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/iiot/simulator/")

    # setup our own namespace
    uri = "https://github.com/Ando144/iiot-plant-monitoring"
    idx = await server.register_namespace(uri)

    # create a new object to hold our methods and variables
    machine1 = await server.nodes.objects.add_object(idx, "Machine1")
    part_count = await machine1.add_variable(idx, "PartCount", 0)
    state = await machine1.add_variable(idx, "State", "RUNNING")
    spindle_temperature = await machine1.add_variable(idx, "SpindleTemperature", 0.0)


    _logger.info("Starting server!")
    async with server:
        time_start = time.monotonic()
        while True:
            await asyncio.sleep(1)
            elapsed_time = time.monotonic() - time_start
            await state.write_value("RUNNING")
            await part_count.write_value(production.parts_produced(elapsed_time, 5.0))
            await spindle_temperature.write_value(random.uniform(44.0, 46.0))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())