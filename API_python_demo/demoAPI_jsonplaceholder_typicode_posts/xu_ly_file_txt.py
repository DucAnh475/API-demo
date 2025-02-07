def read_file_txt(ten_file):

    with open(ten_file, 'r') as file:

        for item in file:
            print(f"{item["userId"]}, {item["id"]}, {item["title"]}, {item["body"]}\n")