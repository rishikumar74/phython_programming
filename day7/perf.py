import os

from supabase import create_client, Client # type: ignore #pip install supabase

from dotenv import load_dotenv # type: ignore # pip install python-dotenv

 

load_dotenv()

 

url = os.getenv("supabase_url")

key = os.getenv("supabase_key")

sb: Client = create_client(url, key)

 

def add_emp(perfid,empid, metric,score,date):

    payload = {"perid": perid,  "empid": empid, "metric": metric,"score":score,"date":date}

    resp = sb.table("performance").insert(payload).execute()

    return resp.data

 

if __name__ == "__main__":
    perid=int(input("Enter perf id "))
    empid=int(input("Enter emp id "))
    metric=input("Enter metrics ").strip()
    score=int(input("Enter score "))
    date=input("Enter id ")
    


 

    created = add_emp(perid,empid, metric,score,date)

    print("Inserted:", created)

 