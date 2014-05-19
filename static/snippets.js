
function query(util) {
  hideRight();
  snipid = "snp" + util.id
  document.getElementById(snipid).style.display = "";
}

function hideRight() {
  var ui = document.getElementsByName("utilinfo");
  for(i = 0; i < ui.length; i++) {
    document.getElementById(ui[i].id).style.display = "none";
  }
  document.getElementById("addform").style.display = "none";
  document.getElementById("searchform").style.display = "none";
}

function addUtil() {
  hideRight();
  document.getElementById("addform").style.display = "";
}

function search() {
  hideRight();
  s = document.getElementById("searchinp").value;
  sterms = s.split(" ");
  for(i = 0; i < sterms.length; i++ ) {
    var ui = document.getElementsByName("utilinfo");
    for(j = 0; j < ui.length; j++) {
      var desc = document.getElementById(ui[j].id + "desc").innerHTML;
      if(desc.search(sterms[i]) != -1) {
        document.getElementById(ui[j].id).style.display = "";
      }
    }
  }
}

function showSearch() {
  document.getElementById("searchform").style.display = "";
}

var callbacks = {
  success: function(o) {
    try {
      alert(o.responseText);
      messages = YAHOO.lang.JSON.parse(o.responseText);
    } catch (x) {
      alert("json FAIL!"+x);
      return;
    }
    print(messages);
  },
  failure: function(o) {
    alert(o.responseText);
    alert("FAIL");
  }
};

//YAHOO.util.Connect.asyncRequest('GET',"rpc_serverutils.py", callbacks);
