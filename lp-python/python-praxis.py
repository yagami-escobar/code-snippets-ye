## 1) Hello World
print("Hello-World")

## 2) Sumar 2 Numeros interactivamente
## WHILE
def run():
    i = 0
    while i < 10:
        print(i+1)
        i += 1
if __name__ == '__main__':
    run()

## FOR
def run():
    for i in range(10):
        print(i+1)

if __name__ == '__main__':
    run()

## 3) Recorrer una frase con Bucles
## FOR
def run():
    command = "npm --version"
    for i in command:
        print(i)
    
    print()
    j = 0
    
    ## WHILE
    while j < len(command):
        print(command[j])
        j = j + 1
    
if __name__ == '__main__':
    run()

