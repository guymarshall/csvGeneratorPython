import os

def delete_csv_files():
    for filename in os.listdir():
        if filename.endswith(".csv") and filename != "data":
            os.remove(filename)

if __name__ == "__main__":
    delete_csv_files()