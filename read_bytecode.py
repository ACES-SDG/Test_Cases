import dis

with open('image_text_lable.cpython-311.pyc', 'rb') as file:
    bytecode = file.read()

dis.dis(bytecode)
