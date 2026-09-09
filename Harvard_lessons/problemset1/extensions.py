filetype=input("Enter your filename ")

def Fileorganizer(filetype):
    match filetype:
        case x if filetype.endswith(".gif"):
            print("image/gif")
        case x if filetype.endswith(".jpeg"):
            print("image/jpeg")
        case x if filetype.endswith(".png"):
            print("image/png")
        case x if filetype.endswith(".jpg"):
            print("image/jpg")
        case x if filetype.endswith(".pdf"):
            print("document/pdf")
        case x if filetype.endswith(".txt"):
            print("document/txt")
        case x if filetype.endswith(".zip"):
            print("document/zip")
        case _:
            print("application/octet-stream")
