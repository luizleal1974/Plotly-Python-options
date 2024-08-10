from pandas import read_excel, DataFrame
import plotly.express as px

# Dados
path = ('https://github.com/luizleal1974/Plotly-Python-options/raw/main/Python_codes/01_Dados.xlsx')
dados = read_excel(path)

# Tabela
x = dados['Religiao']
freq = x.value_counts(normalize = False)
dfr = DataFrame({ 'Religiao': freq.index, 'Freq': freq.values })

# Label
L = list(map(lambda x: x + ' </br></br> ', dfr.Religiao.to_list()))
p = round((dfr.Freq / sum(dfr.Freq))*100, ndigits = 2)
p = list(map("{}%".format, p))
r = [m+str(n) for m,n in zip(L,p)]
dfr = dfr.assign(Rotulo = r)

# Hover label
H = ["Frequencia: " + str(i) + " pessoas" for i in dfr.Freq]
dfr = dfr.assign(Hover_rotulo = H)

# Grafico de setores
fig = px.pie(data_frame = dfr,
             values = 'Freq',
             names = 'Religiao',
             title = "(b)"
             )
fig.update_layout(showlegend = False,
                  title = dict(text = "(b)", font = dict(size = 44, color = 'black')),
                  title_x = 0.5
                  )
fig.update_traces(text = dfr.Rotulo,
                  textposition = 'inside',
                  textinfo = 'text',
                  textfont_size = 32,
                  textfont_color = 'white',
                  textfont_family = 'Calibri',
                  hoverinfo = 'text',
                  hovertemplate = dfr.Hover_rotulo,
                  hoverlabel_font_size = 32,
                  hoverlabel_font_color = 'white',
                  hoverlabel_font_family = 'Calibri'
                  )
fig.show()
