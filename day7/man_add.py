import os

from supabase import create_client, Client # type: ignore #pip install supabase

from dotenv import load_dotenv # type: ignore # pip install python-dotenv

 

load_dotenv()

 

url = os.getenv("supabase_url")

key = os.getenv("supabase_key")

sb: Client = create_client(url, key)

 

def add_emp(manid,name, dept,email):

    payload = {"manid": manid,  "name": name, "dept": dept,"email":email}

    resp = sb.table("managers").insert(payload).execute()

    return resp.data

 

if __name__ == "__main__":
    manid=int(input("Enter id "))
    name=input("Enter name ").strip()
    dept=input("Enter dept ").strip()
   
    email=input("Enter email ").strip()
   


 

    created = add_emp(manid,name, dept,email)

    print("Inserted:", created)

 