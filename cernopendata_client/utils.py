# -*- coding: utf-8 -*-
# This file is part of cernopendata-client.
#
# Copyright (C) 2020 CERN.
#
# cernopendata-client is free software; you can redistribute it and/or modify
# it under the terms of the GPLv3 license; see LICENSE file for more details.

"""cernopendata-client utility functions."""

import click


def parse_parameters(filter_input):
    """Return parsed filter parameters."""
    try:
        filters = " ".join(filter_input).split(",")
        return filters
    except:
        raise click.BadParameter("Wrong input format \n")
