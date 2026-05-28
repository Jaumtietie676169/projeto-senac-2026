const form = document.getElementById('post-form');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    const form_data = new FormData(event.target);

    const autor    = form_data.get('autor')
    const titulo   = form_data.get('titulo')
    const email    = form_data.get('email')
    const historia = form_data.get('historia')

    if (!autor) {
        alert("Os campos 'Autor' é obrigatórios!");
        return;
    }

    if (!historia) {
        alert("Os campos 'História' é obrigatório!");
        return;
    }

    const article = document.createElement('article');
    article.className = "artigo";

    article.innerHTML = `
        <h3>${titulo || 'Sem título'}</h3>
        <p><strong>Autor:</strong> ${autor}</p>
        ${email ? `<p><small>Email: ${email}</small></p>` : ''}
        <p>${historia.replace(/\n/g, '<br />')}</p>
        <hr />
    `;

    document.getElementById('historias').appendChild(article);

    event.target.reset();
});

const overlay = document.createElement('div');
overlay.className = 'modal-overlay';
overlay.innerHTML = `
  <div class="modal-conteudo">
    <button class="modal-fechar">✕</button>
    <div id="modal-corpo"></div>
  </div>
`;
document.body.appendChild(overlay);


overlay.querySelector('.modal-fechar').addEventListener('click', () => {
  overlay.classList.remove('aberto');
});

overlay.addEventListener('click', (e) => {
  if (e.target === overlay) overlay.classList.remove('aberto');
});

document.getElementById('historias').addEventListener('click', (e) => {
  const artigo = e.target.closest('.artigo');
  if (!artigo) return;

  document.getElementById('modal-corpo').innerHTML = artigo.innerHTML;
  overlay.classList.add('aberto');
});