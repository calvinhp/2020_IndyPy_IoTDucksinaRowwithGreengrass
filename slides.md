---
title: IoT Ducks in a Row with Greengrass
author: Calvin Hendryx-Parker, CTO, Six Feet Up
date: IndyPy 2020
---

# Fully Managed Edge Services

-   Secure Communications
-   Group Management of Cores
-   OTA Provisioning and Updates

# Lambda at Your Edge

::: notes
You install the core on your devices

You run AWS Lambdas on your devices
:::


# Offline Operation

-   AWS IoT Device Shadows


# Local Messaging

::: notes
Local only messaging even with no connection to AWS

Utilizes the greengrass SDK on the local devices

Processes rules and deliver messages to other devices or the cloud
:::

# Local Reource Access

-   Serial Ports
-   GPIO
-   Bluetooth

# Greengrass Connectors

## Access to third-party APIs

## On-premises Software

# Run ML Models

-   Local Inference

::: notes
Reduce costs on transfer to the cloud
:::


# Hardware Support

-   Raspberry Pi
-   Intel Atom
-   Nvidia Jetson NX
-   ARM v7 and v8
-   Intel amd64
-   Existing IoT Hardware

::: notes
Supports many Gateways and exisiting edge devices
:::

# Quick Start

### Setup your Raspberry Pi

Grab Temporary AWS Security Credentials

```console
$ aws sts assume-role --role-arn arn:aws:iam::123456789012:role/role-name --role-session-name "RoleSession1"
```

```console
$ export AWS_ACCESS_KEY_ID=...
$ export AWS_SECRET_ACCESS_KEY=...
$ export AWS_SESSION_TOKEN="..."
```

Bootstrap Device

```console
$ wget -q -O ./gg-device-setup-latest.sh https://d1onfpft10uf5o.cloudfront.net/greengrass-device-setup/downloads/gg-device-setup-latest.sh && chmod +x ./gg-device-setup-latest.sh && sudo -E ./gg-device-setup-latest.sh bootstrap-greengrass-interactive
```

# Hello World

``` {.stretch .python}
def greengrass_hello_world_run():
    try:
        if not my_platform:
            client.publish(
                topic="hello/world", queueFullPolicy="AllOrException", payload="Hello world! Sent from Greengrass Core."
            )
        else:
            client.publish(
                topic="hello/world",
                queueFullPolicy="AllOrException",
                payload="Hello world! Sent from " "Greengrass Core running on platform: {}".format(my_platform),
            )
    except Exception as e:
        logger.error("Failed to publish message: " + repr(e))

    # Asynchronously schedule this function to be run again in 5 seconds
    Timer(5, greengrass_hello_world_run).start()
```

# Greengrass Secrets Manager

## Works with Greengrass Connectors

::: notes
Rotate keys and distribute access to other edge resources
:::

# Greengrass Pricing

-   Free tier for 3 devices for the first year
-   Up to 10k devices \-- \$0.16/month/device
-   22% discount for annual commitment

::: notes
prices for of US East 1 and US West 1 billed only in whole months They
get you on everything else

-   transfer
-   storage
:::

# Resources

-   [Getting Started Guide](http://docs.aws.amazon.com/greengrass/latest/developerguide/gg-gs.html)
-   [FAQs](https://aws.amazon.com/greengrass/faqs/)

# Questions?

## <calvin@sixfeetup.com>

[`@calvinhp`](https://twitter.com/calvinhp)
