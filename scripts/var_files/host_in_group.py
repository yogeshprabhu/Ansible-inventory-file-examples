#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


print json.dumps({
    "_meta": {
        "hostvars": {
            "old_host": {}
        }
    },
    "ghost": {
        "hosts": ["old_host"]
    }
})