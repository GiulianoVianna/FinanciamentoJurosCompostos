from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import locale

# Subclasse de QMainWindow com tamanho fixo
class JurosCompostos(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(JurosCompostos, self).__init__(*args, **kwargs)
        self.setFixedSize(442, 179)


# Função para calcular o valor total do financiamento e o valor das parcelas
def calcular():
    # Obtendo os valores de entrada
    principal_str = tela.line_valor.text()
    taxa_juros_str = tela.line_juros.text()
    parcelas_str = tela.line_parcelas.text()

    try:
        # Convertendo strings para tipos numéricos
        principal = float(principal_str)
        taxa_juros = float(taxa_juros_str)
        parcelas = int(parcelas_str)

        # Calculando o total do financiamento e o valor das parcelas
        total_financiamento = principal * (1 + taxa_juros / 100) ** parcelas
        valor_parcelas = total_financiamento / parcelas
        valor_juros = total_financiamento - principal
        percentual = (valor_juros / total_financiamento) * 100
        

        # Exibindo os resultados formatados como moeda brasileira
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        tela.line_valor_parcelas.setText(locale.currency(valor_parcelas, grouping=True))
        tela.line_valor_financiamento.setText(locale.currency(total_financiamento, grouping=True))
        tela.line_valor_juros.setText(locale.currency(valor_juros, grouping=True))
        tela.line_percentual.setText(f'{percentual:.2f}' "%".replace(".", ","))

    # Tratando possíveis erros de conversão de string para número
    except ValueError:
        QMessageBox.warning(tela, "Erro", "Por favor, insira valores numéricos válidos.")


# Função para limpar todos os campos de texto
def limpar():
    line_texto = [
        tela.line_valor,
        tela.line_juros,
        tela.line_parcelas,
        tela.line_valor_parcelas,
        tela.line_valor_financiamento,
        tela.line_valor_juros,
        tela.line_percentual,
    ]
    for widget in line_texto:
        widget.clear()


app = QtWidgets.QApplication([])
tela = JurosCompostos()
uic.loadUi("calculo_juros.ui", tela)

tela.btn_calcular.clicked.connect(calcular)
tela.btn_limpar.clicked.connect(limpar)

tela.show()
app.exec()
