function copyLinkHandler() {
  var copyText = document.getElementById("copy-link");
  copyText.select();
  copyText.setSelectionRange(0, 99999);
  document.execCommand("copy");
  alert("Link copied to clipboard.");
}

function countCharHandler() {
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
}

function modalHandler(id) {
  let message = document.getElementById("message-" + id).innerHTML;
  let header = document.getElementById("header-" + id).innerHTML;

  document.getElementById("exampleModalLongTitle").innerHTML = header;
  document.getElementById("modal-body").innerHTML = message;
}

function toggleFavorite(id) {
  let cname = document.getElementById("fav-" + id).className.split(" ")[1];
  if (cname === "fa-heart") {
    document.getElementById("fav-" + id).className = "fa fa-heart-o ml-3 mt-1";
  } else {
    document.getElementById("fav-" + id).className =
      "fa fa-heart ml-3 mt-1 text-danger";
  }

  let local_url = "http://127.0.0.1:8000/toggle-fav/" + id + "/";
  let twing_url = "https://twing.herokuapp.com/toggle-fav/" + id + "/";
  fetch(twing_url).then((response) => {
    console.log(response.json());
  });
}
