document.addEventListener('DOMContentLoaded', () => {
  const SERVER_URL = 'https://004f-46-247-108-192.ngrok-free.app/check';

  function showToast(message, isError = false) {
    const div = document.createElement('div');
    div.className = [
      'fixed top-4 right-4 px-4 py-3 rounded shadow-lg transition-opacity',
      isError
        ? 'bg-red-100 border border-red-400 text-red-700'
        : 'bg-green-100 border border-green-400 text-green-700'
    ].join(' ');
    div.style.opacity = '0';
    div.innerHTML = message;
    document.body.appendChild(div);
    requestAnimationFrame(() => div.style.opacity = '1');
    setTimeout(() => {
      div.style.opacity = '0';
      div.addEventListener('transitionend', () => div.remove());
    }, 3000);
  }

  async function postToServer(payload) {
    const res = await fetch(SERVER_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    return res.ok ? res.json() : { status: 'error', message: `HTTP ${res.status}` };
  }

  const orderForm = document.getElementById('order-form');
  if (!orderForm) return;

  orderForm.addEventListener('submit', async e => {
    e.preventDefault();
    const btn = orderForm.querySelector('button[type="submit"]');
    btn.disabled = true;
    const originalText = btn.textContent;
    btn.textContent = '🚀 Envoi…';

    const data = {
      type: 'order',
      name:      orderForm.name.value.trim(),
      email:     orderForm.email.value.trim(),
      phone:     orderForm.phone.value.trim(),
      company:   orderForm.company.value.trim() || null,
      projectType: orderForm['project-type'].value,
      description: orderForm.description.value.trim(),
      budget:      orderForm.budget.value,
      deadline:    orderForm.deadline.value,
      terms:       orderForm.terms.checked,
      submittedAt: new Date().toISOString()
    };

    if (!data.name || !data.email || !data.terms) {
      showToast('⚠️ Remplis nom, email et accepte les CGV !', true);
      btn.disabled = false;
      btn.textContent = originalText;
      return;
    }

    let result;
    try {
      result = await postToServer(data);
    } catch (err) {
      console.error(err);
      showToast('🌐 Erreur réseau, réessaie plus tard…', true);
    }

    if (result?.status === 'ok') {
      showToast('🎉 C’est envoyé ! Je t’ai pingé sur Discord.');
      orderForm.reset();
    } else {
      showToast(`😕 Oops : ${result.message || 'échec'}`, true);
    }

    btn.disabled = false;
    btn.textContent = originalText;
  });
});
