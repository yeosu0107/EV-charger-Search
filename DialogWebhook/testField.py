import json

returnVal = {}

returnVal["fulfillmentText"] = "SUCCESS"
tmp = {}
tmp2 = {}
tmp2["text"] = "testMsg"
tmp["text"] = tmp2
returnVal["fulfillmentMessages"] = tmp

test = json.dumps(returnVal, ensure_ascii=False, indent="\t")

t = json.loads(test)

k=123

tt = "개수 : " + str(k)

print(tt)
