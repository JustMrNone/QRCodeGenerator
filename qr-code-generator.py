import qrcode
import sys

def main():
    if len(sys.argv) == 1:
        urlinput = str(input("Enter your URL: "))
        filename = input("Filename(Optional, Default=Qrcode): ")
        if filename == "" or " ":
            filename = "Qrcode"   
        qrmake(urlinput, filename)
        
    elif len(sys.argv) == 2:
        qrmake(sys.argv[1])
    elif len(sys.argv) == 3:
        qrmake(sys.argv[1], sys.argv[2])  
    else:
        print("too many arguments. ")
def qrmake(url, name="Qrcode"):
    try:
        qrimg = qrcode.make(url)
        qrimg.save(f"{name}.png", "PNG")
    except Exception as e:
        print("please enter a valid input")
        
if __name__ == "__main__":
    main()