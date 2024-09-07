import one

print("TOP LEVEL IN TWO.PY")
one.func1()

if __name__ == '__main__':
    print("ONE.PY IS BEING RUN DIRECTLY")
else:
    print("one is being imported")
