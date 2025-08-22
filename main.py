import base64
import sys

def main():
    if len(sys.argv) < 2:
        print("endless-b64:\nUsage: main.py [text] [repeats (optional)]")
        return
    text = sys.argv[1]
    print("Press CTRL+C if you want get encoded text.")
    try:
        while 1:
            text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    except KeyboardInterrupt:
        with open('encoded.txt', 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Encoded text writed in 'encoded.txt'. {len(text)} symbols.")
    

if __name__ == "__main__":
    main()