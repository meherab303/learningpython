mydict={
    "name":"meherab",
    "age":12,
    12:13,
    "roll":[6,54,3,2,1],
    "subject":{
        "chem":10,
        "math":100,
        "failed":{
            "phy":22
        }
    }
}
print(list(mydict.get("subject").get("failed").values()))
print(list(mydict.items()))
names={
"key":"values"
}
print(mydict.update(names))
print(mydict)