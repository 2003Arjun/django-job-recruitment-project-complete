window.onload = function() {
  const messages = document.querySelectorAll('.message');
  messages.forEach(function(message) {
    setTimeout(function() {
      message.style.opacity = '0';
      setTimeout(function() {
        message.style.display = 'none'; 
      }, 1000); 
    }, 5000);
  });
};
