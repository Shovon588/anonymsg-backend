copyLinkHandler = () => {
  var copyText = document.getElementById("copy-link");
  copyText.select();
  copyText.setSelectionRange(0, 99999);
  document.execCommand("copy");
  alert("Link copied to clipboard.");
};

countCharHandler = () => {
  message = document.getElementById("message").value;
  char_left = 256 - message.length;
  if (char_left < 25) {
    document.getElementById("char-left").innerHTML = "";
    document.getElementById("char-left-danger").innerHTML =
      char_left + " characters left.";
  } else {
    document.getElementById("char-left-danger").innerHTML = "";
    document.getElementById("char-left").innerHTML =
      char_left + " characters left.";
  }
};

modalHandler = (id) => {
  let message = document.getElementById("message-" + id).innerHTML;
  let header = document.getElementById("footer-" + id).innerHTML;

  document.getElementById("exampleModalLongTitle").innerHTML = header;
  document.getElementById("modal-body").innerHTML = message;
};
