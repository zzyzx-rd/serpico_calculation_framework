import sys
sys.path.append("..")
import app.jsonTools.jsonReader as jr

def testJson():
    json_data = jr.readData("Tests/data1.json")
    #print("jsondata : " + str(json_data))
    print("0")
    return 0

testJson()