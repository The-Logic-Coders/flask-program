document.getElementById('file-upload-input').addEventListener('change', function(e) {
    var fileName = e.target.files[0].name;
    document.getElementById('file-name').textContent = ' ' + fileName;
    document.getElementById('file-upload').classList.add('file-uploaded');
    document.getElementById('excel-icon').style.display = 'inline-block';
    document.getElementById('choose-file-section').style.display = 'none';
});