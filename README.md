
# Kolibri Proxy SSL plugin

## What is this?

Kolibri is a Learning Management System / Learning App designed to run on low-power devices, targeting the needs of learners and teachers in contexts with limited infrastructure. See [learningequality.org/kolibri](https://learningequality.org/kolibri/) for more info.

The `X-Forwarded-Proto` HTTP header can be set by upstream proxies that are doing SSL/TLS encryption and decryption.  By setting this header the proxy can signal to the Django app that links should be built with the https protocol.

This plugin will tell Kolibri to trust the upstream proxy to set the `X-Forwarded-Proto` header.  Please, do not use this module if you do not trust the upstream proxy to set this header for you.

Please see the [SECURE_PROXY_SSL_HEADER](https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-SECURE_PROXY_SSL_HEADER) Django settings reference for more information.

## How can I install this plugin?

1. Inside your Kolibri virtual environment: `pip install kolibri-proxy-ssl-plugin`

2. Activate the plugin: `kolibri plugin enable kolibri_proxy_ssl_plugin`

3. Restart Kolibri


## Plugin configuration

There is nothing to configure, this plugin simply sets the following Django setting:

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
