def batscore(d):
    name=d.get("name")
    role=d.get("role")
    runs=d.get("runs")
    four=d.get("4")
    six=d.get("6")
    balls=d.get("balls")
    field=d.get("field")

    batscore=int(runs/2)
    if batscore>=50:batscore+=5
    if batscore>=100:batscore+=10

    if runs>0:
        sr=runs*100/balls
        if 80<=sr<100: batscore+=2
        if sr>=100: batscore+=4

    batscore=batscore+four
    batscore=batscore+2*six
    batscore=batscore+10*field

    return{"Name":name, "Role":role, "Batscore":batscore}


def bowlscore(d):
    name=d.get("name")
    role=d.get("role")
    wickets=d.get("wkts")
    runs=d.get("runs")
    balls=(d.get('overs'))
    field=d.get("field")

    bowlscore=10*wickets
    if wickets>=3: bowlscore+=5
    if wickets>=5: bowlscore+=10

    if balls>0:
        er=runs/balls
        if 3.5<er<=4.5: bowlscore+=4
        if 2<er<=3.5: bowlscore+=7
        if er<=2: bowlscore+=10
    
    bowlscore=bowlscore+10*field

    return{"Name":name, "Role":role, "Bowlscore":bowlscore}


