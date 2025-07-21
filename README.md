# Matrix Script

Script em Python para manipulação de imagens no formato **PBM**, utilizando operações matriciais básicas.

> Projeto desenvolvido como parte da disciplina de **Geometria Analítica e Cálculo Vetorial** no curso de **Ciência da Computação - UESB**.

---

## Objetivo

A partir de uma imagem em formato **PBM**, esse script aplica transformações que reorganizam a posição dos pixels por meio das seguintes operações matriciais:

- **Transposição**
- **Permutação de linhas**
- **Permutação de colunas**

Também são utilizadas combinações dessas operações.

Após a execução, serão criadas **8 imagens distintas** na pasta `output/`, localizada no mesmo diretório do script.

---

## Como executar

> Requisitos: Python 3.9+ e `pip`

1. **Clone o repositório:**
``` bash
git clone https://github.com/hevertonn/matrix-script.git
cd matrix-script
```

2. **Instale as dependências:**
``` bash
pip install -r requirements.txt
```

3. **Execute o script:**
``` bash
python main.py caminho/para/sua/imagem.pbm
```

---

## Licença
Este projeto está licenciado sob Licença MIT. Para mais informações, consulte o arquivo [LICENSE](LICENSE).
