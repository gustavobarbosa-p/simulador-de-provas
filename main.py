from tkinter import *

def verificar_resposta():
    receber_resposta = resposta.get()

    if receber_resposta == 'a':
        alternativaA['bg'] = '#ff3333'
        alternativaB['bg'] = '#f2f2f2'
        alternativaC['bg'] = '#f2f2f2'
        alternativaD['bg'] = '#80ff80'
        alternativaE['bg'] = '#f2f2f2'
        exibir['text'] = 'Você errou!'

    elif receber_resposta == 'b':
        alternativaA['bg'] = '#f2f2f2'
        alternativaB['bg'] = '#ff3333'
        alternativaC['bg'] = '#f2f2f2'
        alternativaD['bg'] = '#80ff80'
        alternativaE['bg'] = '#f2f2f2'
        exibir['text'] = 'Você errou!'

    elif receber_resposta == 'c':
        alternativaA['bg'] = '#f2f2f2'
        alternativaB['bg'] = '#f2f2f2'
        alternativaC['bg'] = '#ff3333'
        alternativaD['bg'] = '#80ff80'
        alternativaE['bg'] = '#f2f2f2'
        exibir['text'] = 'Você errou!'

    elif receber_resposta == 'd':
        alternativaA['bg'] = '#f2f2f2'
        alternativaB['bg'] = '#f2f2f2'
        alternativaC['bg'] = '#f2f2f2'
        alternativaD['bg'] = '#80ff80'
        alternativaE['bg'] = '#f2f2f2'
        exibir['text'] = 'Parabéns, você acertou!'

    elif receber_resposta == 'e':
        alternativaA['bg'] = '#f2f2f2'
        alternativaB['bg'] = '#f2f2f2'
        alternativaC['bg'] = '#f2f2f2'
        alternativaD['bg'] = '#80ff80'
        alternativaE['bg'] = '#ff3333'
        exibir['text'] = 'Você errou!'

janela = Tk()
janela.geometry('800x250')
janela.title("Simulado ENEM")

resposta = StringVar()

question01 = Label(janela, font=('Arial', 9), text='(ENEM 2021 Reaplicação) Um professor tem uma despesa mensal de 10% do seu salário com transporte e 30% com alimentação.\n No próximo mês, os valores desses gastos sofrerão aumentos de 10% e 20% respectivamente, mas o seu salário não terá ajuste.\n Com esses aumentos, suas despesas com transporte e alimentação aumentarão em R$ 252,00. O salário mensal desse professor é de')
question01.pack()

alternativaA = Radiobutton(janela, text='a) R$ 840,00.', value='a', variable=resposta, bg='#f2f2f2')
alternativaA.pack()

alternativaB = Radiobutton(janela, text='b) R$ 1 680,00.', value='b', variable=resposta, bg='#f2f2f2')
alternativaB.pack()

alternativaC = Radiobutton(janela, text='c) R$ 2 100,00.', value='c', variable=resposta, bg='#f2f2f2')
alternativaC.pack()

alternativaD = Radiobutton(janela, text='d) R$ 3 600,00.', value='d', variable=resposta, bg='#f2f2f2')
alternativaD.pack()

alternativaE = Radiobutton(janela, text='e) R$ 5 200,00.', value='e', variable=resposta, bg='#f2f2f2')
alternativaE.pack()

botao = Button(text='submeter', command=verificar_resposta)
botao.pack()

exibir = Label(janela, text='', font=('Arial Black', 8))
exibir.pack()

janela.mainloop()