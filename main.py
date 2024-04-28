from rembg import remove
# rename the image here
input_path = '03.jpeg'
output_path = 'out.jpeg'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)