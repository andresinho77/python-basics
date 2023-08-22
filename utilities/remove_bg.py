import rembg

input_img = '/Users/user.name/entrada.png'
output_img = '/Users/user.name/salida.png'
def funcion(input_img, output_img):

    with open(input_img, 'rb') as i:
        with open(output_img, 'wb') as o:
            input = i.read()
            output = rembg.remove(input)
            o.write(output)

funcion(input_img, output_img)