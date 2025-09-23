import os

from supabase import create_client, Client # type: ignore #pip install supabase

from dotenv import load_dotenv # type: ignore # pip install python-dotenv

 

load_dotenv()

 

url = os.getenv("supabase_url")

key = os.getenv("supabase_key")

sb: Client = create_client(url, key)

 

def add_emp(evalid,empid,manid,score,feedback,evaldate):

    payload = {"evalid": evalid,  "empid": empid, "score":score,"feedback":feedback,"evaldate":evaldate}

    resp = sb.table("evaluation1").insert(payload).execute()

    return resp.data

 

if __name__ == "__main__":
    evalid=int(input("Enter eval id  "))
    empid=int(input("Enter emp id  "))
    manid=int(input("Enter man id  "))
    score=int(input("Enter score  "))
    feedback=input("Enter feedback  ")
    evaldate=input("Enter evalution date  ")
    
    


 

    created = add_emp(evalid,empid,manid,score,feedback,evaldate)

    print("Inserted:", created)

 