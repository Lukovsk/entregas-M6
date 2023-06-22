# Atividade 4: Backend para transmissão e armazenamento de imagens

## Enunciado
Desenvolva o software de um backend capaz de receber imagens e armazená-las adequadamente. Não há restrições com relação à tecnologia utilizada.

## Vídeo de demonstração



## Implementação
No notebook ipynb deste repositório, encontra-se um script capaz de identificar rachadures em paredes de concreto. É utilizada a biblioteca `Roboflow` para a criação do dataset necessário e, com o modelo de detecção de objetos pré-treinado, o `YoLo`, esse dataset é utilizado para treinar o modelo. Por fim, foram inseridas duas imagens com rachaduras e o modelo executa a detecção de rachaduras neles. Assim como o vídeo e as imagens abaixo, é possível ver que as rachaduras são identificadas com sucesso.

Na pasta `/src` deste diretório, encontra-se o script em python que cria um servidor em flask que, além de servir um pequeno frontend da pasta `/templates`, possui uma rota ```upload``` que envia uma imagem ao Supabase. O frontend permite que se envie uma imagem ao backend que, por sua vez, envia essa imagem ao supabase, retornando o link da imagem.