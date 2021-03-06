from cern_webinfra_inventory_client.inventory import Inventory
import datetime


def test():
    instance_json = {
        "name": "ergkoeprkg",
        "full_domain": "rokgeropkg",
        "owner": "erokgpoerg",
        "administrators": "erogkoerpokg",
        "category": "erpokgreokg",
        "analytics": "reopkgporekg",
        "aliases": "orekgpoerkg",
        "type": "erkgpoerkgpoer",
        "creation_date": datetime.datetime.now(),
        "content_modification_date": datetime.date(2001, 7, 7),
        "expiration_date": datetime.date(2001, 7, 7),
        "description": "eriufjhreiufh",
        "endpoint": "eferfre",
        "status": "qdqwd",
        "tn_enabled": True,
    }

    iis_json = {
        "path": "",
        "site_type": "personal",
        "name": "ergkoeprkg",
        "full_domain": "rokgeropkg",
        "owner": "erokgpoerg",
        "administrators": "erogkoerpokg",
        "category": "erpokgreokg",
        "analytics": "reopkgporekg",
        "aliases": "orekgpoerkg",
        "type": "erkgpoerkgpoer",
        "creation_date": datetime.date(2001, 7, 7),
        "content_modification_date": datetime.date(2001, 7, 7),
        "expiration_date": datetime.date(2001, 7, 7),
        "description": "eriufjhreiufh",
        "endpoint": "eferfre",
        "status": "qdqwd",
        "tn_enabled": True,
    }

    print(
        Inventory().add_instance('iis', instance_json)
    )
test()