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

copypasta = "Why Windy Landscape doesn't exist????? \nI fucking hate my life, all is shit and so pointless, or at least it was like that until I met Windy Landscape. I don't know how to put this, but I've developed some intense feelings for her, and it's tearing me apart because she's not real.\nI mean have you seen her? Her beautiful gameplay, her delicate decorations, her accompanying song and flow. She's too perfect that I would do anything to make her happy. It's like WOOGI1411 made her just for me (or so I like to think). Every time I see her gameplay, my heart skips a beat. It's true love, guys, and it's hitting me hard.\nSince her debut in the game I have NEVER played other levels than her, if I can't play her I'm not playing GD, ship control? Windy Landscape. Dealing with trolls at the end? Windy Landscape. I have never failed her, never cheated on her, so why god has to punish me? Just why? Why do I live? Life is bullshit, you have a lot of stuff to do and no meaningful reward for it, the only thing I wish in life is impossible.\nI've thought about ways to make her real, like writing a letter to WOOGI1411 and begging him to create a real-life Windy Landscape, but deep down, I know it's a lost cause. It's just a game, right? But I can't help but feel this crushing despair every time I log in and realize that Windy Landscape is trapped in the digital world, forever out of my reach.\nAnd before anyone of you try to say to me: 'jUsT rEacH aNYone' or tell me to go 'therapy', trust me, I tried but my friends are all stupid assholes, they make fun of me for just loving a GD level which isn't real, and therapy is just bullshit and only wants my money, they will never make Windy Landscape real.\nWhy? Why do I have to suffer like this? I hate my life, I hate everything, I hate everyone."

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
    ss = ""
    if(row[1] == "Windy Landscape"):
        ss = copypasta
    if(row[8] != '-'):
        s = row[8] + " Demon"
    dic = {
        "id" : int(row[4]),
        "name" : row[1],
        "author" : row[2],
        "creators" : [],
        "first_victor" : row[3],
        "verification" : row[7],
        "difficulty" : s,
        "cbf" : row[6],
        "percentToQualify" : 100,
        "records" : [],
        "funny" : ss
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
    if(row[8] != '-'):
        s = row[8] + " Demon"
    dic = {
        "id" : int(row[4]),
        "name" : row[1],
        "author" : row[2],
        "creators" : [],
        "verifier" : row[3],
        "first_victor" : row[7],
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

# #ill

# csv_file = open(getDir('ill.csv'), 'r')
# reader = csv.reader(csv_file)

# json_file = open(getDir('illist/_list.json'), 'w')

# arr = []

# for row in reader:
#     arr.append(con_str(row[1]))
#     dic = {
#         "id" : int(row[3]),
#         "name" : row[1],
#         "author" : row[2],
#         "verification" : row[4],
#         "difficulty" : row[5],
#         "records": []
#     }
#     json_ob = json.dumps(dic, indent=4)
#     fi = open(getDir('illist/' + con_str(row[1]) + '.json'), 'w')
#     fi.write(json_ob)
#     fi.close

# json_object = json.dumps(arr, indent=4)
# json_file.write(json_object)

# json_file.close
# csv_file.close