import json
import logging
import platform
import sys
import time

import re
import subprocess
import greengrasssdk


# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Creating a greengrass core sdk client
client = greengrasssdk.client("iot-data")

def function_handler(event, context):
    with open('/proc/cpuinfo') as cpu:
        text = cpu.read()
        logger.info(f"grabbed: {text}")

    try:
        client.publish(
            topic="hello/world/cpu",
            queueFullPolicy="AllOrException",
            payload=json.dumps(
                {
                    "message": f"Current Raspberry Pi cpuinfo: {text}"
                }
            ),
        )
    except Exception as e:
        logger.error("Failed to publish message: " + repr(e))
    return
