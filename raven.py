from Tkinter import *
import csv

file = '/home/pxcx/Desktop/raven.csv'


def main():
    root = Tk()
    root.title('Ravencoin Mining Profits')

    try:
        canvas = Canvas(root, width=1100, height=650, bg = 'white')
        canvas.pack()
        Button(root, text='Quit', command=root.quit).pack()

        canvas.create_line(100,550,975,550, width=2)
        canvas.create_line(100,550,100,45,  width=2)

        canvas.create_text(985,545, font=("Default", 14), text='Dias', anchor=NW)
        canvas.create_text(110,25, font=("Default", 15), text='RVN', anchor=E)

        for i in range(30):
            x = 100 + (i * 30)
            canvas.create_line(x,550,x,545, width=2)
            canvas.create_text(x,554, text='%d'% (i+1), anchor=N)

        for i in range(26):
            y = 550 - (i * 20)
            canvas.create_line(100,y,105,y, width=2)
            canvas.create_text(96,y, text='%d'% (i*10), anchor=E)
            if i > 0 and i%50 == 0:
                canvas.create_line(100,y,975,y, width=1, fill="black", dash=(4, 4))

        scaled = []
        raven_data = []
        raven_data = data()
        count = 0
        rvn_sum = 0
        for i in raven_data:
            scaled.append((100 + 30*(count), i))
            #print '(',count,',',(550-i)/2,')'
            rvn_sum += (550-i)/2
            count += 1

        canvas.create_line(scaled, fill='green', smooth=0, width=2)

        for xs,ys in scaled:
            canvas.create_oval(xs-3,ys-3,xs+3,ys+3, width=1, outline='black', fill='SkyBlue2')
            if xs > 100:
                canvas.create_text(xs,ys-20, text='%d'% ((550-ys)/2), anchor=N)
            else:
                canvas.create_text(xs+15,ys-20, text='%d'% ((550-ys)/2), anchor=N)

        canvas.create_text(100,600, font=("Default", 18), text='~ %3.2f RVN/Dia'% float(rvn_sum/30), anchor=NW)

    except Exception, e:
        print '[ERROR] '+ str(e)

    root.mainloop()

def data():
    with open(file, 'r') as csvfile:
        # get number of columns
        count = 1
        total = 0
        linha = 0
        dias = 0
        data_atual = ''
        total_dia = 0
        dia_anterior = 0

        output = []
        arquivo = csvfile.readlines()
        for line in reversed(arquivo):
            if linha < len(arquivo)-1:
                array = line.split(',')
                data = array[1].split('T')
                data = data[0].replace('"','')
                #data_info = data.split('-')
                #dia = data_info[2]
                valor = float(array[5].replace('"',''))

                total = total + valor

                if data != data_atual:
                    if data_atual:
                        #print(data_atual + '\t' + "{:.2f}".format(total_dia) + ' RVN\t' + "{:.2f}".format( ((total_dia/dia_anterior)-1)*100 if dia_anterior > 0 else 0 ) + "%")
                        #print("(",count,",",total_dia,")")
                        #output.append( (100 + 30*(count-1), 550-(2*total_dia)) )
                        output.append(550-(2*total_dia))
                        count += 1
                    dias += 1
                    dia_anterior = total_dia
                    total_dia = valor
                    data_atual = data
                else:
                    total_dia += valor

            linha += 1

        #print('\n\nTOTAL: ' + "{:.2f}".format(total))
        #print('MEDIA: ' + "{:.2f}".format(total/dias))


        start = len(output)-30 if len(output) > 30 else 0
        return output[start:]

main()
