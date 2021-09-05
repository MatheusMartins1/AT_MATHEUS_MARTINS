(function ($) {

  "use strict";

  var fullHeight = function () {

    $('.js-fullheight').css('height', $(window).height());
    $(window).resize(function () {
      $('.js-fullheight').css('height', $(window).height());
    });

  };
  fullHeight();

  $('#sidebarCollapse').on('click', function () {
    $('#sidebar').toggleClass('active');
  });


  //Get the button
  let mybutton = document.getElementById("btn-back-to-top");

  // When the user scrolls down 20px from the top of the document, show the button
  window.onscroll = function () {
    scrollFunction();
  };

  function scrollFunction() {
    if (
      document.body.scrollTop > 20 ||
      document.documentElement.scrollTop > 20
    ) {
      mybutton.style.display = "block";
    } else {
      mybutton.style.display = "none";
    }
  }
  // When the user clicks on the button, scroll to the top of the document
  mybutton.addEventListener("click", backToTop);

  function backToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }



  // -----------------------

  /* 
  Copyright (c) 2021 by elcanziba (https://codepen.io/elcanziba/pen/evBZGB)
   
  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
   
  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
   
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
  */

  $(document).ready(function () {
    $("div.card-flap.flap1").hide();
    var zindex = 10;

    $("div.card.processador").click(function (e) {
      e.preventDefault();

      var isShowing = false;

      if ($(this).hasClass("d-card-show")) {
        isShowing = true;
      }

      if ($("div.dashboard-cards").hasClass("showing")) {
        // a card is already in view
        $("div.card.d-card-show").removeClass("d-card-show");

        if (isShowing) {
          // this card was showing - reset the grid
          $("div.dashboard-cards").removeClass("showing");
          $("div.card-flap.flap1").hide();
        } else {
          // this card isn't showing - get in with it
          $(this)
            .css({ zIndex: zindex })
            .addClass("d-card-show");
        }

        zindex++;

      } else {
        $("div.card-flap.flap1").show();
        // no dashboard-cards in view
        $("div.dashboard-cards")
          .addClass("showing");
        $(this)
          .css({ zIndex: zindex })
          .addClass("d-card-show");

        zindex++;
      }

    });
  });

})(jQuery);
