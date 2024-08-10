from pandas import read_excel, DataFrame
import plotly.express as px

# Dados
path = ('https://github.com/luizleal1974/Plotly-Python-options/raw/main/Python_codes/01_Dados.xlsx')
dados = read_excel(path)

# Tabela
x = dados['Religiao']
freq = x.value_counts(normalize = False)
dfr = DataFrame({ 'Religiao': freq.index, 'Freq': freq.values })

# Grafico de setores
fig = px.pie(data_frame = dfr,
             values = 'Freq',
             names = 'Religiao',
             title = '(a)'
             )
fig.update_layout(showlegend = False,
                  title = dict(text = "(a)", font = dict(size = 44, color = 'black')),
                  title_x = 0.5
                  )
fig.update_traces(textposition = 'inside',
                  textinfo = 'percent+label',
                  textfont_size = 32,
                  textfont_color = 'white',
                  textfont_family = 'Calibri',
                  hoverlabel_font_size = 32,
                  hoverlabel_font_color = 'white',
                  hoverlabel_font_family = 'Calibri'
                  )
fig.show()

