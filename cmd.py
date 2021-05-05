#!/usr/bin/env python3
# Using Python 3.8.6

import click
import bson
from bson.json_util import loads, dumps, DEFAULT_JSON_OPTIONS

@click.command()
@click.option( "--etob", is_flag=True )
@click.option( "--btoe", is_flag=True )
@click.option( "--file"  )
def command( etob, btoe, file ):

    if etob:
        with open( file ) as fh:
            ext_json = fh.read()
            print( loads( ext_json ) )
    elif btoe:
        with open( file, 'rb' ) as fh:
            bson_file = fh.read()
            extended_json = bson.decode_all( bson_file )
            print( extended_json )
    else:
        print( "Nothing!!" )
