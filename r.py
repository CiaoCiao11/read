with open('food.txt','r') as f:
  for line in f:
    print(line.strip())#.strip()可除去左右空白及換行