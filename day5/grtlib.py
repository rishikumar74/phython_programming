from supabase import create_client, Client # type: ignore

from dotenv import load_dotenv # type: ignore

import os

 

load_dotenv()

 

url = os.getenv("supabase_url")

key = os.getenv("supabase_key")

sb: Client = create_client(url, key)

 

def list_products():

    resp = sb.table("books").select("*").execute()

    return resp.data

 

if __name__ == "__main__":

    products = list_products()

    if products:

        print("Products:")

        for p in products:

            print(f"{p['bid']}: {p['bname']} author:{p['bauthor']}  ₹{p['bprice']}")

    else:

        print("No products found.")
