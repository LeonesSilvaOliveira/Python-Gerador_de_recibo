from fpdf import FPDF
from num2words import num2words

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
nome = input('Digite o nome: ')
cpf = str(input('Digite o CPF: '))
local = input('Digite o local do recibo: ')
while True:
    data = input('Digite a data no formato DD/MM/AAAA: ')
    if len(data) == 10 and data[2] == "/" and data[5] == "/":
        print(f'Data inserida: {data}')
        break
    else:
        print('Formato de data errado, por favor inserir no modelo correto')
valor = float(input('Digite o valor do serviço: '))

# Converte o valor em reais para por extenso
valor_por_extenso = num2words(valor, lang='pt_BR', to='currency')

pagamento = ''

while pagamento not in ['débito', 'pix', 'crédito', 'dinheiro']:
    pagamento = input('Digite o meio de pagamento (Débito, PIX, Crédito, Dinheiro): ').lower()
    if pagamento == 'crédito':
        credito = input('Digite em quantas vezes: ')


# Defina o texto do recibo
texto = f'Pelo presente, eu {nome}, inscrito no CPF sob nº {cpf}, declaro que RECEBI na data de hoje {data}, o valor de R$ {valor:.2f} ({valor_por_extenso}), por meio de {pagamento}, de [Nome do Pagador], inscrito no CPF sob nº [CPF do Pagador], referente a [Motivo].'

# Texto2
texto2 = 'Sendo expressão de verdade e sem qualquer coação, firmo o presente recibo.'

# Adicione o título "Recibo"
pdf.cell(0, 10, txt='Recibo', ln=True, align='C')
pdf.ln(10)  # Pule uma linha

# Adicione o texto do recibo
pdf.multi_cell(0, 10, txt=texto, align='C')
pdf.ln(10)  # Pule uma linha

# Adicione o texto2
pdf.multi_cell(0, 10, txt=texto2, align='C')

pdf.ln(10)


pdf.ln(10)

pdf.multi_cell(0,10, txt = '__________________________________________________', align = 'C')
pdf.multi_cell(0,10, txt = nome, align = 'C')

pdf.cell(0,10, txt = f"{local}", align = 'L')
pdf.cell(0 ,10, txt = data, align = 'R')

# Salve o PDF em um arquivo
pdf.output("recibo.pdf", 'F')
print('PDF gerado com sucesso')
