import os

from supabase import create_client, Client # type: ignore #pip install supabase

from dotenv import load_dotenv # type: ignore # pip install python-dotenv

 

load_dotenv()

 

url = os.getenv("supabase_url")

key = os.getenv("supabase_key")

sb: Client = create_client(url, key)

 

def add_emp(empid,name, dept,role,email,phone):

    payload = {"empid": empid,  "name": name, "dept": dept,"role":role,"email":email,"phone":phone}

    resp = sb.table("employees").insert(payload).execute()

    return resp.data

 

if __name__ == "__main__":
    empid=int(input("Enter id "))
    name=input("Enter name ").strip()
    dept=input("Enter dept ").strip()
    role=input("Enter role ").strip()
    email=input("Enter email ").strip()
    phone=int(input("Enter phno "))


 

    created = add_emp(empid,name, dept,role,email,phone)

    print("Inserted:", created)

 