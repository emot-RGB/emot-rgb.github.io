from urllib.request import urlopen
import json



def get_data():
    datasheet = urlopen('https://docs.google.com/spreadsheets/d/e/2PACX-1vRCcvlKkOUsCY0m7q3a7XuyOs6CeHk7KY2ld9MJXwh4nhqv5fyBR9sJ45CtnW2oTHgwSlxZYGTXAkWP/pubhtml')


    coded_data = datasheet.read()

    data = coded_data.decode("utf-8")

    d = data.split("<td")

    all_comments = list









    date = "date"
    tm = "time"
    text = "text"
    pic = "pic"


    with open('emot-rgb.github.io/saved data/page_content.json', 'r') as file:

        content = json.load(file)

        num = "0"
        
        def add_to_comment(a):
            #print(content)
            v = a.split("\\")
            c = v[0]
            d = v[1]
            #print(v)
            if "date" in a : 
                content[num][c] = d
            if "time" in a : 
                content[num][c] = d
            if "text" in a : 
                content[num][c] = d
            if "pic" in a  :
                content[num][c] = d
                

        for i in d:
            a = "\0"
            c = 0

            if "/td" in i and 'class="s0' in i:
                if "pic" in i:
                    a = i.split(" ")
                    for x in a:
                        if "href" in x:
                            a = x.split('"')
                            a = ('pic \\' + a[1])
                else:
                    a = i.split("</td>")
                    a = a[0].split(">")
                    a = a[1]
            
            if a != "\0":
                #print(a)
                if "num" in a:
                    num = a.split("\\")
                    num = num[1]
                    #print("            ",num)
                    content[num] = {}
                add_to_comment(a)
                
            

        content = json.dumps(content, indent=4)

        

    with open('emot-rgb.github.io/saved data/page_content.json', 'w') as file:
        file.write(content)
    
    return content

get_data()