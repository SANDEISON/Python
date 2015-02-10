arquivo = open("ola.html", "w", encoding ="utf-8")
arquivo.write('''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <title> Titulo da Pagina </title>

</head>
<body>
olá
</body>

</html>
''')
arquivo.close()
