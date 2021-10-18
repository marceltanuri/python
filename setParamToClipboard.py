import sys
import pyperclip

if len(sys.argv)<2:
    print("Missing param. You should enter a numeric param")
    sys.exit(0)

## Get param
_param = sys.argv[1]

## Copy param to clipboard
pyperclip.copy(_param)

## Print param
print("\nYour param has been copy to the clipboard:")
print(_param)