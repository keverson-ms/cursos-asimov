arquivo = "2025_20_05_notaFiscal.pdf"

print(arquivo.replace('.pdf', '.docx'))
print(arquivo.endswith('.pdf'))

print(arquivo.endswith('.docx'))

print(arquivo.startswith('2023'))

print(arquivo.startswith('2022'))

if arquivo.startswith('2025') and arquivo.endswith('.pdf'):
    print('Nota fiscal encontrada!')

letra = 'a'
print(f'Vezes da ocorrência da letra {letra}: {arquivo.count("a")}' )

print(arquivo.lower())
print(arquivo.upper())
print(arquivo.find('F'))
