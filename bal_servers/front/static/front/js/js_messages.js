document.querySelectorAll('.close').forEach(function (button) {
    button.addEventListener('click', function () {
        this.parentElement.style.display = 'none';
    });

    // Добавляем функцию для автоматического закрытия через 2 секунды
    setTimeout(function () {
        button.parentElement.style.display = 'none';
    }, 5000);
});