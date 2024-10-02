from requests_html import HTMLSession
import time

__author__ = 'jacurran'


def dhcp_convert_camera(ip, username, password):
    my_session = HTMLSession()
    first_payload = {
        "version": "1.0",
        "action": "login",
        "userName": username,
        "password": password,
        "sesionTemp": ""
    }
    sessionID=str()
    r = my_session.post(f"http://{ip}/login.cs", data=first_payload)
    for line in r.text.splitlines():
        if "sessionID=" in line:
            sessionID = line.split("=")[-2][:-7]
            time.sleep(2)
            break
    second_payload = {
        "version": "1.0",
        "action":"set",
        "addressingType": "1",
        "ipVersion": "1",
        "sessionID":sessionID,
        "mtu":"1500"
    }
    my_session.get(f"http://{ip}/ipaddressing.cs", params=second_payload)


dhcp_convert_camera(ip="XXXXXXX", username="XXXXX", password="XXXXXXX")
dhcp_convert_camera(ip="XXXXXXX", username="XXXXX", password="XXXXXXX")

#############################################################################

def dhcp_convert_8020_camera(ip, username, password):
    session = HTMLSession()
    creds = {
        'username':username,
        'password':password
    }
    session.post(f"http://{ip}/login.html",data=creds)
    payload = {
        "network_type":"lan",
        "network_resetip":"1",
        "upnppresentation_enable":"0",
        "upnpportforwarding_enable":"0",
        "network_ipv6_enable":"0",
        "network_ipv6_allowoptional":"0",
        "network_ipv6_addonipaddress":"",
        "network_ipv6_addonprefixlen":"64",
        "network_ipv6_addonrouter":"",
        "network_ipv6_addondns":"",
        "network_restart":"1",
    }
    session.post(f"http://{ip}/cgi-bin/admin/setparam.cgi",data=payload)


dhcp_convert_8020_camera(ip="XXXXXXXXX", username="XXXX", password="XXXXX")

#############################################################################

