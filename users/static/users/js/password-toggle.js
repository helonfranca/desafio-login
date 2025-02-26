document.getElementById("password-toggle-1").addEventListener("click", function () {
  let passwordField = document.getElementById("password1");
  let icon = this.querySelector("i");

  if (passwordField.type === "password") {
    passwordField.type = "text";
    icon.classList.remove("fa-eye");
    icon.classList.add("fa-eye-slash");
  } else {
    passwordField.type = "password";
    icon.classList.remove("fa-eye-slash");
    icon.classList.add("fa-eye");
  }
});

document.getElementById("password-toggle-2").addEventListener("click", function () {
  let passwordField = document.getElementById("password2");
  let icon = this.querySelector("i");

  if (passwordField.type === "password") {
    passwordField.type = "text";
    icon.classList.remove("fa-eye");
    icon.classList.add("fa-eye-slash");
  } else {
    passwordField.type = "password";
    icon.classList.remove("fa-eye-slash");
    icon.classList.add("fa-eye");
  }
});
