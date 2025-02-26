window.addEventListener('load', function () {
  let errorMessages = document.querySelectorAll('.error-message');
  errorMessages.forEach(function (message) {
    setTimeout(function () {
      message.style.display = 'none';
    }, 10000);
  });

  let messages = document.getElementById("errorMessages");
  if (messages) {
    setTimeout(function () {
      messages.style.display = 'none';
    }, 10000);
  }
});
