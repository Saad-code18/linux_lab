import sys

def solve():
    if len(sys.argv) < 2:
        return
    shift = int(sys.argv[1])
    full_text = sys.stdin.read()
    processed_text = ""
    for char in full_text.upper():
        if 'A' <= char <= 'Z':
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            processed_text += shifted_char
    output = ""
    for i in range(len(processed_text)):
        output += processed_text[i]
        if (i + 1) % 5 == 0:
            if (i + 1) % 50 == 0:
                output += "\n"
            else:
                output += " "
                
    print(output.strip())

if __name__ == "__main__":
    solve()