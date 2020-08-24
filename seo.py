# Auditoría SEO
import urllib.request as request
from bs4 import BeautifulSoup  # Librería para acceso a etiquetas web
from urllib.request import urlopen

def ActividadesSEO():
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("                                   AUDITORÍA SEO BÁSICA                                                    ")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("\nNOTA: Se debe ingresar el protocolo, el nombre del sitio web y el dominio en ese orden.")
    print("EJEMPLO: http://python.org")

    DatoEntrada = input("\nIngresa el sitio web: ")
    print("* El sitio web escogido es: ", DatoEntrada)

# Detección de viewport
    try:
        Y = request.urlopen(DatoEntrada)
        soup = BeautifulSoup(Y.read(), features='html.parser')
        print("* Etiqueta meta: ", soup.find('meta', attrs={'name': 'viewport'}))
    except:
        print("* Etiqueta meta: Problema al localizarla")

# Verificación de idioma del sitio web
    try:
        lang = soup.find('html')['lang']
        print('* Idioma(s) del sitio web: ', lang)
    except:
        print("* Idioma sel sitio web: No encontrado")

# Verificación de descripción #
    try:
        site = request.urlopen(DatoEntrada)
        soup = BeautifulSoup(site, 'html.parser')
        description = soup.find('meta', attrs={'name': 'description'})
        print("* Tamaño de la descripción: ", len(description.get('content')), "caracteres")
    except:
        print("* Tamaño de la descripción: No encontrado")

# Verificación de WWW #
    try:
        req = request.Request(DatoEntrada)
        res = request.urlopen(req)
        print('* Confirmación de existencia World Wide Web: ', res.geturl())
    except:
        print("* Exitencia de WWW: No encontrado")
# Verificación de etiqueta Title#
    try:
        html = urlopen(DatoEntrada)
        print("* Tamaño de etiqueta Title: " , len(soup.html.head.title.string))
        print("* Texto de etiqueta Title: ", soup.html.head.title.string)
    except:
        print("* Tamaño de etiqueta Title: No encontrado")
# Palabras clave #
    try:
        site = request.urlopen(DatoEntrada)
        soup = BeautifulSoup(site, 'html.parser')
        keywords = soup.find('meta', attrs={'name':'keywords'})
        print("* Palabras clave: [", keywords.get('content',","), "]")
    except:
      print("* Palabras clave: No encontradas")

# Busqueda del test.ico
    try:
        page = request.urlopen(DatoEntrada)
        soup = BeautifulSoup(page, 'html.parser')
        icon_link = soup.find('link', rel="icon")
        icon = request.urlopen(DatoEntrada + icon_link['href'])
    except:
        print("* Problema con el archivo .ico")
        with open("test.ico", "wb") as f:

            try:
             f.write(icon.read())
             print("* Archivo test.ico: Encontrado")
            except:
             print("* Archivo test.ico: No encontrado")

        #  ALT Imagenes #
        try:
            print("* Imagenes encontradas: ")
            count = 1
            for image in soup.find_all('img'):
                print(' - Imagen #', count, ":", image["src"], count, ":", image.get('alt', 'None'))
            count += 1
        except:
            print("* Imágenes: No encontradas ")
    # Peso de la página  #
    try:
        req = request.Request(DatoEntrada)
        Resultado = request.urlopen(req)
        urlObtenida = Resultado.geturl()
        site = request.urlopen(urlObtenida)
        meta = site.info()
        if (site.headers['content-length'] == None):
            print("* Longitud del contenido: No encontrada")
        else:
            print("* Longitud total del contenido: ", site.headers['content-length'] )

    except:
        print("* Longitud total del contenido: No encontrada")
    Reingreso()

def Reingreso():

    Volver = input("\n ¿Deseas ingresar otra URL? (S/N): ")
    if Volver == "S":
        ActividadesSEO()
    elif Volver == "s":
        ActividadesSEO()
    elif Volver == "N":
        return FinCodigo()
    elif Volver == "n":
        return FinCodigo()

def FinCodigo():
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("                             ¡GRACIAS POR HACER USO DEL PROGRAMA!                                          ")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    exit()

while True:
        ActividadesSEO()






