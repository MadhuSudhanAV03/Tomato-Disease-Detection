(() => {
  const fileInput = document.getElementById('file');
  const previewImg = document.getElementById('preview-img');
  const previewEmpty = document.getElementById('preview-empty');
  const submitBtn = document.getElementById('submit-btn');
  const spinner = document.getElementById('spinner');
  const form = document.getElementById('upload-form');

  function resetPreview() {
    previewImg.style.display = 'none';
    previewImg.src = '';
    previewEmpty.style.display = 'block';
    submitBtn.disabled = true;
  }

  fileInput.addEventListener('change', (ev) => {
    const file = ev.target.files && ev.target.files[0];
    if (!file) { resetPreview(); return; }
    const reader = new FileReader();
    reader.onload = (e) => {
      previewImg.src = e.target.result;
      previewImg.style.display = 'block';
      previewEmpty.style.display = 'none';
      submitBtn.disabled = false;
    };
    reader.readAsDataURL(file);
  });

  form.addEventListener('submit', () => {
    submitBtn.disabled = true;
    spinner.style.display = 'inline';
  });

})();
