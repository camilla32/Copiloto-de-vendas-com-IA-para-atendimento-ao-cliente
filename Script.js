function enviarMensagem(){

let campo =
document.getElementById("mensagem");

let texto =
campo.value;

if(texto === "") return;

let chat =
document.querySelector(".chat-box");

chat.innerHTML += `
<div class="user-message">
${texto}
</div>
`;

campo.value="";

}

function resposta(valor){

alert(
"Fluxo selecionado: " + valor
);

}