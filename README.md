# Script de automação para a tarefa de pesquisa do MS Rewards no pc.

### Para funcionar corretamente, verificar se os seguintes modulos estão instalados:<br>
pip install pyautogui <br>
pip install pillow <br>
pip install opencv-python <br>
pip install pynput <br>

### O script foi desenvolvido e testado no windows, mas tambem funciona no linux, a pre-configuração vai depender da distribuição utilizada.

# O script foi desenvolvido desenvolvido em uma tela 1080p com dimensionamento em 100%, caso tente rodar ele em qualquer outra confirugação o mesmo não irá funcionar.<br>
## Configuração para um sistema que não utiliza 1080p/100%.

### Verificar config do sistema
 - Para funcionar verirfique se as aconfigurações de tela estão assim (Testado no widows)
![image](https://github.com/user-attachments/assets/bd70a330-06e2-4e98-b12e-99aeb02bd977)

 - Caso não esteja como indicado na image será necessário tirar print de 2 elementos do Edge e substituir na pasta imagens do projeto com os mesmos nomes

   1 - barra_de_pesquisa.png
   ![barra_de_pesquisa](https://github.com/user-attachments/assets/5cbd7c0a-66c7-4984-a318-677180878c47)<br>
   2 - apagar.png<br>
   ![apagar](https://github.com/user-attachments/assets/885ca0f5-18a6-4b8d-ba49-cbfb71bee241)

 - Os dois elementos podem ser encontrados na tela de pesquisa do navegador Edge

### Rodando o script
 - Para rodar o script basta deixar a tela de pesquisa previamente aberta para que o script encontre a barra de pesquisa e rodar o codigo em python da forma que achar melhor (Com vscode por exemplo)
