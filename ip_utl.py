#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "ketian"
"""
This code is used to 
"""

import socket
import geoip2.database
import validators

def ip_validate(ipaddress):
    if validators.ip_address.ipv4(ipaddress) is True:
        return True
    elif validators.ip_address.ipv6(ipaddress) is True:
        return True
    else:
        return False


def read_maxmind_database(path='GeoLite2-City.mmdb'):
    reader = geoip2.database.Reader(path)
    return reader

def ip_to_geo_mapping(ipAddress,reader=None):

    if not ip_validate(ipAddress):
        print ("not valid IP")
        return None

    if reader is None:
        reader = read_maxmind_database()

    try:
        response = reader.city(ipAddress)
    except geoip2.errors.AddressNotFoundError:
        #print ("No")
        return None

    iso = response.country.iso_code
    #longitude = response.location.longitude
    #latitude = response.location.latitude

    #print (response.subdivisions.most_specific.name)
    #print (iso,longitude,latitude)
    return iso


def get_ip_from_domain_name(hostname):
    """
    :param domainName:
    :return:
    """
    addr = socket.gethostbyname(hostname)
    ip_to_geo_mapping(addr)

    return addr

#########Main##########
if __name__=="__main__":
    domain = "https://www.w3schools.com/"
    hostname = "maps.google.com"
    get_ip_from_domain_name(hostname)

    ip1 = "46.173.219.164"
    ip2 = "195.161.114.173"
    ip3 = "abcd:ef::42:1"
    ip_to_geo_mapping(domain)
    ip_to_geo_mapping(ip1)
    ip_to_geo_mapping(ip2)
    ip_to_geo_mapping(ip3)