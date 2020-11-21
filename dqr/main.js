async function main() {
  var getUrlParameter = function getUrlParameter(sParam) {
      var sPageURL = window.location.search.substring(1),
          sURLVariables = sPageURL.split('&'),
          sParameterName,
          i;

      for (i = 0; i < sURLVariables.length; i++) {
          sParameterName = sURLVariables[i].split('=');

          if (sParameterName[0] === sParam) {
              return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
          }
      }
  };

  var config = 'config.json';

  // Testing code
  var test = getUrlParameter('testconfig');
  var intest = false;
  var nonredirect = getUrlParameter('nonredirect');
  if (test) {
    config = test;
    intest = true
  }

  // Actual logic
  config && $.getJSON(config, function(data) {
    console.log(data);
    var dest = getUrlParameter('dest');
    const url = data[dest].url;
    var author = data[dest].author;
    if (author) {
      if (author.length > 0) {
        author = author.trim();
      }
      if (author.length === 0) { // empty string
        author = undefined;
      }
    }

    $.getJSON(url, function(data) {
      console.log(data);
      var len = data.length;
      for (var i = len-1; i >= 0; i--) {
        if (!author || (author && author === data[i].user.login)) { // If author not exists or author is the commenter
          var matches = data[i].body.match(/\bhttps?:\/\/\S+/gi);

          if (matches) {
            if (intest) {
              console.log(matches);
              console.log(author);
              console.log(i);
            } 
            
            // Update the link var in case redirect fails
            link.attr('href', matches[0]);
            link.text("If redirect fails, please click this link.");

            if (!nonredirect) {
              window.location.replace(matches[0]); // If have multiple url only the first one will be used.
            }
            
            break;
          }
        }
      }
    });

  });
}