import csv
import json
import pathlib

abs_path = pathlib.Path(__file__)

abs_path = abs_path.parent

def getDir(s):
    return abs_path.joinpath(s)


def con_str(s):
    t=''
    for idx in range(len(s)):
        if s[idx] == ' ':
            t = t + "_"
        else:
            t = t + s[idx]
    return t

#platlist

csv_file = open(getDir('plat.csv'), 'r')
reader = csv.reader(csv_file)

json_file = open(getDir('platlist/_list.json'), 'w')

arr = []

for row in reader:
    arr.append(con_str(row[1]))
    s = "unrated"
    if(row[7] != '-'):
        s = row[7] + " Demon"
    dic = {
        "id" : int(row[4]),
        "name" : row[1],
        "author" : row[2],
        "creators" : [],
        "verifier" : row[3],
        "first_victor" : "-",
        "verification" : row[6],
        "difficulty" : s,
        "cbf" : row[5],
        "percentToQualify" : 100,
        "records" : []
    }
    json_ob = json.dumps(dic, indent=4)
    fi = open(getDir('platlist/' + con_str(row[1]) + '.json'), 'w')
    fi.write(json_ob)
    fi.close

json_object = json.dumps(arr, indent=4)
json_file.write(json_object)

json_file.close
csv_file.close

#completion

csv_file = open(getDir('sc.csv'), 'r')
reader = csv.reader(csv_file)

json_file = open(getDir('list/_list.json'), 'w')

arr = []

for row in reader:
    arr.append(con_str(row[1]))
    s = "unrated"
    if(row[8] != '-'):
        s = row[8] + " Demon"
    dic = {
        "id" : int(row[4]),
        "name" : row[1],
        "author" : row[2],
        "creators" : [],
        "verifier" : row[9],
        "first_victor" : row[3],
        "verification" : row[7],
        "difficulty" : s,
        "cbf" : row[6],
        "percentToQualify" : 100,
        "records" : []
    }
    json_ob = json.dumps(dic, indent=4)
    fi = open(getDir('list/' + con_str(row[1]) + '.json'), 'w')
    fi.write(json_ob)
    fi.close

json_object = json.dumps(arr, indent=4)
json_file.write(json_object)

json_file.close
csv_file.close

# challenge

csv_file = open(getDir('cl.csv'), 'r')
reader = csv.reader(csv_file)

json_file = open(getDir('cllist/_list.json'), 'w')

arr = []

for row in reader:
    arr.append(con_str(row[1]))
    s = "unrated"
    # if(row[7] != '-'):
    #     s = row[7] + " Demon"
    dic = {
        "id" : int(row[4]),
        "name" : row[1],
        "author" : row[2],
        "creators" : [],
        "verifier" : row[3],
        "first_victor" : row[5],
        "verification" : row[6],
        "difficulty" : s,
        "cbf" : "No",
        "percentToQualify" : 100,
        "records" : []
    }
    json_ob = json.dumps(dic, indent=4)
    fi = open(getDir('cllist/' + con_str(row[1]) + '.json'), 'w')
    fi.write(json_ob)
    fi.close

json_object = json.dumps(arr, indent=4)
json_file.write(json_object)

json_file.close
csv_file.close

# classic

csv_file = open(getDir('classic.csv'), 'r')
reader = csv.reader(csv_file)

json_file = open(getDir('obglist/_list.json'), 'w')

arr = []

for row in reader:
    arr.append(con_str(row[1]))
    s = "unrated"
    if(row[7] != '-'):
        s = row[7] + " Demon"
    dic = {
        "id" : int(row[4]),
        "name" : row[1],
        "author" : row[2],
        "creators" : [],
        "verifier" : row[3],
        "first_victor" : "-",
        "verification" : row[6],
        "difficulty" : s,
        "cbf" : row[5],
        "percentToQualify" : 100,
        "records" : []
    }
    json_ob = json.dumps(dic, indent=4)
    fi = open(getDir('obglist/' + con_str(row[1]) + '.json'), 'w')
    fi.write(json_ob)
    fi.close

json_object = json.dumps(arr, indent=4)
json_file.write(json_object)

json_file.close
csv_file.close