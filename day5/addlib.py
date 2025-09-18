import os

from supabase import create_client, Client # type: ignore #pip install supabase

from dotenv import load_dotenv # type: ignore # pip install python-dotenv

 

load_dotenv()

 

url = os.getenv("supabase_url")

key = os.getenv("supabase_key")

sb: Client = create_client(url, key)

 

def add_book(bname,bauthor, bprice):

    payload = {"bname": bname,  "bauthor": bauthor, "bprice": bprice}

    resp = sb.table("books").insert(payload).execute()

    return resp.data

 

if __name__ == "__main__":

    bname = input("Enter book name: ").strip()

    bauthor = input("Enter author name: ").strip()

    bprice = float(input("Enter price: ").strip())


 

    created = add_book(bname, bauthor, bprice)

    print("Inserted:", created)

 