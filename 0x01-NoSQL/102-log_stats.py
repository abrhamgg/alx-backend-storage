#!/usr/bin/env python3
"""log status"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    nginx = db.nginx

    print("{} logs".format(nginx.count_documents({})))
    print("Methods:")
    print("\tmethod GET: {}".format(nginx.count_documents({"method": "GET"})))
    print("\tmethod POST: {}".format(nginx.count_documents(
        {"method": "POST"})))
    print("\tmethod PUT: {}".format(nginx.count_documents(
        {"method": "PUT"})))
    print("\tmethod PATCH: {}".format(nginx.count_documents(
        {"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(nginx.count_documents(
        {"method": "DELETE"})))
    print("{} status check".format(nginx.count_documents(
        {"method": "GET"} and {"path": "/status"})))
    print("IPs:")
    doc = db.nginx.aggregate([
        {"$group": {"_id": "$ip", "num": {"$sum": 1}}},
        {"$sort": {"num": -1}},
        {"$limit": 10}
        ])
    for i in doc:
        print("\t{}: {}".format(i['_id'], i['num']))
    client.close()
