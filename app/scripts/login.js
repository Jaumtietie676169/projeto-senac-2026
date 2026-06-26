document.getElementById("entrar").addEventListener("click", () => {

    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;

    if(email === "" || senha === ""){
        alert("Preencha tudo!");
        return;
    }

    window.location.href = "form.html";

});

document.getElementById("criar").addEventListener("click", () => {

    alert("Conta criada com sucesso!");

    window.location.href = "form.html";

});
